# Audrey Tarronas (ateauds)
# COP2002.0T1
# 02/11/2025
# Exercise 3: If statements
# Creating Python program using if statements to create a program to find manufacturer from hex digits

# Variables
# Setting up which manufacturer has each hex digit (used for myself)

oracle = "00:00:17"
intelCorporation = "00:07:E9"
microsoftCorp = "04:27:28"
appleInc = "04:26:65"
huawaiTech = "04:33:89"
ciscoSystems = "00:00:0C"

# Interface

print("MAC Manufacturer Program")
print("------------------------\n")

# Command for user to input hex digit to run program

hexDigit = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

# If statements to sort through each hex digit for the program

if hexDigit == "00:00:17":
    print("For", hexDigit, "the MAC manufacturer is Oracle.")
elif hexDigit == "00:07:E9":
    print("For", hexDigit, "the MAC manufacturer is Intel Corporation.")
elif hexDigit == "04:27:28":
    print("For", hexDigit, "the MAC manufacturer is Microsoft Corporation.")
elif hexDigit == "04:26:65":
    print("For", hexDigit, "the MAC manufacturer is Apple, Inc.")
elif hexDigit == "04:33:89":
    print("For", hexDigit, "the MAC manufacturer is Huawei Technologies Co., Inc.")
elif hexDigit == "00:00:0C":
    print("For", hexDigit, "the MAC manufacturer is Cisco Systems, Inc.")
else:
    print("For", hexDigit, "the MAC manufacturer is Unknown.")
