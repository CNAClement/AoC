import re
dic = {0: '11', 1: '4', 2: '31', 3: '7', 4: '12', 5: '6' , 6 : '0' , 7 : '1'  }

dic = {cle : int(valeur) for cle, valeur in dic.items() }

lliste = [(x , y)  for x  in range(4) for y in range(4)]
print(lliste)

dic = {"C" : [2] , "D" : [8]  }
dic["A"] = [1 + _ for _ in range(4)]
dic["B"] = [_ * _ for _ in range(6)]
dic["E"] = [20]
print(16 in dic["B"])
max_dic = max(dic.values())
print(max_dic)
print(f"dictionnaire : {dic}")
dic["B"].

print("ok")

max = 0
for valeur in dic.values() :
    for _ in range(len(valeur)) :
        if valeur[_] > max :
            max = valeur[_]
            print(max)
print(max)


max_dic = max(dic.values())
print(f"valeur max : {max_dic}")

for clé in dic.keys() :
    if dic[clé] == max_dic :
        print(f"clé associée à la valeur max : {clé}")

valeur = 0
while valeur in dic.values() :
    print("on teste la valeur suivante")
    valeur +=1
print(f"première valeur pas dans le dictionnaire : {valeur}")



