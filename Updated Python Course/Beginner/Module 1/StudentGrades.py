students = {}

def add_studens(name, info):
    students[name] = info
    print("Student added with key:value pair as \n", name, ":", info)


Bobby = {"grade":"88", "DOB": "10/10/2000"}
Johnny = {"grade":"8", "DOB": "22/4/1989"}
Lizzy = {"grade":"55", "DOB": "10/10/2006"}

add_studens("Bobby", Bobby)

add_studens("Johnny", Johnny)

add_studens("Lizzy", Lizzy)