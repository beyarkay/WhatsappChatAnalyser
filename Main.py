class Message(object):
    def __init__(self, time, sender, content):
        self.time = time
        self.sender = sender
        self.message = content

    def parse_message(self, message):
        # return [time, sender, message]
        return 'message'


class Person(object):
    def __init__(self, name):
        self.name = name


print('WhatsApp Chat Analyser')
CHAT_FILE_URL = '_chat.txt'
CHAT_FILE = open(CHAT_FILE_URL, encoding='utf-8')

old = ""
for num, line in enumerate(CHAT_FILE):
    if line == old:
        print(num, line)
    old = line
