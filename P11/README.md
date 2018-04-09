# P11 Modified run-length encoding.
Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

### Example
```
>>> import main
>>> main.encode([1, 1, 2, 3, 3, 1, 2, 2, 3, 3])
[[2, 1], 2, [2, 3], 1, [2, 2], [2, 3]]
```
