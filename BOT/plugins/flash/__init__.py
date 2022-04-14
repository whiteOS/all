from asyncio import events
from email import message
from multiprocessing.synchronize import Event
import random, json
from nonebot import on_command, on_keyword, on_message, on_notice, on_regex, export
from nonebot.permission import SUPERUSER
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.message import Message
from nonebot.adapters.cqhttp.event import MessageEvent, GroupMessageEvent, NoticeEvent, GroupRecallNoticeEvent, FriendRecallNoticeEvent
from nonebot.adapters.cqhttp.utils import unescape
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN, PRIVATE_FRIEND


flash = on_regex(pattern=r'type=flash', priority=5, block=True)
@flash.handle()
async def flash(bot:Bot, event:MessageEvent):
    if event.message_type == "private":
        msg = "发现闪照：\n" + str(event.message).replace("&#91;","[").replace("url=,type=flash&#93;","subType=0]")
        await bot.send_group_msg(group_id=*,message=msg)
#    elif event.message_type == "group":
#        msg = "发现闪照：\n" + str(event.message).replace("type=flash,","")
#        await bot.send_group_msg(group_id=*,message=msg)