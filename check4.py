fileinp = input("Enter a file name: ")
filename = open(fileinp)
count = 0
for line in filename:
    if line.startswith('Subject:'):
        count = count + 1
    print("There were", count, "subject lines in", fileinp)
