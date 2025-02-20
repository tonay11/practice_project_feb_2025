import os

f = open('session_1/beatrix_potter_the_story_of_a_fierce_bad_rabbit.txt')
print(f.read())

with open('session_1/beatrix_potter_the_story_of_a_fierce_bad_rabbit.txt', 'r') as file:
    data = file.read().rstrip()
    print (data)

with open('session_1/beatrix_potter_the_story_of_a_fierce_bad_rabbit.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

print (mylist)


