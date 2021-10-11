import tkinter as tk
import modelData
import pandas as pd
import sqlite3
from tkinter import ttk, Canvas, messagebox

class formManage(ttk.Frame):
    def __init__(self, container, name_form):
        super().__init__(container)
        self.columnconfigure(2, weight=2)
        self.label_form = []
        self.entry_form = []
        if name_form == 'show':
            label = ('Site Name\t', "Password\t")
            for i in range(2):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i,column=0, sticky='W')
                ttk.Label(self, text=':').grid(row=i,column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5,pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=1, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(self, text='Show Password',
                                                 command=self.master.showPassword)
            self.show_password_butt.place(x=116, y=69)
            self.quid_butt = ttk.Button(self, text='Quit',
                                        command=self.master.destroy)
            self.quid_butt.place(x=228, y=69)
        elif name_form == 'add':
            label = ('Site Name', 'Enter Password', 'Re-Enter Password')
            for i in range(3):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky='W')
                ttk.Label(self, text=':').grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5,pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=2, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(self, text='Add Password',
                                                 command=self.master.addPassword)
            self.show_password_butt.place(x=117, y=95)
            self.quid_butt = ttk.Button(self, text='Quit',
                                        command=self.master.destroy)
            self.quid_butt.place(x=229, y=95)
        elif name_form == 'change':
            label = ('Site Name', 'Old Password', 'New Password', 'Re-New Password')
            for i in range(4):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky='W')
                ttk.Label(self, text=':').grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5,pady=2)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=3, column=0, sticky='wnse', pady=5)
            ttk.Label(self).grid(row=4, column=0, pady=2)
            self.show_password_butt = ttk.Button(self, text='Change Password',
                                            command=self.master.changePassword)
            self.show_password_butt.place(x=115, y=99)
            self.quid_butt = ttk.Button(self, text='Quit',
                                        command=self.master.destroy)
            self.quid_butt.place(x=227, y=99)
        elif name_form == 'delete':
            label = 'Site Name\t'
            for i in range(1):
                lab = ttk.Label(self, text=label)
                lab.grid(row=i, column=0, sticky='W', padx=5, pady=5)
                ttk.Label(self, text=':').grid(row=i, column=1, sticky='w')
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5, pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=4, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(self, text='Delete Password',
                                                 command=self.master.deletePassword)
            self.show_password_butt.place(x=121, y=39)
            self.quid_butt = ttk.Button(self, text='Quit',
                                        command=self.master.destroy)
            self.quid_butt.place(x=233, y=39)
        elif name_form == 'login':
            label = ('Username', 'Password')
            for i in range(2):
                lab = ttk.Label(self, text=label[i])
                lab.grid(row=i, column=0, sticky='W', padx=5, pady=5)
                ttk.Label(self, text=':').grid(row=i, column=1)
                entry = ttk.Entry(self, width=30)
                entry.grid(row=i, column=2, padx=5,pady=5)
                self.label_form.append(lab)
                self.entry_form.append(entry)
                # self.grid(row=5, column=0, sticky='wnse', pady=5)
            self.show_password_butt = ttk.Button(self, text='Login',
                                                 command='')
            self.show_password_butt.place(x=115, y=65)
            self.quid_butt = ttk.Button(self, text='Quit',
                                        command=self.master.destroy)
            self.quid_butt.place(x=211, y=65)
            self.register_butt = ttk.Button(self, text='Register',
                                            command=self.master.register_user)
            self.register_butt.place(x=115, y=95)
            self.forget_password_butt = ttk.Button(self, text='Forget',
                                                   command=self.master.forget_password)
            self.forget_password_butt.place(x=211, y=95)
            self.login2_butt = ttk.Button(self, text='Login',
                                          command=self.master.login)
            self.login2_butt.place(x=20, y=67, height=53, width=75)

        self.grid(row=1, column=0, sticky='wnse', pady=5)
        # self.pack(fill=tk.BOTH, expand=True)

    def getFromEntry(self):
        value = []
        for entry in self.entry_form:
            value.append(entry.get())
        return value

    def deleteAll(self):
        for entry in self.entry_form:
            entry.delete(0, tk.END)

