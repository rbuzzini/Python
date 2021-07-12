# Given a word w and a string s, find all indices in s which are the starting 
# locations of anagrams of w. For example, given w is ab and s is abxaba,
#  return [0, 3, 4]


# Solution 1 (book):
# Go over each word-sized window in s and check if it forms an anagram of w.

from collections import Counter


# Define a function which return true if s2 is the anagram of s1 of false
# otherwise
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


# final_function:
def anagram_indices(s, w):
    # Initialize indices empty list.
    indices = []


    for i in range(len(s)):
        sub_s = s[i:(i + len(w))]
        if is_anagram(sub_s, w) == True:
            indices.append(i)
        else:
            pass
    

    return indices


s_check = "abxaba"
word = "ab"
print(anagram_indices(s_check, word))


# In the code above, we use Python's buil-in Counter collection.
# This would make O(w x s) time, where w is the length of the word and s is the
# length of the input string. Can we make this any faster? 



# Solution 2 (book):

from collections import defaultdict


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]


def anagram_indices2(s, w2):
    indices = []


    freq = defaultdict(int)
    for char in w2:
        freq[char] += 1
    

    for char in s[:len(w2)]:
        freq[char] -= 1
        del_if_zero(freq, char)
    

    if not freq:
        indices.append(0)

    
    for i in range(len(w2), len(s)):
        start_char, end_char = s[i - len(w2)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)


        freq[end_char] -= 1
        del_if_zero(freq, end_char)


        if not freq:
           beginning_index = i - len(w2) + 1
           indices.append(beginning_index)

    return indices

print(anagram_indices2(s_check, word))
print("First function is equal to second function result? {0}".format(
    anagram_indices(s_check, word) == anagram_indices2(s_check, word)
))

# This runs in O(s) time and space