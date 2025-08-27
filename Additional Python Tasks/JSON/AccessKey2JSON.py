import json

def convertoJSON():
    data = {"key1" : "value1", "key2" : "value2"}

    jsonData = json.dumps(data)

    print(data['key2'])

def main():
    convertoJSON()

main()