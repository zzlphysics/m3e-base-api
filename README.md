# m3e-base-api

这个项目基于 [Colab Notebook](https://colab.research.google.com/drive/1vmG10_J8h07qqR3SYr_6ikuJZeKLMHxM#scrollTo=M5cpPbN91B0Y)，提供 `m3e-base` 的类 OpenAI 的 API 调用，支持在 CPU/GPU 环境下运行，可以通过 Docker 部署。

## 快速开始

以下指南假设你已经安装了 Docker 和 Docker Compose。如果使用 CUDA，还需要安装 NVIDIA Container Toolkit ([安装指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html))。


### 构建和运行

1. **克隆仓库**

   ```bash
   git clone https://github.com/zzlphysics/m3e-base-api.git
   cd m3e-base-api
   ```

2. **构建 Docker 镜像**

   ```bash
   docker build -t m3e-base-api .
   ```

   或者使用 Docker Compose：

   ```bash
   docker-compose up --build
   ```

3. **运行容器**

   直接使用 Docker：

   ```bash
   docker run -d -p 6000:6000 -e PORT=6000 -e DEVICE=cpu m3e-base-api
   ```

   或

   ```bash
   docker run -d -p 6000:6000 -e PORT=6000 -e DEVICE=cuda --gpus all m3e-base-api
   ```

   或者使用 Docker Compose：

   ```bash
   docker-compose up
   ```

### 使用 API

发送 POST 请求到 `/v1/embeddings`，包含 JSON 格式的文本数据：

```bash
curl -X POST http://localhost:6000/v1/embeddings \
     -H "Content-Type: application/json" \
     -d '{"input": "Hello, world!"}'
```

## 配置

### 环境变量

- `PORT`：Flask 服务监听的端口（默认为 6000）。
- `DEVICE`：用于运行模型的设备，可以是 `cpu` 或 `cuda`（默认为 `cpu`）。

### Docker Compose

在 `docker-compose.yml` 文件中，你可以修改服务设置，包括端口映射和环境变量。


## 许可证

[MIT](LICENSE)