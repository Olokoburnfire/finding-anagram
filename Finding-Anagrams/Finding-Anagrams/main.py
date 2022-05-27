# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # my code was added here
    print("sorted(word)", sorted(word))
    print("sorted(anagram)", sorted(anagram))
    return sorted(word) == sorted(anagram)

print(find_anagram("hello", "check"))

print(find_anagram("below", "elbow"))



