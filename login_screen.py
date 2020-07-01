import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessage
from PIL import ImageTk, Image
from database_ import database


table = 'users'
#print(my_database.check_val_incol('user1', 'username', table))



"""
Ao inicializar, ira chamar o login_screen que herda a classe login_model
Creating a class of "Frame"
When initializing the class, we need to pass the 'self' and the master

# tela: self.winfo_screenheight() and self.winfo_screenwidth()
"""

class login_model(tk.Frame):
    def __init__(self, title):
        tk.Frame.__init__(self)
        #self.master = master      #<-- Defines the window as self.root
        self.master.title("{}".format(title))
        self.master.resizable(False, False)

        window_height = int(self.winfo_screenheight() * 0.3)
        window_width = int(self.winfo_screenwidth() * 0.3)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.master.geometry("{}x{}+{}+{}".format(400, 220, x_cordinate, y_cordinate))

    def show(self):
        self.lift()

class login_screen(login_model):
    def __init__(self, master):
        title = "Tela de login"
        login_model.__init__(self, title) #<-- Inheritate from login_model
        self.defaultfont = tkFont.Font(family="Helvetica", size="13")
        self.myfont = tkFont.Font(family="Helvetica", size="11", weight="normal", underline=1)
        self.frame = tk.Frame()

        self.create_frames(), self.arrange_frames()
        self.create_widgets(), self.arrange_wigets()
        self.forgot_p = forgot_pass_screen()
        self.master.title('teste')

    def create_frames(self):#MUDEI O CARAIO PRA self.root TIRAR SE DER ERRO N ESQUECER
        self.banner_frame = tk.Frame(self.frame)       # Banner Frame
        self.canvas = tk.Canvas(self.banner_frame, width=395, height=70)
        self.bottom_frame = tk.Frame(self.frame)       # Bottom Frame
        self.login_frame = tk.Frame(self.frame)        # Login Frame
        self.hyper_link_frame = tk.Frame(self.frame)

    def arrange_frames(self):
        self.frame.pack(side=tk.TOP)    #Main Frame DOS OUTROS


        self.banner_frame.pack(side=tk.TOP)
        self.login_frame.pack(side=tk.TOP)
        self.hyper_link_frame.pack(side=tk.TOP)
        self.bottom_frame.pack(side=tk.BOTTOM)
        #self.img = ImageTk.PhotoImage(Image.open("./sources/banner.png"))
        #self.canvas.create_image(20, 20, anchor=tk.N + tk.E, image=img)

        self.canvas = tk.Canvas(self.banner_frame, width=395, height=70)
        self.canvas.pack()

    def create_widgets(self):
        self.label = tk.Label(self.banner_frame, text="Clique aqui", font=self.myfont, fg='blue')
        self.login_text = tk.Label(self.login_frame, text='Login:', font=self.defaultfont)
        self.pass_text = tk.Label(self.login_frame, text='Senha:', font=self.defaultfont)
        self.login_entry = tk.Entry(self.login_frame)
        self.pass_entry = tk.Entry(self.login_frame)
        self.forgot_text = tk.Label(self.hyper_link_frame, text="Esqueci minha senha", font=self.myfont, fg='blue', cursor="arrow")

        self.forgot_text.bind("<ButtonPress-1>", lambda x: self.forgot_p.lift())
        self.login_button = tk.Button(self.bottom_frame, text='Entrar', width=10, height=2, font=self.defaultfont)

    def arrange_wigets(self):
        self.login_text.grid(row=0, column=0, sticky=tk.W), self.login_entry.grid(row=0, column=1, pady=0, sticky=tk.E)
        self.pass_text.grid(row=1, column=0, sticky=tk.W), self.pass_entry.grid(row=1, column=1, pady=0, sticky=tk.E + tk.W)
        self.forgot_text.grid(row=0, column=0, sticky=tk.E)
        self.login_button.grid(row=0, column=0, pady=8, padx=8)

class forgot_pass_screen(login_model):
    def __init__(self):
        title = 'Esqueci minha senha'
        login_model.__init__(self, title)





if __name__ == "__main__":
    root = tk.Tk()
    mainf = login_screen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()











"""
    # Configure database
    config = {
        'host': 'localhost',
        'user': 'root',
        'pass': 'rootpass123',
        'db': 'accounts'
    }
    my_database = database(config['host'], config['user'],
                           config['pass'], config['db'])"""








"""def check_user(self, username, password):
            command = "SELECT user FROM ACCOUNTS WHERE user = '{}' ".format(username)
            db.cursor.execute(command)
            user = db.cursor.fetchone()
            if username != 0:
                command1 = "SELECT pass FROM ACCOUNTS WHERE user = '{}' ".format(username)
                db.cursor.execute(command1)
                passw = db.cursor.fetchone()
                if password is not None:
                    if password == passw:
                        print(password)
                    else:
                        print('nop')
                else:
                    print("Campo 'Senha' vazio.")
            else:
                print("Campo 'Login' vazio.")"""
