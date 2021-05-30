fhandle = open('mbox-short.txt')
counts  = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
print(sorted( [(val, key) for key, value in counts.items()]))
#for key, val in counts.items():
#    newtup = (val, key)
#    lst.append(newtup)

#lst = sorted(lst, reverse = True)

#for val, key in lst[:10]:
#    print(key, val)
