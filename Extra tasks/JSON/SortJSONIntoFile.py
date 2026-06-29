import json

def sort_write():
    sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

    print("Writing JSON into file")
    with open("sample.json", "w") as write_file:
        json.dump(sampleJson, write_file, indent=4, sort_keys=True)
    print("Writing completed.")

def main():
    sort_write()


main()