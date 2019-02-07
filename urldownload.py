import urllib.request
#this handles the download of the log file
def retrieve():
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, './log')
