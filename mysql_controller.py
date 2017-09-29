import mysql.connector
from mysql.connector import errorcode


# Creates a connection with the database 'emergps'
class MySQL_connector:
    def __init__(self, user, password, host):
        try:
            self.cnx= mysql.connector.connect(user=user, password=password,
                                      host=host,
                                      database='emergps')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)



    # Disaster is a dict that contains name, href, location, date and active as keys
    def add_disaster(self, new_disaster):
        cursor = self.cnx.cursor()

        add_disaster = ("INSERT INTO disaster (disaster_name, graphic_url, href, location, created_at, active) VALUES (%s, %s, %s, %s, %s, %s)")

        disaster_date = new_disaster['created_at'][:-6]

        data_disaster = (str(new_disaster['name']), str(new_disaster['graphic_url']),str(new_disaster['href']), str(new_disaster['location']), str(disaster_date), new_disaster['active'])

        # Insert disaster
        cursor.execute(add_disaster, data_disaster)

        # Make sure data is committed to the database
        self.cnx.commit()
        cursor.close()


    # Retrieves a list with the last NUMBER_OF_DISASTERS disasters
    def retrieve_last_disasters(self, number_of_disasters=1):
        cursor = self.cnx.cursor()

        query = ("SELECT * FROM disaster ORDER BY id DESC LIMIT %s OFFSET %s")

        cursor.execute(query, (number_of_disasters,0))

        last_disasters = [{"name": x[1], "graphic_url": x[2], "location": x[4], "href": x[3], "date":x[4]} for x in cursor]

        cursor.close()
        return last_disasters


    # Checks if the disaster given as url parameter is already in the database or not
    def is_retrieved_disaster_new(self, disaster_url):
        last_disaster = self.retrieve_last_disasters()
        return disaster_url == last_disaster[0]['href']