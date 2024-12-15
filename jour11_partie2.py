"""La méthode "naïve" de la partie 1 ne marche pas sur la partie 2, pour des raisons de bruteforce.
Solution : faire un graph de type DFS où on teste, pierre par pierre, son devenir.
Utiliser une fonction de caching de manière à garder en mémoire le résultat pour une pierre à un niveau donné.
Par exemple si on sait que la pierre numéro "20" sur la depth "4" donne le résultat [ .... ] et que l'on retombe
sur ces mêmes conditions plus tard (une autre pierre "20" sur une depth "4" ), on n'a pas besoin de tout refaire.

On peut même se dire que si on tombe sur une pierre "20" sur un depth n < 4 (exemple : n = 2 ), on peut directement sauter
et ne traiter que les (4-n) dernières depths à partir du résultat de fonction("20", "4" ).
Nécessite un cache capable de gérer les sauts conditionnels, pas si simple (ChatGPT).

Dans les deux cas je suis un peu sceptique car l'espace de nombres possibles est très grand et très hétérogène,
donc la probabilité de tomber sur un nombre déjà connu me semble relativement faible (quoi que, la transformation
qui divise en 2 la longueur des nombres permet de rester sur un espace relativement restreint)
Multiplier par 2024 ( ~2*10^3) permet de dire que quasiment une fois sur deux, on repasse d'une longueur impaire
(puissance de 10 paire) à une longueur impaire, puisque pair + 3 = impair. Quasiment car *2,.. )



 Autre idée : bfs (au lieu de dfs), et lorsque l'on arrive à une profondeur donnée, on regarde s'il y a
 des doublons, et si oui, on supprime tout mais on rajoute un facteur multiplicatif pour le résultat à la fin.
 Si la pierre "20" à la profondeur "60" donne 1000 pierres à l'arrivée, et qu'à la profondeur 60
 on rencontre 10 pierres 20, on obtiendra 1000 * 10 pierres. """