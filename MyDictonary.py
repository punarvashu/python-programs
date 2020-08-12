#Exercise : 1

print("Welcome to Dictionary\n")

Dictionary={"Injustice" : "Lack Of Justice.",
            "Appetite" : "Desire.",
            "Massacre" : "Great slaughter.",
            "Monogamy":"System of being married to only one person at a time."}

print(Dictionary.keys())

print("\nEnter word from keys to get meaning:")

Search=input()

print(Dictionary[Search])
print("\nThanks for using Dictionary")