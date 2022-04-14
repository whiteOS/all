#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
#初始化nb
nonebot.init()
app = nonebot.get_asgi()
#连接驱动
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
#加载插件(除此处其他配置不建议更改)
nonebot.load_builtin_plugins()
nonebot.load_plugins('plugins')
#启动bot
if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")