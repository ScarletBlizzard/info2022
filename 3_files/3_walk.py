import shutil
import os

shutil.unpack_archive("main.zip")
answer = []

for current_dir, dirs, files in os.walk("main"):
    for name in files:
        if name.endswith(".py"):
            if current_dir not in answer:
                answer.append(current_dir)
            continue

with open("3_answer.txt", "w") as file:
    file.write("\n".join(sorted(answer)))
