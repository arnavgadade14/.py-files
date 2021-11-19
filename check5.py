fileinp = input("Enter a file name: ")
try:
    filename = open(fileinp)
except:
    print("File cannot be opened:", fileinp)
    quit()
count = 0
for line in filename:
    if line.startswith('Subject:'):
        count = count + 1
    print("There were", count, "subject lines in", fileinp)
