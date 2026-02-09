# -------------------------------------------------------------------------------------
#   Project Name  : Automated Disk Sanitiser
#   Author Name   : Omkar Mahadev Bhargude
3
#   Description   : This automation script is used for deleting duplicate files
#                   files from the given directory keeping only original ones.
#                   Scan the directory, detect duplicate files using MD5 checksum
#                   and delete duplicates (Keeping the original ones)
#
#   Date          : Monday - 09/02/2026
# -------------------------------------------------------------------------------------

import sys
import schedule
import time
import os
import hashlib
import shutil

def CalculateCheckSum(FileName):
    Ret = True
    Ret = os.path.exists(FileName)

    if(Ret == False):
        return
    
    Ret = os.path.isfile(FileName)
    if(Ret == False):
        return

    hobj = hashlib.md5()
    
    # to calculate checksum always open file in binary mode
    fobj = open(FileName, "rb")
    
    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

# -------------------------------------------------------------------------------------
#   Function Name       : FindDuplicateFiles
#   Function Parameter  : str(Directory Name)
#   Description         : Finds duplicate file using calculatechecksum method
#                         return dictionary of list
#   Author Name         : Omkar Mahadev Bhargude
#   Date                : Monday-09/02/2026
# -------------------------------------------------------------------------------------
def FindDuplicateFiles(DirName):
    # empty dict K = checksum, V = list of file path having same checksum
    Duplicate = {}

    for root, dirs, files in os.walk(DirName):
        for fname in files:
            fname = os.path.join(root, fname)
            Checksum = CalculateCheckSum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

# -------------------------------------------------------------------------------------
#   Function Name       : DeleteDuplicate
#   Function Parameter  : str(Directory Name)
#   Description         : Deletes the duplicate file keeping one original
#   Author Name         : Omkar Mahadev Bhargude
#   Date                : Monday-09/02/2026
# -------------------------------------------------------------------------------------
def DeleteDuplicate(DirName):
    MyDict = FindDuplicateFiles(DirName)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    dcnt = 0
    dfiles = []

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                dfiles.append(subvalue)
                os.remove(subvalue)
                dcnt = dcnt + 1
        Count = 0

    return dcnt, dfiles

# ---------------------------------------------------------------
def MoveLog(DirName):
    folderName = "DiskSanitiserLogFiles"
    os.makedirs(folderName, exist_ok=True)

    path = os.path

    for root, dirs, files in os.walk(DirName):
        for fname in files:
            if fname.endswith == ".log":
                try:
                    src = os.path.join(DirName, fname)
                    dest = os.path.join(path, fname)
                    shutil.move(src, dest)
                except OSError as e:
                    pass
# -------------------------------------------------------------------------------------
#   Function Name       : CreateLog
#   Description         : creates a report of script in a log file
#   Author Name         : Omkar Mahadev Bhargude
#   Date                : Monday-09/02/2026
# -------------------------------------------------------------------------------------
def CreateLog(DirName):

    Ret = True

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    timestamp = time.strftime("%Y:%m:%d_%H:%M:%S")
    LogFileName = os.path.join(DirName, "DiskSanitiserReport_%s.log" %timestamp)
    print("Log file gets created with name : ",LogFileName)

    Border = "-"*60

    fobj = open(os.path.join(LogFileName),"w")

    fobj.write(Border+"\n")
    fobj.write("-------------- Automated Disk Sanitiser Report -------------\n")

    Cnt, Arr = DeleteDuplicate(DirName) 

    if(len(Arr) != 0):
        fobj.write("Duplicate files Deleted with Names :\n")
        for i in Arr:
            fobj.write(i+"\n")  

    cal = time.ctime()
    fobj.write("Total duplicate files deleted : "+str(Cnt)+"\n")
    fobj.write("This log file was created at : "+str(cal)+"\n")
    fobj.write("-------------- Thank you for using our script --------------\n")
    fobj.write(Border+"\n")
    fobj.close()

    MoveLog(DirName)
# ------------------------------------------------------------------------------
#   Entry point function
# ------------------------------------------------------------------------------
def main():

    if(len(sys.argv) != 2):
        print("Invalid number of command line arguments")
        print("Please specify the name of directory")
        return
    
    schedule.every(15).seconds.do(CreateLog,sys.argv[1])

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()