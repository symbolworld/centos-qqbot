
import nonebot
from nonebot import require

# 设置一个定时器
timing = require("nonebot_plugin_apscheduler").scheduler

# 设置在09:00发送信息
@timing.scheduled_job("cron", hour='09', minute='00',  second = '00' ,id="dingshi")
async def _():
    (bot,) = nonebot.get_bots().values()

    await bot.send_msg(
        message_type="group",
        # 群号
        group_id=191321985,
        message='大家早上好~~(_^_^_)~~~来自小草的每日问候。'
    )
