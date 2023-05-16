dict = {}
with open("input.txt","r") as file:
     for word in file:
         for c in word:
             if dict.get(c) == None:
                dict[c] = 1
             else:
                dict[c] += 1
print(dict)
