import urllib.parse

from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.rule import to_me
import requests,json,datetime

# 通过tenapi接口获取
catch = on_command("每日一言",aliases={'每日一句好话'}, priority=5,rule=to_me)
erciyuan = on_command("二次元",aliases={'二次元照片','二次元图片'}, priority=5,rule=to_me)
bing = on_command("必应",aliases={'必应照片','必应图片'}, priority=5,rule=to_me)
# 通过韩小韩api接口获取
history = on_command("历史上的今天", priority=5,rule=to_me)
weibo = on_command("微博热搜",aliases={'微博热搜榜'}, priority=5,rule=to_me)
douyin = on_command("抖音热搜",aliases={'抖音热搜榜'}, priority=5,rule=to_me)
ithot = on_command("IT资讯",aliases={'IT热搜'}, priority=5,rule=to_me)
baidu = on_command("贴吧热搜",aliases={'贴吧热议'}, priority=5,rule=to_me)
# mp3 = on_command("转语音",aliases={'文字转语音'}, priority=5,rule=to_me)
# 搏天随机壁纸
btstu = on_command('随机壁纸',priority=5,rule=to_me)
# 随机
random_image = on_command('美女',aliases={'随机美女','随机美女照片','随机美女图片'},priority=5,rule=to_me)
random_img = on_command('风景照',aliases={'随机风景照'},priority=5,rule=to_me)
random_ecy = on_command('随机二次元',aliases={'随机二次元照片'},priority=5,rule=to_me)
girls = on_command('极品美女照片',aliases={'极品美女图片'},priority=5,rule=to_me)
gqwallpaper = on_command('壁纸',aliases={'高清壁纸'},priority=5,rule=to_me)
setu = on_command('色图',aliases={'随机色图'},priority=5,rule=to_me)

@catch.handle()
async def catch_handle(args: Message = CommandArg()):
    message = 'https://tenapi.cn/yiyan/?format=text'
    req = requests.get(url=message)
    await catch.send(Message(str(req.text)))

#通过tenapi获取
# @history.handle()
# async def history_handle(args: Message = CommandArg()):
#     message = 'https://tenapi.cn/lishi/'
#     req = requests.get(url=message)
#     await history.send(Message(str(req.text)))

#通过韩小韩API获取历史上的今天
@history.handle()
async def history_handle(args: Message = CommandArg()):
    url = 'https://api.vvhan.com/api/hotlist?type=history'
    req = requests.get(url=url)
    json_str = json.loads(req.text)
    if json_str['success']:
        title = json_str['title'] + '\t更新时间：' + json_str['update_time'] + '\n'
        content = ''
        l = len(json_str['data'])
        for i in range(l):
            content += str(json_str['data'][i]['index']) + '.' + json_str['data'][i]['title'] + '\n'
            # content += str(json_str['data'][i]['index'])  + '.' + json_str['data'][i]['title'] + '\n' + json_str['data'][i]['desc'] + '\n\n'
        content = title + content
        try:
            await history.send(Message(content))
        except:
            await history.send(Message('请求异常，等会再获取吧...'))
    else:
        await history.send(Message('获取数据失败'))
#通过韩小韩API获取抖音热搜
@douyin.handle()
async def douyin_handle(args: Message = CommandArg()):
    url = 'https://api.vvhan.com/api/hotlist?type=douyinHot'
    req = requests.get(url=url)
    json_data = json.loads(req.text)
    if json_data['success']:
        title = json_data['title'] + json_data['subtitle'] + '\t更新时间：' + json_data['update_time'] + '\n'
        content = ''
        l = len(json_data['data'])
        if l > 30:
            l = 30
        for i in range(l):
            content += str(json_data['data'][i]['index']) + '.' + json_data['data'][i]['title'] + '\n'
        content = title + content
        data = '热榜榜首链接：\n' + json_data['data'][0]['url']
        try:
            # await weibo.send(Message(content))
            await douyin.send(MessageSegment.text(content + data ))
        except:
            await douyin.send(Message('请求异常，等会再获取吧...'))
    else:
        await douyin.send(Message('获取数据失败'))
