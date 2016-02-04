#!/usr/bin/python

import sys
import os.path
from crontab import CronTab

def mycron(file, hour):
    if os.path.isfile(file) == True or os.path.isdir(file) == True and int(hour) > 0:
        user_cron = CronTab(user='ubuntu')
        cron_list = user_cron.find_comment(file)
        if len(list((cron_list))) > 0:
            user_cron.remove_all(comment = file)
        job = user_cron.new(command='/usr/bin/python /home/ubuntu/workspace/backito2.py '+file, comment=file)
        job.setall(None, None, None, None, None)
        user_cron.write();
    else:
        print "Invalid file/dir or hour"

def main():

    file = sys.argv[1]
    hour = sys.argv[2]

    if len(sys.argv) != 3:
        print "Usage : sudo python backito.py FILE/DIRECTORY REPETITION"
    elif hour.isdigit():
        mycron(file, hour)
    else:
        print "Hour must be an integer"
main()