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
    prevmonth=""
    #Regex function
    ##begin parsing
    file = open("log1","r")
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
            except AttributeError:
                malformedEntrys+=1
    ##Create reports directory
    path = os.getcwd()+"/reports/monthlyLogs"
    try:
        os.makedirs(path)
    except OSError:
        print ("Directory %s currently exists" % path)
    #Create monthly file
    for i in file_data:
            z = re.match('(\w+).*\[(.*?)\] \"\S+ (.*?)\" (\d+) (\w+|-)',i)
            try:
                m = path+"/"+(z.group(2)[3:6])+"_"+(z.group(2)[7:11])
                prevmonth=(z.group(2)[3:6])+"_"+(z.group(2)[7:11])
                mreport = open(m, 'a+')
                mreport.write(i)
                mreport.close()
            except AttributeError:
                m = path+"/"+(prevmonth)
                mreport = open(m, 'a+')
                mreport.write(i)
                mreport.close()
    ##create reports
    # n = path+"/overallUsageReport"
    # nreport = open(n, 'w+')
    # nreport.write("This is report of detailed usage statistics\n")
    # nreport.write("===========================================\n")
    # nreport.write("        Monthly Usage Statistics           \n")
    #
    # nreport.write("                Statistics                 \n")
    # nreport.write("Total Request Count  -  " + str(totalRequests) + '\n')
    # nreport.write("3XX Status Codes  -  " +str(status300count) +' ('+ str(round(status300count/totalRequests*100,2)) +'%)\n')
    # nreport.write("4XX Status Codes  -  " +str(status400count) +' ('+ str(round(status400count/totalRequests*100,2)) +'%)\n')
    # nreport.write("Malformed Log Entries  -  " +str(malformedEntrys) +' ('+ str(round(malformedEntrys/totalRequests*100,2)) +'%)\n')
    # nreport.write("Most Requested File  -  " +str(max(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(max(accessedFiles, key=accessedFiles.get), "none")) +' requests)\n'))
    # nreport.write("Least Requested File  -  " +str(min(accessedFiles, key=accessedFiles.get) +' ('+ str(accessedFiles.get(min(accessedFiles, key=accessedFiles.get), "none")) +' request)\n'))
    # # nreport.write("Status Codes:\n")
    # for key in sorted(codefreq):
    #     nreport.write("  HTTP Status Code "+str(key)+ ' occurred '+ str(codefreq[key])+" times\n")
    # nreport.write("===========================================\n")
    # nreport.write("File Access Statistics:\n")
    # for key in sorted(accessedFiles):
    #     nreport.write("  "+str(key)+ ' was accessed '+ str(accessedFiles[key])+" times\n")

    return
##Line to find the date `print(i[i.find('[')+1:i.find(']')])`
