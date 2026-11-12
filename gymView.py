from mysql import connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Qwert@12345",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from member where id=%s"
            values=(id,)           
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor=super().get_connection()
            query="insert into member(name,place,mobile,plan,fee,joined_date) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New member added successfully..!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=super().get_connection()
            query="select * from member"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            return records
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("No member found..!")
            print(record)
        except Exception as e:
            print(e)
                


            
connection_instance=DbConnect()
print(connection_instance.get_connection())

member_instance=GymMemberManager()
member_instance.post(
    name="Rohan",
    place="Trivandrum",
    mobile="9001455831",
    plan="3 months",
    fee=1000,
    joined_date=datetime.now().strftime('%Y-%m-%d')
)
member_instance.get()   
member_instance.retrieve(id=2)       
