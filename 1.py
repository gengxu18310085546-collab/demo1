import tkinter as tk
import random

POPUP_COUNT = 130
WIDTH = 220
HEIGHT = 100
BG_COLOR = "#FF477E"
TEXT_COLOR = "white"
DELAY = 120  # 单位毫秒，数值越大弹窗间隔越慢

root = tk.Tk()
root.withdraw()
window_list = []

# 批量生成弹窗并先隐藏
for _ in range(POPUP_COUNT):
    win = tk.Toplevel(root)
    x = random.randint(0, 1400)
    y = random.randint(0, 750)
    win.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
    win.title("中招啦！")
    win.config(bg=BG_COLOR)
    win.attributes("-alpha", 0)  # 先完全隐藏

    label = tk.Label(win,
                     text="哈哈哈哈哈哈~气死你",
                     font=("黑体", 14, "bold"),
                     fg=TEXT_COLOR,
                     bg=BG_COLOR)
    label.pack(expand=True)
    window_list.append(win)

# 递归依次显示弹窗
def show_next(index=0):
    if index >= len(window_list):
        return
    win = window_list[index]
    win.attributes("-alpha", 1)  # 显示弹窗
    root.after(DELAY, show_next, index + 1)

show_next()
root.mainloop()
