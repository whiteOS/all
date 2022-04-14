from nonebot import on_message
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import MessageEvent, PrivateMessageEvent

su = []


wb_matcher = on_message(priority=11)


def get_key(msg_type, id):
        if msg_type == "private":
            return f'收到来自用户-{id}的消息：'

@wb_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    if isinstance(event, PrivateMessageEvent) and event.user_id not in su:
        msg_type = 'private'
        id = event.user_id
        key = get_key(msg_type, id)
        msg = key + event.message
        await bot.send_msg(message_type="private",message=msg,user_id=*)
