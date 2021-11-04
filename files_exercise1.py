file_files = open("teams.txt", "w")

file_files.write("Montreal Canadiens" + "\n")
file_files.write("Hampton & Richmond" + "\n")
file_files.write("West Bromwich Albion" + "\n")
file_files.write("Kansas City Chiefs" + "\n")
file_files.write("Streatham Redhawks")

file_files.close()

find_a_line = open("teams.txt", "r")
lines = find_a_line.readlines()
print(lines[0])
print(lines[3])

