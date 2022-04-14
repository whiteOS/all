from asyncio import events
from http import cookies
from os import stat
from fastapi import Cookie
from multiprocessing.synchronize import Event
import random, json, requests, re
from nonebot import on_command, on_keyword, on_message, on_notice, on_regex, export
from nonebot.permission import SUPERUSER
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.message import Message
from nonebot.adapters.cqhttp.event import MessageEvent, GroupMessageEvent, NoticeEvent, GroupRecallNoticeEvent, FriendRecallNoticeEvent, PrivateMessageEvent
from nonebot.adapters.cqhttp.utils import unescape
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN, PRIVATE_FRIEND

proxies = {'http': "http://127.0.0.1:8888",'https': "https://127.0.0.1:8888"}
cookie = {  'iPlanetDirectoryPro':'lZUwSEoetOf9fDP6G5wJjr','JSESSIONID':'D551614E1C92707957787AFED2056B2B'}
y_building_dict = { "16栋A区":"471","16栋B区":"472","17栋":"451","弘毅轩1栋A区":"141","弘毅轩1栋B区":"148","弘毅轩2栋A区1-6楼":"197","弘毅轩2栋B区":"201","弘毅轩2栋C区":"205","弘毅轩2栋D区":"206","弘毅轩3栋A区":"155","弘毅轩3栋B区":"183","弘毅轩4栋A区":"162","弘毅轩4栋B区":"169","留学生公寓":"450","敏行轩1栋A区":"176","敏行轩1栋B区":"184","行健轩1栋A区":"85","行健轩1栋B区":"92","行健轩2栋A区":"99","行健轩2栋B区":"106","行健轩3栋A区":"113","行健轩3栋B区":"120","行健轩4栋A区":"127","行健轩4栋B区":"134","行健轩5栋A区":"57","行健轩5栋B区":"64","行健轩6栋A区":"71","行健轩6栋B区":"78","至诚轩1栋A区":"1","至诚轩1栋B区":"8","至诚轩2栋A区":"15","至诚轩2栋B区":"22","至诚轩3栋A区":"29","至诚轩3栋B区":"36","至诚轩4栋A区":"43","至诚轩4栋B区":"50"}
y_building_str = '''16栋A区
16栋B区
17栋
弘毅轩1栋A区
弘毅轩1栋B区
弘毅轩2栋A区1-6楼
弘毅轩2栋B区
弘毅轩2栋C区
弘毅轩2栋D区
弘毅轩3栋A区
弘毅轩3栋B区
弘毅轩4栋A区
弘毅轩4栋B区
留学生公寓
敏行轩1栋A区
敏行轩1栋B区
行健轩1栋A区
行健轩1栋B区
行健轩2栋A区
行健轩2栋B区
行健轩3栋A区
行健轩3栋B区
行健轩4栋A区
行健轩4栋B区
行健轩5栋A区
行健轩5栋B区
行健轩6栋A区
行健轩6栋B区
至诚轩1栋A区
至诚轩1栋B区
至诚轩2栋A区
至诚轩2栋B区
至诚轩3栋A区
至诚轩3栋B区
至诚轩4栋A区
至诚轩4栋B区'''
j_building_dict = {'西苑2栋':'9','东苑11栋':'178','西苑5栋':'33','东苑14栋':'132','东苑6栋':'131','南苑7栋':'97','东苑9栋':'162','西苑11栋':'75','西苑6栋':'41','东苑4栋':'171','西苑8栋':'57','东苑15栋':'133','西苑9栋':'65','南苑5栋':'96','西苑10栋':'74','东苑12栋':'179','南苑4栋':'95','东苑5栋':'130','西苑3栋':'17','西苑4栋':'25','外教楼':'180','南苑3栋':'94','西苑7栋':'49','西苑1栋':'1','南苑8栋':'98'}
j_building_str = '''西苑1栋
西苑2栋
西苑3栋
西苑4栋
西苑5栋
西苑6栋
西苑7栋
西苑8栋
西苑9栋
西苑10栋
西苑11栋
东苑4栋
东苑5栋
东苑6栋
东苑9栋
东苑11栋
东苑12栋
东苑14栋
东苑15栋
南苑3栋
南苑4栋
南苑5栋
南苑7栋
南苑8栋
外教楼'''
y_aid = '0030000000002501'
j_aid = '0030000000002502'
j_name = "金盆岭校区"
y_name = "云塘校区"
charge_data = {}
key = ""

