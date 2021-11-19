filename = open("openanotherfile.py")
for line in filename:
    line = line.rstrip()
    if not "open" in line:
        continue
    print(line)
