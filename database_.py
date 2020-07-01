import mysql.connector as mysql
#rootpass123
# DATABASE: accounts, TABLE: users

class database(object):
    def __init__(self, host, user, user_pass, database_name):

        self.host, self.database_name = host, database_name
        self.user, self.user_pass = user, user_pass
        try:
            self.datab = mysql.connect(
                host=host,
                user=user,
                passwd=user_pass,
                database=database_name)
            self.cursor = self.datab.cursor()
        except mysql.Error as err:
            print('Something went wrong:\n{}'.format(err))

    def check_val_incol(self, val, col, table):
        self.cursor.execute("SELECT {} FROM {} where {} = '{}' LIMIT 1".format(col,
                                                                               table,
                                                                               col,
                                                                               val))
        if self.cursor.fetchone():
            return True
        else:
            return False
