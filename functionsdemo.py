"""
CTEC 121
<Tristan Sahagun>
<Mod 5 Lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main1():
    print()
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear Fread...")
    print("Happy birthday to you!")
    print()

# remove duplication/redundancy
''' IPO happy()
Input(s): None
Process: prints/outputs chorus of happy birthday song
output: prints to terminal screen
'''

def happy():
    print("Happy birthday to you!")

def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()

# generalize for any person
''' IPO happyBday()
Input(s): a name
Process: prints/outputs the verse of happy birthday song
output: prints to terminal screen
'''
def happyBday(name):
    print("Happy birthday, dear ", name, "...", sep="")

def main3():
    print()
    happy()
    happy()
    happyBday("")
    happy()
    print()

# combine song into a function
''' IPO singhappyBday()
Input(s): a name
Process: prints/outputs happy birthday song
output: prints to terminal screen
'''
def singhappyBday(name):
    happy()
    happy()
    happyBday(name)
    happy()
    print()

def main4():
    print()
    singhappyBday("Fred")
    singhappyBday("Lucy")
    singhappyBday("Bill")

main4()    