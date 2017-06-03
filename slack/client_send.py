from slackclient import SlackClient


API_KEY = ''  # API_KEY can be copied from site above
sc = SlackClient(API_KEY)

sc.api_call('chat.postMessage', channel='#bot-testing', text='Hello world from ipython')


######

import time

sc = SlackClient(API_KEY)

if sc.rtm_connect():
    while True:
        msgs = sc.rtm_read()
        if msgs:
            print msgs
        time.sleep(1)
else:
    print 'Failed to connect'
