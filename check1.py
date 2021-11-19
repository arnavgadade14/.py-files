filename = open("add.py")
for line in filename:
    line = line.rstrip()
    if line.startswith("print"):
        print(line)
