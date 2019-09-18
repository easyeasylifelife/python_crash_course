"""
learn : append(), insert(arg1, arg2), del, pop(), remove()
"""

motorcycles = ['honda', 'ducati', 'bmw']
print(motorcycles)


#modify motorcycles list 'honda' becomes 'yamaha'
motorcycles[0] = 'yamaha'
print(motorcycles)


#adding new list element using append() method
motorcycles.append('suzuki')
print(motorcycles)


#create empty list, and then add element using append() method
handphone = []
print(handphone)

handphone.append('nokia')
print(handphone)

handphone.append('samsung')
print(handphone)

handphone.append('sony')
print(handphone)

#new line
print('/n')

#inserting element using insert(arg1, arg2)
handphone.insert(1, 'oppo')
print(handphone)


#removing using del Statement
print(motorcycles)
del motorcycles[0]
print(motorcycles)


#popping element from a list using pop()
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print('\n')

#the use of pop()
girlfriends = []
girlfriends.append('karin')
girlfriends.append('fersa')
girlfriends.append('laras')
girlfriends.append('rosa')
print(girlfriends)

girlfriends.insert(2, 'melani')
print(girlfriends)

del girlfriends[2]
print(girlfriends)

my_fiance = girlfriends.pop()
first_girlfriend = girlfriends.pop(0)
print('\nMy first girlfriend is ' + first_girlfriend.title() + '.')
print('And, the last one, whose will be my wife is ' + my_fiance.title() + '.')


#removing item by value using remove()
print(handphone)
handphone.remove('oppo')
print(handphone)

#also use remove() method to work with a value that's being removed
expensive_handphone = 'sony'
handphone.remove(expensive_handphone)
print(handphone)
