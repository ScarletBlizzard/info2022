with open("random_text.txt", "w") as file:
    file.write("  random line 1  \n")
    file.write("  random line 2  \n")

with open("random_text.txt", "r") as file:
    for line in file:
        print(line.strip())

