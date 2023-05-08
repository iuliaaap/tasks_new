import os

word = "Lorem"
cnt = 0
lst = []
maxim=-10000
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        f = open(file,"r")
        for line in f.readlines():
            if word in line:
                cnt = cnt + 1
        lst.append((file, cnt, os.path.getsize(file)))
        cnt=0
        f.close()
max_no = 0
max_size = 0

for i in range(len(lst)):
    if max_no < lst[i][1]:
        max_no = lst[i][1]
        max_size = lst[i][2]

g = open("output.txt","w")
g.write(f"Numarul maxim de aparitii este {max_no}")
g.close