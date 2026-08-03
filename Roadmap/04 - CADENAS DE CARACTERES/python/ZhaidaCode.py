"""
Operaciones 
"""

s1="Hola"
s2="Python"

print(s1 +" "+ s2) #Concatenar

#indexing
print(s1[0] + s1[1])

#Longitud
print(len(s1))

#slice
print(s1[0:3])

#busqueda
print("a" in s1)

#Division
print(s1.split("o"))
print(s2.split("t"))

print("-------------")
print(s1.lower())
print(s2.upper())
print(s1.isdigit())



#Dificultad extra

def check(word1:str, word2:str):
          #palindromo
          if word1 == word1[::-1] and word2 == word2[::-1]:
                print(f"{word1} y {word2} es un palindromo")
               

          elif sorted(word1) == sorted(word2):
                print(f"{word1} y {word2} son anagramas")

          elif set(word1) == set(word2):
                print(f"{word1} y {word2} son isogramas")

          else:
                print(f"{word1} y {word2} no son palindromos, anagramas ni isogramas")

check("oso", "oso")
