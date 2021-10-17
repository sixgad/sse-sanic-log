# **Server-Sent Events实现实时日志查看器**

SSE(Server-sent events)：服务器发送事件。是基于http协议，和WebSocket的全双工通道（web端和服务端相互通信）相比，SSE只是单通道（服务端主动推送数据到web端），但正是由于此特性，在不需要客户端频繁发送消息给服务端，客户端却需要实时或频繁显示服务端数据的业务场景中可以使用。

### 博客地址

https://paker.net.cn/article?id=24

### 使用方法

拉取项目代码

> git clone git@github.com:sixgad/sse-sanic-log.git

安装依赖包

> pip install requirements.txt

运行

> python run.py

访问 127.0.0.1:8091/index

点击打印日志按钮即可