# class containerFormLogin(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#
#         self.columnconfigure(2, weight=2)
#         self.label_form = []
#         self.entry_form =[]
#         label = ('User Name', 'Password')
#         for i in range(2):
#             lab = ttk.Label(self, text=label[i])
#             lab.grid(row=i, column=0, sticky='W')
#             ttk.Label(self, text=':').grid(row=i, column=1)
#             entry = ttk.Entry(self, width=30)
#             entry.grid(row=i, column=2)
#             self.label_form.append(lab)
#             self.entry_form.append(entry)
#         self.grid(row=1, column=0)
#         # self.

# class ContainerFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#
#         self.name_frame = 'Login'
#         self.att = {'padx': 5, 'pady': 5}
#         options = self.att
#         self.label_name = ttk.Label(self, text=self.name_frame, font=("Arial", 14, 'bold'))
#         self.label_name.pack()
#         # self.label_name.configure(underline=True)
#         self.canvas = Canvas(self, height=3, width=100)
#         self.line_under_label = self.canvas.create_line(5, 2, 300, 2)
#         self.canvas.pack(fill=tk.BOTH)
#         self.FrameLoginForm(options)
#
#         self.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
#     def login(self):
#         print('master', self.master.masterAuth)
#         self.master.masterAuth = True
#         self.terminateLoginForm()
#         self.FrameShowPass(self.att)
#         # return True
#
#     def cancel(self):
#         self.master.destroy()
#
#     def FrameShowPass(self, options):
#         self.name_frame = 'Show Password'
#         self.label_name.configure(text=self.name_frame)
#         self.form_frameShow = ttk.Frame(self)
#         self.form_frameShow.columnconfigure(0, weight=1)
#         self.form_frameShow.columnconfigure(2, weight=2)
#         self.form_label1Show = ttk.Label(self.form_frameShow, text='User Name')
#         self.form_label1Show.grid(row=0, column=0, sticky='w', **options)
#         self.form_label2Show = ttk.Label(self.form_frameShow, text="Password")
#         self.form_label2Show.grid(row=1, column=0, sticky='w', **options)
#         self.form_frame_entry_show_append = []
#         for i in range(2):
#             ttk.Label(self.form_frameShow, text=':').grid(row=i, column=1)
#             entry = ttk.Entry(self.form_frameShow, width=30)
#             entry.grid(row=i, column=2)
#             self.form_frame_entry_show_append.append(entry)
#         self.form_frameShow.pack()
#
#     def FrameLoginForm(self, options):
#         self.form_frame = ttk.Frame(self)
#         # login form
#         self.form_frame.columnconfigure(0, weight=1)
#         self.form_frame.columnconfigure(2, weight=2)
#         self.form_label1 = ttk.Label(self.form_frame, text='User Name')
#         self.form_label1.grid(row=0, column=0, sticky='w', **options)
#         self.form_label2 = ttk.Label(self.form_frame, text="Password")
#         self.form_label2.grid(row=1, column=0, sticky='w', **options)
#
#         self.form_frame_entry_append = []
#         for i in range(2):
#             ttk.Label(self.form_frame, text=':').grid(row=i, column=1)
#             entry = ttk.Entry(self.form_frame, width=30)
#             entry.grid(row=i, column=2)
#             self.form_frame_entry_append.append(entry)
#         self.form_frame.pack(**options)
#
#         self.form_frameMisc = tk.Label(self, text='', font=(15))
#         self.form_frameMisc.pack()
#         self.form_butt_frame = ttk.Frame(self)
#         self.form_butt_login = ttk.Button(self.form_butt_frame, text='Login',
#                                           command=self.login)
#         self.form_butt_login.grid(row=0, column=1, sticky='W',padx=10)
#         self.form_butt_cancel = ttk.Button(self.form_butt_frame, text='Cancel',
#                                            command=self.cancel)
#         self.form_butt_cancel.grid(row=0, column=2, sticky='E', padx=10)
#         # self.form_butt_frame.pack(padx=20)
#         self.form_butt_frame.place(x=85, y=100)
#
#     def terminateLoginForm(self):
#         self.form_frame.pack_forget()
#         self.form_butt_frame.place_forget()
#         self.form_frameMisc.pack_forget()
#
# class ControlFrame(ttk.Labelframe):
#     def __init__(self, container):
#
#         super().__init__(container)
#         self['text'] = 'Options'
#         # self.isAuth = False
#
#         # # radio button
#         # self.selcted_value = tk.IntVar()
#         # if self.master.masterAuth:
#         # #     ttk.Radiobutton(self, text='Login', value=0,
#         # #                     variable=self.selcted_value,
#         # #                     command=self.change_frame)
#         # #     # if self.master.masterAuth:
#         # #     #     break
#         # # else:
#         #     ttk.Radiobutton(self, text='Show Password', value=1,
#         #                     variable=self.selcted_value,
#         #                     command=self.change_frame).grid(row=0, column=1, padx=5, pady=5, sticky='w')
#         #     ttk.Radiobutton(self, text='Add Password', value=2,
#         #                     variable=self.selcted_value,
#         #                     command='').grid(row=1, column=0, padx=5, pady=5, sticky='w')
#         #     ttk.Radiobutton(self, text='Delete Password', value=3,
#         #                     variable=self.selcted_value,
#         #                     command='').grid(row=1, column=1, padx=5, pady=5, sticky='w')
#         #     self.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
#
#         # # login frame
#         # self.loginFrame = ttk.Frame(container)
#         # self.login_title = ttk.Label(self.loginFrame, text='Login')
#         # self.login_title.pack()
#
#         # Form Frame Container
#         self.frames = {}
#         self.frames[0] = ContainerFrameForm(
#             container,
#             'Login'
#         )
#
#         self.change_frame()
#
#     def change_frame(self):
#         frame = self.frames[self.selcted_value.get()]
#         frame.tkraise()
#
class containerLabel(ttk.Frame):
    def __init__(self, container, name):
        super().__init__(container)

        self.label = ttk.Label(self, text=name, font=("Arial", 14))
        self.label.pack(padx=5, pady=5)
        self.grid(row=0, column=0, sticky='we')
        # self.pack(expand=True)

