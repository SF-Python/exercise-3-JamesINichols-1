# cinquez johnson (cinjohnson81)
# W25 COP2002.0T1
# Fabruary 8, 2025
# If Statements
# Program to determine the manufacturer of a NIC card


print("MAC Manufacturer Program")

print("________________________")

print()

MAC_addresses = input ("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

if MAC_addresses == "00:00:17":
    print ("For 00:00:17 the MAC manufacturer is Oracle")

elif MAC_addresses == "00:07:E9":
    print ("For 00:07:E9 the MAC manufacturer is Microsoft Corporation")

elif MAC_addresses == "04:26:65":
    print ("For 04:26:65 the MAC manufacturer is Apple, Inc.")

elif MAC_addresses == "04:33:89":
    print ("For 04:33:89 the MAC manufacturer is Huawei Technologies Co.,Ltd")

elif MAC_addresses == "00:00:0C":
    print ("For 00:00:0C the MAC manufacturer is Cisco Systems, Inc")

else:
    print ("Unknown")