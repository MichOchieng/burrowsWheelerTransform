import re
from os import walk
from pathlib import Path

class bwt:

    INPUT_FILES  = []
    INPUT_STRING: str

    TRANSFORM_PAIRS = []

    RESULT: str

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

    def getTransform(self,string):
        # This will create tuples and add them to TRANSFORM_PAIRS to be sorted later
        self.TRANSFORM_PAIRS.append((string[0],string[len(string)-1]))

        for x in range(len(string)-1):
            string = self.rotate(string)
            self.TRANSFORM_PAIRS.append((string[0],string[len(string)-1]))
        print(self.TRANSFORM_PAIRS)
        print(sorted(self.TRANSFORM_PAIRS,key=lambda x: (x[0],x[1])))

    def rotate(sel,string) -> str:
        # Moves last char in a string to the front of the string
        char = string[len(string)-1]
        # print("Rotation: " + (char + string[:-1]))
        return (char + string[:-1])

    def run(self):
        for file in self.INPUT_FILES:
            self.getString(file)
            self.getTransform(self.INPUT_STRING)

if __name__ == "__main__":
    program = bwt()
    program.run()