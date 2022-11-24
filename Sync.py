# -*- coding: utf-8 -*-
import sys, os, json, time, hashlib, shutil
from Utils import Utils
from glob import glob
from pathlib import Path

utils = Utils(None)
def GetFileMD5(src:str) -> str: # Get file to MD5 Hash
    if not os.path.exists(src):
        return ""
    CHUNK_SIZE = 8192
    with open(src, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(CHUNK_SIZE)

    return file_hash.hexdigest()
def GetFilesNameList(srcDir:str, filters:list=["*.*"], excluded:list=[], removeSrcDir=True) -> list:
    Output = []
    if os.path.exists(srcDir) and os.path.isdir(srcDir):
        for x in os.walk(srcDir):
            for filter in filters:
                for fullpath in glob(os.path.join(x[0], filter)):
                    fileExtension = Path(fullpath).suffix
                    filePath = fullpath.replace(srcDir, "")

                    foundInExcluded = False
                    for exc in excluded:
                        if fileExtension == exc or (filePath == exc or filePath == os.sep+exc):
                            foundInExcluded = True
                            break

                    if foundInExcluded:
                        continue

                    resultPath = fullpath
                    if removeSrcDir:
                        resultPath = resultPath.replace(srcDir, "")
                    Output.append(resultPath)




        #Output = [y for x in os.walk(srcDir) for y in glob(os.path.join(x[0], filter))]
    return Output
def CopyFile(src:str, des:str) -> bool:
    if not os.path.exists(src):
        return False
    os.makedirs(os.path.dirname(des), exist_ok=True)
    if os.path.exists(des):
        if os.path.isfile(des):
            os.remove(des)
    shutil.copyfile(src, des)
    return True

#print(GetFilesList(r"C:\Users\Emre\Desktop\Test1"))