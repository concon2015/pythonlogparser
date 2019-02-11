#local - - [25/Oct/1994:00:04:38 -0600] "GET index.html HTTP/1.0" 200 3185
import os
import re
import operator
def parse():
    ##Delcarations##
    totalRequests = 0
    status400count = 0
    status300count= 0
    malformedEntrys = 0
    accessedFiles = {}
    codefreq= {}
    monthlyUsageCounter = []
    monthlyUsageResults = []
    accessedDailyCount = {}
    prevmonth=""
    nmonth=""
    ##Create reports directory
    path = os.getcwd()+"/reports/monthlyLogs"
    try:
        os.makedirs(path)
    except OSError:
        print ("Directory %s currently exists" % path)
    file = open("log","r")
    file_data =file.readlines()
    totalRequests = len(file_data)
    for i in file_data:
            try:
                z = re.match('(\w+).*\[(.*?)\] \"\S+ (.*?)\" (\d+) (\w+|-)',i)
                #300 and 400 counters
                if z.group(4)[0]=="3":
                    status300count+=1
                elif z.group(4)[0]=="4":
                    status400count+=1
                #codefreq counters
                if z.group(4) in codefreq:
                    codefreq[z.group(4)]+=1
                else:
                    codefreq[z.group(4)]=1
                #accessedFiles counters
                if z.group(3).split(' ')[0] in accessedFiles:
                    accessedFiles[z.group(3).split(' ')[0]]+=1
                else:
                    accessedFiles[z.group(3).split(' ')[0]]=1
                #create monthly log files
                try:
                    prevmonth = (z.group(2)[3:6])+"_"+(z.group(2)[7:11])
                    m = path+"/"+prevmonth
                except (IsADirectoryError, AttributeError):
                    m = path+"/"+prevmonth
                #limit the number of times that the system needs to open file
                if prevmonth==nmonth:
                    mreport.write(i)
                elif nmonth=="":
                    mreport = open(m, 'a+')
                    mreport.write(i)
                    nmonth=prevmonth
                else:
                    mreport.close()
                    mreport = open(m, 'a+')
                    mreport.write(i)
                    nmonth=prevmonth
                #daily access counters
                if z.group(2)[0:11] in accessedDailyCount:
                    accessedDailyCount[z.group(2)[0:11]]+=1
                else:
                    accessedDailyCount[z.group(2)[0:11]]=1

            except AttributeError:
                malformedEntrys+=1
    #create reports
    n = path+"/overallUsageReport"
    nreport = open(n, 'w+')
    nreport.write("This is report of detailed usage statistics\n")
    nreport.write("===========================================\n")
    nreport.write("        Monthly Usage Statistics           \n")

    nreport.write("                Statistics                 \n")
    nreport.write("Total Request Count  -  " + str(totalRequests) + '\n')
    nreport.write("3XX Status Codes  -  " +str(status300count) +' ('+ str(round(status300count/totalRequests*100,2)) +'%)\n')
    nreport.write("4XX Status Codes  -  " +str(status400count) +' ('+ str(round(status400count/totalRequests*100,2)) +'%)\n')
    nreport.write("Malformed Log Entries  -  " +str(malformedEntrys) +' ('+ str(round(malformedEntrys/totalRequests*100,2)) +'%)\n')
    nreport.write("Most Requested File  -  " +str(max(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(max(accessedFiles, key=accessedFiles.get), "none")) +' requests)\n'))
    nreport.write("Least Requested File  -  " +str(min(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(min(accessedFiles, key=accessedFiles.get), "none")) +' request)\n'))
    nreport.write("===========================================\n")
    nreport.write("Status Codes:\n")
    sorted_codefreq=sorted(codefreq.items(), key=operator.itemgetter(1),reverse=True)
    for i in sorted_codefreq:
        nreport.write("  HTTP Status Code "+str(i[0])+ ' occurred '+ str(i[1])+" times\n")
    nreport.write("===========================================\n")
    nreport.write("Page Requests by Date:\n")
    for i in accessedDailyCount:
        nreport.write("  "+str(i) + ' had '+ str(accessedDailyCount[i])+" page requests\n")
    nreport.write("===========================================\n")
    nreport.write("File Access Statistics:\n")
    sorted_accessedFiles=sorted(accessedFiles.items(), key=operator.itemgetter(1),reverse=True)
    for i in sorted_accessedFiles:
        nreport.write("  "+str(i[0])+ ' was accessed '+ str(i[1])+" times\n")

    return
