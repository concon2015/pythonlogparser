#local - - [25/Oct/1994:00:04:38 -0600] "GET index.html HTTP/1.0" 200 3185
import os
def parse():
    ##Delcarations##
    totalRequests = 0
    daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    status400count = 0
    status300count= 0
    malformedEntrys = 0
    accessedFiles = {}
    codefreq= {}
    monthlyUsageCounter = []
    monthlyUsageResults = []

    ##begin parsing
    file = open("log","r")
    file_data =file.readlines()
    totalRequests = len(file_data)
    for i in file_data:
        if len(i) > 60:
            ##selects all data between the first and second quotation marks
            a = i[i.find('"')+1:i.find('"',(i.find('"')+1))]
            ##selects the status code
            b = i[i.find('HTTP/1.0"')+10:i.find('HTTP/1.0"')+13]
            ##add to 300, 400 counters
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

    ##Create reports directory
    path = os.getcwd()+"/reports/monthlyLogs"
    try:
        os.makedirs(path)
    except OSError:
        print ("Directory %s currently exists" % path)
    ##Create monthly file
    for i in file_data:
        if len(i)>60:
            m = path+"/"+(i[i.find('[')+8:i.find('[')+12]+"_"+i[i.find('[')+4:i.find('[')+7])
            mreport = open(m, 'a+')
            mreport.write(i)
            mreport.close()
    ##create reports
    n = path+"/overallUsageReport"
    nreport = open(n, 'w+')
    nreport.write("This is report of detailed usage statistics\n")
    nreport.write("===========================================\n")
    nreport.write("        Monthly Usage Statistics           \n")
    for i in file_data:
        if len(i)>60:
            g = i[i.find('[')+8:i.find('[')+12]+"_"+i[i.find('[')+4:i.find('[')+7]
            if g in monthlyUsageCounter:
                l=monthlyUsageCounter.index(g)
                monthlyUsageResults[l]+=1
            else:
                monthlyUsageCounter.append(g)
                monthlyUsageResults.append(1)
    for i in monthlyUsageCounter:
        j=monthlyUsageCounter.index(i)
        nreport.write(monthlyUsageCounter[j] + '  -  ' + str(monthlyUsageResults[j]) + "\n")
    nreport.write("===========================================\n")
    nreport.write("                Statistics                 \n")
    nreport.write("Total Request Count  -  " + totalRequests + '\n')
    nreport.write("3XX Status Codes  -  " +status300count +'\n')
    nreport.write("4XX Status Codes  -  " +status400count +'\n')
    nreport.write("Malformed Log Entries  -  " + malformedEntrys + '\n')
    return
##Line to find the date `print(i[i.find('[')+1:i.find(']')])`
