import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
