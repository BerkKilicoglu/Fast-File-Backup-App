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
def Sync(backupName:str, Src:str, Des:str, ExcludedFileTypes:list=[], ui=None) -> int: # returns: total changed files count
    try:
        ProcessedFilesInSrc = GetFilesNameList(Src, excluded=ExcludedFileTypes,
                                               removeSrcDir=False)  # , FilesInDes = GetFilesNameList(Src, [".txt"]), GetFilesNameList(Des)
        if True:
            if backupName:
                DestinationPath = f"{Des}{os.sep}{backupName}"
            else:
                DestinationPath = f"{Des}"
        else:  # new version, optional backup.
            DateNow = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            DestinationPath = f"{Des}{os.sep}{backupName}{os.sep}{DateNow}"

        os.makedirs(DestinationPath, exist_ok=True)
        totalChangedFiles = 0
        for FileSrc in ProcessedFilesInSrc:
            ResultDes = FileSrc.replace(Src, DestinationPath)
            ParsedFileName = FileSrc.replace(Src, "")
            if len(ParsedFileName) > 0:  # For safety.
                ParsedFileName = ParsedFileName[1:]  # Remove os.sep in first character
            if os.path.exists(ResultDes):  # For more performance, hash compare, if hashes are the same; it will not copy.
                hashSrc = GetFileMD5(FileSrc)
                hashDes = GetFileMD5(ResultDes)
                if hashSrc == hashDes:
                    print("Not copied file: %s [Files are the same]" % str(FileSrc))
                    continue

            if CopyFile(FileSrc, ResultDes):
                totalChangedFiles += 1
            else:
                print("[ERR] File: %s not copied (CopyFile is false)" % str(FileSrc))
            if ui:
                ui.lblStatus.setText(
                f"<b>Status: </b> File copying ({ParsedFileName}) {totalChangedFiles}/{len(ProcessedFilesInSrc)} {((totalChangedFiles) / len(ProcessedFilesInSrc) * 100)}%")
        return totalChangedFiles
    except Exception as err:
        utils.hataKodGoster("Sync: %s"%str(err))
        return 0
#print(GetFilesList(r"C:\Users\Emre\Desktop\Test1"))