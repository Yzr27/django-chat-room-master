# 使用官方 Python 3.8 基础镜像
FROM python:3.8

# 维护者信息
LABEL maintainer="twtrubiks"

# 确保 Python 输出直接在终端中打印，而不是首先被缓冲
ENV PYTHONUNBUFFERED=1

# 创建工作目录
RUN mkdir /django_chat_room
WORKDIR /django_chat_room

# 复制项目文件到工作目录
COPY . /django_chat_room/

# 安装系统依赖，特别是为了 `mysqlclient`
RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
RUN pip install -r requirements.txt

# 暴露端口8000用于访问 Django 应用
EXPOSE 8000

# 容器启动时执行的命令，运行 Django 服务
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
