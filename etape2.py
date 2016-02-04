#!/usr/bin/python

import ftplib
import os
import sys
import datetime


def avance(session, dir_mv):
    session.cwd(dir_mv)
    os.chdir(dir_mv)

def crea_tab(tab):
    result = [os.curdir, os.pardir] + os.listdir(tab)
    leni = len(result)
    return (result, leni)
    
def back(result, lenre, session):
    session.cwd('../')
    os.chdir('../')
    boucle(result, lenre, session)
    
def boucle(result, lenre, session):
    tab = []
    i = 0
    while (i < lenre):
        if (result[i] == ".." or result[i] == "."):
            print ""
        elif result[i] in session.nlst():
            print ""
        else:
            if ((os.path.isfile(result[i])) == True):
                file = open(result[i],'rb')
                session.storbinary('STOR ./' + result[i], file)
                file.close()
            elif ((os.path.isdir(result[i])) == True):
                session.mkd('./' + result[i])
                tab, leni = crea_tab(result[i])
                avance(session, result[i])
                boucle(tab, leni, session)
                back(result, lenre, session)
        i = i + 1


backup = sys.argv[1]
if len(sys.argv) != 2:
    print "Usage : sudo python etape2.py FILE/DIRECTORY"
elif (((os.path.isfile(backup)) != True) and ((os.path.isdir(backup)) != True)):
    print "FILE/DIRECTORY you want to backup doesn't exist"
else:
    session = ftplib.FTP('ftp.backito_cha.comlu.com','a3573842','mdp789456123')
    result = [os.curdir, os.pardir] + os.listdir(backup)
    lenre = len(result)
    now = datetime.datetime.now()
    date = now.ctime()
    if backup in session.nlst():
        session.mkd(backup + date)
        session.rename(backup, backup + date)
    i = 0
    session.mkd(backup)
    session.cwd(backup)
    os.chdir(backup)
    while (i < lenre):
        if (result[i] == ".." or result[i] == "."):
            print ""
        elif result[i] in session.nlst():
            print ""
        else:
            if ((os.path.isfile(result[i])) == True):
                file = open(result[i],'rb')
                session.storbinary('STOR ./' + result[i], file)
                file.close()
            elif ((os.path.isdir(result[i])) == True):
                session.mkd('./' + result[i])
                tab, leni = crea_tab(result[i])
                avance(session, result[i])
                boucle(tab, leni, session)
                back(result, lenre, session)
        i = i + 1
    


# session.quit()