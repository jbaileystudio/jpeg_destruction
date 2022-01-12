
import os

#print 1000 digits in a column
#for i in range(1,10):
#	print (i)

#print("0---")

# Open file and read it  #
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.read())

#print("1---")

# Open file and specify how many characters you want read#
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.read(6))

#print("2---")

# Open file and return first line#
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.readline())

#print("3---")

# Open file and return first two lines#
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.readline())
#print(f.readline())

#print("4---")


#(jpeg to txt) Split the target filename by '.' and replace the last entry by the new extension you want
my_file = '/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.txt')

print("image becomes .txt")

# Loop through the file and read it line by line#
f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.txt", "rb")
for x in f:
  print(x)




#(txt to jpeg) Split the target filename by '.' and replace the last entry by the new extension you want
my_file = '/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.txt'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.jpeg')

print("image becomes .jpeg")






# Close the file opened
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.readline())
#f.close()