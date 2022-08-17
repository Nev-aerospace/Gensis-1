DataSendTime = 0
DataSendTime = int(
    input("Data Checking Launched set data post int in seconds: "))
while DataSendTime <= 0 or DataSendTime >= 20:
    print("You sure you placed it corecct?")
    DataSendTime = int(
        input("Data Checking Launched set data post int in seconds: "))
