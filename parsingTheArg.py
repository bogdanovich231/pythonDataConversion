if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Using: main.py pathFile1.x pathFile2.y")
        print("where x and y are one of the .xml, .json, and .yml (.yaml) formats.")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    convertFile(inputFile, outputFile)
