# -*- coding: UTF-8 -*-
# @Time : 2021/10/13 14:49
# @Author : zp

import json
import datetime
from sanic import Sanic, response
from sanic_jinja2 import SanicJinja2
import asyncio

app = Sanic(__name__)
app.static('/static', './static')
tp = SanicJinja2(app)

async def get_message(channel):
    # 可替换为自己的日志读取逻辑
    await asyncio.sleep(1)
    s = datetime.datetime.now()
    # 2021-10-14 09:46:53.780 | INFO     | models.handler:addvisit:20 - Visit 新增 id 8348
    log_text = f"{str(s)} | INFO     | main:api:521 - " +f'channel:{channel}' + f' 当前时间：{s.strftime("%Y-%m-%d %H:%M:%S")}'
    return json.dumps({"info":log_text})

@app.route('/index',methods=['GET'])
async def index(request):
    return tp.render('index.html',request)

@app.route('/message')
async def message(request):
    channel = request.args.get("channel",'log')
    async def sample_streaming_fn(response):
            id = 0
            while True:
                id += 1
                await response.write('id: {}\nevent: message\ndata: {}\n\n'.format(id, await get_message(channel)))
    return response.stream(sample_streaming_fn, content_type='text/event-stream')
if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=8091)