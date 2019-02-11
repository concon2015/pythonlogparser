#local - - [25/Oct/1994:00:04:38 -0600] "GET index.html HTTP/1.0" 200 3185
import os
import re
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

    ##begin parsing
    file = open("log","r")
    file_data =file.readlines()
    totalRequests = len(file_data)
    for i in file_data:
        if len(i) > 60:
            z = re.match('(\w+) - - \[(.*?)\] \"(.*?)\" (\d+) (\w+|-)',i)
            print(z)
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


            if a[0:3] == "GET":
                if(a[4:-9] in accessedFiles):
                    accessedFiles[a[4:-9]] += 1
                else:
                    accessedFiles[a[4:-9]] = 1
            elif a [0:3] == "HEA":
                if(a[4:-9] in accessedFiles):
                    accessedFiles[a[4:-9]] += 1
                else:
                    accessedFiles[a[5:-9]] = 1
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
        nreport.write(monthlyUsageCounter[j] + '  -  ' + str(monthlyUsageResults[j]) + " requests\n")
    nreport.write("===========================================\n")
    nreport.write("                Statistics                 \n")
    nreport.write("Total Request Count  -  " + str(totalRequests) + '\n')
    nreport.write("3XX Status Codes  -  " +str(status300count) +' ('+ str(round(status300count/totalRequests*100,2)) +'%)\n')
    nreport.write("4XX Status Codes  -  " +str(status400count) +' ('+ str(round(status400count/totalRequests*100,2)) +'%)\n')
    nreport.write("Malformed Log Entries  -  " +str(malformedEntrys) +' ('+ str(round(malformedEntrys/totalRequests*100,2)) +'%)\n')
    nreport.write("Most Requested File  -  " +str(max(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(max(accessedFiles, key=accessedFiles.get), "none")) +' requests)\n'))
    nreport.write("Least Requested File  -  " +str(min(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(min(accessedFiles, key=accessedFiles.get), "none")) +' request)\n'))
    # nreport.write("Status Codes:\n")
    # for key in sorted(codefreq):
    #     nreport.write("  HTTP Status Code "+str(key)+ ' occurred '+ str(codefreq[key])+" times\n")
    # nreport.write("===========================================\n")
    # nreport.write("File Access Statistics:\n")
    # for key in sorted(accessedFiles):
    #     nreport.write("  "+str(key)+ ' was accessed '+ str(accessedFiles[key])+" times\n")

    return
##Line to find the date `print(i[i.find('[')+1:i.find(']')])`
