from util import Stack, Queue 

f = open('words.txt', 'r')
word_set = set(f.read().lower().split("\n"))
f.close()
​
def get_neighbors(word):
    '''
    Get all words that are one letter
    away from the given word
    '''
    # Get same length words first
    results = []
    list_word = list(word)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # If resulting word is in the word_set, add to results
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    return results
​
# get_neighbors("cat")
​
# # Create an equality function
# def words_are_neighbors(w1, w2):
#     '''
#     return True if words are one letter apart
#     False otherwise
#     '''
#     list_word = list(w1)
#     # Go through each letter in the word
#     for i in range(len(list_word)):
#         # swap with each letter in the alphabet
#         for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
#             # Check if that equals given word
#             temp_word = list_word.copy()
#             temp_word[i] = letter
#             if "".join(temp_word) == w2:
#                 return True
#     return False
​
# def words_are_neighbors(w1, w2):
#     print(f"comparing {w1} - {w2}")
#     if len(w1) != len(w2):
#         return False
#     for i in range(len(w1)):
#         if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
#             return True
#     return False
​
​
# def words_are_neighbors(word1, word2):
#     for i in range(len(word1)):
#         list_word1 = list(word1)
#         list_word2 = list(word2)
#         list_word1.pop(i)
#         list_word2.pop(i)
#         if list_word1 == list_word2:
#             return True
​
# words_are_neighbors("abc", "abd")
​
# neighbors = {}
​
# # Go through each word
# for word in words:
#     neighbors[word] = set()
#     # Go through each potential neighbor
#     for potential_neighbor in words:
#         # Add to neighbors if they match
#         if words_are_neighbors(word, potential_neighbor):
#             neighbors[word].add(potential_neighbor)
​
​
# def get_neighbors(word):
#     return neighbors[word]
​
# 3: Traverse the graph (BFS)
def word_ladder(begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if it's our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        # If not, mark as visited
        if w not in visited:
            visited.add(w)
            # Enqueue path to each neighboring word
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
​
​
print("HERE")
print(word_ladder("sail", "boat"))
print("END")
​
​
​
​
