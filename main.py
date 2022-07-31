#Mod 3 Zad 1
print("Mod 3 zad 1") 
print()
d = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    }
suma = 0
for k in d:
    temp = [v.capitalize() for v in d[k]]
    print(f"Idę do {k.capitalize()} kupię tu naspępujące rzeczy {temp}")
    suma = suma + len(d[k])    
print(f"W sumie kupuję {suma} produktów")
print()

#Mod 3 Zad 2
print("Mod 3 zad 2") 
print()
licz1 = [x for x in range(0,100) if not x % 5]
licz2 = [y**3 for y in licz1]
print(licz1)
print(licz2)
print("'Hispańska inkwizycja' to najlepszy skecz Monty Pythona")
print("test1")
print("test2")
