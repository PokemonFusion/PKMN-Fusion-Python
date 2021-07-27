import sys
import os


def makedir(dirName):
    # Create target Directory if don't exist

    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:
        print("Directory " , dirName ,  " already exists")


makedir(os.path.join("FunctionFiles", "Import"))
makedir(os.path.join("FunctionFiles", "Export"))

basefolder = os.path.join("FunctionFiles", "Import")


for root, subdirs, files in os.walk(basefolder):
    makedir(root.replace("Import", "Export"))
    for file in files:
        data = ""
        with open(os.path.join(root, file), "r") as filename:
            for line in filename:
                if line.startswith('def'):
                    words = line.split()
                    newfunction = "{} {}((**bvalues):\n".format(words[0], words[1])
                    data += newfunction
                else:
                    data += line
            if not data.endswith('\n'):
                data += '\n'

        with open(os.path.join(root.replace('Import', 'Export'), file), "w+") as filename:
            filename.write(data)
