# CoinSumChallenge
Redone in python to better show my understanding
Coding Challenge where a List of coins and a sum goal.
The program will find the least amount of coins possible to meet the sum goal.

The user is prompted to enter a list of coins available (example: 1 2 3 4 5) and a goal sum (example: 9)
The program returns the number of coins used and the coins that were used. (example: 2, [5, 4])
  - logging for debugging

Algorithm:
  - goal was to touch the fewest number of coins while reaching the solution
  - since the list is sorted, I use the median index to understand if the best coin to use is to the right or left
      - when the set is of even size it uses the higher median to try to use the bigger number first.
  - if the coin is not found it takes the median of the best direction set
  - if a neighboring or current coin is a perfect match it stops searching (with a search by medians the neighbors are visited last)

Things I could have done:
  - keep a cashe of previously touced coins to avoid finding them again 
      - this could be done by passing a future number while holding the solution with the current
  - after completing my code I thoguht of a better option for touching less indexes without checking neighboring values
        - will be implementing the optimal solution as well
