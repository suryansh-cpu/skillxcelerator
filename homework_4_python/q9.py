words = ["sequoia", "education", "automobile", "abstemious"]
vowels = set("aeiou")
valid_words = [word for word in words if vowels <= set(word.lower())]
longest_word = max(valid_words, key=len)
print("Longest word with all vowels:", longest_word)
