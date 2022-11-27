import re
from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message
__all__=["dit","xin_dit","_98dit"]

qqwubi = on_command("86 ",aliases={'86?','86？'}, priority=5)

dit = {}
xin_dit = {}
_98dit = {}
def create_dict():
    f = open('qqwubi.txt', mode='r', encoding='utf-8')
    list = f.readlines()
    for l in list:
        line = l.strip()
        chars = re.split(" |\t|\n", maxsplit=1, string=line)
        if len(chars) == 2 and chars[0] not in dit:
            dit[chars[0]] = chars[1]
    f.close()
def create_xin_dict():
    with open('xin.txt', mode='r', encoding='utf-8') as f:
        list = f.readlines()
        for l in list:
            line = l.strip()
            chars = re.split(" |\t|\n", maxsplit=1, string=line)
            if len(chars) == 2 and chars[1] not in xin_dit:
                xin_dit[chars[1]] = chars[0]    #xin.txt与qqwubi.txt中的汉字与编码反了

def create_98_dict():
    with open('98.txt', mode='r', encoding='utf-8') as f:
        list = f.readlines()
        for l in list:
            line = l.strip()
            chars = re.split(" |\t|\n", maxsplit=1, string=line)
            if len(chars) == 2 and chars[1] not in _98dit:
                _98dit[chars[1]] = chars[0]    #98.txt与qqwubi.txt中的汉字与编码反了

create_dict()
create_xin_dict()
create_98_dict()

def check_wubi(characters):
    global dit
    ret = ''
    try:
        ret = dit[characters]
    except Exception as e:
        ret = 'NULL'
    finally:
        return str(ret)
def check_xin_wubi(characters):
    global xin_dit
    ret = ''
    try:
        ret = xin_dit[characters]
    except Exception as e:
        ret = 'NULL'
    finally:
        return str(ret)

def check_98_wubi(characters):
    global _98dit
    ret = ''
    try:
        ret = _98dit[characters]
    except Exception as e:
        ret = 'NULL'
    finally:
        return str(ret)

@qqwubi.handle()
async def qqwubi_handle(args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    ret_86,ret_xin,ret_98 = 'NULL','NULL','NULL'
    ret_86 = check_wubi(str(arg[0]))
    ret_xin = check_xin_wubi(str(arg[0]))
    ret_98 = check_98_wubi(str(arg[0]))
    msg =   '【查】：' + arg[0] + '\n' + \
            '86版：   ' + ret_86 + '\n' + \
            '98版：   ' + ret_98 + '\n' + \
            '新世纪：' + ret_xin
    await qqwubi.finish(Message(msg))
