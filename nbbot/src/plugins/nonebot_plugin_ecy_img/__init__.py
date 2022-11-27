from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.rule import to_me
import requests,json
__all__=["type_dic"]

# 通过韩小韩api接口，随机返回一张二次元图片，每日一句，风景照，垃圾分类,今日运势
catch = on_command("动漫",aliases={'动漫图片'}, priority=5,rule=to_me)
day = on_command("每日一句",aliases={'每日一句'}, priority=5,rule=to_me)
scenery = on_command("风景照片",aliases={'随机风景照片'}, priority=5,rule=to_me)
wallpaper = on_command("bing壁纸",aliases={'每日壁纸','必应壁纸','必应每日壁纸'}, priority=5,rule=to_me)
gabage = on_command("垃圾分类", aliases={'垃圾分类 '},priority=5,rule=to_me)
horoscope = on_command("今日运势",aliases={'今日运势 '},priority=5,rule=to_me())
girl = on_command("美女福利",aliases={'美女照片','福利','电脑美女'},priority=5,rule=to_me())
girl_phone = on_command("手机美女",aliases={'手机照片'},priority=5,rule=to_me())
joke = on_command("笑话",aliases={'每日一笑'},priority=5,rule=to_me())
lol = on_command("英雄联盟",aliases={'LOL','lol','LOL照片','lol照片'},priority=5,rule=to_me())
# snow = on_command("下雪",aliases={'下雪了'},priority=5,rule=to_me())

@catch.handle()
async def catch_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/acgimg'
    await catch.send(MessageSegment.image(file=f'{msg}'),cache=False)

@day.handle()
async def day_handle(args: Message = CommandArg()):
    message = 'https://api.vvhan.com/api/ian'
    req = requests.get(url=message)
    # await day.send(MessageSegment.image(file=f'{message}'),cache=False)
    await day.send(Message(str(req.text)))

@scenery.handle()
async def scenery_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/view'
    await scenery.send(MessageSegment.image(file=f'{msg}'), cache=False)

@wallpaper.handle()
async def wallpaper_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/bing'
    await wallpaper.send(MessageSegment.image(file=f'{msg}'), cache=False)

