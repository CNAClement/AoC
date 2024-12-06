from dataclasses import dataclass
from functools import lru_cache as cache
import time

start=time.time()
# Retrieve input and store in local file
try:
    with open(r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\Avent\2023\12_1.txt', 'r') as f:
        input_data = f.read().splitlines()
except ValueError as e:
    logger.error(e)


def validate(test, answer):
    """
    Args:
        test: the answer given by our solution
        answer: the expected answer, e.g. from instructions
    """
    if test != answer:
        raise AssertionError(f"{test} != {answer}")


@dataclass(frozen=True)
class SpringsRecord():
    record: str
    damaged_groups: tuple

    @cache # to cache, our SpringRecord must be immutable - hence frozen
    def get_arrangements_count(self, char_idx: int, curr_group_idx: int, curr_group_len: int):
        """ Permet de tester toutes les combinaisons par récursivité.
        Plutôt que la solution bruteforce que j'ai employée précédemment, permet de n'avoir à gérer que 3 variables
        qui permettent de prendre une photo parfaite de l'état de l'enregistrement à l'instant t.

        Args:
            char_idx (int): current position in the record
            curr_group_idx (int): current group in damaged_groups
            curr_group_len (int): current length of damaged group

        Returns:
            int: count of arrangements
        """
        if char_idx < len(self.record):
            #print(f"paramètres de la fonction : char_idx : {char_idx}, curr_group_idx : {curr_group_idx}, curr_group_len : {curr_group_len} ; caractère traité : {self.record[char_idx]} , sur l'enregistrement {self.record} ")
            count = 0
        # base case - check if we have a complete and valid arrangement
        if char_idx == len(self.record):  # if we're at the end; all chars have been processed
            #print(f"fin de l'enregistrement")
            if curr_group_idx == len(self.damaged_groups) and curr_group_len == 0:
                #print("tous les groupes sont remplis correctement")
                return 1  #arrangement valide, on ajoute 1 au count
            elif curr_group_idx == len(self.damaged_groups) - 1 and self.damaged_groups[curr_group_idx] == curr_group_len:
                #print("le dernier groupe vient d'être rempli correctement")
                return 1   #arrangement valide, on ajoute 1 au count
            else:  # we have not completed all groups, or current group length is too long
                return 0  # invalide

        # Process the current char in the record by recursion
        # Determine valid states for recursion
        for char in [".", "#"]:
            # On traite juste cette liste (nommée char) comme on traiterait n'importe quelle liste construite "en dur" ou non, en prenant ses éléments un par un. For ligne in lignes, for element in tableau, etc.
            # Premier passage, char vaut "."
            if self.record[char_idx] in (char, "?"):
                # On regarde si le caractère effectivement traité est égal soit à la valeur actuelle de char (qui vaut SOIT "." SOIT "#"), soit à "?"
                # Autrement dit, si le caractère traité est "#" et qu'on est dans le cas char = "." , on ne fait rien et on passe juste à l'itération suivante du for, c'est à dire char = "#" avant de dérouler le traitement de type "#"
                # Inversement, si le caractère traité est "." et qu'on est dans le cas char = "#"  , ça signifie qu'on a déjà effectué les actions de type "." dans le passage précédent de la boucle, et là on ne fait rien.
                # L'un dans l'autre, lorsque char_idx = "." ou "#" (donc pas "?" ), sur les deux passages, il y en a un où il ne se passe rien, et l'autre où il se passe les traitements adapté au caractère en question (cf en dessous).
                # Si char_idx = ?" , on passera dans les deux cas de la boucle, d'abord dans les actions de type "." , puis dans les actions de type "?"
                if char == ".":
                    # Redite : Il faut vraiment comprendre que l'on passera dans cette boucle même si char_idx = "?" .
                    #  A ce stade, char_idx ne peut pas valoir "#", si c'était le cas on n'aurait pas pu passer le test précédent puisque char_idx (#) n'est pas dans (char,"?" ).
                    #char est juste un index qui permet de dire quel type d'actions on va effectuer, si ce sont les actions de type "." ou du type "#"
                    # Le "." et le "?" sont traités de la même façon, si c'est un "?" il n'y a pas de substitution (replace) au sens littéral du terme, on va simplement faire l'action "comme si c'était un point".

                    #print("Actions de type '.' ")
                    if curr_group_len == 0:  #On n'est pas en train de construire un groupe, donc aucune incidence si on passe simplement au caractère suivant sans rien faire
                        count += self.get_arrangements_count(char_idx + 1, curr_group_idx, 0)
                    elif (curr_group_idx < len(self.damaged_groups)
                          and curr_group_len == self.damaged_groups[curr_group_idx]):
                        # Le groupe est terminé, on passe au suivant
                        count += self.get_arrangements_count(char_idx + 1, curr_group_idx + 1, 0)
                    #else : #on rentre ici lorsqu'on a un point et un groupe en cours de constitution mais pas terminé, ou si curr_group_idx = len(self.damaged_groups)..
                    # Si le caractère est traité commme un "." (soit parce que c'est vraiment un ".", soit parce que c'est un "?" :
                    # puisqu'on se retrouve avec des groupes qui ne pourront jamais correspondre à la longueur attendue (exemple : (1,1, x ) au lieu de (1,2,y) , ça ne sert à rien de continuer.
                    # Là, ce qu'il se passe c'est qu'on n'appelle pas la fonction récursive, on remonte donc "directement" jusqu'au for en se mettant dans le cas char = "#" (qui sera le cas utile).
                    # Conséquence : si c'est un "?" , il sera traité comme un "#" (ça ne servait à rien de le traiter comme un ".", comme expliqué précédemment)
                    # si c'est un ".", il ne sera pas traité du tout (not in (char, ? ) ) , et là on sort vraiment de la boucle puisqu'on a traité les deux cas char = "." puis char = "#".
                    # Donc on reprend directement à une boucle antérieure.
                else:
                    #de même que pour l'autre cas, si on rentre ici c'est que char_idx n'est pas un "."  (et qu'on en est au "#" de la boucle for qui itère sur la liste ["." , "#" ]
                    # Que char_idx soit un vrai "#" ou un "?" , on va faire des actions de type "#" , c'est-à-dire augmenter la taille du groupe en cours de traitement.
                    count += self.get_arrangements_count(char_idx + 1, curr_group_idx, curr_group_len + 1)
        # Comme commenté précédemment : en cas de "?" , on passe dans les deux cas de la boucle (actions de type "." puis actions de type "#" ), contrairement aux fois où char_idx vaut "." ou "#" où on n'effectue qu'un seul type d'actions (le bon).
        # Le fait que la fonction soit récursive (c'est-à-dire qu'elle s'appelle elle-même dans chacun des cas) fait que le 2eme cas sera traité beaucoup plus tard (une fois que le 1er cas sera arrivé jusqu'au bout de la chaine).
        # Si on a 5 "?" dans la chaine à traiter, le premier passage complet de la chaine les aura tous valorisés à "." (ça aura fait "?????" puis ".????" puis "..???" puis "...??" puis "....?" puis "....." )
        # Ensuite, grâce au principe du for, on traitera le cas "....#" , puis "...#.", puis "...##" , puis "..#.." , "..#.#", "..##." , "..###" etc.
        return count

def parse_records(data) -> list[SpringsRecord]:
    spring_records = []
    for line in data:
        record_part, groups_part = line.split()
        #print(f"ligne : {line} , ligne split : {line.split()}, record_part = {record_part} (=line.split[0] : {line.split()[0]}) et groups_part = {groups_part} (=line.split[1] : {line.split()[1]})")
        spring_records.append(SpringsRecord(record_part, tuple([int(x) for x in groups_part.split(",")])))
        #SpringsRecord(record_part, ... ) ==> créé un objet de la classe SpringsRecord, avec self.record qui va prendre la valeur du premier paramètre (ici record_part )
        # et self.damaged_group qui va prendre la valeur du second paramètre, ici un tuple avec les chiffres récupérés dans groups_part.

        #n.b : pourquoi faire tuple([int for blabla]) ?
        #Réponse : voici le retour du print précédent : ligne : #???????#. 1,6 , ligne split : ['#???????#.', '1,6'], record_part = #???????#. (=line.split[0] : #???????#.) et groups_part = 1,6 (=line.split[1] : 1,6)
        # on voit que groups_part = 1,6  (sans les parenthèses et en "un seul morceau" ), ça ne correspond pas vraiment à ce que l'on attend qui est plutôt de la forme : (1,6) avec deux valeurs bien distinctes (1 et 6).
    print(f"spring_records : {spring_records}")
    # spring_records est donc une liste d'instances de la classe SpringsRecord

    return spring_records

# For Part 2
def unfold(record: SpringsRecord, replica_count:int=5) -> SpringsRecord:
    """
    Replace record with n copies of the record, separated by ?
    Replace the damaged groups with a version that is n*current
    """
    new_rec = "?".join(replica_count*[record.record])
    new_groups = replica_count*record.damaged_groups
    return SpringsRecord(new_rec, new_groups)

def solve(records: list[SpringsRecord], part: int = 2):
    counts = 0
    for record in records:
        if part == 2:
            record = unfold(record)
        #print(f"record traité : {record}")
        count = record.get_arrangements_count(0, 0, 0)
        #if logger.getEffectiveLevel() == logging.DEBUG:  # avoid wasted compute effort
         #   logger.debug(f"{record=}, {count=}")
        counts += count

    return counts

sample_inputs = []
sample_inputs.append("""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""")
sample_answers = [21]

print("début du sample")

#for curr_input, curr_ans in zip(sample_inputs, sample_answers):
#    curr_records = parse_records(curr_input.splitlines())
#   validate(solve(curr_records), curr_ans)  # test with sample data

#logger.info("Tests passed!")
print("fin du sample")


records = parse_records(input_data)
#print(f"records : {records}") #c'est une liste qui contient, pour chaque ligne du fichier, des éléments records et group_damaged : exemple : SpringsRecord(record='.???????#.', damaged_groups=(1, 6))

soln = solve(records)
#logger.info(f"Part 1 soln={soln}")
print(soln)
print(time.time()-start)