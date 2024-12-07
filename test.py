from re import findall
from operator import add, mul

cat = lambda x,y: int(str(x) + str(y))

ans = 0
for i, line in enumerate(open(r"C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2024\7.txt")):
    tgt, x, *Y = map(int, findall(r'\d+', line))

    X = [x]

    for y in Y:
        X = [op(x,y) for x in X for op in (add,mul)]

    if tgt in X:
        ans += tgt
        print(f"correction : ligne n° {i+1} : {line} ")

print(ans)