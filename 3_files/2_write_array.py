def write_array(array, file_name):
    with open(file_name, "w") as file:
        file.write("\n".join(array))

write_array(input().split(), input())