#通过韩小韩API获取微博热搜榜
@weibo.handle()
async def weibo_handle(args: Message = CommandArg()):
    url = 'https://api.vvhan.com/api/hotlist?type=wbHot'
    req = requests.get(url=url)
    json_data = json.loads(req.text)
    if json_data['success']:
        title = json_data['title'] + json_data['subtitle'] + '\t更新时间：' + json_data['update_time'] + '\n'
        content = ''
        l = len(json_data['data'])
        if l > 30:
            l = 30
        for i in range(l):
            content += str(json_data['data'][i]['index']) + '.' + json_data['data'][i]['title'] + '\n'
        content = title + content
        data = '热榜榜首链接：\n' + json_data['data'][0]['url']
        try:
            # await weibo.send(Message(content))
            await weibo.send(MessageSegment.text(content + data ))
        except:
            await weibo.send(Message('请求异常，等会再获取吧...'))
    else:
        await weibo.send(Message('获取数据失败'))
#通过韩小韩API获取IT资讯榜
@ithot.handle()
async def ithot_handle(args: Message = CommandArg()):
    url = 'https://api.vvhan.com/api/hotlist?type=itInfo'
    req = requests.get(url=url)
    json_data = json.loads(req.text)
    if json_data['success']:
        title = json_data['title'] + json_data['subtitle'] + '\t更新时间：' + json_data['update_time'] + '\n'
        content = ''
        l = len(json_data['data'])
        if l > 30:
            l = 30
        for i in range(l):
            content += str(json_data['data'][i]['index']) + '.' + json_data['data'][i]['title'] + '\n'
        content = title + content
        data = 'IT资讯榜首链接：\n' + json_data['data'][0]['url']
        try:
            # await weibo.send(Message(content))
            await ithot.send(MessageSegment.text(content))
            await ithot.send(MessageSegment.text(data))
        except:
            await ithot.send(Message('请求异常，等会再获取吧...'))
    else:
        await ithot.send(Message('获取数据失败'))
#通过韩小韩API获取百度贴吧热搜
@baidu.handle()
async def baidu_handle(args: Message = CommandArg()):
    url = 'https://api.vvhan.com/api/hotlist?type=baiduRY'
    req = requests.get(url=url)
    json_data = json.loads(req.text)
    if json_data['success']:
        title = json_data['title'] + json_data['subtitle'] + '\t更新时间：' + json_data['update_time'] + '\n'
        content = ''
        l = len(json_data['data'])
        if l > 30:
            l = 30
        for i in range(l):
            content += str(json_data['data'][i]['index']) + '.' + json_data['data'][i]['title'] + '\n'
        content = title + content
        data = '百度贴吧热搜榜首链接：\n' + json_data['data'][0]['url']
        try:
            await baidu.send(MessageSegment.text(content + data))
            # await baidu.send(MessageSegment.text(data))
        except:
            await baidu.send(Message('请求异常，等会再获取吧...'))
    else:
        await baidu.send(Message('获取数据失败'))
# #通过韩小韩API获取文字转语音
# @mp3.handle()
# async def mp3_handle(args: Message = CommandArg()):
#     arg = args.extract_plain_text().split()
#     if len(arg) == 1:
#         try:
#             text = arg[0]# 要转的文字
#             # url = f'https://api.vvhan.com/song.html?txt={text}'
#             # data = requests.get(url=url)
#             # msg_text = json.loads(data.text)
#             # req = requests.get(url=url)
#             # json_data = json.loads(req.text)
#             audio = f"[CQ:tts,text={text}]"
#             await mp3.send(Message(audio))
#         except:
#             await mp3.send(Message('请求异常，等会再试吧~~'))
#     else:
#         await mp3.send(Message('请输入正确的格式：\n@小草 转语音 文字内容'))



# 图片类
@erciyuan.handle()
async def erciyuan_handle():
    msg = 'https://tenapi.cn/acg'
    await erciyuan.send(MessageSegment.image(file=f'{msg}'), cache=False)

@bing.handle()
async def bing_handle():
    msg = 'https://tenapi.cn/bing/'
    await bing.send(MessageSegment.image(file=f'{msg}'), cache=False)

@btstu.handle()
async def btstu_handle():
    msg = 'https://api.btstu.cn/sjbz/api.php'
    await btstu.send(MessageSegment.image(file=f'{msg}'), cache=False)

