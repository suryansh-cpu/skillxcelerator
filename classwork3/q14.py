phrase = input("Enter your superhero phrase: ")
words = phrase.split()
acronym = ""
for word in words:
    acronym = acronym + word[0].upper()
print("Your superhero codename is:", acronym)