class containerButt_opt(ttk.Labelframe):
    def __init__(self, container):
        super().__init__(container)
        self.rad_value = tk.IntVar()
        ttk.Radiobutton(
            self,
            text='Show Password',
            value=0,
            variable=self.rad_value,
            command=self.master.updateContainer2
        ).grid(row=0,column=0, padx=5, pady=5, sticky='w')
        ttk.Radiobutton(
            self,
            text='Add Password',
            value=1,
            variable=self.rad_value,
            command=self.master.updateContainer2
        ).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        ttk.Radiobutton(
            self,
            text='Change Password',
            value=2,
            variable=self.rad_value,
            command=self.master.updateContainer2
        ).grid(row=0, column=1, padx=5, pady=5, sticky='w')
        ttk.Radiobutton(
            self,
            text='Delete Password',
            value=3,
            variable=self.rad_value,
            command=self.master.updateContainer2
        ).grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.grid(row=2, column=0, sticky='nswe')
        # self.pack(2, fill=tk.BOTH)

# Main app
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Password Manager')
        self.resizable(False, False)
        self.dataModel = modelData.dataModel()
        self.masterAuth = False
        self.whoami = ''
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(0, weight=1)
        # self.title_label = ttk.Labelframe(self)
        self.title_label_frame = {}
        for name, label in (('login', 'Login'),
                            ('show', 'Show Password'),
                            ('delete', 'Delete Password'),
                            ('change', 'Change Password'),
                            ('add', 'Add Password')):
            self.title_label_frame[name] = containerLabel(self, label)
        self.container_frame = dict()
        self.container_frame = {
            'login': formManage(self, 'login'),
            'add': formManage(self, 'add'),
            'show': formManage(self,'show'),
            'delete': formManage(self,'delete'),
            'change': formManage(self, 'change')
        }
        self.container_frame['login'].tkraise()
        self.updateContainer()
        # print(self.container_frame)
        # self.container_Butt_opt['show'].tkraise()

    def showPassword(self):
        print('debug, password appears')
        [site, _] = self.container_frame['show'].getFromEntry()
        # if len(password) < 1 and len(site):
        #     self.container_frame['show'].deleteAll()
        if self.dataModel.check_exist_data(site, self.whoami):
            pwd = self.dataModel.get_password(site, self.whoami)
            self.container_frame['show'].entry_form[1].delete(0, tk.END)
            self.container_frame['show'].entry_form[1].insert(0, pwd)
        else:
            messagebox.showerror("Error!",
                                 "Your data doesn't exist, you can add it first")

    def addPassword(self):
        [site, pwd1, pwd2] = self.container_frame['add'].getFromEntry()
        # print('debug add password', val)
        # print()
        if pwd1 == pwd2:
            if 7 < len(pwd1) < 50:
                if not self.dataModel.check_exist_data(site, self.whoami):
                    self.dataModel.add_password(site, pwd1, self.whoami)
                    messagebox.showinfo("Success!",
                                        "Your password have been saved!")
                    self.container_frame['add'].deleteAll()
                else:
                    messagebox.showerror("Error!",
                                         "Your password didn't saved!\nYour password is currently exist in data base!")
            else:
                messagebox.showerror("Error!",
                                     "Your password must contain 8 up to 50 character!")
        else:
            messagebox.showerror("Error!",
                                 "Your password didn't same!/nPlease enter the same password!")

    def deletePassword(self):
        # print('test delete password button')
        [site] = self.container_frame['delete'].getFromEntry()
        if self.dataModel.check_exist_data(site, self.whoami):
            self.dataModel.deletePassword(site, self.whoami)
            messagebox.showinfo("Success!",
                                f"Data {site} password have been deleted!")
        else:
            messagebox.showerror("Error!",
                                 f"Your {site} site doesn't exists!")

    def changePassword(self):
        print('debug test change password button')
        [site, oldPass, newPass1, newPass2] = self.container_frame['change'].getFromEntry()
        if newPass1 == newPass2:
            if 7 < len(newPass1) < 50:
                # check existing user and password is dealing with it
                if self.dataModel.check_exist_data(site, self.whoami):
                    if oldPass == self.dataModel.get_password(site, self.whoami):
                        self.dataModel.update_password(site, newPass1)
                        messagebox.showinfo("Success!",
                                            f"Your {site} password updated.")
                    else:
                        messagebox.showerror("Error!",
                                             "Please enter correct old password!")
                else:
                    messagebox.showerror("Error!",
                                         "Your site didn't exist in data base")
            else:
                messagebox.showerror("Error!",
                                     "Password must have 8 to 50 character")
        else:
            messagebox.showerror("Error!",
                                 "Please enter the same new Password correctly!")

    def updateContainer(self):
        if not self.masterAuth:
            container = self.container_frame['login']
            label = self.title_label_frame['login']
            label.tkraise()
            container.tkraise()
        elif self.masterAuth:
            container = self.container_frame['show']
            label = self.title_label_frame['show']
            label.tkraise()
            container_opt = containerButt_opt(self)
            self.container_frame_opt = container_opt
            container_opt.tkraise()
            container.tkraise()

    def updateContainer2(self):
        self.grid_rowconfigure(1, weight=2)
        name = self.container_frame_opt.rad_value.get()
        opt = ''
        if name == 0:
            opt = 'show'
            self.container_frame[opt].deleteAll()
        elif name == 1:
            opt = 'add'
            self.container_frame[opt].deleteAll()
        elif name == 2:
            opt = 'change'
            self.container_frame[opt].deleteAll()
        elif name == 3:
            opt = 'delete'
            self.container_frame[opt].deleteAll()

        container = self.container_frame[opt]
        label = self.title_label_frame[opt]
        label.tkraise()
        # container.grid_forget()
        # container.grid(row=1, column=0)
        container.tkraise()
        print('container', container)

    def login(self):
        [user, password] = self.container_frame['login'].getFromEntry()
        if self.dataModel.check_exist_data_login(user):
            pwd = self.dataModel.get_password_login(user)
            print('db', pwd, 'form', password)
            if pwd == password:
                self.masterAuth = True
                messagebox.showinfo("Information",
                                    "You have been Logged in")
                self.whoami = user
                self.updateContainer()
            else:
                messagebox.showerror("Error!",
                                     "Your Password incorrect!\nPlease Enter Correct Password!")
        else:
            messagebox.showerror("Error!",
                                 "Your username didn't exist or wrong!,\nPlease enter your correct username or contact developer!")

    def register_user(self):
        pass

    def forget_password(self):
        pass


if __name__ == '__main__':
    app = App()
    # formManage(app, 'show')
    # containerFormLogin(app)
    app.mainloop()