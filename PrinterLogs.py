# -*- coding: utf-8-*-
import time
import win32print
import socket,datetime
printstr = ""

def print_job_checker():
    server = socket.gethostname()
    while True:
        jobs = []
        for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,None, 1):
            flags, desc, name, comment = p
            phandle = win32print.OpenPrinter(name)
            print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
            if print_jobs:
                jobs.extend(list(print_jobs))
            for job in print_jobs:

                document = job["pDocument"]
                username = job['pUserName']
                identity = job['JobId']
                jobstate = job['Status']
                machinename = job['pMachineName'].replace("\\\\","")
                pTime = datetime.datetime.now().isoformat()
                today = datetime.date.today().isoformat()
                Pages = job['TotalPages']
                printstr = "[Server:" + server + "],[Who:" + username + "],[Computer:" + machinename + "],[Print Time:"+ pTime +"],[JobID:"+ str(identity) + "]"
                print (printstr)
            win32print.ClosePrinter(phandle)
        time.sleep(0.5)
print_job_checker()