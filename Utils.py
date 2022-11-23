import sys, os, json

class Utils():
    def isWindows(self) -> bool:
        return os.name == 'nt'
    def pathConvert(self, path:str)->str:
        if self.isWindows():
            return path.replace("/", "\\").replace("\\\\","\\")
        else:
            return path.replace("\\\\", "/").replace("\\", "/")