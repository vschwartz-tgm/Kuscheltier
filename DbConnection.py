import psycopg2
import datetime
import os

class DatabaseConnector():

    def __init__(self, host="192.168.99.100",port="32770", dbname="kuscheltier", user="kuscheltier_user", password="1234"):
        print("DatabaseConnector.__init__")
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

        try:
            self.conn = psycopg2.connect(host=self.host, dbname=self.dbname, port=self.port, user=self.user, password=self.password)
        except:
            raise Exception('connection failed')


    def add_buch(self, genre, ausgewaehlt, path):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Buch (name, datum, uhrzeit, beschreibung, ort, hinweis) VALUES(%s, %s, %s, %s, %s, %s)",(name, datum, uhrzeit, beschreibung, ort, hinweis))
        cur.close()
        self.conn.commit()
        pass


    def add_termin(self, name, datum, uhrzeit, beschreibung, ort, hinweis):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Termine (name, datum, uhrzeit, beschreibung, ort, hinweis) VALUES(%s, %s, %s, %s, %s, %s)",(name, datum, uhrzeit, beschreibung, ort, hinweis))
        cur.close()
        self.conn.commit()
        pass

    def del_termin(self, name):
        cur = self.conn.cursor()
        cur.execute("Delete from Termine where name='"+name+"'")
        cur.close()
        self.conn.commit()
        pass

    def add_pillent(self, name, montag, dienstag, mittwoch, donnerstag, freitag, samstag, sonntag, zeit):
        pass


    def get_buch_list(self):
        pass


    def get_termin_list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from Termine")
        rows = cur.fetchall()
        cur.close()

        print("\nShow me the databases:\n")
        print(rows)
        for row in rows:
            print("   "), row[0]
        pass


    def get_pillen_list(self):
        pass




d = DatabaseConnector()
for i in range(100):
    # d.add_termin("name"+str(i),datetime.date(2005, 11, 18), datetime.time(i%2,1,1),"beschreibung","ort","hinweis")
    d.del_termin("name"+str(i))
d.get_termin_list()



