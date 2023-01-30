from time import time
import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file) 
        self.cursor = self.connection.cursor()

    def add_billing_check(self, user_id, bill_id, tag):
        with self.connection:
            request = self.cursor.execute("SELECT * FROM `check` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            if not bool(len(request)):
                result = self.cursor.execute("INSERT INTO `check` (`user_id`, `bill_id`, `tag`) VALUES (?,?,?)", (user_id, bill_id, tag,))
            else:
                self.cursor.execute("DELETE FROM `check` WHERE `user_id` = ?", (user_id,))
                return self.cursor.execute("INSERT INTO `check` (`user_id`, `bill_id`, `tag`) VALUES (?,?,?)", (user_id, bill_id, tag,))
                
    def get_billing_check(self, bill_id):
        result = self.cursor.execute("SELECT * FROM `check` WHERE `bill_id` = ?", (bill_id,)).fetchmany()
        if not bool(len(result)):
            return False
        return result[0]

    def remove_billing_check(self, bill_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `check` WHERE `bill_id` = ?", (bill_id,))
        
    def add_user_with_tag(self, user_id, tag):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `tag`, `timestart`, `timeleft`) VALUES (?,?,?,?)", (user_id, tag, time(), f"{time()+2592000}",))
        
    def get_tags(self):
        with self.connection:
            result = self.cursor.execute("SELECT title, price FROM tags").fetchall()
            set = []
            for title, price in result:
                set.append([title, price])
            return set
    
    def get_price(self, title):
        with self.connection:
            result = self.cursor.execute("SELECT price FROM tags WHERE title = ?", (title,)).fetchone()
            return result[0]
        
    def get_billing_tag(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT tag FROM `check` WHERE `user_id` = ?", (user_id,)).fetchone()
            if not bool(len(result)):
                return False
            return result[0]


    def cleeaner(self):
        with self.connection:
            return self.cursor.execute(f"SELECT user_id FROM `users` WHERE `timeleft` > {time()}").fetchall()
            