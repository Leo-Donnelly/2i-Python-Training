import json

def prettyPrintJSON():
    sampleJson = {"key1": "value1", "key2": "value2"}

    pretty_print = json.dumps(sampleJson, indent=2, separators=(",", " = "))

    print(pretty_print)

def main():
    prettyPrintJSON()

main()