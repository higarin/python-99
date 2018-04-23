# P27 Group the elements of a set into disjoint subsets.

a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons? Write a predicate that generates all the possibilities via backtracking.

### Example
```
>>> import main
>>> main.group3(['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])
[[['aldo', 'beat'], ['carla', 'david', 'evi'], ['flip', 'gary', 'hugo', 'ida']], [['aldo', 'beat'], ['carla', 'david', 'flip'], ['evi', 'gary', 'hugo', 'ida']], [['aldo', 'beat'], ['carla', 'david', 'gary'], ['evi', 'flip', 'hugo', 'ida']], ...
```

b) Generalize the above predicate in a way that we can specify a list of group sizes and the predicate will return a list of groups.

### Example
```
>>> import main
>>> main.group([2, 3, 4], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida'])
[[['aldo', 'beat'], ['carla', 'david', 'evi'], ['flip', 'gary', 'hugo', 'ida']], [['aldo', 'beat'], ['carla', 'david', 'flip'], ['evi', 'gary', 'hugo', 'ida']], [['aldo', 'beat'], ['carla', 'david', 'gary'], ['evi', 'flip', 'hugo', 'ida']], ...
```

Note that we do not want permutations of the group members; i.e. [[aldo,beat],...] is the same solution as [[beat,aldo],...]. However, we make a difference between [[aldo,beat],[carla,david],...] and [[carla,david],[aldo,beat],...].

You may find more about this combinatorial problem in a good book on discrete mathematics under the term "multinomial coefficients".
