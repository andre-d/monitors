#!/usr/bin/python

import os
import sys
import alerts

def monitor_logdir(path, tag, threshold):
    tag = "monitor_{%s}" % tag
    
    num_files = len(os.listdir(path))
    
    if num_files > threshold:
        alerts.harold.alert(tag, "%s has too many files [%d/%d]" % (path, num_files, threshold))

def main():
    # Usage is: logsize.py 10 some_logs /var/logs/somelogs
    #           10                 - Max number of files before alert
    #           some_logs          - Tag used for harold
    #           /var/logs/somelogs - Folder in which to look for files 
    threshold = int(sys.argv[1])
    tag = sys.argv[2]
    path = sys.argv[3]
    monitor_logdir(path, tag, threshold)

if __name__ == "__main__":
    main()
