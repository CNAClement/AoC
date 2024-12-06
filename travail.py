def produitListe(liste):
    if liste == [] :
        return 1
    if len(liste)==1:
        return liste[0]
    else :
        return liste[-1] * produitListe(liste[:-1])


print(produitListe([1,2,3,4]))