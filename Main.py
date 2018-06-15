import datetime


class Message(object):
    def __init__(self, time, sender, content, ID):
        self.ID = ID
        self.time = time
        self.sender = sender
        self.content = content
        self.isImage = content == '<image omitted>'

    def __repr__(self):
        return self.ID.__str__() + ' ' + self.time.__str__() + ' ' + self.sender + ': ' + self.content


class Person(object):
    def __init__(self, name):
        self.name = name


def populate_messages():
    message_id = 0
    cnt = 0
    current = ""
    for line in CHAT_FILE:
        # Don't refactor line.strip() into one call, breaks when there are only newline characters.
        if line[0] != '[':
            current += '\n' + line.strip()
            continue
        if cnt == 0:
            current = line.strip()
            cnt += 1
            continue
        else:
            messages.append(parse_message(current, message_id))
            message_id += 1
            current = line.strip()


def parse_message(message_string, num):
    # TODO check for images
    date = message_string[1:11]
    time = message_string[13:21]
    start_content = message_string.index(':', 22)
    name = message_string[23:start_content]
    content = message_string[message_string.index(':', 22) + 2:]
    dt = datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]), int(time[:2]), int(time[3:5]),
                           int(time[6:8]))
    return Message(dt, name, content, num)


def get_timespan():
    return messages[len(messages) - 1].time - messages[0].time


def create_timeline():
    pass


def get_totals():
    totals = {'days': get_timespan().days, 'images': 0,
              'messages': len(messages), 'words': 0, 'letters': 0}

    for message in messages:
        if message.isImage:
            totals['images'] += 1
            totals['messages'] -= 1
        else:
            # TODO handle emojis correctly
            for word in message.content.split():
                totals['words'] += 1
                totals['letters'] += len(word)

    return totals


def get_activity_times():
    pass


def get_most_active_day():
    pass


def get_averages():
    totals = get_totals()
    averages = {'lpm': 0, 'wpm': 0, 'mpd': 0, 'lpd': 0}

    averages['wpm'] = totals['words'] / totals['messages']
    averages['lpm'] = totals['letters'] / totals['messages']
    averages['mpd'] = totals['messages'] / totals['days']
    averages['lpd'] = totals['letters'] / totals['days']

    return averages

    # words per message, letters per message, messages per day and letters per day


def get_ratios():
    pass


print('WhatsApp Chat Analyser')
CHAT_FILE_URL = '_chat.txt'
CHAT_FILE = open(CHAT_FILE_URL, encoding='utf-8')

# Fill messages list
messages = []
populate_messages()
print(get_timespan())
create_timeline()
print(get_totals())
get_activity_times()
get_most_active_day()
print(get_averages())
get_ratios()

print('fin')
