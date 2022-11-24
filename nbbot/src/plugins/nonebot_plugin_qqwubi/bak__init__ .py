import re
from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message

qqwubi = on_command("86",aliases={'86 '}, priority=5)
# 输入一个汉字，返回它的编码
def check_wubi(characters):
    with open('qqwubi.txt', mode='r', encoding='utf-8') as f:
        for i in range(1,94943):
            r = f.readline(i)
            chars = re.split(" |\t|\n", maxsplit=1,string = r)
            if characters in chars:
                return r.rstrip('\n')
    return None

@qqwubi.handle()
async def qqwubi_handle(args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    ret = check_wubi(str(arg[0]))
    if ret != None:
        await qqwubi.finish(Message(ret))
    else:
        await qqwubi.finish(Message('QQ五笔查无此字或此词( =^_^= )'))


