from datetime import date

def updateDiary(diaryTextFile, name, mood):
    with open(diaryTextFile, "r", encoding="utf-8") as textFile:
        contents = textFile.read()

    contents = contents.replace("{{name}}", name)
    contents = contents.replace("{{mood}}", mood)

    todaysDate = date.today()
    contents += f"\n\nToday's date is {todaysDate}"

    with open(f"{todaysDate}.txt", "w", encoding="utf-8") as newFile:
        newFile.write(contents)

    print(f"Diary updated and saved as {todaysDate}.txt")

updateDiary(
    r"C:\Users\LeoDonnelly\OneDrive - 2i Limited\Documents\Python Iniative\2i-Python-Training\Updated Python Course\Beginner\Module 2\diaryTemplate.txt",
    "Leo",
    "happy"
)
