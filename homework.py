file1 = open('Codingal1.txt')
print("Reading the first 18 characters")
print(file1.read(24))
file1.close

file2 = open('Codingal1.txt')
print("Reading the first two lines")
print(file2.readline())
print(file2.readline())
file2.close()

file3 = open('Codingal1.txt')
print("Reading lines")
print(file3.readlines())
file3.close

file4 = open('Codingal.txt', 'w')
print("Lines that do not have with Coding")
for ln in file1.readlines() :
  if not (ln.startswith('Coding')) :
    print(ln)
    
    file4.write(ln)

file1.close()
file4.close()