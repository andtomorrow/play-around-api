import os, requests
from bored_base import *

bd = Bored()

bd.URL = 'http://www.boredapi.com/api/activity'

os.system('clear')
bd.introduction()

os.system('clear')
chx = bd.askCriteria()

os.system('clear')
p1, p2 = bd.params_setting(chx)

os.system('clear')
the_ac = bd.recommand(p1, p2)

os.system('clear')
sentence = f"I recommend you <{the_ac['activity']}>. It's a(n) {the_ac['type']} activity where {the_ac['participants']} persons are involved."

if bd.crtr == 'price':
    print(sentence, 'Besides, it costs no money!')
else:
    print(sentence)


'''
activity : Description of the queried activity
accessibility : A factor describing how possible an event is to do with zero being the most accessible
[0.0, 1.0]
type : Type of the activity
["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
participants : The number of people that this activity could involve
[0, n]
price : A factor describing the cost of the event with zero being free
[0, 1]
key : A unique numeric id [1000000, 9999999]
'''
