file = open("sample.txt", "r")
lines = file.readlines()
new_list = []
for line in lines:
     new_list.append(line.upper())
out_file = open("output.txt" , "w")
out_file.writelines(new_list)
out_file.close()