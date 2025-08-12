### begin
# om iets te printen gebruik je print(***)

#gebruik "" voor string
# gebruikt () om functies aan te roepen
# gebrukt {} geformateerde string
# gebruik [] lijst of slice



# print("Hello, World!")      # str printen = tekst
# print(1)                    # int printen
# print(3.14)                 # float printen
# print(True)                 # bool printen
# print([1, 2, 3])            # list printen (een verzameling van variabelen)
# print(["hallo", True, 3])   # list printen

# hoe weet ik wat voor type iets is?
# print(type("Hello, World!"))  # type van een string
# print(type(1))                # type van een integer
# print(type(3.14))             # type van een float
# print(type(True))             # type van een boolean

# variabelen toewijzen
# naam1 = "Samantha" # str
# # naam = naam.split('ma') # list
# # # heel veel code

# # print(type(naam))

# naam2 = "Stijn"
# print(naam1 + " en " +naam2)

# #formatteren is invullen - geformateerde string
# print(f"{naam2} leert mij Python.")

#lijst maken met []
#met . open je functies
namen=["Samantha", "Stijn", "Maggie", "Samia"]
#totaal aantal waarden in lijst
#print(len(namen))

#loop door namen - stoppen net voor elke , om te kijken wat er stond
for naam in namen:
    #iets doen in loop
    print(f"{naam} is leuk")

