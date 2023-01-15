import os
from bored_base import *

bd = Bored()
px = Pixab()


bd.URL = 'http://www.boredapi.com/api/activity'

os.system('clear')
bd.introduction()

os.system('clear')
chx = bd.askCriteria()

os.system('clear')
p1, p2 = bd.params_setting(chx)

os.system('clear')
the_ac = bd.recommand(p1, p2)

if "No activity found with the specified parameters" in the_ac.values():
    sentence = "I'm sorry, there's no activity that I can suggest you for now."
    print(sentence)
else:
    sentence = f"I recommend you <{the_ac['activity']}>. It's a(n) {the_ac['type']} activity where {the_ac['participants']} persons are involved."


    params = {'q':the_ac['activity']}
    img_json = px.search_img(params)
    
    if img_json['total'] == 0:
        img_link = ''
    else:
        img_link = img_json['hits'][0]['pageURL']

    if img_link:
        show_img_link = "\nHere's a URL of image you might like:\n" + img_link
    else:
        show_img_link = ''


    os.system('clear')
    if the_ac['link']:
        sentence += "\nHere's a URL you might like:\n" + the_ac['link'] + show_img_link
    else:
        sentence += "\n" + show_img_link


    if bd.crtr == 'price':
        print(sentence, '\nBesides, it costs no money!')
    else:
        print(sentence)
