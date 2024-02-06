
# Hanoi Sort

Hanoi sort is a sorting algorithm based on the Tower of Hanoi.

To run this application, run `python3 hanoi_sort.py`.
The interface expects users to input the list of integers they wish to sort in the order they appear in the list.
Alternatively, the defined function hanoi_sort(comp, lst) can be called in code, where comp is the comparator for the items of the list (defined as if x < y, then comp(x, y) < 0, if x == y, then comp(x, y) == 0, and if x > y, then comp(x, y) > 0), and lst is the list of items to be sorted.

## Algorithm

Hanoi sorts starts by creating a Tower of Hanoi state, initialising one tower to the input list. It then repeats the following indefinitely until a valid check occurs:

1) We choose two random Hanoi spaces, x and y
2) If they are the same, we return to the top
3) If both the chosen spaces are empty, then we check if the final remaining space is sorted. If it is we return.
4) Otherwise, we check if moving the top item from x to y is a valid Hanoi move. If it is we perform the Hanoi move.

A move is a valid Hanoi move if either: the item is being put onto an empty tower, or if the item is being put on top of an item smaller than it according to the comparator (so that they are in order).

## Time Complexity

I may calculate this one day. Probably not though. It is probably at least on average exponential, since solving the tower of Hanoi is exponential.
