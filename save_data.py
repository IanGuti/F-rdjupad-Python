import sqlite3
import logging

class DataSaver:
    """Class to save the data in a database"""
    def __init__(self, data):
        self.log = logging.getLogger(__name__)
        self.data = data
        
    def save(self):
        """Save the data in a database"""
        try:
            con = sqlite3.connect("my_database.db")
            self.log.info("Connecting to database")
            self.data.to_sql('my_games', con, if_exists='append', index = False)
            self.log.info("Data was added or  to 'my_database'")
            
        except sqlite3.OperationalError as e:
            self.log.warning(e)
            print("OperationalError", e)
        
        # Close connection
        finally:
            if con:
                con.close()