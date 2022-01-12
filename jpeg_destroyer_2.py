import os
import binascii
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

#variables
percent_removed = .01


script_path=get_script_path()

with open(script_path+'/edgar.jpeg', 'rb') as image_file:
    data = binascii.b2a_hex(image_file.read()," ") #inbetween every hexidecimal representation adds a space
    #data = binascii.b2a_hex(image_file.read()) #no space

print (data)
print ("\n\n\n\n\n")
#print (hex(data[100]))
#print (data[100])

middle = int(len(data)/2) #location of the data (right now in the middle)
slice_percentage_length = int(len(data)*percent_removed)  #percentage slice of the data
start_of_slice = middle-int(slice_percentage_length/2) #start of slice data
end_of_slice = middle+int(slice_percentage_length/2) #end of slice data
if data[end_of_slice] != ' ': #check if data is whole 
	if data[end_of_slice+1] != ' ':
		end_of_slice = end_of_slice+2
	else:
		end_of_slice = end_of_slice+1
if data[start_of_slice] != ' ': #check if data is whole 
	if data[start_of_slice+1] != ' ':
		start_of_slice = start_of_slice+3
	else:
		start_of_slice = start_of_slice+2

if (end_of_slice-start_of_slice) % 2: #spits out 0 or 1, to check is # is even or odd
	 end_of_slice = end_of_slice + 3

middle_data_slice = data[start_of_slice:end_of_slice] #slice of the middle of the data


#print (middle) # middle position in the data (bytes)
#print (data[middle]) # decimal (representing the same value as hex a different way)
#print (hex(data[middle])) # hex

#data [middle-8:middle+8]
print ("Data slice from the middle removed below")
print (middle_data_slice)

starting_value = middle-int(slice_percentage_length/2)

data = bytearray(data)

print (int(len(data)))

for hex_value in middle_data_slice: #remove the data from the slice
	data.pop(starting_value)

print (int(len(data)))

#data = data.replace(' ','')
#data = binascii.a2b_hex(data)
#with open(script_path+"/edgar_1.jpeg", 'wb') as image_file:
#    image_file.write(data)

data = bytes(data)

data=data.strip()
data=data.replace(b' ', b'')
#print(data)
data = binascii.a2b_hex(data)
with open(script_path+"/edgar_1.jpeg", 'wb') as image_file:
    image_file.write(data)


