#local - - [25/Oct/1994:00:04:38 -0600] "GET index.html HTTP/1.0" 200 3185
def parse():
    ##Delcarations##
    totalRequests = 0
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    status400count = 0
    status300count= 0
    malformedEntrys = 0
    accessedFiles = {}
    ##begin parsing
    file = open("log1","r")
    file_data =file.readlines()
    totalRequests = len(file_data)
    for i in file_data:
        if len(i) > 30:
            print(i)
        else:
            malformedEntrys+=1


    return
