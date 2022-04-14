import time
from nonebot import on_request
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import FriendRequestEvent

msg = '''你好！
'''
onr = on_request(priority=10,block=True)


@onr.handle()
async def _(bot: Bot, event: FriendRequestEvent):
    await event.approve(bot)
    user_id = event.get_user_id()
    time.sleep(1)
    await bot.send_private_msg(user_id=user_id, message=msg)