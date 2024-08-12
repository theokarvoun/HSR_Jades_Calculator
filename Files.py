import re

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
    def readFileAsList(name, extension) -> list:
        filename = name + extension
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Split the lines into text and date parts
        separated_lines = []
        for line in lines:
            match = re.match(r'^(.*?)(\d{4}-\d{2}-\d{2})$', line.strip())
            if match:
                text_part = match.group(1).strip()
                date_part = match.group(2).strip()
                separated_lines.append((text_part, date_part))
            else:
                separated_lines.append((line.strip(), None))  # If no date is found, add None

        return separated_lines
    def extractDates(data):
        dates = [date for _, date in data]
        return dates
    def extractText(data):
        text_parts = [text for text, _ in data]
        return text_parts

if __name__ == '__main__':
    #print(FileReader.readFile(name='Data',extension='.txt'))
    #print(FileReader.readFile(name='Data2',extension='.txt'))
    #list1 = FileReader.readFileAsList(name='Data',extension='.txt')
    #list2 = FileReader.readFileAsList(name='Data2',extension='.txt')
    #dates1 = [date for _, date in list1]
    #dates2 = [date for _, date in list2]
    #print(dates1)
    #print(dates2)
    #text_parts = [text for text, _ in list2]
    #print(text_parts)
    print(FileReader.extractDates(data=FileReader.readFileAsList(name='Data',extension='.txt')))
    print(FileReader.extractDates(data=FileReader.readFileAsList(name='Data2',extension='.txt')))
    print(FileReader.extractText(data=FileReader.readFileAsList(name='Data2',extension='.txt')))