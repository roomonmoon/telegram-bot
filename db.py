from time import time
import sqlite3

month = 2592000
timeout = 900

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file) 
        self.cursor = self.connection.cursor()

    def add_billing_check(self, user_id, bill_id, tag):
        with self.connection:
            request = self.cursor.execute("SELECT * FROM `check` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            if not bool(len(request)):
                result = self.cursor.execute("INSERT INTO `check` (`user_id`, `bill_id`, `tag`, `time`) VALUES (?,?,?,?)", (user_id, bill_id, tag, time()))
            else:
                self.cursor.execute("DELETE FROM `check` WHERE `user_id` = ?", (user_id,))
                return self.cursor.execute("INSERT INTO `check` (`user_id`, `bill_id`, `tag`, `time`) VALUES (?,?,?,?)", (user_id, bill_id, tag, time()))
                

    def get_billing_check(self, bill_id):
        result = self.cursor.execute("SELECT * FROM `check` WHERE `bill_id` = ?", (bill_id,)).fetchmany()
        if not bool(len(result)):
            return False
        return result[0]
    
    def get_billing_tag(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT tag FROM `check` WHERE `user_id` = ?", (user_id,)).fetchone()
            if not bool(len(result)):
                return False
            return result[0]

    def remove_billing_check(self, bill_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `check` WHERE `bill_id` = ?", (bill_id,))
        
    def remove_timeout_bill(self):
        return self.cursor.execute(f"DELETE FROM `check` WHERE `time` + {timeout} < {time()}")
        
    def add_user_with_tag(self, user_id, tag):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `tag`, `timestart`, `timeleft`) VALUES (?,?,?,?)", (user_id, tag, time(), f"{time()+month}",))
        
    def add_tag(self, title, price):
        with self.connection:
            return self.cursor.execute("INSERT INTO `tags` (`title`, `price`) VALUES (?,?)", (title, price,))

    def get_tags(self):
        with self.connection:
            result = self.cursor.execute("SELECT title, price FROM tags").fetchall()
            set = []
            for title, price in result:
                set.append([title, price])
            return set
        
    def remove_tag(self, title):
        with self.connection:
            if not bool(len(self.cursor.execute("SELECT * FROM `tags` WHERE `title` = ?", (title,)).fetchmany(1))):
                return False
            else:
                self.cursor.execute("DELETE FROM `tags` WHERE `title` = ?", (title,))
                return True
            
            
        
    def get_price(self, title):
        with self.connection:
            result = self.cursor.execute("SELECT `price` FROM `tags` WHERE `title` = ?", (title,)).fetchone()
            return result[0]

        
    def remove_user_with_tag(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `users` WHERE `user_id` = ?", (user_id,))


    def get_user_with_timeleft(self):
        with self.connection:
            return self.cursor.execute(f"SELECT `user_id` FROM `users` WHERE `timeleft` < {time()}").fetchall()
    
    def add_admins(self, user_id, fullname):
        with self.connection:
            return self.cursor.execute("INSERT INTO `admins` (`user_id`, `fullname`) VALUES (?,?)", (user_id, fullname,))