import wxpy, time, threading
from tkinter import *

class Wechat_Send_Messenger():
    '''
    Wechat_Send_Messenger能对指定的微信好友发送一条或者多次重发发送一条信息
    get_wechat_text函数目前弃用
    '''
    def __init__(self):
        pass

    def sendwechat(self, wechat_name, wechat_time, wechat_text):
        num = 1
        try:
            bot = wxpy.Bot()
        except:
            Label(self.top, text='微信登陆出错，请核对是否能在微信网页版登录').grid(row=4)

        my_friend = bot.friends().search(wechat_name)[0]
        if wechat_time == 0:
            my_friend.send(wechat_text)
            Label(self.top, text='发送成功').grid(row=4)
        else:
            try:
                while True:
                    my_friend.send(wechat_text)
                    text = '已发送'+ str(num) + '条消息'
                    Label(self.top, text=text).grid(row=4)
                    Button(self.top, text='停', command=bot.logout).grid(row=4, column=1, sticky=E, padx=10, pady=5)
                    #print(text)
                    num = num + 1
                    time.sleep(wechat_time)
            except AssertionError as f:
                print(f)
                bot.logout()
        bot.logout()

    def get_wechat_text(self):
        with open('wechat_text.txt') as f:
            wechat_text = f.read()
        return wechat_text

    def get_info(self):
        #wechat_text = self.get_wechat_text()
        wechat_text = self.tk_messenger.get()
        wechat_time = int(self.tk_time.get())
        wechat_name = self.tk_name.get()
        #创建一个进程执行这个函数
        wechat_t = threading.Thread(target=self.sendwechat, args=(wechat_name, wechat_time, wechat_text))
        wechat_t.start()

    def tk(self):
        self.top = Tk()
        self.top.title('wechat atuo send messenger')
        Label(text='要发送的好友：').grid(row=0, column=0)
        self.tk_name = Entry(self.top)  # 好友
        self.tk_name.grid(row=0, column=1)
        Label(text='重复(0-不重复)：').grid(row=1, column=0)
        self.tk_time = Entry(self.top)  # 重复时间
        self.tk_time.grid(row=1, column=1)
        Label(self.top, text="发送的消息：").grid(row=2, column=0)
        self.tk_messenger = Entry(self.top)  # 输入内容
        self.tk_messenger.grid(row=2, column=1)
        Button(self.top, text="发送", width=10, command=self.get_info).grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Button(self.top, text="退出", width=10, command=self.top.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)
        mainloop()

if __name__ == '__main__':
    wechat = Wechat_Send_Messenger()
    wechat.tk()