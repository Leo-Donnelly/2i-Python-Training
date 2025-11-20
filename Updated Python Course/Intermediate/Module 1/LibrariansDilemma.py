chapters = [
    "Down the Rabbit-Hole",
    "The Pool of Tears",
    "A Caucus-Race and a Long Tale",
    "The Rabbit Sends in a Little Bill",
    "Advice from a Caterpillar"
]

for i, chapter in enumerate(chapters):
    print(f"{i}: {chapter}")

# i = 1
# for chapter in chapters:
#     i+=1
#     print(f"{i}: {chapter}")


with open("down_the_rabbit-hole.txt", "r", encoding="utf-8") as file:

    line_number = 1
    # for line in file:
    #     print(f"Line {line_number}: {line.strip()}")
    #     line_number +=1
    
    for line in enumerate(file):
        print(f"Line{line_number}: {line.strip()}")