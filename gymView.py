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
            self.connection = super().get_connection()
            self.cursor = self.connection.cursor()
            query="insert into member(name,place,mobile,plan,fee,joined_date) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New member added successfully..!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            super().get_connection()
            self.cursor = self.connection.cursor()
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
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                query="delete from member where id=%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("Member deleted Successfully..!")
            else:
                print("No member found..!")
        except Exception as e:
            print(e)
    
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder= ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query=f"update member set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                return True, "Member Updated Successfully..!"
            else:
                return False, "No member found..!"
        except Exception as e:
            print(e)           


            
connection_instance=DbConnect()
print(connection_instance.get_connection())

member_instance=GymMemberManager()
member_instance.post(
    name="Rohan",
    place="Trivandrum",
    mobile="9021455802",
    plan="3 months",
    fee=1000,
    joined_date=datetime.now().strftime('%Y-%m-%d')
)
member_instance.get()   
# member_instance.retrieve(id=2)  
# member_instance.delete(id=1)
# member_instance.put(id)    

