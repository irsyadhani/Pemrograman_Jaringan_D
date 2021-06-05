from tkinter import *
import tkinter as tk
import socket
import threading
import sys
from tkinter import filedialog as fd
import os

class ChatApplication():
    def __init__(self):
        self.users = {}
        self.users['clement'] = {'nama': 'Lionel Messi', 'negara': 'Argentina', 'password': 'surabaya', 'incoming': {},
                               'outgoing': {}}
        self.users['irsyad'] = {'nama': 'Jordan Henderson', 'negara': 'Inggris', 'password': 'surabaya',
                                   'incoming': {}, 'outgoing': {}}
        self.users['rida'] = {'nama': 'rida', 'negara': 'Inggris', 'password': 'surabaya', 'incoming': {},
                              'outgoing': {}}

        self.sign_in()



    def sign_in(self):
        self.login_win = Tk()
        self.login_win.title('Sign In')
        self.login_win.geometry('500x350')
        self.login_win.configure(bg="light blue")

        self.login_user = StringVar()
        self.login_pass = StringVar()

        self.msg1 = tk.Label(self.login_win, text='User Name', relief=GROOVE)
        self.msg1.place(relx=0.2, rely=0.3, anchor=CENTER)

        self.msg2 = tk.Label(self.login_win, text=' Password ', relief=GROOVE)
        self.msg2.place(relx=0.2, rely=0.5, anchor=S)

        self.user_name = Entry(self.login_win, textvariable=self.login_user, relief=GROOVE)
        self.user_name.place(relx=0.6, rely=0.3, anchor=CENTER, width=300)

        self.user_pass = Entry(self.login_win, show="*",
                          textvariable=self.login_pass, relief=GROOVE)
        self.user_pass.place(relx=0.6, rely=0.5, anchor=S, width=300, )

        self.button = tk.Button(self.login_win, text='Sign In', width=20, height=2, command= lambda: self.login(self.login_user.get(), self.login_pass.get()),
                           activebackground="dark grey", activeforeground="red", relief=GROOVE)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.stop = tk.Button(self.login_win, text='EXIT', width=20, command=self.login_win.destroy,
                         bg="red", activebackground="red", relief=GROOVE)
        self.stop.place(relx=0.3, rely=1, anchor=SE)

        self.login_win.mainloop()

    def successLogin(self):
        self.success = Toplevel()
        self.success.geometry("350x250")
        self.success.configure(bg="light green")
        self.success.title("Successfull Sign In")
        self.stop = tk.Button(self.success, text='Success', width=25, height=2, command=self.success.destroy,
                              bg="green", activebackground="light grey", relief=GROOVE)
        self.stop.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.login_win.destroy

    def wrongPass(self):
        self.wrong_pass = Toplevel()
        self.wrong_pass.geometry("350x250")
        self.wrong_pass.title("Wrong PassWord")
        self.wrong_pass.configure(bg="yellow")
        self.stop = tk.Button(self.wrong_pass, text='Wrong Password', width=25, height=2,
                              command=self.wrong_pass.destroy, bg="red", activebackground="red", relief=GROOVE)
        self.stop.place(relx=0.5, rely=0.5, anchor=CENTER)

    def userNotFound(self):
        self.user_not_found = Toplevel()
        self.user_not_found.geometry("350x250")
        self.user_not_found.title("User not Found ")
        self.user_not_found.configure(bg="yellow")
        self.stop = tk.Button(self.user_not_found, text='User not Found Kindly register First', width=30,
                              height=2, command=self.user_not_found.destroy, bg="red", activebackground="red",
                              relief=GROOVE)
        self.stop.place(relx=0.5, rely=0.5, anchor=CENTER)

    def login(self, username, password):
        if(username in self.users and password==self.users[username]['password']):
            self.successLogin()
            self.connect_to_server()
            self.contact_server()
            self.chat_screen()
            # self.chat_screen()
        elif(username in self.users and password!=self.users[username]['password']):
            self.wrongPass()
        else:
            self.userNotFound()

    def connect_to_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect(("127.0.0.1", 8000))
        except:
            print("Server Not found!")
            sys.exit()

    def contact_server(self):
        self.s.send(str.encode(self.login_user.get()))
        self.welcome_msg = self.s.recv(2048).decode()
        if "ERROR" in self.welcome_msg:
            print(self.welcome_msg)
            sys.exit()
        self.is_connected = True

    def recieve_message_from_server(self):
        while self.is_connected:
            message = self.s.recv(2048).decode()
            if self.login_user.get() in message.split(':')[0]:
                message = "Me :" + message.split(':')[1]
            self.chatbox.insert(END, str(message))


    def send_messages_to_server(self):
        message = self.messagebox.get()
        self.s.send(str.encode(message))
        self.messagebox.delete(0, END)

    def send_file_to_server(self):
        self.s.send("FILE".encode())
        self.s.send(str("client_" + os.path.basename(self.filename)).encode())
        file = open(self.filename, "rb")
        print("Send : ", self.filename)
        data = file.read(1024)
        while data:
            self.s.send(data)
            data = file.read(1024)

    def browseFile(self):
        self.filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=self.filetypes)

        self.messageFile.configure(text=self.filename)

    def chat_screen(self):
        self.chatroom_size = '750x450+250+100'
        self.chatroom_title = 'Chatroom ' +str(self.login_user.get())
        self.backgroungcolor = 'pink'
        self.chatbox_size = (90, 25)
        self.messagebox_width = 70
        self.send_button_background_color = 'cyan'
        self.send_button_foreground_color = 'black'

        self.root = Tk()
        self.root.geometry(self.chatroom_size)
        self.root.title(self.chatroom_title)
        self.root.config(bg=self.backgroungcolor)

        self.chatbox = Listbox(self.root, height=self.chatbox_size[1], width=self.chatbox_size[0])
        self.chatbox.grid(row=0, column=0, padx=(35, 20), pady=30, columnspan=3)

        self.messagebox = Entry(self.root, width=self.messagebox_width)
        self.messagebox.grid(row=1, column=0, columnspan=2, padx=(35, 0))
        self.messageFile = Label(self.root, width=50, text="Pilih File")
        self.messageFile.grid(row=3, column=0, columnspan=2, padx=(35, 0))

        self.send_button = Button(self.root, text='Send',
                                  bg=self.send_button_background_color,
                                  fg=self.send_button_foreground_color,
                                  command=self.send_messages_to_server)
        self.send_button.grid(row=1, column=2)
        self.file_button = Button(self.root, text='Browse File',
                                  bg=self.send_button_background_color,
                                  fg=self.send_button_foreground_color,
                                  command=self.browseFile)
        self.file_button.grid(row=3, column=2)

        self.fileSubmit_button = Button(self.root, text='Send File',
                                  bg=self.send_button_background_color,
                                  fg=self.send_button_foreground_color,
                                  command= self.send_file_to_server)
        self.fileSubmit_button.grid(row=4, column=2)

        self.chatbox.insert(END, str(self.welcome_msg))

        listen_for_messages_thread = threading.Thread(target=self.recieve_message_from_server)
        listen_for_messages_thread.start()

        self.root.mainloop()


if __name__ == "__main__":
    chat_app = ChatApplication()