charge = on_command("充电费", priority=5, block=True)
@charge.args_parser
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if str(event.get_message()) == "取消":
        await charge.finish("已取消操作..")
    if state["_current_key"] == "area":
        if str(event.get_message()) not in ["金盆岭校区","云塘校区","金盆岭","云塘"]:
            await charge.reject(f"请输入校区:金盆岭校区,云塘校区")
        state[state["_current_key"]] = str(event.get_message())
    if state["_current_key"] == "building":
        if state["area"] in ["金盆岭校区","金盆岭"]:
            if str(event.get_message()) not in j_building_str:
                await charge.reject(f"请按照示例输入楼栋：\n{j_building_str}")
            state[state["_current_key"]] = str(event.get_message())
        if state["area"] in ["云塘校区","云塘"]:
            if str(event.get_message()) not in y_building_str:
                await charge.reject(f"请按照示例输入楼栋：\n{y_building_str}")
            state[state["_current_key"]] = str(event.get_message())
    if state["_current_key"] == "room":
        state[state["_current_key"]] = str(event.get_message())
    if state["_current_key"] == "tran":
        state[state["_current_key"]] = str(event.get_message())
    if state["_current_key"] == "c":
        global key
        key = str(random.randint(1000000000,9999999999))
        await bot.send_group_msg(group_id=653997022,message=f"QQ:{event.get_user_id()}\nkey:{key}")
        state[state["_current_key"]] = str(event.get_message())
    if state["_current_key"] == "key":
        state[state["_current_key"]] = str(event.get_message())



@charge.handle()
async def _(bot: Bot, event: PrivateMessageEvent, state: T_State):
    if str(event.get_message()) == "帮助":
        await charge.finish(f"#充电费\n[校区]\n[楼栋]\n[宿舍号]\n[金额]")
    raw_args = str(event.get_message()).strip()
    if raw_args:
        args = raw_args.split()
        if len(args) == 1:
            state["area"] = args[0]
        if len(args) == 2:
            state["area"] = args[0]
            state["building"] = args[1]
        if len(args) == 3:
            state["area"] = args[0]
            state["building"] = args[1]
            state["room"] = args[2]
        if len(args) == 4:
            state["area"] = args[0]
            state["building"] = args[1]
            state["room"] = args[2]
            state["tran"] = args[3]

@charge.got("area", prompt=f"往哪个校区充呢？\n金盆岭还是云塘\n输入取消即可取消")
@charge.got("building", prompt=f"往哪栋楼充呢？\n如：\n弘毅轩1栋A区\n16栋A区\n西苑1栋\n\n特例：弘毅轩2栋A区1-6楼")
@charge.got("room", prompt=f"房间号呢？\n有字母一定要带上哦！\n如：A110")
@charge.got("tran", prompt=f"请输入金额（元）\n1~999的整数")

async def _(bot: Bot, event: MessageEvent, state: T_State):
    global charge_data
    area = state["area"]
    building = state["building"]
    room = state["room"]
    tran = str(int(float(state["tran"])*100))
    r_room = { "roomid": room, "room": room }
    r_floor =  { "floorid": "", "floor": "" }
    if area in ["金盆岭校区","金盆岭"]:
        charge_data = { 'account':'256395','acctype':'###','aid':j_aid,'areaid':j_name,'areaname':j_name,'building':building,'buildingid':j_building_dict[building],
                        'floor':'','floorid':'','json':'true','paytype':'1','room':room,'roomid':room,'sign':'SH-A7','tran':tran}
        r_area = { "area": j_name, "areaname": j_name }
        r_building = { "buildingid": j_building_dict[building], "building": building }
        query_elec_roominfo = {"aid":j_aid, "account":"256395", "room":r_room, "floor":r_floor, "area":r_area, "building":r_building}
    elif area in ["云塘校区","云塘"]:
        charge_data = { 'account':'256395','acctype':'###','aid':y_aid,'areaid':y_name,'areaname':y_name,'building':building,'buildingid':y_building_dict[building],
                        'floor':'','floorid':'','json':'true','paytype':'1','room':room,'roomid':room,'sign':'SH-A7','tran':tran}
        r_area = { "area": y_name, "areaname": y_name }
        r_building = { "buildingid": y_building_dict[building], "building": building }
        query_elec_roominfo = {"aid":y_aid, "account":"256395", "room":r_room, "floor":r_floor, "area":r_area, "building":r_building}
    else:
        await charge.finish(f"参数错误，请检查")
    jsondata = {"query_elec_roominfo":query_elec_roominfo}
    remian_data ={'jsondata':str(jsondata).replace("\'","\""),
        'funname':'synjones.onecard.query.elec.roominfo',
        'json':'true'}
    remain = requests.request(method='POST', url="http://yktwd.csust.edu.cn:8988/web/Common/Tsm.html", cookies=cookie, data=remian_data)
    await charge.send("目前" + json.loads(remain.text)["query_elec_roominfo"]["errmsg"] + "\n充值成功后约1小时到账\n但数分钟内来电")

@charge.got("c", prompt=f"输入[确认]即可继续充值\n输入[取消]可取消充值")
@charge.got("key", prompt=f"请向我发送本次充值密钥")

async def _(bot: Bot, event: MessageEvent, state: T_State):
    if key == state["key"]:
        r = requests.request(method='POST', url="http://yktwd.csust.edu.cn:8988/web/Elec/PayElecGdc.html", cookies=cookie, data=charge_data)
        await charge.finish(json.loads(r.text)["pay_elec_gdc"]["errmsg"])
    else:
        await charge.reject("key错误！\n\n你是不是想白嫖我？")
    