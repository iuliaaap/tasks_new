dict = {}
k = 0
f = open("input.txt","r")
txt = f.readline()

for ch in txt:
   if ch.isalpha():
         k += 1
         if ch in dict.keys():
            dict[ch] += 1
         else:
            dict[ch] = 1

print(dict)

for key in dict.keys():
    dict[key] = dict[key]/k * 100

print(dict)


