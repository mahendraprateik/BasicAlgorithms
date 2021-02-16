# Problem 7: HTTP Router implementation using trie

## Method and Data Structures:
We use 3 classes, one to create trie node, one to create trie data strructure and another one to wrap the two together with the functionality of searching a handler.

## Worst case time complexity is: <b> O(n) </b>

Trie node class insertion takes O(1) time as we are assigning children to a dictionary

Trie data structure insertion takes O (n) time where n is the length of the path list. For instance path "/about/me" generates a ["about", "me"] list and run for
the length of the list which is 2 in this case.
Trie data structure find runs in O(n) time complexity for the same above reason.

The router class directly implements the trie data structure by calling the above class hence it takes O(n) time complexity for both insertion and finding.
It takes an additional O(n) complexity to generate a list by splitting the path.

## Worst case space complexity is: <b> O(n * m) </b>
Since the only space we are creating is the nodes for each of the nodes (n) and m is the length of each node's value.
