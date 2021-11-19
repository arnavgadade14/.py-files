han = open("newline.py")

for line in han:
    line = line.rstrip()
    print("Line", line)
    wds = line.split()
    if len(wds) < 3 or wds[0] != "newlinetext":
        continue
    print(wds[2])
