my_name = 'Toni'
print (my_name)
city = 'London'
hobbies = 'walking, reading and music'
print (hobbies)
mySeparator = ". "
my_text = 'My name is '+ my_name + mySeparator + 'I live in ' + city + mySeparator + 'My hobbies are ' + hobbies
print (my_text)
f = open ("daz ds session 1 task 1.txt", "w")
f = open("daz ds session 1 task 1.txt", "a" )
f.write("my_text")
f.close()

#open and read the file after the appending:
f = open("daz ds session 1 task 1.txt", "r")
print(f.read())