@gabage.handle()
async def gabage_handle(args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    s = '\n'
    if len(arg) == 1:
        url = 'https://api.vvhan.com/api/la.ji?lj=' + str(arg[0])
        req = requests.get(url=url)
        json_str = json.loads(req.text)     # {"success":true,"name":"纸张","sort":"可回收物"}
        if json_str['success']:
            s = '名称：\t' + json_str['name'] + '\n' + '类别：\t'+json_str['sort']
    else:
        s = "请输入正确格式：\n@小草 垃圾分类 垃圾名"
    await gabage.finish(Message(s))

type_dic = {
    '白羊座':'aries','金牛座':'taurus','双子座':'gemini','巨蟹座':'cancer',
    '狮子座':'leo','处女座':'virgo','天秤座':'libra','天蝎座':'scorpio',
    '射手座':'sagittarius','摩羯座':'capricorn','水瓶座':'aquarius','双鱼座':'pisces'
       }
# 默认查今日运势
# time_dic = {
#     '今日运势':'today','明日运势':'nextday','一周运势':'week',
#     '一月运势':'month','一年运势':'year','爱情运势':'love'
# }
@horoscope.handle()
async def horoscope_handle(args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    title = ''  # 标题
    time = ''  # 日期
    fortune = '运势'  # 运势
    fortune_all = ''  # 综合运势
    fortune_love = ''  # 爱情运势
    fortune_work = ''  # 学业/工作运势
    fortune_money = ''  # 财富运势

    index_health = ''  # 健康指数
    index_discuss = ''  # 商谈指数
    lucky_color = ''
    lucky_number = ''
    lucky_constellation = ''  # 速配星座
    short_comment = ''  # 短评
    fortune_text = '运势解析'  # 运势解析
    fortune_text_all = ''  # 综合运势
    fortune_text_love = ''  # 爱情运势
    fortune_text_work = ''  # 学业/工业
    fortune_text_money = ''  # 财富运势
    fortune_text_health = ''  # 健康运势
    s = ''
    # 只根据星座判断今日运势
    if len(arg) == 1:
        # url = 'https://api.vvhan.com/api/horoscope?type=scorpio&time=today'
        if arg[0] in list(type_dic.keys()):
            type = type_dic[arg[0]]
            # time = time_dic[arg[1]]
            url = 'https://api.vvhan.com/api/horoscope?' + 'type=' + type + '&time=today'
            req = requests.get(url=url)
            json_str = json.loads(req.text)
            if json_str['success']:
                title = json_str['data']['title']
                time = json_str['data']['time']
                fortune_all = str(json_str['data']['fortune']['all'])
                fortune_love = str(json_str['data']['fortune']['love'])
                fortune_work = str(json_str['data']['fortune']['work'])
                fortune_money = str(json_str['data']['fortune']['money'])
                index_health = json_str['data']['index']['health']
                index_discuss = json_str['data']['index']['discuss']
                lucky_color = json_str['data']['luckycolor']
                lucky_number = json_str['data']['luckynumber']
                lucky_constellation = json_str['data']['luckyconstellation']
                short_comment = json_str['data']['shortcomment']
                fortune_text_all = json_str['data']['fortunetext']['all']
                fortune_text_love = json_str['data']['fortunetext']['love']
                fortune_text_work = json_str['data']['fortunetext']['work']
                fortune_text_money = json_str['data']['fortunetext']['money']
                fortune_text_health = json_str['data']['fortunetext']['health']

                s = '标题：\t' + title + '\n'+ \
                    '更新时间：  ' + time + '\n' + \
                    '运势：\n' + '综合运势：' + fortune_all +'\n' + '爱情运势：' + fortune_love + '\n' + \
                    '学业/工作：' + fortune_work + '\n' + '财富运势：' + fortune_money +'\n' + \
                    '指数：\n' + '健康指数：' + index_health + '\n' + '商谈指数：' + index_discuss + '\n' + \
                    '幸运色：\t' + lucky_color + '\n' + '幸运数字：\t' + lucky_number + '\n' + \
                    '速配星座：\t' + lucky_constellation + '\n' + '短评：' + short_comment + '\n' + \
                    '运势解析：\n' + '综合运势：\n' + fortune_text_all + '\n' + \
                    '爱情运势：\n' + fortune_text_love + '\n' + '学业/工作：\n' + fortune_text_work + '\n' + \
                    '财富运势：\n' + fortune_text_money + '\n' + '健康运势：\n' + fortune_text_health

                # {
                #     "success": true,
                #     "data":
                #         {
                #             "title": "天蝎座今日运势", "time": "11月25日",
                #             "fortune": {"all": 3, "love": 4, "work": 4, "money": 3},
                #             "index": {"health": "82%", "discuss": "80%"},
                #             "luckycolor": "土黄色", "luckynumber": "6", "luckyconstellation": "白羊座",
                #             "shortcomment": "近朱者赤近墨者黑",
                #             "fortunetext":
                #                 {
                #                     "all": "整体运势平平，容易受外界的影响，会是近朱者赤近墨者黑。建议多与积极上进的正能量人群来往，也会有学习取经的机会，及时调整状态。
                #                     生活方面需要提高自律性，不宜在不务正业的无聊事上浪费过多的时间。",
                #                                                     "love": "单身的心思有点浮躁，不宜贸然行动。恋爱中的还需学着主动，保持感情里两人关系的平衡。",
                # "work": "需要旁人的鞭策，才会积极行动起来，否则也容易进入“当一天和尚撞一天钟”的状态。",
                # "money": "维持收支平衡的状态，进账多少就能花出去多少，没有理财的意识，也没存到钱。",
                # "health": "不能再给自己逃避运动找借口，或有体重上升的压力，是时候该落实健康的减肥计划。"
                # }
                # }
                # }

        else:
            s = "请输入正确格式：\n@小草 今日运势 星座\n比如：\n@小草 今日运势 金牛座"

    else:
        s = "请输入正确格式：\n@小草 今日运势 星座\n比如：\n@小草 今日运势 金牛座"
    await horoscope.finish(Message(s))

@girl.handle()
async def girl_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/girl'
    await girl.send(MessageSegment.image(file=f'{msg}'), cache=False)


@girl_phone.handle()
async def girl_phone_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/mobil.girl'
    await girl_phone.send(MessageSegment.image(file=f'{msg}'), cache=False)

@joke.handle()
async def joke_handle(args: Message = CommandArg()):
    message = 'https://api.vvhan.com/api/joke'
    req = requests.get(url=message)
    await joke.send(Message(str(req.text)))

# 怎么返回特效？
# @snow.handle()
# async def snow_handle(args: Message = CommandArg()):
#     message = 'https://api.vvhan.com/api/snow'
#     req = requests.get(url=message)
#     await snow.send(Message(str(req.text)))

@lol.handle()
async def lol_handle(args: Message = CommandArg()):
    msg = 'https://api.vvhan.com/api/lolskin'
    await lol.send(MessageSegment.image(file=f'{msg}'), cache=False)