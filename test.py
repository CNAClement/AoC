liste_1 = [2, 3, "3"]
print(liste_1)
print(list(liste_1))

dic_traite = {0: 'A', 1: 'B'}
nouveau_dic = {2: 'C', 3: 'D'}


if 5 in dic_traite :
    print("true")

print(len(dic_traite))
print(0 in dic_traite)

# Concaténation
dic_traite = dic_traite | nouveau_dic

print(dic_traite)

dic = {0: (1,2,1), 1: (2,3,1), 2: (1,2,0), 3: (2,4,1), 4: (1,2,1), 5: (2,3,0)}
print(dic.values())


for x in dic :
    print(x)

dic_traite = {x:dic[x] for x in dic if dic[x][2] == 1 }
print(dic_traite)
