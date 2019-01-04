import threading
import csv
import time
import random
import settings

from InstagramAPI import InstagramAPI

class Unfollower(threading.Thread):

    def __init__(self):
        super(Unfollower, self).__init__()
        self._stop_event = threading.Event()

    def run(self):
        self.bulkunfollow()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def bulkunfollow(self):
        api = InstagramAPI(settings.USER_NAME, settings.USER_PW)
        with open("followed_users.txt") as file:
            reader = csv.reader(file)
            users = []
            for row in reader:
                users.extend(row)
            file.close()
        if api.login():
            print("Login succes!")
            for user in users[1:]:
                api.unfollow(user)
                print("unfollowed user " + user)
                i = random.random()
                time.sleep((i + 0.5) * 5)
        else:
            print("Can't login!")
