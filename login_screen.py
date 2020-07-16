import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessage
from PIL import ImageTk, Image
from database_ import database
from mainp import changepage, HEIGHT, WIDTH, NAME_COMP, config_window


table = 'users'
#print(my_database.check_val_incol('user1', 'username', table))



"""
Ao inicializar, ira chamar o login_screen que herda a classe login_model
Creating a class of "Frame"
When initializing the class, we need to pass the 'self' and the master

# tela: self.winfo_screenheight() and self.winfo_screenwidth()
"""

class login_model(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master      #<-- Defines the window as self.root


class login_screen(login_model):
    def __init__(self, master):
        config_window(master)
        title = "Welcome to {}".format(NAME_COMP)
        login_model.__init__(self, master) #<-- Inheritate from login_model
        self.master = master
        self.master.title(title)

        self.defaultfont = tkFont.Font(family="Helvetica", size="13")
        self.myfont = tkFont.Font(family="Helvetica", size="11", weight="normal", underline=1)

        # Creating main frame and its widgest
        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)

        self.create_frames(), self.arrange_frames()
        self.create_widgets(), self.arrange_wigets()



    def create_frames(self): #MUDEI O CARAIO PRA self.root TIRAR SE DER ERRO N ESQUECER
        self.banner_frame = tk.Frame(self.frame)       # Banner Frame
        self.canvas = tk.Canvas(self.banner_frame, width=395, height=75)

        self.login_frame = tk.Frame(self.frame)        # Login Frame
        self.hyper_link_frame = tk.Frame(self.frame)   # Esqueci senha Frame
        self.bottom_frame = tk.Frame(self.frame)       # Bottom Frame
    def arrange_frames(self):
        # <-- Frame principal

        self.banner_frame.pack(side=tk.TOP, expand = True, fill = tk.BOTH)
        self.canvas.pack(side = tk.TOP,  expand = True, fill = tk.BOTH, padx= 3, pady= 2)

        self.login_frame.pack(side=tk.TOP)

        self.hyper_link_frame.pack(side=tk.TOP)

        self.bottom_frame.pack(side=tk.BOTTOM, fill = tk.BOTH)

        # Banner in canvas
        self.img = ImageTk.PhotoImage(Image.open("./resources/solar_banner.png"))
        self.canvas.create_image(0,0, anchor = tk.NW, image=self.img)
    def create_widgets(self):
        # Banner Frame
        self.label = tk.Label(self.banner_frame, text="Clique aqui", font=self.myfont, fg='blue')

        # Login Frame
        self.login_text = tk.Label(self.login_frame, text='Login:', font=self.defaultfont)
        self.pass_text = tk.Label(self.login_frame, text='Password:', font=self.defaultfont)
        self.login_entry = tk.Entry(self.login_frame)
        self.pass_entry = tk.Entry(self.login_frame, show="*")

        # Hyper link Frame
        self.forgot_text = tk.Label(self.hyper_link_frame, text="Forgot my password", font=self.myfont, fg='blue')

        # Bottom Frame
        #self.forgot_text.bind("<ButtonPress-1>", lambda x: self.forgot_p.lift())
        self.login_button = tk.Button(self.bottom_frame, text='Enter', width=10, height=2,
                                      font=self.defaultfont,
                                      command=lambda : changepage(self.master))
    def arrange_wigets(self):
        # Login Frame
        self.login_text.grid(row=0, column=0, sticky=tk.W), self.login_entry.grid(row=0, column=1, pady=0, sticky=tk.E)
        self.pass_text.grid(row=1, column=0, sticky=tk.W), self.pass_entry.grid(row=1, column=1, pady=0, sticky=tk.E + tk.W)

        # Hyper link Frame
        self.forgot_text.pack(side=tk.TOP)

        # Bottom Frame
        self.login_button.pack(side=tk.RIGHT, padx= 30)


class forgot_pass_screen(login_model):
    def __init__(self, master):
        config_window(master)
        login_model.__init__(self, master)
        self.master = master
        self.master.title("Forgot my password")
        self.create_widgets(), self.arrange_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="This is page 3")
        self.back = tk.Button(self, text="Voltar", command=lambda : changepage(self.master))
    def arrange_widgets(self):
        self.label.pack(side=tk.TOP, fill="both", expand=True)
        self.back.pack(side=tk.BOTTOM, fill="both", expand=True)










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
