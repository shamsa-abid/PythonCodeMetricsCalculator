def get_closest_vowel(word):
  from string import ascii_letters
  vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
  consonants = set(ascii_letters) - vowels
  triples = zip(word[:-2], word[1:-1], word[2:])
  found = [middle for left, middle, right in triples 
            if left in consonants and right in consonants and middle in vowels]
  return found[-1] if found else ""