import sqlite3

class dataModel:
    """
    DataBase manipulation
    """

    def __init__(self):
        """
        Init data table
        """
        self.db_name = "password.db"
        query = """           
            CREATE TABLE IF NOT EXISTS USERS (
                IdUser INTEGER PRIMARY KEY AUTOINCREMENT, 
                UserName CHAR(50) NOT NULL UNIQUE, 
                UserPassword CHAR(50) NOT NULL);

            CREATE TABLE IF NOT EXISTS SITE_PASSWORD (
                IdSitePassword INTEGER PRIMARY KEY AUTOINCREMENT, 
                SiteName CHAR(50) NOT NULL, 
                SitePassword CHAR(50) NOT NULL, 
                UserName CHAR(50),
                FOREIGN KEY (UserName) REFERENCES USERS(UserName));
        """
        try:
            with self.connect_to_db() as con:
                con.execute("PRAGMA foreign_keys = 1")
                cur = con.cursor()
                cur.executescript(query)
        except sqlite3.Error as err:
            print(err)

    def drop_table(self, table):
        """
        Drop all Table PASSWORD
        """
        query = "DROP TABLE ?"
        with self.connect_to_db() as con:
            con.execute(query, table)
            con.commit()

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
        user = user.lower()
        try:
            with self.connect_to_db() as con:
                query = "SELECT UserPassword FROM USERS WHERE UserName = ?"
                password = con.execute(query, (user,))
                # print(password.fetchone()[0])
                return password.fetchone()[0]
        except sqlite3.Error as err:
            print("get_password_login error: ", err)

    def check_exist_data_login(self, user):
        """Check site and password if exist"""
        try:
            with self.connect_to_db() as con:
                query = "SELECT UserName FROM USERS WHERE UserName = ?"
                username = con.execute(query, (user,))
                username = username.fetchone()
                # print(f"Check user: {username}")
                return username
        except sqlite3.Error as err:
            print("check_exist_data_login error: ", err)

    def add_data_user(self, user, password):
        """
        Adding User and Master Password
        """
        user = user.lower()
        try:
            with self.connect_to_db() as con:
                query = (
                    "INSERT INTO USERS (UserName, UserPassword) VALUES (?,?);"
                )
                task = (user, password)
                con.execute(query, task)
                con.commit()
        except sqlite3.Error as err:
            # print error message
            print("add_data_user error: ", err)

    def change_password_user(self, user, password):
        """
        Change and update user password
        """
        user = user.lower()
        con = self.connect_to_db()
        query = "UPDATE USERS SET UserPassword = ? WHERE UserName = ?"
        task = (password, user)
        try:
            with self.connect_to_db() as con:
                con.execute(query, task)
                con.commit()
        except sqlite3.Error as err:
            print("change_password_user error: ", err)

    def get_password(self, site, user):
        """
        Get a password from a site
        """
        user = user.lower()
        site = site.lower()
        query = "SELECT SitePassword FROM SITE_PASSWORD WHERE UserName = ? AND SiteName = ?"
        try:
            with self.connect_to_db() as con:
                sitePassword = con.execute(query, (user, site))
                sitePassword = sitePassword.fetchone()
                # print(sitePassword)
                return sitePassword[0]
        except sqlite3.Error as err:
            print("get passwor error: ", err)

    def add_password(self, site, password, user):
        """
        Add new site and password data
        """
        site = site.lower()
        user = user.lower()
        query = """
            INSERT INTO SITE_PASSWORD (SiteName, SitePassword, UserName)
            VALUES (?,?,?);
        """
        try:
            with self.connect_to_db() as con:
                con.execute(query, (site, password, user))
                con.commit()
        except sqlite3.Error as err:
            print("add_password error: ", err)

    def check_exist_data(self, site, user):
        """
        Check site and password if exist
        return: True if SiteName exist.
        """
        site = site.lower()
        user = user.lower()
        query = """
            SELECT SiteName FROM SITE_PASSWORD 
            WHERE SiteName = ? AND UserName = ?;
        """
        try:
            with self.connect_to_db() as con:
                siteName = con.execute(query, (site, user))
                siteName = siteName.fetchone()
                if siteName:
                    return True
                else:
                    return False
        except sqlite3.Error as err:
            print("check_exist_data_site error: ", err)

    def update_password(self, site, new_password):
        """
        Update existing site password
        """
        site = site.lower()
        con = self.connect_to_db()
        query = "UPDATE SITE_PASSWORD SET SitePassword = ? WHERE SiteName = ?"
        task = (new_password, site)
        cur = con.cursor()
        cur.execute(query, task)
        con.commit()
        cur.close()
        con.close()

    def deletePassword(self, site, user):
        """
        delete existing site password
        """
        site = site.lower()
        user = user.lower()
        con = self.connect_to_db()
        query = "DELETE FROM SITE_PASSWORD WHERE SiteName = ? AND UserName = ?"
        task = (site, user)
        con.execute(query, task)
        con.commit()
        con.close()

if __name__ == "__main__":
    pass
