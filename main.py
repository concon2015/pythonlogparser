from urldownload import retrieve
from parse import *
import time


def main():
    start = time.time()
    #retrieve()
    parse()
    end = time.time()
    print(str(round(end - start,2)) +"seconds for execution")
main()
