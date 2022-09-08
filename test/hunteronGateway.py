import tkinter as tk
from tkinter import messagebox
import os
import uuid

access_mac = ["acde48001122", "acde48001122"]

# 窗口UI
root = tk.Tk()  # 创建窗口
root.title('猎上内网开关')
root.iconbitmap('/Users/mac/Desktop/hunteron/devops-api/test/favicon.ico')
root.minsize(350, 350)

# 窗体内容
tk.Label(root, text="欢迎使用猎上网关服务!", fg="red", font=('Times', 20, 'bold italic')).pack()


# 窗体按钮方法实现
def Proxy_on():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    print("本机mac地址为：", mac)
    if mac in access_mac:
        print("mac地址校验通过：access.")

        os.system('networksetup -setautoproxyurl Wi-Fi http:/proxy.pac')
        os.system('networksetup -setautoproxystate "WI-FI" on')
        messagebox.showinfo("猎上服务", "内网通道已开启")
    else:
        print("mac地址校验失败：failed.")

        messagebox.showinfo("猎上服务", "本机未开通服务，请联系管理员。")


def Proxy_off():
    # os.system('networksetup -setautoproxyurl Wi-Fi http:/proxy.pac')
    os.system('networksetup -setautoproxystate "WI-FI" off')
    messagebox.showinfo("猎上服务", "内网通道已关闭")


def close():
    """
    创建弹窗
    """
    messagebox.showinfo("猎上服务", "内网通道已关闭")


tk.Button(root, text="开启", command=Proxy_on).pack()
tk.Button(root, text="关闭", command=Proxy_off).pack()

root.mainloop()  # 让窗口一直显示，循环
