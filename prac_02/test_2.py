temp_file = open("temp.txt", "r")
first_line_str = temp_file.readline()
print(first_line_str)

for line_str in temp_file:
    print(line_str)

last_line_str = temp_file.readline()
last_line_str1 = temp_file.readline()
last_line_str2 = temp_file.readline()
last_line_str3 = temp_file.readline()
print("last_line_str is: ", last_line_str)
print("last_line_str1 is: ", last_line_str1)
print("last_line_str2 is: ", last_line_str2)
print("last_line_str3 is: ", last_line_str3)

temp_file.close()
print()
print()
temp_file = open("temp.txt", "r")
file_contents_list = temp_file.readlines()
print(file_contents_list)
print()
print()

out_file = open("output.txt", "w")
out_file.writelines(file_contents_list)

out_file.close()