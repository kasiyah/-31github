Time and Space Complexity in Python Dictionary

 ------------------------------------------------------------------------------------
|                Operation           |   Time Complexity    |    Space Complexity    |
| Creating a Dictionary              |    O(len(dict))      |         O(n)           |
| Inserting a Value in a Dictionary  |     O(1)/O(n)        |         O(1)           |
| Traversion a given Dictionary      |        O(n)          |         O(1)           |
| Accessing a given cell             |        O(1)          |         O(1)           |
| Searching a given value*           |        O(n)          |         O(1)           |
| Deleting a given value             |        O(1)          |         O(1)           |
 ------------------------------------------------------------------------------------

* if using in operator - Time Complexity is O(1) since the key is known