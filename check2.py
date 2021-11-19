filename = open("add.py")
for line in filename:
    line = line.rstrip()
    if not line.startswith("print"):
        continue
    print(line)
