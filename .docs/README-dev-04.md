# 이러닝 시스템 - chat
```shell
python scripts/add_service_app.py edu chat

>>> import channels.layers
>>> from asgiref.sync import async_to_sync
>>> cl = channels.layers.get_channel_layer()
>>> async_to_sync(cl.send)('test', {'message': 'hello'}0
  File "<console>", line 1
    async_to_sync(cl.send)('test', {'message': 'hello'}0
                          ^
SyntaxError: '(' was never closed
>>> async_to_sync(cl.send)('test', {'message': 'hello'})
>>> async_to_sync(cl.receive)('test')
{'message': 'hello'}

```