import tkinter as tk
import sqlite3
from tkinter.messagebox import askyesno
import pandas as pd
from tkinter import simpledialog, messagebox


class dataModel:
    """
    DataBase manipulation
    """

    def __init__(self):
        """
        Init data table
        """
        self.db_name = 'password.db'
        self.is_auth = False
        con = self.connect_to_db()
        query_user = "CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, USER CHAR(50) NOT NULL UNIQUE, PASSWORD CHAR(50) NOT NULL);"
        query_init = "CREATE TABLE IF NOT EXISTS PASSWORD (ID INTEGER PRIMARY KEY AUTOINCREMENT, USER CHAR(50) NOT NULL UNIQUE, SITE CHAR(50) NOT NULL UNIQUE, PASSWORD CHAR(50) NOT NULL);"
        con.execute(query_user)
        con.execute(query_init)
        con.commit()
        con.close()

    def drop_table(self):
        """
        Drop all Table PASSWORD
        """
        con = self.connect_to_db()
        query = "DROP TABLE PASSWORD"
        con.execute(query)
        con.commit()
        con.close()

    def connect_to_db(self, close=60):
        """
        Create a connection to DB file, if doesn't exist, create it
        """
        sql_connection = None
        try:
            sql_connection = sqlite3.connect(self.db_name, close)
            return sql_connection
        except sqlite3.Error as err:
            print(err)
            if sql_connection is not None:
                sql_connection.close()

    def get_password(self, user, site=None):
        """Get password user and site"""
        if site is None:
            conn = self.connect_to_db(close=20)
            if conn is not None:
                df = pd.read_sql_query("SELECT * FROM USERS", conn)
                password = df[df['USER']==user].iloc[0, 2]
                conn.close()
                return password
        else:
            """
            Get a password from a site, if site is not None
            """
            conn = self.connect_to_db(close=30)
            if conn is not None:
                df = pd.read_sql_query("SELECT * FROM PASSWORD", conn)
                # print(len(df))
                if len(df) > 0:
                    try:
                        password = df[df['SITE'] == site].iloc[0, 3]
                        del df
                        conn.close()
                        return password
                    except:
                        # messagebox.showerror("Error!", "The password site's didn't exists!")
                        print("Password doesn't exist")
            else:
                print("need connection first")

    def add_password(self, site, password):
        """
        Add new site and password data
        """
        conn = self.connect_to_db(close=30)
        query = f"INSERT INTO PASSWORD (SITE, PASSWORD) VALUES (?,?)"
        task = (site, password)
        cur = conn.cursor()
        cur.execute(query, task)
        conn.commit()
        cur.close()
        conn.close()

    def check_exist_data(self, site=None, user=None):
        """Check site and password if exist"""
        con = self.connect_to_db(close=30)
        if site is not None:
            df = pd.read_sql_query('SELECT * FROM PASSWORD', con)
            if len(df[df['SITE'] == site]) > 0:
                # there is a password
                con.close()
                return True
            else:
                con.close()
                return False
        if user is not None:
            df = pd.read_sql_query("SELECT * FROM USERS", con)
            if len(df[df['USER']==user]) > 0:
                # there is a user
                con.close()
                return True
            else:
                con.close()
                return False

    def update_password(self, site, new_password):
        """
        Update existing site password
        """
        con = self.connect_to_db()
        query = "UPDATE PASSWORD SET PASSWORD = ? WHERE SITE = ?"
        task = (new_password, site)
        cur = con.cursor()
        cur.execute(query, task)
        con.commit()
        cur.close()
        con.close()


