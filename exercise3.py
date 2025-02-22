##Sebastian Brant (sbrantstudent)
##COP2002.0T1
##February 12, 2025
##Exercise 3: If Statements
##Takes hex digits from user input and prints the corresponding manufacturer name.


#Make two lists, for hexadecimal and manufacturer.
hexCode=["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]
manufacturerName=["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]

#Input statement draws from the user input.
userInput=input("Enter the first 6 hex values of the MAC address: ")

#Conditional boolean statement to be used in for loop.
found=False

#For loop the iterates through the hexCode list to match the user input, then print the manufacturer if a match is found.
for i in range(len(hexCode)):
    if userInput==hexCode[i]:
        print(manufacturerName[i])
        found=True
        break

#If there is no match, the code prints "Unknown".
if not found:
    print("Unknown")


