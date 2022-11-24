import re
from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message
__all__=["dit"]

dit = {}
def create_dict():
    f = open('qqwubi.txt', mode='r', encoding='utf-8')
    list = f.readlines()
    for l in list:
        line = l.strip()
        chars = re.split(" |\t|\n", maxsplit=1, string=line)
        if len(chars) == 2 and chars[0] not in dit:
            dit[chars[0]] = chars[1]
    f.close()

create_dict()

qqwubi = on_command("86",aliases={'86 '}, priority=5)

def check_wubi(characters):
    global dit
    ret = ''
    try:
        ret = dit[characters]
    except Exception as e:
        ret = 'NULL'
    finally:
        return str(ret)

@qqwubi.handle()
async def qqwubi_handle(args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    ret = check_wubi(str(arg[0]))
    if ret != 'NULL':
        await qqwubi.finish(Message(arg[0] + '    ' + ret))
    else:
        await qqwubi.finish(Message('QQ五笔查无此字或此词( =^_^= )'))


