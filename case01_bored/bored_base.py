import requests

class Bored:
    def __init__(self):
        # self.URL = 'http://www.boredapi.com/api/activity/'
        self.criteria_list = ['participants', 'price', 'type']
        self.q_list = [
            'How many people to get involved?\nType a number > ',
            'Select type of the activity\n1) educational 2) recreational 3) social 4) diy 5) charity 6) cooking 7) relaxation 8) music 9) busywork\nType a number > '
            ]
        self.crtr = ''
    
    def introduction(self):
        self.usr_input = input("As you're bored, I will get you a nice activity chosen just for you.\nPress enter > ")

    def askCriteria(self):
        chx = int(input("What is your criteria for an activity?\n1) Together with others!\n2) Don't want to spend money.\n3) What kind of activity..?\nPlease choose by number > "))
        return chx
    
    def random(self):
        rsp_json = requests.get(url = self.URL).json()
        return rsp_json
    
    # def choose(self, n):
    #     choice = self.criteria_list[n-1]
    #     return choice

    def params_setting(self, chx):
        if chx == 1:
            self.crtr = 'participants'
            self.q_answer = input(self.q_list[0]).strip()
        elif chx == 2:
            self.crtr = 'price'
            self.q_answer = ''
        elif chx == 3:
            self.crtr = 'kind'
            self.q_answer = input(self.q_list[1]).strip()
        return self.crtr, self.q_answer
    
    def recommand(self, p1, p2):
        self.URL = str(self.URL + f'?{p1}={p2}')
        result = requests.get(url = self.URL).json()
        return result

    





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
