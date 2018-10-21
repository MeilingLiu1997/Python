# Due on Wednesday
import random

def main():
    personList = ["Hillary", "Donald",'Peter','Tom','Jerry','Sharon','Vivian','Jay','Frank','Jack']
    placeList = ['the Golden Gate park','Beijing','San Francisco', "Philadelphia",'Shanghai','Hawayi','Tokyo']
    pluralnounList = ['children','the family','people','parents','workers','oceans','computers','parks','classrooms','pens']
    actionList = ['run','play','jump','go','watch','take','give','get','drink','eat','end','start','claim']
    adjectivesList = ["hungry",'cold','hot','frustrate','tired','thirsty','careful','rude','stupid','thin','fat']
    foodList = ['food','pizza','noodle','rice','coke','sushi','steak','pork','soup','vegetables','fruits']


    def display():
        food = foodList[random.randint(0, len(foodList) - 1)]
        person = personList[random.randint(0, len(personList) - 1)]
        place1 = placeList[random.randint(0, len(placeList) - 1)]
        plural_noun = pluralnounList[random.randint(0, len(pluralnounList) - 1)]
        action = actionList[random.randint(0, len(actionList) - 1)]
        adjectives = adjectivesList[random.randint(0, len(adjectivesList) - 1)]
        place2 = placeList[random.randint(0, len(placeList) - 1)]

        print('Last summer, we went for a vacation with ', person, ' on a trip to ',place1,'. '
        'The weather there is very ',adjectives,'! Northern ',place1,
        ' has many ',plural_noun,' and they make ', plural_noun,' there.\n\n'
        'Many people also go to the ', place2, ' to ', action, '.The people that live there love to eat ', food, '. They '
        'also like to ', action, ' in the sun and swim in the ', plural_noun,'.\n\nIt was a really ', adjectives,' trip!',sep='')

    display()
    new = input('Want to see another version?(y/n)')
    while new == 'y':
        display()
        new = input('Want to see another version?(y/n)')
    else:
        quit()
main()