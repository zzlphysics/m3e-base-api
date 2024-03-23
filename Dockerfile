# 基于 NVIDIA CUDA 镜像
FROM nvidia/cuda:12.1.1-base-ubuntu22.04

# 安装 Python 和 pip
RUN apt-get update && apt-get install -y python3 python3-pip

# 设置工作目录
WORKDIR /app

# 复制当前目录下的内容到工作目录
COPY . /app

# 安装依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 定义环境变量（可以被运行时覆盖）
ENV PORT=6000 DEVICE=cpu

# 暴露端口
EXPOSE $PORT

# 启动 Flask 应用
CMD ["sh", "-c", "python3 m3e-api.py --host=0.0.0.0 --port=$PORT"]