class main_window:
    """Main Window"""

    def __init__(self, master):
        self.data_base = dataModel()
        self.master = master
        self.master.resizable(0, 0)
        self.master.title('Password Manager')
        self.title_label = tk.Label(master=self.master, text='Password Manager', height=2, font=(25))
        self.show_pass_frame = tk.Frame(master=self.master, borderwidth=1)
        self.show_pass_frame_butt = tk.Frame(master=self.master, borderwidth=1)
        self.add_change_frame_butt = tk.Frame(master=self.master, borderwidth=1)
        self.show_pass_frame.grid_columnconfigure(2, weight=1)
        self.show_pass_name_titile = tk.Label(master=self.show_pass_frame, text='Nama ')
        self.show_pass_name = tk.Entry(master=self.show_pass_frame, width=50)
        self.show_pass_title = tk.Label(master=self.show_pass_frame, text='Password ')
        self.show_pass_value = tk.Entry(master=self.show_pass_frame, width=50)
        # susun
        self.show_pass_name_titile.grid(row=0, column=0, sticky='W')
        self.show_pass_name.grid(row=0, column=2)
        self.show_pass_title.grid(row=1, column=0, sticky='W')
        self.show_pass_value.grid(row=1, column=2)
        self.label1 = tk.Label(master=self.show_pass_frame, text=':').grid(row=0, column=1)
        self.label2 = tk.Label(master=self.show_pass_frame, text=':').grid(row=1, column=1)
        self.show_pass_butt = tk.Button(master=self.show_pass_frame_butt, text='Show Password',
                                        command=self.show_password)
        self.show_pass_butt.pack(fill=tk.X)
        self.add_pass_frame_butt = tk.Button(master=self.show_pass_frame_butt, text='Add Password',
                                             command=self.new_window)
        self.add_pass_frame_butt.pack(fill=tk.X)
        self.change_pass_frame_but = tk.Button(master=self.show_pass_frame_butt, text="Change Password",
                                               command=self.change_password_window)
        self.change_pass_frame_but.pack(fill=tk.X)
        # packing
        self.title_label.pack(fill=tk.X)
        self.show_pass_frame.pack(fill=tk.X)
        self.show_pass_frame_butt.pack(fill=tk.X)

    def new_window(self, site=None):
        """
        Launch add_password Window
        """
        self.newWindow = tk.Toplevel(self.master)
        self.app = add_password(self.newWindow, site)

    def change_password_window(self):
        """
        Launch change password window
        """
        self.new_change_pass_window = tk.Toplevel(self.master)
        self.app = change_password(self.new_change_pass_window)

    def show_password(self):
        """
        Show the password in main window
        """
        situs = self.show_pass_name.get()
        print(type(situs), '+' + situs + '+')
        if len(situs) > 0:
            situs = situs.lower()
            password = self.data_base.get_password(site=situs)
            if password is not None:
                self.show_pass_value.delete(0, tk.END)
                self.show_pass_value.insert(0, password)
            else:
                """Site password didn't exist, create the password?"""
                confirm = askyesno(title='Confirmation',
                                   message="{} password didn't exist,\n Do You want to create it first?".format(situs))
                if confirm:
                    self.new_window(situs)

