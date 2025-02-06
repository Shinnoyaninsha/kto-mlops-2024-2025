import unittest

"""
Count names with more than seven letters
"""
# def names(prenoms:list[str]) -> int:
#     more_than_seven = 0
#     for prenom in prenoms:
#         if len(prenom) > 7:
#             more_than_seven += 1
#             print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
#         else:
#             print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
#     return more_than_seven
def compter_noms_plus_de_x_lettres(list_prenoms:list[str], seuil:int=7) -> int:
    plus_long_que_seuil:int = 0
    for prenom in list_prenoms:
        if len(prenom) > seuil:
            plus_long_que_seuil += 1
            print(f"{prenom} est un prénom avec un nombre de lettres supérieur à {seuil}")
        else:
            print(f"{prenom} est un prénom avec un nombre de lettres inférieur ou égal à {seuil}")
    return plus_long_que_seuil

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        plus_long_que_seuil = compter_noms_plus_de_x_lettres(list_prenoms=prenoms)
        self.assertEqual(plus_long_que_seuil, 4)

if __name__ == '__main__':
    unittest.main()