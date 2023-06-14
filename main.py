import sys
import os
import json
import xml.etree.ElementTree as ET
import yaml
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
import asyncio.subprocess
def convertFile(inputFile, outputFile):
    _, extension = os.path.splitext(inputFile)

    if extension == '.xml':
        tree = ET.parse(inputFile)
        root = tree.getroot()
        data = xml_to_dict(root)
    elif extension == '.json':
        with open(inputFile, 'r') as jsonFile:
            data = json.load(jsonFile)
    elif extension == '.yml' or extension == '.yaml':
        with open(inputFile, 'r') as yamlFile:
            data = yaml.safe_load(yamlFile)
    else:
        QMessageBox.critical(None, "Unsupported file format", "Unsupported file format.")
        return

    _, outputExtension = os.path.splitext(outputFile)

    if outputExtension == '.xml':
        root = dict_to_xml(data)
        tree = ET.ElementTree(root)
        tree.write(outputFile, encoding='utf-8', xml_declaration=True)
    elif outputExtension == '.json':
        with open(outputFile, 'w') as jsonOutput:
            json.dump(data, jsonOutput, indent=4)
    elif outputExtension == '.yml' or outputExtension == '.yaml':
        with open(outputFile, 'w') as yamlOutput:
            yaml.dump(data, yamlOutput, default_flow_style=False)
    else:
        QMessageBox.critical(None, "Unsupported output file format", "Unsupported output file format.")
        return

    QMessageBox.information(None, "Data conversion complete", "The data conversion is complete.")

def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result

def dict_to_xml(data):
    root = None
    if isinstance(data, dict):
        root = ET.Element('root')
        for key, value in data.items():
            child = dict_to_xml(value)
            child.tag = key
            root.append(child)
    else:
        root = ET.Element('item')
        root.text = str(data)
    return root

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

if __name__ == '__main__':
    if len(sys.argv) != 3:
        asyncio.run(processFiles())
    else:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
        asyncio.run(convertFile(inputFile, outputFile))
