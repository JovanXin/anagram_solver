
def add_words():
  word_list = []
  with open('words.txt', 'r') as file1:
    for words in file1:
      word_list.append(words.lower())
  global word_dict
  word_dict = {word.strip(): sorted(word.strip()) for word in word_list}



def anagram(user_anagram):
  user_anagram_lower = user_anagram.lower()
  sorted_anagram = sorted([letter for letter in user_anagram_lower])
  for word in word_dict:
    if sorted_anagram == word_dict[word]:
      return (f"The solution to your anagram is {word}")
  return (f"Your anagram, {user_anagram}, does not seem to be present in our dictionary, \nor is not a real word")

add_words()
print(anagram(input("what is your word: ")))