chapters = [
    "Down the Rabbit-Hole",
    "The Pool of Tears",
    "A Caucus-Race and a Long Tale",
    "The Rabbit Sends in a Little Bill",
    "Advice from a Caterpillar"
]

# i = 1
# for chapter in chapters:
#     i+=1
#     print(f"{i}: {chapter}")

for i, chapter in enumerate(chapters):
    chapters[i-1] = chapter.upper()
    print(f' {i}: {chapters[i-1]}')

# with open("down_the_rabbit-hole.txt", "r", encoding="utf-8") as file:

# line_number = 1
# for line in file:
#     print(f"Line {line_number}: {line.strip()}")
#     line_number +=1

for line_number, line in enumerate(file, 1):
    print(f"Line {line_number}: {line.strip()}")