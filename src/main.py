word = input('give me a word: ')
without_dbls = word
banned_letter = ''
for letter in word:
  same_letters = -1
  if banned_letter == letter:
    continue
  for otherletter in word:  
    if letter == otherletter:
      same_letters += 1
    if same_letters > 0:
      banned_letter = letter 
  without_dbls = without_dbls.replace(letter,'',same_letters)
print('without double letters: ',without_dbls)
