import re
from os import walk
from pathlib import Path

class bwt:

    INPUT_FILES  = []
    INPUT_STRING: str

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

    def burrowsWheeler(self,string):
        print(string)

    def run(self):
        for file in self.INPUT_FILES:
            self.getString(file)
            self.burrowsWheeler(self.INPUT_STRING)

if __name__ == "__main__":
    program = bwt()
    program.run()