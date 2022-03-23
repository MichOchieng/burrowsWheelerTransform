import re
from os import walk
from pathlib import Path

from numpy import sort

class bwt:

    INPUT_FILES  = []
    INPUT_STRING: str

    BW_MATRIX  = []
    FIRST_COL  = ""
    SECOND_COL = ""

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
        except:
            print("Error reading input file.")

    def createMatrix(self,string):
        for x in range(len(string)):
            string = self.rotate(string)
            self.BW_MATRIX.append(string)

    def getTransform(self,string):
        # Generate + sort matrix
        self.createMatrix(string)
        self.BW_MATRIX.sort()

        for x in self.BW_MATRIX:
            self.FIRST_COL  = (self.FIRST_COL + x[0]) + str(self.FIRST_COL.count(x[0]))
            self.SECOND_COL = (self.SECOND_COL + x[-1]) + str(self.SECOND_COL.count(x[-1])) 

        self.RESULT = self.RESULT + self.FIRST_COL[:2]
        # create a dictionary using each letter in FIRST_COL with the corresponding letter in SECOND_COL
        self.DICTIONARY = dict(
                    zip(
                        re.findall("..",self.FIRST_COL),
                        re.findall("..",self.SECOND_COL)
                        )
                    )
        
        self.getInverse(self.FIRST_COL[:2])
    
    def getInverse(self,key):
        # Loop through first transform 
        if len(self.RESULT) < len(self.FIRST_COL):
            char = self.DICTIONARY[key]
            self.RESULT = self.RESULT + char
            self.getInverse(char)
        else: # Reverse the string
            self.RESULT = self.RESULT[::-1]

    def rotate(sel,string) -> str:
        # Moves last char in a string to the front of the string
        char = string[len(string)-1]
        # print("Rotation: " + (char + string[:-1]))
        return (char + string[:-1])

    def run(self):
        for file in self.INPUT_FILES:
            self.getString(file)
            self.getTransform(self.INPUT_STRING)
            print(re.sub(r'\d+','',self.RESULT[:-1]))

if __name__ == "__main__":
    program = bwt()
    program.run()