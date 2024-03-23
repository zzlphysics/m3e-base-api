import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

# 从环境变量中获取端口号和设备，如果没有设置，则使用默认值
PORT = int(os.environ.get("PORT", 6000))
DEVICE = os.environ.get("DEVICE", "cpu").lower()

# 如果设备设定为'gpu'，则使用'cuda'，否则使用'cpu'
DEVICE = "cuda" if DEVICE == "gpu" else "cpu"

m3e = SentenceTransformer('moka-ai/m3e-base', device=DEVICE)

app = Flask(__name__)

app.config["BASE_URL"] = f"http://localhost:{PORT}"

@app.route("/")
def index():
    return "Hello from Colab!"

@app.route('/v1/embeddings', methods=['POST'])
def embeddings():
    data = request.json
    input_text = data.get('input')
    model = data.get('model')
    if model is None:
        model = "moka-ai/m3e-base"

    if input_text is None:
        return jsonify(error="No input text provided"), 400
    
    if isinstance(input_text, str):
        sentences = [input_text]
    elif isinstance(input_text, list):
        sentences = input_text

    embeddings = m3e.encode(sentences)
    embeddings = embeddings.tolist()
    data = [{"object": "embedding", "embedding": x, "index": i} for i, x in enumerate(embeddings)]

    response = {
        "object": "list",
        "data": data,
        "model": model,
        "usage": {
            "prompt_tokens": 0,
            "total_tokens": 0
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=False)
