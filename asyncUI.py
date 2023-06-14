async def processFiles():
    app = QApplication(sys.argv)
    widget = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Select input and output files:")
    layout.addWidget(label)

    hbox = QHBoxLayout()
    inputButton = QPushButton("Select Input File")
    outputButton = QPushButton("Select Output File")
    hbox.addWidget(inputButton)
    hbox.addWidget(outputButton)
    layout.addLayout(hbox)

    convertButton = QPushButton("Convert")
    layout.addWidget(convertButton)

    widget.setLayout(layout)

    input_file = None
    output_file = None

    def selectInputFile():
        nonlocal input_file
        input_file, _ = QFileDialog.getOpenFileName(None, "Select Input File")
        if input_file:
            inputButton.setText(os.path.basename(input_file))

    def selectOutputFile():
        nonlocal output_file
        output_file, _ = QFileDialog.getSaveFileName(None, "Select Output File")
        if output_file:
            outputButton.setText(os.path.basename(output_file))

    def convert():
        nonlocal input_file, output_file
        if input_file and output_file:
            asyncio.create_task(convertFile(input_file, output_file))

    inputButton.clicked.connect(selectInputFile)
    outputButton.clicked.connect(selectOutputFile)
    convertButton.clicked.connect(convert)

    widget.show()
    sys.exit(await app.exec_())
