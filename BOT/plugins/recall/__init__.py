from asyncio import events
from email import message
from multiprocessing.synchronize import Event
import random, json
from nonebot import on_command, on_message, on_notice, on_regex, export
from nonebot.permission import SUPERUSER
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.message import Message
from nonebot.adapters.cqhttp.event import MessageEvent, GroupMessageEvent, NoticeEvent, GroupRecallNoticeEvent, FriendRecallNoticeEvent
from nonebot.adapters.cqhttp.utils import unescape
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN, PRIVATE_FRIEND



recall = on_notice(priority=5,block=True)
@recall.handle()
async def recall(bot:Bot, event:NoticeEvent):
    try:
        if event.notice_type == "group_recall":
            pass
#            msg = await bot.get_msg(message_id=event.message_id)
#            user_name = msg["sender"]["nickname"]
#            user_id = msg["sender"]["user_id"]
#            msg_text = msg["message"]
#            group_id = event.group_id
#            sendmsg = "群聊：{0:}\n用户：{1:}\nQQ号：{2:}\n以下消息被撤回：\n{3:}".format(group_id,user_name,user_id,msg_text)
#            await bot.send_group_msg(group_id=*,message=sendmsg)
        elif event.notice_type == "friend_recall":
            msg = await bot.get_msg(message_id=event.message_id)
            user_name = msg["sender"]["nickname"]
            user_id = msg["sender"]["user_id"]
            msg_text = msg["message"]
            sendmsg = "好友：{0:}\nQQ号：{1:}\n以下消息被撤回：\n{2:}".format(user_name,user_id,msg_text)
            await bot.send_group_msg(group_id=*,message=sendmsg)
        else:
            pass
    except:
        print("防撤回出错了！")