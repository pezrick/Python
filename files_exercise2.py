read_only = open("teams.txt", "r")
read_only.readline()
line2 = read_only.readline()
line3 = read_only.readline()
line4 = read_only.readline()
line5 = read_only.readline()

read_only.close()

write_only = open("teams.txt", "w")
exercise_text = "This is a new line"
write_only.write(exercise_text + "\n")
write_only.write(line2)
write_only.write(line3)
write_only.write(line4)
write_only.write(line5)

write_only.close()

filex = open("teams.txt", "r")
print(filex.readline())
print(filex.readline())
print(filex.readline())
print(filex.readline())
print(filex.readline())

filex.close()