from difflib import get_close_matches
wordlist = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        wordlist.append(line)
 
 
text = input("Write text: ")
words = text.split()
 
wrong_spelled = [] 
output_text = []
 
for word in words:
    clean_word = word.strip(".,!?;:").lower()
    if clean_word in wordlist:
        output_text.append(word)
    else:
        output_text.append(f"*{word}*")
        wrong_spelled.append(clean_word)
 
print(" ".join(output_text))
print("suggestions:")
for word in wrong_spelled:
    suggestions = get_close_matches(word, wordlist)
    print(f"{word}: {', '.join(suggestions)}")