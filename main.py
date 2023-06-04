import sys
import os
import json
import xml.etree.ElementTree as ET
import yaml
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
        print("Unsupported file format.")
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
        print("Unsupported output file format.")
        return

    print("The data conversion is complete.")


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


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Использование: program.exe pathFile1.x pathFile2.y")
        print("где x и y - один из форматов .xml, .json и .yml (.yaml).")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    convertFile(inputFile, outputFile)
