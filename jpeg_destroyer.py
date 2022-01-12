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

# Loop through the file and read it line by line#
f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
for x in f:
  print(x)
f.close()

# Close the file opened
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.readline())
#f.close()