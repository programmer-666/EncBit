class eLib():
    def __init__(self,key):
        self.key = key

    def TextToAscii(self,Text):
        lst = []
        for i in Text.upper():
            lst.append(ord(i))
        return lst

    def encryption(self,BitList):
        lst = []
        for i in BitList:
            lst.append(i^self.key)
        return lst

    def AsciiToText(self,AscLst):
        lst = []
        for i in AscLst:
            lst.append(chr(i))
        return lst

    def WriteAFile(self,fname,format,content):
        File = open(fname+"."+format,"w")
        for i in content:
            File.write(i)
        File.close()
