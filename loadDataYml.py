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
    
    # Task 4: Load data into an object from a .yml file and check if the file syntax is correct.
    
        # elif extension == '.yml' or extension == '.yaml':
    #     with open(inputFile, 'r') as yamlFile:
    #         data = yaml.safe_load(yamlFile)
