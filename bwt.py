import re
from os import walk
from pathlib import Path

class bwt:

    INPUT_FILES = []

    def __init__(self) -> None:
        self.getFiles()

    def getFiles(self):
        # Finds input files in current directory and appends them to the INPUT_FILES array
        myPath = Path(__file__).parent.resolve()
        for file in next(walk(myPath), (None, None, []))[2]:
            if re.search("^input_.*.txt",file):
                print("Found: " +  file)
                self.INPUT_FILES.append(file)

if __name__ == "__main__":
    program = bwt()