print("MAC Manufacturer Program")
print("------------------------")
print()
Oracle="00:00:17"
Intel_Corporation="00:07:E9"
Microsoft_Corpoation="04:27:28"
Apple="04.26.65"
HuaweiTechnoloies_Co_Ltd="04:33:89"
Cisco_SystemsInc="00.00.0C"
Not_valid_value_or_not_found="Unknown"


x=input("Enter the first 6 hex values of the MAC address(format as {XX.XX.XX}): ")
if Intel_Corporation==x.upper():

    print("For 00:07:E9 the MAC manufacturer is Intel Corporation." )

