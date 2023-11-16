# 使用官方 Python 运行时作为父镜像
FROM python:3.9

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装 requirements.txt 中列出的所有必需的包
RUN pip install --no-cache-dir -r requirements.txt

# 指定容器启动时运行的命令
CMD ["python", "./main.py"]