@random_image.handle()
async def random_image_handle():
    msg = 'https://api.wuque.cc/random/images'
    await random_image.send(MessageSegment.image(file=f'{msg}'), cache=False)

@random_img.handle()
async def random_img_handle():
    msg = 'https://api.likepoems.com/img/sina/nature'
    await random_img.send(MessageSegment.image(file=f'{msg}'), cache=False)

@random_ecy.handle()
async def random_ecy_handle():
    msg = 'https://www.dmoe.cc/random.php'
    await random_ecy.send(MessageSegment.image(file=f'{msg}'), cache=False)

@girls.handle()
async def girls_handle():
    msg = 'https://api.r10086.com/img-api.php?type=极品美女图片'
    await girls.send(MessageSegment.image(file=f'{msg}'), cache=False)

@gqwallpaper.handle()
async def gqwallpaper_handle():
    msg = 'https://api.ixiaowai.cn/gqapi/gqapi.php'
    await gqwallpaper.send(MessageSegment.image(file=f'{msg}'), cache=False)

# 给setu写一个CD时间
# data_dir = './data/'
# def write_cd(): #写入cd时间
#     with open(data_dir + 'setucd.json',mode='w',encoding='utf-8') as f:
#         CD = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         dict = {
#             "CD": str(CD)
#         }
#         json.dump(dict,f,indent=4)
#
# @setu.handle()
# async def setu_handle():
#     CD_isOK = False
#     with open(data_dir + 'setucd.json',mode='r',encoding='utf-8') as f:
#         content = json.load(f)
#         if (not content):
#             write_cd()
#             CD_isOK = True # 首次发送
#         else:
#             CD = content["CD"]
#             old_CD = datetime.datetime.strptime(CD, "%Y-%m-%d %H:%M:%S")
#             sec = (datetime.datetime.now() - old_CD).seconds
#             if (sec >= 30):
#                 write_cd()
#                 # 发送图片
#                 CD_isOK = True
#             else:
#                 # CD 中，过会再发
#                 CD_isOK = False
#
#     if CD_isOK:
#         url = 'https://api.lolicon.app/setu/v2'
#         req = requests.get(url=url)
#         json_str = json.loads(req.text)
#         # {"error":"","data":[{"pid":81090812,"p":0,"uid":300488,"title":"無題",
#         # "author":"げきねこにゃんにゃんにゃん丸","r18":false,"width":1563,"height":2207,
#         # "tags":["ユニ(プリコネ)","尤妮（公主连结）","白マイクロビキニ","おへそ","肚脐","極上の貧乳","极上贫乳"],
#         # "ext":"png","uploadDate":1587916121000,
#         # "urls":{"original":"https://i.pixiv.re/img-original/img/2020/04/27/00/48/41/81090812_p0.png"},"aiType":0}]
#         # }
#         # json_str['success']:
#         original = json_str['data'][0]['urls']['original']
#         if original:
#             await setu.send(MessageSegment.image(file=f'{original}'), cache=False)
#         else:
#             await setu.send(Message('没有找到色图'))
    # else:
    #     await setu.send(Message('10秒CD中，等会再获取。'))
@setu.handle()
async def setu_handle():
    url = 'https://api.lolicon.app/setu/v2'
    req = requests.get(url=url)
    json_str = json.loads(req.text)
    # {"error":"","data":[{"pid":81090812,"p":0,"uid":300488,"title":"無題",
    # "author":"げきねこにゃんにゃんにゃん丸","r18":false,"width":1563,"height":2207,
    # "tags":["ユニ(プリコネ)","尤妮（公主连结）","白マイクロビキニ","おへそ","肚脐","極上の貧乳","极上贫乳"],
    # "ext":"png","uploadDate":1587916121000,
    # "urls":{"original":"https://i.pixiv.re/img-original/img/2020/04/27/00/48/41/81090812_p0.png"},"aiType":0}]
    # }
    # json_str['success']:
    original = json_str['data'][0]['urls']['original']
    if original:
        try:
            await setu.send(MessageSegment.image(file=f'{original}'), cache=False)
        except:
            await setu.send(Message('请求异常，LSP们过会再获取吧...'))
    else:
        await setu.send(Message('没有找到色图'))
