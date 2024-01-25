
# open file and read the file content
f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.read())
# read first five letters
f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.read(5))

# read one line
f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.readline())

# read two lines
f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.readline())
print(f.readline())

# loop through a line

f = open('/home/datasirpi/Documents/demofile1.txt', "r")
for x in f:
  print(x)

# close file
f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.readline())
f.close()

# append the line

f = open('/home/datasirpi/Documents/demofile1.txt', "a")
f.write("Now the file has more content!")
f.close()

f = open('/home/datasirpi/Documents/demofile1.txt', "r")
print(f.read())


