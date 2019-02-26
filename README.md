# Python Log Parser - TCMG 476

This is a python log parser built for TCMG 476. It will download an Apache log file and parse it.

# What will the code do?

 - It will give the total number of requests 
 - It will give percentages of status codes for requests(2xx,3xx,4xx,5xx)
 - The top ten most requested files
 - The top busiest days for web traffic
 - The most and least requested files
 - Split the code into individual monthly log files
 - Access count for daily, weekly and monthly sections of time.


# Instructions for Use
  - You can run the file by running the main.py file.
 ```sh
$ python main.py
```

# Challanges
- Designing a robust solution without "hardcoding" the solution
    - This program was designed in a way that any Apache log file of the same version will work without being dependent on the specific version of log file.
- Making the program run efficiently
    - The program started off very inefficient due to looping though the file multiple times as well as repeatedly opening and closing the results files. By minimizing the number of loops through the program as well as the opening and closing the result files.
- Providing the proper amount of data
    - The original report was 12,000+ lines long. This included every file access count, daily count, weekly count, etc. This proved to be too much data and the report was trimmed down to about 100 lines of the most relvant data. The program collects all the relevant data but only add the most relevant to the final report. The program can easily be modified to include the most robust log outputs. 
