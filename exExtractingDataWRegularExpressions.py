import re #imports Regular Expressions
fn = input('Enter the name of the file: \n')
try:
    fh = open(fn)
except:
    print('File cannot be opened:', fn)
    exit()

total = 0
count = 0
for lx in fh: #read each line in the file
    count = count+1 #count the number of items in list
    lx = lx.rstrip() #strips whitespace from right side of string
    x = re.findall('[0-9]+', lx) #find the numbers

    for num in x: #loops through the numbers in the x list
        total += int(num) #turns numbers in x into integers and adds to "total" variable
print('Sum:',total)
