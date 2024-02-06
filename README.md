
# Hanoi Sort

Hanoi sort is a sorting algorithm based on the Tower of Hanoi.

To run this application, run `python3 hanoi_sort.py`. The interface expects users to input the list of integers they wish to sort in the order they appear in the list.
Alternatively, the defined function `hanoi_sort(comp, lst)` can be called in code, where `comp` is the comparator for the items of the list (defined as if `x < y`, then `comp(x, y) < 0`, if `x == y`, then `comp(x, y) == 0`, and if `x > y`, then `comp(x, y) > 0`), and `lst` is the list of items to be sorted. The list will be sorted in ascending order.

## Algorithm

Hanoi sorts starts by creating a Tower of Hanoi state, initialising one tower to the input list. It then repeats the following indefinitely until a valid check occurs:

1) We choose two random Hanoi spaces, x and y.
2) If they are the same, we return to the top.
3) If both the chosen spaces are empty, then we check if the final remaining space is sorted. If it is we return.
4) Otherwise, we check if moving the top item from x to y is a valid Hanoi move. If it is we perform the Hanoi move.

A move is a valid Hanoi move if either: the item is being put onto an empty tower, or if the item is being put on top of an item smaller than it according to the comparator (so that they are in order).

## Example

Let us attempt to sort the list `[2, 3, 1]`, aiming to sort the list in ascending order

We represent the Hanoi state as three columns, yielding the initial state as follows:
```
A|B|C
-|-|-
1| | 
3| | 
2| | 
```
We pick column `B` and column `A`. Since column `B` is empty, the move is invalid and we pick again.  
We pick column `A` and column `A`. Since the columns are the same, the move is invalid and we pick again.  
We pick column `C` and column `B`. Since both columns are empty, we check to see if `A` is in order. It is not, so we pick again.  
We pick column `A` and column `B`. The move is valid, so the new state is:
```
A|B|C
-|-|-
 | | 
3| | 
2|1| 
```
We pick column `C` and column `B`. Since column `C` is empty, the move is invalid and we pick again.  
We pick column `A` and column `B`. The move is valid, so the new state is:
```
A|B|C
-|-|-
 | | 
 |3| 
2|1| 
```
We pick column `A` and column `B`. Since `2` need to come before `3`, the move is invalid and we pick again.  
We pick column `B` and column `C`. The move is valid so the new state is:
```
A|B|C
-|-|-
 | | 
 | | 
2|1|3 
```
We pick column `A` and column `B`. The move is valid, so the new state is:
```
A|B|C
-|-|-
 | | 
 |2| 
 |1|3 
```
We pick column `C` and column `A`. The move is valid, so the new state is:
```
A|B|C
-|-|-
 | | 
 |2| 
3|1|
```
We pick column `C` and column `C`. Since the columns are the same, the move is invalid and we pick again.  
We pick column `A` and column `B`. The move is valid, so the new state is:
```
A|B|C
-|-|-
 |3| 
 |2| 
 |1|
```
We pick column `B` and column `B`. Since the columns are the same, the move is invalid and we pick again.  
We pick column `C` and column `B`. Since column `C` is empty, the move is invalid and we pick again.  
We pick column `A` and column `B`. Since column `C` is empty, the move is invalid and we pick again.  
We pick column `C` and column `A`. Since both columns are empty, we check to see if `B` is in order. It is, so we return the contents of the column, returning `[1, 2, 3]`.  

## Time Complexity

I may calculate this one day. Probably not though. Its worst case is trivially unbound: it could keep choosing to move an item between two valid spots. Its best case is trivially linear: if the list is already sorted, and it happens to choose the two spots which are empty, then it merely performs one check to ensure the list is sorted, which is linear. It is probably at least exponential on average, since solving the tower of Hanoi is exponential.
