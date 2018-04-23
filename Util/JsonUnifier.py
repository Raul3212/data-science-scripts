import glob
import json

def main():
    jsonFileNames = glob.glob('./*.json')
    data = []
    for jsonFileName in jsonFileNames:
        jsonFile = open(jsonFileName, 'r')
        data.append(json.load(jsonFile))
        jsonFile.close()
    jsonFinalFile = open('TODOS.json', 'w')
    json.dump(data, jsonFinalFile)
    jsonFinalFile.close()

if __name__ == '__main__':
    main()