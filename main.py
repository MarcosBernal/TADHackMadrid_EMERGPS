from mysql_controller import *
from validator_reliefWEB import *
import time
from multiprocessing import Process, Queue, Lock



# Actively pulls from the endpoint to get new data and alert if a new disaster happens
def pull_scheduler():
    mysql_connection = MySQL_connector("emergps_master", "emergps", "localhost")

    while True:
        response = pull_new_data_from_endpoint()['data'][0]['href']

        print "HI"

        if not mysql_connection.is_retrieved_disaster_new(response):
            disasters = get_additional_data_of_disaster(response)
            mysql_connection.add_disaster(disasters)
            #trigger_action(launch_sms)
            print "Adding disaster"
        else:
            print "Already inside"
        time.sleep(180)




if __name__ == "__main__":
    api_pull_scheduler = Process(target=pull_scheduler())
    api_pull_scheduler.start();
    api_pull_scheduler.join();










