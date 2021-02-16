# Problem 5: Trie

## Method and Data Structures:
We use classes to create a trie data structure where we track a word like it is a tree and mark the end with a boolean value. We could have siply used a list but the
tim complexity increases drastically as we traverse through each word and check all characters of each word in the worst case.

## Worst case time complexity is: <b> O(m) </b>
Insert character in a trie children dictionary -> O (1)
Insert a word in a Trie data structure -> O (m), where m is the length of the largest word
Finding a word in a trie data structure -> O (m) where m is the length of the largest word

## Worst case space complexity is:
The space complexity of trie seems to be: O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie.
