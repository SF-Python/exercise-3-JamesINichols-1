# Hannah Raynard (GHUN DarkenedI)
# COP 2002 OT1
# 2025-02-14
# MAC manufacturer program
# This program will prompt the user for input then match it to specific variables

# program start
print("MAC Manufacterer Program")
print("------------------------")
print()
# Prompts user for input
userPrompt=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

# Prints prompt to the screen
print(userPrompt)

# List for keeping track of all the manufacturers
manufacturerList=["Oracle","Intel Corporation", "Microsoft Corporation","Apple, Inc.", "Huawei Technologies Co., Ltd", "Cisco Systems, Inc"]

# if/elif/else statements
if userPrompt=="00:00:17" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[0]}")
elif userPrompt=="00:07:E9" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[1]}")
elif userPrompt=="04:27:28" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[2]}")
elif userPrompt=="04:26:65" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[3]}")
elif userPrompt=="04:33:89" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[4]}")
elif userPrompt=="00:00:0C" :
    print(f"for {userPrompt} the MAC manufacterer is {manufacturerList[5]}")
else:
    print("Not found.")
