phrase = "BACKEND DEVELOPERS"
words = phrase.split()
new = ""
for word in words:
    new = new + word[0].upper()
print("Your superhero codename is:", new)