import re


def scanPDF():
    with open("/home/ayoub/devHacking/python/fileScan/jScript.txt") as f:
        for line in f.readlines():
            if (re.search("/JS", line)):
                if (line.split()[1]!=0):
                    
                    return "malicious"
                    break 
            if (re.search("/JavaScript", line)):
                if (line.split()[1]!=0):
                    
                    return "malicious"
                    break 

            if (re.search("/AA", line)):
                if (line.split()[1]!=0):
                    
                    return "malicious"
                    break 

            if (re.search("/OpenAction", line)):
                if (line.split()[1]!=0):
                    
                    return "malicious"
                    break 

            if (re.search("/EmbeddedFile", line)):
                if (line.split()[1]!=0):
                    
                    return "malicious"
                    break 

            if (re.search("/Encrypt", line)):
                if (line.split()[1]!=0):
                    
                    return  "malicious"
                    break 
        return 'clean'
        
            


