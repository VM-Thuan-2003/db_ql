import datetime
from bson.objectid import ObjectId
# rule for user

class user:
    def __init__(self, buffer, db) -> None:
        self.buffer = buffer
        self.payload = {
            "status" : False,
            "msg"    : "none msg",
            "buffer" : {
                "fullName" :    self.buffer.fullName,
                "address" :     self.buffer.address,
                "subject" :     self.buffer.subject,
                "tax" :         self.buffer.tax,
                "description" : self.buffer.description,
                "cost" :        self.buffer.cost
            },
            "time_create_user" : datetime.datetime.now()
        }
        self.db = db
    def check_new_user(self):
        cursor  = self.db.find({"fullName" : self.buffer.fullName})
        count = len(list(cursor))
        if count == 0:
            return True
        else:
            return False
    def validation_user(self):
        return
    def load_user(self,id):
        cursor  = self.db.find({"_id" : ObjectId(id)})
        count = len(list(cursor))
        if(count > 0):
            ddb = self.db.find_one({"_id" : ObjectId(id)})
            self.payload["buffer"]["fullName"]    = ddb["fullName"]
            self.payload["buffer"]["address"]     = ddb["address"]
            self.payload["buffer"]["subject"]     = ddb["subject"]
            self.payload["buffer"]["tax"]         = ddb["tax"]
            self.payload["buffer"]["description"] = ddb["description"]
            self.payload["buffer"]["cost"]        = ddb["cost"]
            self.payload["time_create_user"]      = ddb["time_create_user"]
            return user.log_return(self,True)
        else:
            return user.log_return(self,False)
    def new_user(self):
        if user.check_new_user(self) == True:
            return user.log_return(self,True)
        else:
            return user.log_return(self,False)
    def edit_user(self):
        
        return user.log_return(self,False)
    def remove_user(self):
        
        return user.log_return(self,False)
    def log_return(self,status, msg="none msg"):
        self.payload["status"] = status
        self.payload["msg"] = msg
        return self.payload