def main():
    answer=input("Enter the first 6 hex values of the MAC adress (format as XX:XX:XX): ")
    if (answer=="00:00:17"):
        manufacturer="Oracle"
    elif (answer=="00:07:E9"):
        manufacturer="Intel Corporation"
    elif (answer=="04:27:28"):
        manufacturer="Microsoft Corporation"
    elif (answer=="04:26:65"):
        manufacturer="Apple, Inc."
    elif (answer=="04:33:89"):
        manufacturer="Huawei Technologies Co.,Ltd"
    elif (answer=="00:00:0C"):
        manufacturer="Cisco Systems, Inc"
    else: 
        manufacturer="Unknown"
    print(f"For {answer} the MAC manufacturer is {manufacturer}.")
if (__name__=="__main__"):
    main()
