#!/usr/bin/python

import ftplib
import os
import sys

def avance(session, dir_mv):
    session.cwd(dir_mv)
    os.chdir(dir_mv)

def crea_tab(tab):
    result = [os.curdir, os.pardir] + os.listdir(tab)
    leni = len(result)
    return (result, leni)
    
def boucle(result, lenre, session):
    i = 0
    tab = []
    while (i < lenre):
        if (result[i] == ".." or result[i] == "."):
            print ""
        elif ((os.path.isfile(result[i])) == True):
            file = open(result[i],'rb')
            session.storbinary('STOR ./' + result[i], file)
            file.close()
        elif ((os.path.isdir(result[i])) == True):
            session.mkd('./' + result[i])
            # tab, leni = crea_tab(result[i])
            # avance(session, result[i])
            # boucle(tab, leni, session)
        i = i + 1

backup = sys.argv[1]
session = ftplib.FTP('ftp.backito_cha.comlu.com','a3573842','mdp789456123')
result = [os.curdir, os.pardir] + os.listdir(backup)
lenre = len(result)
i = 0
session.mkd(backup)
session.cwd(backup)
os.chdir(backup)
while (i < lenre):
    if (result[i] == ".." or result[i] == "."):
        print ""
    elif ((os.path.isfile(result[i])) == True):
        file = open(result[i],'rb')
        session.storbinary('STOR ./' + result[i], file)
        file.close()
    elif ((os.path.isdir(result[i])) == True):
        session.mkd('./' + result[i])
        tab, leni = crea_tab(result[i])
        if os.listdir(result[i])=="":
            print ""
        else:
            avance(session, result[i])
            boucle(tab, leni, session)
    i = i + 1
    


# session.quit()