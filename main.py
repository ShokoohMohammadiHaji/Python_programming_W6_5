
def readValues(PfileName) -> str:
    content = ""
    sourceFile = open(PfileName, "r", encoding="utf-8")

    Row = sourceFile.readline()

    while Row != "":
        content += Row.strip() + ";"
        Row = sourceFile.readline()

    sourceFile.close()
    return content


def analyseValues(Pfile):
    cleanFile = Pfile.strip(";").split(";")

    cleanFileInt = []

    for i in range(len(cleanFile)):
        cleanFileInt.append(int(cleanFile[i]))

    cleanFileInt.sort()

    total = 0

    for i in range(len(cleanFileInt)):
        total += cleanFileInt[i]

    lineCounter = len(cleanFileInt)

    greatest = cleanFileInt[-1]

    average = total / lineCounter

    result = displayResults(total, lineCounter, greatest, average)

    return result


def displayResults(Ptotal, PlineCounter, Pgreatest, Paverage):
    result = "Count;Sum;Greatest;Average\n"
    result += f'{PlineCounter};{Ptotal};{Pgreatest};{Paverage:.2f}\n'

    return result


def main():
    print("Program starting.")

    fileName = input("Insert filename: ")

    file = readValues(fileName)

    result = analyseValues(file)

    print(result)

    print("Program ending.")


if __name__ == "__main__":
    main()
