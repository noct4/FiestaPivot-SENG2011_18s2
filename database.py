import os
import sqlite3

class Database(object):

#   Common functions
    def __init__(self):
        db = self.get_db()

        with open("schema.sql") as f:
            db.executescript(f.read())

        self.close(db)

    def get_db(self):
        db = sqlite3.connect('database.db')
        return db

    def close(self, db):
        db.commit()
        db.close()

# Login db functions
    def register_user(self, username, password, email, city, state):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE email=? AND password=?)", (email, password))
        temp =  cursor.fetchone()

        if temp != (0, ):
            # there is already a user using this user name
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO accounts (username, password, email, city, state) VALUES (?, ?, ?, ?, ?)''',(username, password, email, city, state))
            db.commit()
            db.close()
            return 1

    def isValidUser(self, email, password):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts WHERE email=? AND password=?)", (email, password, ))
        temp =  cursor.fetchone()

        isValid = False

        if temp != (0, ):
            # there is already a user using this user name
            isValid = True


        self.close(db)

        return isValid

    def get_name(self, email):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT username FROM accounts WHERE email=?", (email, ))
        temp = cursor.fetchone()

        if temp == False:
            return False

        self.close(db)
        print(temp)
        return temp[0]

# Advertisement db functions
    #UNTESTED
    def create_ad(self, userEmail, title, price, city, state, descr, date, start_time, end_time):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute('''INSERT INTO ads (userEmail, title, price, city, state, descr, status, date, start_time, end_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(userEmail, title, price, city, state, descr, "ACTIVE", date, start_time, end_time,))
        
        self.close(db)
        return True
    
    #UNTESTED
    def updateTitle_ad(self, adID, newTitle):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM ads WHERE adID=?)", (adID))
        temp =  cursor.fetchone()
        
        if temp == 0:
            # Could not find ad assocoated with this adID
            print("Something went wrong, ad does not exist\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO ads (title) VALUES (?)''',(newTitle))
            db.commit()
            db.close()
            return 1

    #UNTESTED
    def updatePrice_ad(self, adID, newPrice):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM ads WHERE adID=?)", (adID))
        temp =  cursor.fetchone()
        
        if temp == 0:
            # Could not find ad assocoated with this adID
            print("Something went wrong, ad does not exist\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO ads (price) VALUES (?)''',(newPrice))
            db.commit()
            db.close()
            return 1

    #UNTESTED
    def updateLocation_ad(self, adID, newLocation):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM ads WHERE adID=?)", (adID))
        temp =  cursor.fetchone()
        
        if temp == 0:
            # Could not find ad assocoated with this adID
            print("Something went wrong, ad does not exist\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO ads (location) VALUES (?)''',(newLocation))
            db.commit()
            db.close()
            return 1

    #UNTESTED
    def updateDescription_ad(self, adID, newDesc):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM ads WHERE adID=?)", (adID))
        temp =  cursor.fetchone()
        
        if temp == 0:
            # Could not find ad assocoated with this adID
            print("Something went wrong, ad does not exist\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO ads (description) VALUES (?)''',(newDesc))
            db.commit()
            db.close()
            return 1
    
    #UNTESTED
    def updateActive_ad(self, adID, newActive):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM ads WHERE adID=?)", (adID))
        temp =  cursor.fetchone()
        
        if temp == 0:
            # Could not find ad assocoated with this adID
            print("Something went wrong, ad does not exist\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO ads (active) VALUES (?)''',(newActive))
            db.commit()
            db.close()
            return 1

# Bid db functions
    #UNTESTED
    def create_bid(self, adID, userID, price, comment):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM bids WHERE adID=? AND userID=?)", (adID, userID))
        temp = cursor.fetchone

        if temp == (0, ): #TODO - CHECK THIS
            # Could not find userID or adID
            print("Something went wrong, could not access correct user or ad\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO bids (adID, userID, price, comment) VALUES (?, ?, ?, ?)''',(adID, userID, price, comment))
            db.commit()
            db.close()
            return 1
    
    #UNTESTED
    def updatePrice_bid(self, adID, userID, newPrice):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM bids WHERE adID=? AND userID=?)", (adID, userID))
        temp =  cursor.fetchone()
        
        if temp == (0, ): #TODO - CHECK THIS
            # Could not find userID or adID
            print("Something went wrong, could not access correct user or ad\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO bids (price) VALUES (?)''',(newPrice))
            db.commit()
            db.close()
            return 1

    #UNTESTED
    def updateComment_bid(self, adID, userID, newComment):
        db = self.get_db()
        cursor = db.cursor()

        cursor.execute("SELECT EXISTS(SELECT 1 FROM bids WHERE adID=? AND userID=?)", (adID, userID))
        temp =  cursor.fetchone()
        
        if temp == (0, ): #TODO - CHECK THIS
            # Could not find userID or adID
            print("Something went wrong, could not access correct user or ad\n")
            db.commit()
            db.close()
            return 0
        else :
            cursor.execute('''INSERT INTO bids (comment) VALUES (?)''',(newComment))
            db.commit()
            db.close()
            return 1