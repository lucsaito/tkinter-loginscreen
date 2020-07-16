from login_screen import *
import login_screen as ls

HEIGHT = 210
WIDTH = 400
NAME_COMP = "SimpleScreen"
pagenum = 1


def config_window(root):
    window_height = int(root.winfo_screenheight() * 0.3)
    window_width = int(root.winfo_screenwidth() * 0.3)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))
    root.resizable(False, False)


def changepage(root):
    # The idea is to destroy all the widgets then build another page when the button is pressed.
    global pagenum
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        ls.forgot_pass_screen(root).pack(side="top", fill="both", expand=True)
        pagenum = 2
    else:
        ls.login_screen(root).pack(side="top", fill="both", expand=True)
        pagenum = 1

if __name__ == "__main__":
    root = tk.Tk()
    main = ls.login_screen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()