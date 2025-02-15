file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi! I am Penguin.I'm an year old")
file.close()