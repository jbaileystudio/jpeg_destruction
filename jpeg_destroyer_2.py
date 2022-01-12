import os
import binascii
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

script_path=get_script_path()

with open(script_path+'/edgar.jpeg', 'rb') as image_file:
    data = binascii.b2a_hex(image_file.read()," ") #inbetween every hexidecimal representation adds a space
    #data = binascii.b2a_hex(image_file.read()) #no space

print (data)
print ("\n\n\n\n\n")
#print (hex(data[100]))
#print (data[100])

middle = int(len(data)/2)
slice_percentage_length = int(len(data)*.01)
middle_data_slice = data[middle-int(slice_percentage_length/2):middle+int(slice_percentage_length/2)] #slice of the middle of the data


#print (middle) # middle position in the data (bytes)
#print (data[middle]) # decimal (representing the same value as hex a different way)
#print (hex(data[middle])) # hex

#data [middle-8:middle+8]
print ("Data slice from the middle removed below")
print (middle_data_slice)

modified_data = data

starting_value = middle-int(slice_percentage_length/2)

data = bytearray(data)

print (int(len(data)))

for hex_value in middle_data_slice: #remove the data from the slice
	data.pop(starting_value)

print (int(len(data)))


