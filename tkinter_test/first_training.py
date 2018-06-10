import tkinter as tk

# 初始化对象
window = tk.Tk()
# 给窗口起个名字
window.title("my window")
# 设置窗口的大小
window.geometry("600x400")

# 需要改变的字符串
var = tk.StringVar()
var.set("Hello,python!")

# 这是一个标签,设置说明文字
label_1 = tk.Label(window,
                   textvariable=var,
                   bg="greenyellow",
                   font=("Courier New", 18),
                   width=15, height=1)

# 将label安放在什么地方
label_1.pack()

# 以一个点来固定label的位置
# label_1.place()

# 设置一个点击事件函数
on_hit = False


def hit_me():
    global on_hit
    if on_hit is False:
        on_hit = True
        var.set("You hit me")
    else:
        on_hit = False
        var.set("Hello,python!")


# 设置一个按钮
button = tk.Button(window, text="hit me",
                   width=15, height=1,
                   command=hit_me)

button.pack()

# 不断地刷新窗口
window.mainloop()
