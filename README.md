## Purpose of the task:
- Getting the syntax right in Git
- Becoming familiar with standards for storing data in text files
- Creating an IT project and managing its version in GiT 
- Getting familiar with Github Actions
- Any programming language, Python preferred

## Project Description:
Data conversion program that supports .xml, .json and .yml (.yaml) formats
#### Usage: program.exe pathFile1.x pathFile2.ywhere x and y are one of the .xml, .json and .yml (.yaml) formats.
The above program call should correctly recognize the format, retrieve the data from pathFile1.x, and then create a new file pathFile2.y and convert the data according to the new format.
For python development, a .exe file should be generated from the project usingpyinstaller.exe (available for installation via pip). 
To avoid creating multiple .dlls you need to use the 
#### flag--onefile:
#### pyinstaller.exe --onefile project.py
In addition, you can attach a simple UI (User Interface) to the project, suggested is PyQt (available via pip).
When running a program that has its own UI, it will additionally launch a command line window. To avoid this behavior, you need to generate an .exe file with the command:
#### pyinstaller.exe --onefile --noconsole project.py
