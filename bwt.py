import re
from os import walk
from pathlib import Path

class bwt:

    INPUT_FILES  = []
    INPUT_STRING: str

    SORTED_INPUT: str

    RESULT     = ""
    DICTIONARY: dict

    def __init__(self) -> None:
        self.getFiles()

    def getFiles(self):
        # Finds input files in current directory and appends them to the INPUT_FILES array
        myPath = Path(__file__).parent.resolve()
        for file in next(walk(myPath), (None, None, []))[2]:
            if re.search("^input_.*.txt",file):
                self.INPUT_FILES.append(file)

    def getString(self,file):
        try:
            with open(file) as inputFile:
                lines = inputFile.readlines()
                self.INPUT_STRING = lines[0]
                self.SORTED_INPUT = ''.join(sorted(lines[0]))
                self.RESULT       = ""
        except:
            print("Error reading input file.")

    def addCount(self,string) -> str:
        temp = ""
        for c in string:
            temp = temp + (c + (str(temp.count(c))))
        return temp

    def invert(self):
        self.INPUT_STRING = self.addCount(self.INPUT_STRING)
        self.SORTED_INPUT = self.addCount(self.SORTED_INPUT)
        
        # Add $ to the result
        self.RESULT = self.RESULT + self.SORTED_INPUT[:2]
        
        self.DICTIONARY = dict(
                    zip(
                        re.findall("..",self.SORTED_INPUT),
                        re.findall("..",self.INPUT_STRING)
                        )
                    )
        self.search(self.SORTED_INPUT[:2])
    
    def search(self,key):
        if len(self.RESULT) < len(self.SORTED_INPUT):
            char = self.DICTIONARY[key]
            self.RESULT = self.RESULT + char
            self.search(char)
        else: # Reverse the string
            self.RESULT = self.RESULT[::-1]

    def run(self):
        for file in self.INPUT_FILES:
            self.getString(file)
            self.invert()
            print(file + " produced an output of: " + re.sub(r'\d+','',self.RESULT[:-1]))

if __name__ == "__main__":
    program = bwt()
    program.run()