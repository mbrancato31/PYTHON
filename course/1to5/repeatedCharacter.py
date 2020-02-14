sentence = "This is a common interview question"
senunpacked = [*sentence]
letters = {}


for letter in senunpacked:
    if letter not in letters:
        letters[letter] = 0
    if letter in letters:
        letters[letter] += 1

greater = 0

for letter in letters:
    if greater < letters[letter]:
        greater = letters[letter]

print(greater)
