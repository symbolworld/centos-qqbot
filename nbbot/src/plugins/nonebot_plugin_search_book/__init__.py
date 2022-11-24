from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message
from nonebot.rule import to_me

books_website = ['https://xmsoushu.com/#/','http://www.nlc.cn/','https://ebook2.lorefree.com/','https://book.sciencereading.cn']
books_webname = ['熊猫搜索(集合多网站)：','国家藏书馆：','lorefree：','科学文库(科学类图书)']
search_book = on_command("找书",aliases={'找书单','书籍','找书网站'}, priority=5,rule=to_me)

@search_book.handle()
async def search_book_handle(args: Message = CommandArg()):
    ret = ['\n']
    for i in range(len(books_website)):
        ret.append(str(books_webname[i] + '\n' + books_website[i] + '\n'))
    await search_book.send(Message(ret), at_sender=True)


