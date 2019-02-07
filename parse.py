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
    codefreq= {}
    ##begin parsing
    file = open("log1","r")
    file_data =file.readlines()
    totalRequests = len(file_data)
    for i in file_data:
        if len(i) > 30:
            ##selects all data between the first and second quotation marks
            a = i[i.find('"')+1:i.find('"',(i.find('"')+1))]
            ##selects the status code
            b = i[i.find('HTTP/1.0"')+10:i.find('HTTP/1.0"')+13]
            ##add to 300, 400 counters
            print(b)
            if b[0]=='3':
                status300count+=1
            elif b[0]=='4':
                status400count+=1
            ##find the frequency of status codes
            if(b in codefreq):
                codefreq[b] += 1
            else:
                codefreq[b] = 1
            ##find the frequency of accessed files
            if(a[4:-9] in accessedFiles):
                accessedFiles[a[4:-9]] += 1
            else:
                accessedFiles[a[4:-9]] = 1
        else:
            malformedEntrys+=1

    print(status300count)
    print(status400count)
    print(totalRequests)
    return
