import time
import random

from slackclient import SlackClient


jokes = [
    'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',
    'What is the difference between a snowman and a snowwoman? ... Snowballs.',
    'Life is all about perspective. The sinking of the Titanic was a miracle to the lobsters in the ship\'s kitchen.',
    'I want to die peacefully in my sleep, like my grandfather.. Not screaming and yelling like the passengers in his car.',
    'When wearing a bikini, women reveal 90 % of their body... men are so polite they only look at the covered parts.',
    'Just read that 4,153,237 people got married last year, not to cause any trouble but shouldn\'t that be an even number?',
]

python_lines = [
    (
        ('King Arthur', 'Look, you stupid bastard, you\'ve got no arms left!',),
        ('Black Knight', 'Yes I have.',),
        ('King Arthur', 'Look!',),
        ('Black Knight', 'Just a flesh wound.'),
    ),
    (
        ('Black Knight', "'Tis but a scratch."),
        ('King Arthur', "A scratch!? Your arm's off!"),
        ('Black Knight', "No, it isn't."),
        ('King Arthur', "Well, what's that then?!"),
        ('Black Knight', "I've had worse."),
    ),
    (
        ('French', "I fart in your general direction! Your mother was a hampster, and your father smelt of eldeberries!"),
        ('King Arthur', "Is there anyone else up there we can talk to?"),
        ('French', "No! now go away away or I shall taunt you a second time!"),
    ),
]


def slack_listener(api_key):
    sc = SlackClient(api_key)

    if sc.rtm_connect():
        while True:
            msgs = sc.rtm_read()
            for msg in msgs:
                if msg.get('text'):
                    print msg['text']
                    if msg['text'].count('monty') and msg['text'].count('python'):
                        lines = python_lines[random.randint(0, len(python_lines) - 1)]
                        # lines = python_lines[0]
                        for speaker, line in lines:
                            sc.api_call('chat.postMessage',
                                        channel=msg.get('channel', '#bot-testing'),
                                        text=line,
                                        username=speaker, icon_emoji=':smiling_imp:')
                            time.sleep(1)
            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"

        # if msg['text'].count('tell'):
        #     if msg['text'].count('joke'):
        #         sc.api_call('chat.postMessage',
        #                     channel=msg.get('channel', '#bot-testing'),
        #                     text=jokes[random.randint(0, len(jokes) - 1)],
        #                     username=speaker, icon_emoji=':smiling_imp:')


                # sc.api_call('chat.postMessage',
#             channel='#bot-testing',
#             text=jokes[random.randint(0, len(jokes) - 1)],
#             username='joker', icon_emoji=':+1:')