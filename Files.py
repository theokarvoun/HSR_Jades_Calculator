class FileWriter:
    def writeToFile(content,name,extension) -> None:
        fileName = name+extension
        file = open(fileName,'w')
        file.write(content)
        file.close()

    def appendToFile(content,name,extension) -> None:
        fileName = name+extension
        file = open(fileName,'a')
        file.write(content)
        file.close()

class FileReader:
    def readFile(name,extension) -> str:
        filename = name+extension
        file = open(filename,'r')
        return file.read()