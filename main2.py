# -*- coding: UTF-8 -*-    或者  #coding=utf-8
from wxpy import *
import time
import random
def login_c():
    pass
def prn_obj(obj): 
  print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()]) 
bot = Bot(console_qr=1)
tuling = Tuling(api_key='7964d3c1c34f443f81b9d4b44abfc6f4')
remind=ensure_one(bot.groups().search(u'红包提醒2018群'))
list1 = [u'帮我签到团 签到一下谢谢！', u'谁还没签到团签到的，签到一下。',u'签到领一下红包',u'谁能帮我签到一下？谢谢啦！！',u'扫码签到团签到']
groups = bot.groups().search(u'拼多多')
dict={}#房间发言次数字典
currentindex=0
listimg=['xiaoxi.png','chaoqiandao.jpg','weiqiandao.jpg','xiaoweiqiandao.jpg']


for iterating_var in groups:
    dict[iterating_var.raw['UserName']]=0
    #print(dict[iterating_var.raw['EncryChatRoomId']])
    #print iterating_var.name,iterating_var.raw['UserName']

    
all_groups = bot.groups().search()
print(all_groups)
if len(all_groups)>0 :
    @bot.register(all_groups)
    def reply_my_friend(msg):
        print(msg)
        dict[msg.raw['FromUserName']]=dict[msg.raw['FromUserName']]+1
        if msg.is_at==True :
            remind.send(msg)
        if msg.type=='Note' :
            if msg.text==u'收到红包，请在手机上查看':
                remind.send(msg.create_time)
                remind.send(msg)
                print(msg)
# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    time.sleep(2)
    new_friend.send(u'你好,你是做什么的。')
    
    
@bot.register(Friend, TEXT)
def print_friend_msg(msg):
    global currentindex
    #发送者名称
    if msg.sender.name==u'皮皮超' :
        if msg.text=='cmd' :
            return '\n'.join(listimg)
        elif msg.text=='0' :
            currentindex=0
            return listimg[0]
        elif msg.text=='1' :
            currentindex=1
            return listimg[1]
        elif msg.text=='2' :
            currentindex=2
            return listimg[2]
        elif msg.text=='3' :
            currentindex=3
            return listimg[3]
        elif msg.text=='index' :
            return listimg[currentindex]
    time.sleep(7)
    time.sleep(random.randint(1,4))
    res=tuling.reply_text(msg)
    #res=res+'(主人不在,机器人自动回复,有事请留言.)'
    
    return res

# 进入 Python 命令行、让程序保持运行
#embed()
# 或者仅仅堵塞线程
# bot.join()
time.sleep(60*3)
while True :
    for group in groups:
        if dict[group.raw['UserName']] > 5 :
            dict[group.raw['UserName']]=0
            time.sleep(2)
            group.send_image('/alidata/www/wxpy/'+listimg[currentindex])
            time.sleep(1)
            group.send(list1[random.randint(0,len(list1)-1)])
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(60*27)
bot.join()



