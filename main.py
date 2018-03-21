# -*- coding: UTF-8 -*-    或者  #coding=utf-8
from wxpy import *
import time
def login_c():
    pass
bot = Bot(console_qr=1)


all_groups = bot.groups().search()
if len(all_groups)>0 :
    @bot.register(all_groups)
    def reply_my_friend(msg):
        print(msg)

#while True :
#    groups = bot.groups().search(u'拼多多')
#    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#    time.sleep(60*30)
    #for group in groups:
    #    group.send_image('/alidata/www/wxpy/xiaoxi.png')
embed()


