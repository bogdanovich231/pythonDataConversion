if __name__ == '__main__':
    if len(sys.argv) != 3:
        asyncio.run(processFiles())
    else:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
        asyncio.run(convertFile(inputFile, outputFile))
