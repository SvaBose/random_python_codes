def english_to_piglatin(word): 
  consonants = '' 
  firstletter = ''
  if word[0].lower() in 'aeiou': 
    return word + 'way'
  if word[0] not in 'aeiou':
    consonants += word[0].lower()
    if word[0].isupper() == True:
      firstletter = word[1].upper()  
    if word[0].islower() == True: 
      firstletter = word[1].lower()  
    word = word[2:]
    return firstletter + word + consonants + 'ay'

# Main Code 
word = input("What word do you want to see in pig latin? ")
print(english_to_piglatin(word))


