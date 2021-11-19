filename = open("while.py")
for line in filename:
    if line.startswith("num"):
        print(line)
