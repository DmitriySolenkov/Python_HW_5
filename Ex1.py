def path(string):
    *path_name, file_name = string.split("/")
    path = ""
    for elem in path_name:
        path = path + elem + "/"
    file_name, file_ext = file_name.split(".")
    return path, file_name, file_ext


string = "C:/Users/Soldi/OneDrive/Documents/Homework/Python/HW_5.py"
my_tuple = path(string)
print(my_tuple)