class add_password:
    """Add Password Window window"""

    def __init__(self, master, added_site):
        self.data_base = dataModel()
        self.master = master
        self.added_site = added_site
        self.master.resizable(0, 0)
        self.master.title('Add Site Password')
        self.maintitle = tk.Label(master=self.master, text='Add Site Password', font=(25))
        self.maintitle.pack(fill=tk.X)
        self.frame_form = tk.Frame(master=self.master)
        self.frame_form.columnconfigure(2, weight=1)
        self.name_label_situs = tk.Label(self.frame_form, text='Site Name')
        self.name_password_1 = tk.Label(self.frame_form, text='Enter Password')
        self.name_password_2 = tk.Label(self.frame_form, text='Re Enter Password')
        self.name_label_situs.grid(row=0, column=0, sticky='W')
        self.name_password_1.grid(row=1, column=0, sticky='W')
        self.name_password_2.grid(row=2, column=0, sticky='W')
        # add ":"
        self.frame_form_entry_append = []
        for i in range(3):
            self.name_label = tk.Label(self.frame_form, text=':')
            self.name_label.grid(row=i, column=1)
            self.frame_form_entry = tk.Entry(self.frame_form, width=50)
            self.frame_form_entry.grid(row=i, column=2, sticky='W')
            self.frame_form_entry_append.append(self.frame_form_entry)
        self.frame_form.pack(fill=tk.BOTH)
        self.frame_bottom_butt = tk.Frame(master=self.master)
        self.bottom_butt_add_pass = tk.Button(master=self.frame_bottom_butt, text='Add New Password',
                                              command=self.save_new_password)
        self.bottom_butt_clear_field = tk.Button(master=self.frame_bottom_butt, text='Clear All Field',
                                                 command=self.clear_field)
        # self.frame_bottom_butt.columnconfigure()
        self.bottom_butt_clear_field.grid(row=0, column=0)
        self.bottom_butt_add_pass.grid(row=0, column=2)
        self.frame_bottom_butt.pack()
        if self.added_site is not None:
            self.frame_form_entry_append[0].insert(0, self.added_site)

    def clear_field(self):
        """
        clear all field in the form
        """
        for i in range(3):
            self.frame_form_entry_append[i].delete(0, tk.END)

    def save_new_password(self):
        """
        Save the added site password
        """
        # print(self.frame_form_entry_append[0].get())
        form = []
        for i in range(3):
            form.append(self.frame_form_entry_append[i].get())
        # check password1 & 2 is same
        if form[1] == form[2]:
            if len(form[1]) > 0:
                # check len password
                if len(form[1]) > 7:
                    # check existing password
                    if self.data_base.check_exist_data(site=form[0]):
                        # data ada
                        messagebox.showwarning("Warning!", "This site already exist in Data Base")
                    else:
                        self.data_base.add_password(form[0], form[1])
                        messagebox.showwarning("Information", "Your password have been saved!")
                        self.master.destroy()
                if len(form[1]) > 50:
                    messagebox.showwarning("Warning!", "Max Password Character is 50")
                if len(form[1]) < 8:
                    messagebox.showwarning("Warning!", "Minimum Password Character is 8")
            else:
                print('Password Empty')  # debugging
        else:  # password didn't match
            messagebox.showwarning("Warning!", "Your password didn't match,\nPlease Enter The same password!")


class change_password:
    """Change Password Window Window"""

    def __init__(self, master):
        self.data_base = dataModel()
        self.master = master
        self.master.resizable(0, 0)
        self.master.title('Change Site Password')
        self.maintitle = tk.Label(master=self.master, text='Change Site Password', font=(25))
        self.maintitle.pack(fill=tk.X)
        self.frame_form = tk.Frame(master=self.master)
        self.frame_form.columnconfigure(2, weight=1)
        self.name_label_situs = tk.Label(self.frame_form, text='Site Name')
        self.name_old_password = tk.Label(self.frame_form, text='Old Password')
        self.name_new_password_1 = tk.Label(self.frame_form, text='Enter New Password')
        self.name_new_password_2 = tk.Label(self.frame_form, text='Re Enter New Password')
        self.name_label_situs.grid(row=0, column=0, sticky='W')
        self.name_old_password.grid(row=1, column=0, sticky='W')
        self.name_new_password_1.grid(row=2, column=0, sticky='W')
        self.name_new_password_2.grid(row=3, column=0, sticky='W')
        # add ":"
        self.frame_form_entry_append = []
        for i in range(4):
            self.name_label = tk.Label(self.frame_form, text=':')
            self.name_label.grid(row=i, column=1)
            self.frame_form_entry = tk.Entry(self.frame_form, width=50)
            self.frame_form_entry.grid(row=i, column=2, sticky='W')
            self.frame_form_entry_append.append(self.frame_form_entry)
        self.frame_form.pack(fill=tk.BOTH)
        self.frame_bottom_butt = tk.Frame(master=self.master)
        self.bottom_butt_add_pass = tk.Button(master=self.frame_bottom_butt, text='Change Password',
                                              command=self.change_password)
        self.bottom_butt_clear_field = tk.Button(master=self.frame_bottom_butt, text='Clear All Field',
                                                 command=self.clear_field)
        # self.frame_bottom_butt.columnconfigure()
        self.bottom_butt_clear_field.grid(row=0, column=0)
        self.bottom_butt_add_pass.grid(row=0, column=2)
        self.frame_bottom_butt.pack()

    def clear_field(self):
        """
        clear all field in the form
        """
        for i in range(4):
            self.frame_form_entry_append[i].delete(0, tk.END)

    def change_password(self):
        """
        Performing change password into DB
        """
        form = []
        for i in range(4):
            form.append(self.frame_form_entry_append[i].get())
        # get old password and check if it's on data base
        if self.data_base.check_exist_data(site=form[0].lower()):
            # data exists, get the old password
            old_password = self.data_base.get_password(form[0].lower())
            # check old_password with old password from input
            if old_password == form[1]:
                # old password match, check new password match
                if form[2] == form[3]:
                    # new password match let's process it, that password match the requirement
                    if len(form[2]) > 7:
                        if len(form[2]) < 50:
                            """change the password"""
                            self.data_base.update_password(form[0].lower(), form[2])
                            messagebox.showinfo("Update Successfully!",
                                                "Your password have been updated")
                            self.master.destroy()
                        else:
                            messagebox.showerror("Error!",
                                                 "maximum password length is 50 character")
                    else:
                        messagebox.showerror("Error!",
                                             "minimum password length is 8 character")
                else:
                    # new password didn't match, give exception
                    messagebox.showerror("Error!",
                                         "Your new password didn't same,\nplease enter the same new password!")
            else:
                # old password didn't match
                messagebox.showerror("Error!",
                                     "Your Old Password didn't match, please enter your correct old password")
        else:
            """data doesn't exist in data base"""
            messagebox.showerror("Error!",
                                 "Your site and password didn't exist in data base\nYou can add it first!")
            # self.master.destroy()

