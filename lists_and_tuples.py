import random

numbercollection = [5,15,17,10]
numbercollection[2] = 170
print(numbercollection[2]) #170

numbercollection = [5,15,17,10]
## numbercollection.shufle
## print(numbercollection.shufle) #AttributeError: 'list' object has no attribute 'shufle'
sh=random.shuffle(numbercollection)
print(sh) #None
print(numbercollection) #[5, 10, 15, 17]

## Eu21 notes:
pickRandomNumFromList=random.choice(numbercollection) #Choice returns value
random.shuffle(numbercollection) #Shuffle changes the list itself

tuplenumbercollection = (5,15,17,10)
pickRandomNumFromTuple=random.choice(tuplenumbercollection) #Choice works for both tuples and lists
print(pickRandomNumFromTuple)

numbercollection = [5,15,17,10]


print(numbercollection) #[5, 10, 15, 17] - changed order of items in the original list
pickRandomNumFromList=random.choice(numbercollection) #Choice returns value
print(pickRandomNumFromList)

anyTypeList = ["test", 5.55, 777, True]
type(anyTypeList) #<class 'list'>

## Tuples never change their !!!order!!! and their !!!values!!!
## We need them when information should never be shuffeled(something more reliable than a list)

SergeyPII= ("Sergey", "Nesvizh roddom", "12.11.2018")
SashaPII= ("Sasha", "Minsk roddom", "11.11.2019")
MashaPII= ("Masha", "Nesvizh roddom", "11.11.2011")
type(SergeyPII)#<class 'tuple'>
#Birthday of a child will always be in the 3rt element (that is index 2)
print(SergeyPII[2])
#let's try to change the year of birth of Sergey
## SergeyPII[2] = "12.11.2010"# TypeError: 'tuple' object does not support item assignment



