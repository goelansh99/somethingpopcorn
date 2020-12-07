import mysql.connector as mysql

class connector():
    def __init__(self,host='remotemysql.com',database='',user='',password=""):
        self.HOST = host # or "domain.com"
        # database name, if you want just to connect to MySQL server, leave it empty
        self.DATABASE = database
        # this is the user you create
        self.USER = user
        # user password
        self.PASSWORD = password
        # connect to MySQL server
        self.db_connection = mysql.connect(host=self.HOST, database=self.DATABASE, user=self.USER, password=self.PASSWORD)
        print("Connected to:", self.db_connection.get_server_info())
        # enter your code here!

con=connector()
cursor=con.db_connection.cursor()
cursor.execute("use "+str(con.DATABASE))
cursor.execute("""create table if not exists users (
    `id` integer primary key auto_increment not null,
    `name` varchar(255) not null,
    `password` varchar(255) not null,
    `groupid` integer)""")
    
print("[+] Table `users` created")
