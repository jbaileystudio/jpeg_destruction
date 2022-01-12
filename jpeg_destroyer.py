
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

#Get the img file as a sequence of bytes:
#with open("/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg", "rb") as fp:
#    img = fp.read()

#with open('/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg', 'rb') as f:
#    binValue = f.read(1)
#    while len(binValue) != 0:
#        hexVal = hex(ord(binValue))
        # Do something with the hex value
#        binValue = f.read(1)

print("Run image displayed as string\n")

# convert img to string
import base64
with open("/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)

print("\nEnd of image displayed as string\n")

print("------")

print("\nRun img to .txt\n")

#(jpeg to txt) Split the target filename by '.' and replace the last entry by the new extension you want
my_file = '/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.txt')

print("Success - Image becomes .txt (See below)\n")

#Loop through the file and print it line by line giving you hex values
f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.txt", "rb")
for x in f:
  print(x)

# convert img to bytearray
#with open("/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.jpeg", "rb") as image:
#  f = image.read()
#  b = bytearray(f)
#  print (b[0])

# See the integer values 0 to 29 displayed as 2 hex digits, format the integers as 2 hex digits
#for i in range(30):
#    print (f"{i:02x}")

print("\nEnd of image as .txt\n")

print("Run .txt to image\n")

#(txt to jpeg) Split the target filename by '.' and replace the last entry by the new extension you want
my_file = '/Users/ijames/Documents/GitHub/jpeg_destruction/edgar.txt'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.jpeg')

print("Success - .txt becomes image\n")



# Close the file opened
#f = open("/Users/ijames/Documents/GitHub/jpeg_destruction/demotext.txt", "r")
#print(f.readline())
#f.close()