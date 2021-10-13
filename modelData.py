import sqlite3
import pandas as pd

class dataModel:
    """
    DataBase manipulation
    """

    def __init__(self):
        """
        Init data table
        """
        self.db_name = 'password.db'
        con = self.connect_to_db()
        query_init = "CREATE TABLE IF NOT EXISTS PASSWORD (ID INTEGER PRIMARY KEY AUTOINCREMENT, SITE CHAR(50) NOT " \
                     "NULL UNIQUE, PASSWORD CHAR(50) NOT NULL, USER CHAR(50) NOT NULL);"
        query_init2 = "CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, USER CHAR(50) NOT NULL " \
                      "UNIQUE, PASSWORD CHAR(50) NOT NULL); "
        con.execute(query_init)
        con.execute(query_init2)
        con.commit()
        con.close()

    def drop_table(self, table):
        """
        Drop all Table PASSWORD
        """
        con = self.connect_to_db()
        query = "DROP TABLE ?"
        con.execute(query, table)
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

    def get_password_login(self, user):
        """
        Get a password from a site
        """
        conn = self.connect_to_db(close=30)
        user = user.lower()
        if conn is not None:
            df = pd.read_sql_query("SELECT * FROM USERS", conn)
            # print(len(df))
            if len(df) > 0:
                try:
                    password = df[df['USER'] == user].iloc[0, 2]
                    del df
                    conn.close()
                    return password
                except:
                    # messagebox.showerror("Error!", "The password site's didn't exists!")
                    print('Password gaada')
        else:
            print("need connection first")

    def check_exist_data_login(self, user):
        """Check site and password if exist"""
        con = self.connect_to_db(close=30)
        df = pd.read_sql_query('SELECT * FROM USERS', con)
        user = user.lower()
        if len(df[df['USER'] == user]) > 0:
            # there is a password
            con.close()
            return True
        else:
            con.close()
            return False

    def add_data_user(self, user, password):
        """
        Adding User and Master Password
        """
        con = self.connect_to_db()
        user = user.lower()
        if con is not None:
            query = "INSERT INTO USERS (USER, PASSWORD) VALUES (?,?);"
            task = (user, password)
            cur = con.cursor()
            cur.execute(query, task)
            con.commit()
            cur.close()
            con.close()
        else:
            # print("connect to db first")
            pass

    def change_password_user(self, user, password):
        """
        Change and update user password
        """
        user = user.lower()
        con = self.connect_to_db()
        query = "UPDATE USERS SET PASSWORD = ? WHERE USER = ?"
        task = (password, user)
        cur = con.cursor()
        cur.execute(query, task)
        con.commit()
        cur.close()
        con.close()

    def get_password(self, site, user):
        """
        Get a password from a site
        """
        conn = self.connect_to_db(close=30)
        user = user.lower()
        site = site.lower()
        if conn is not None:
            df = pd.read_sql_query(f"SELECT * FROM PASSWORD WHERE USER = '{user}'", conn)
            # print(len(df))
            if len(df) > 0:
                try:
                    password = df[df['SITE'] == site].iloc[0, 2]
                    del df
                    conn.close()
                    return password
                except:
                    messagebox.showerror("Error!", "The password site's didn't exists!")
                    # print('Password gaada')
        else:
            print("need connection first")

    def add_password(self, site, password, user):
        """
        Add new site and password data
        """
        site = site.lower()
        user = user.lower()
        conn = self.connect_to_db(close=30)
        query = "INSERT INTO PASSWORD (SITE, PASSWORD, USER) VALUES (?,?,?)"
        task = (site, password, user)
        cur = conn.cursor()
        cur.execute(query, task)
        conn.commit()
        cur.close()
        conn.close()

    def check_exist_data(self, site, user):
        """Check site and password if exist"""
        site = site.lower()
        user = user.lower()
        con = self.connect_to_db(close=30)
        df = pd.read_sql_query('SELECT * FROM PASSWORD', con)
        if len(df[df['SITE'] == site]) > 0:
            if len(df[df['USER']==user]) > 0:
                # there is a password
                con.close()
                return True
            else:
                return False
        else:
            con.close()
            return False

    def update_password(self, site, new_password):
        """
        Update existing site password
        """
        site = site.lower()
        con = self.connect_to_db()
        query = "UPDATE PASSWORD SET PASSWORD = ? WHERE SITE = ?"
        task = (new_password, site)
        cur = con.cursor()
        cur.execute(query, task)
        con.commit()
        cur.close()
        con.close()

    def deletePassword(self, site, user):
        site = site.lower()
        user = user.lower()
        con = self.connect_to_db()
        query = "DELETE FROM PASSWORD WHERE SITE = ? AND USER = ?"
        task = (site, user)
        con.execute(query, task)
        con.commit()
        con.close()

if __name__ == '__main__':
    pass