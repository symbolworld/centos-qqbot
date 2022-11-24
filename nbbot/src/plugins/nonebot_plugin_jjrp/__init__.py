import random
from datetime import date
from nonebot.plugin import on_command
# from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot,Event, GROUP
from nonebot.adapters.onebot.v11.message import Message

def luck_simple(num):
    if num >= 95:
        return '今日人品爆棚！！！'
    elif num >= 90:
        return '今日人品非常棒!!'
    elif num >= 80:
        return '今日人品还行'
    elif num >= 60:
        return '今日人品及格'
    elif num >= 40:
        return '今日人品小凶，多做好事吧~'
    elif num >= 20:
        return '今日人品大凶，出门注意车辆！'
    else:
        return '今日人品....下雨天注意打雷吧~~'

qqlist = ['3036199716']
jrrp = on_command("jrrp",aliases = {"今日人品"}, priority=50)
@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = 0
    if event.get_user_id() in qqlist:
        lucknum = rnd.randint(90, 100)
    else:
        lucknum = rnd.randint(1,100)
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}，"{luck_simple(lucknum)}"'))


