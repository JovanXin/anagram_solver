
def anagram(user_anagram):
  sorted_anagram = ''.join(sorted(user_anagram.lower())) #turns user inputted word into lowercase and sorted
  with open('words.txt', 'r') as file1:
    for word in file1:
      sorted_word = ''.join(sorted(word.lower())) #turns each word into lowercase and sorted
      if sorted_word == sorted_anagram: 
        return (f"The solution to your anagram is {word}")
      return (f"Your anagram, {user_anagram}, does not seem to be present in our dictionary, \nor is not a real word")

print(anagram(input("what is your word: ")))
