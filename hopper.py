import time
import threading
import os



age_limit = 55


class hopper:
    def __init__(self) -> None:
        self.belly = []
        self.name = ''
        self.age = 0
        t1 = threading.Thread(target=hunger,args=[self])
        t2 = threading.Thread(target=ager,args=[self])
        t1.start()
        t2.start()

def hunger(hopper):
    # hunger loop to drain the belly
    while True:
        if hopper.belly:
            time.sleep(10)
            hopper.belly.pop()

def feed(hopper):
    print('feeding interface')
    while True:
        food = input('>> ')
        if food != 'exit':
            hopper.belly.append(food)
        else:
            break

def showstats(hopper):
    statlist = ['age', 'belly', 'name','exit']
    print('stats interface')
    print(statlist)
    while True:
        statinput = input('>> ')
        if statinput == 'belly':
            print(hopper.belly)
        elif statinput == 'age':
            print(hopper.age)
        elif statinput == 'name':
            print(hopper.name)
        elif statinput == 'exit':
            break

def setstats(hopper):
    print('stat setting interface')
    while True:
        print('please set your hoppers name')
        statsettinginput = input('>> ')
        hopper.name = statsettinginput
        print('please set your hoppers age')
        statsettinginput = int(input('>> '))
        hopper.age = statsettinginput
        break
  
# the method to age the hopper will slowly increase age every 15 seconds
def ager(hopper):
    while True:
        time.sleep(15)
        hopper.age += 1
        # hopper age limit varable
        if hopper.age == age_limit:
            print('age limit reached')
            killhopper(h1)

def killhopper(hopper):
    # fuction to kill hopper aka del hopper object
    # then exit the game because you lost
    print('Hopper died')
    os.abort()

h1 = hopper()

# the mail loop that starts the menus and lets you set the hoppers attrs.
def mainLoop():
    oplist = ['show', 'feed', 'kill', 'exit']
    setstats(h1)
    while True:
        print('~ Main game menu ~')
        print(oplist)
        user_input = input(">> ")
        if user_input == 'feed':
            feed(h1)
        elif user_input == 'show':
            showstats(h1)
        elif user_input == 'kill':
            killhopper(h1)
        elif user_input == 'exit':
            os.abort()
            break
        else:
            print('in error')
        print('bruh')


h1 = hopper()
t1 = threading.Thread(target=mainLoop)
t1.start()
