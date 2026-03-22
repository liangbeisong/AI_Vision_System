# AI Vision System

一个基于YOLOv8的AI视觉识别系统，使用Python开发，支持物体检测和识别功能。

## 项目特性

- 使用YOLOv8n模型进行高效的物体检测
- 支持实时视频流处理
- 使用PyInstaller打包为独立可执行文件
- 轻量级设计，易于部署

## 环境要求

- Python 3.8+
- Windows操作系统

## 安装步骤

1. 克隆或下载项目文件到本地目录

2. 安装Python虚拟环境（推荐）：

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. 安装依赖包：

   ```bash
   pip install -r requirements.txt
   ```

   如果没有requirements.txt文件，请手动安装以下包：

   ```bash
   pip install ultralytics opencv-python numpy
   ```

## 使用方法

### 开发环境运行

```bash
python main.py
```

### 打包为可执行文件

项目已包含PyInstaller配置文件（main.spec），可直接构建：

```bash
pyinstaller main.spec
```

构建完成后，可执行文件位于 `dist/main/` 目录下。

## 项目结构

```text
AI_Vision_System/
├── main.py              # 主程序文件
├── main.spec            # PyInstaller配置文件
├── pyproject.toml       # 项目配置
├── README.md            # 项目说明
├── models/
│   └── yolov8n.pt       # YOLOv8模型文件
└── build/               # PyInstaller构建文件
    └── main/
```

## 模型说明

项目使用YOLOv8n（Nano）模型，该模型具有以下特点：

- 体积小（约6MB）
- 推理速度快
- 检测精度适中
- 适合边缘设备部署

## 自定义配置

如需修改检测参数，请编辑 `main.py` 文件中的相关配置项。

## 许可证

本项目采用MIT许可证。

## 贡献

欢迎提交Issue和Pull Request来改进项目。

## 联系方式

如有问题，请通过GitHub Issues联系。
