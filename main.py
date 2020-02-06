# -*- coding: UTF-8 -*-

from fbchat import log, Client, ThreadType, Message
from termcolor import colored
from getpass import getpass
import qldt_schedule_creator
import colorama
import os
import json
import pickle
import time

colorama.init()


class Lpht(Client):
    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        if author_id != self.uid:
            print(colored('Received new message', 'green'))
            schedule, img_url = qldt_schedule_creator.main(message_object.text)
            self.send(Message(text=schedule), thread_id=author_id)


def start():
    global client
    print("Logging in...")
    session = None
    if os.path.isfile('fb_session'):
        with open('fb_session', 'r') as f:
            session = json.load(f)
    client = Lpht(input("facebook username: "), getpass("facebook password: "), session_cookies=session)
    with open('fb_session', 'w') as f:
        json.dump(client.getSession(), f)
    time.sleep(1)
    print("Hello, i'm Lpht, i'm listening...")
    client.listen()
    print(colored("listen completed!", 'white', 'on_red'))


start()
