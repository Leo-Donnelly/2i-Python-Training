import json

def accessSalary():
    sampleJson = """{ 
    "company":{ 
        "employee":{ 
            "name":"emma",
            "payble":{ 
                "salary":7000,
                "bonus":800
            }
        }
    }
    }"""

    jsonData = json.loads(sampleJson)


    print(jsonData['company']['employee']['payble']['salary'])

def main():
    accessSalary()

main()    