class authUser:
    def __init__(self, master):
        self.data_base = dataModel()
        self.master = master
        self.master.resizable(0, 0)
        self.master.title("Auth User")
        self.mainTitle = tk.Label(master=self.master,
                                  text="Login", font=(15))
        self.mainTitle.pack(fill=tk.X)
        self.inputForm_Frame = tk.Frame(master=self.master)
        self.inputForm_Frame.columnconfigure(2, weight=1)
        self.inputForm_user = tk.Label(master=self.inputForm_Frame,
                                       text="User")
        self.inputForm_password = tk.Label(master=self.inputForm_Frame,
                                           text="Password")
        self.inputForm_user.grid(row=0, column=0, sticky='W')
        self.inputForm_password.grid(row=1, column=0, sticky="W")
        self.inputForm_entry_append = []
        for i in range(2):
            label = tk.Label(self.inputForm_Frame, text=":")
            label.grid(row=i, column=1)
            entry = tk.Entry(self.inputForm_Frame, width=30)
            entry.grid(row=i, column=2, sticky="W")
            self.inputForm_entry_append.append(entry)
        self.inputForm_Frame.pack(fill=tk.X)
        self.buttLoginFrame = tk.Frame(master=self.master)
        self.buttLoginFrame.columnconfigure(2, weight=1)
        self.buttonLoginLogin = tk.Button(master=self.buttLoginFrame, text="Login",
                                          command=self.login)
        self.buttonLoginCancel = tk.Button(master=self.buttLoginFrame, text="Cancel",
                                           command=self.cancel)
        self.buttonLoginLogin.grid(row=0, column=0, sticky='E')
        self.buttonLoginCancel.grid(row=0, column=2, sticky='E')
        self.buttLoginFrame.pack()

    def cancel(self):
        self.master.destroy()

    def login(self):
        user = self.inputForm_entry_append[0].get()
        password = self.inputForm_entry_append[1].get()
        if len(user) > 0 and len(password) > 0:
            # let's check that user exist
            if self.data_base.check_exist_data(user=user):
                password_db = self.data_base.get_password(user=user)
                if password_db == password:
                    self.data_base.is_auth = True
                    print('user', user, 'is authenticated')
                    root = tk.Tk()
                    app = main_window(root)
                    root.mainloop()
                    self.master.destroy()
                else:
                    messagebox.showerror("Error!",
                                         "Please enter the correct password!")

def main():
    """
    Launch the application
    """
    root = tk.Tk()
    app = main_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
