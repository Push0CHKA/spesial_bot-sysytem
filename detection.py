import time

from mods.detect import parser
from mods import ai

token = '6869968d4dd1c78f8a5fe858c5f56e599fc03f7beb8a2ef1915303eb2d6d10ac1da6be7bfc4cf7014f454'

file = open('files/bots.txt', 'r')
ids = ''
cnt = 1
#for line in file:
#    parser.download_main_data(user_ids=line.replace('\n', ''), token=token)
#parser.download_friends_data(44609877, token)

ai.get_dataset()


