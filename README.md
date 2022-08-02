# 2-sum NBA players height problem
## Overview
The problem to solve can be summarized as follows: 
>Given a set of NBA players, which are the pairs of players whose height in inches adds up to a given natural number?
## Conditions
The solution program should meet the following conditions:
- The program should download the dataset form https://mach-eight.uc.r.appspot.com
- The program should print a list of all pairs of players whose height in inches adds up to the integer input to the application.
- The algorithm to find the pairs must be faster than $O (n^2)$ 
- If no matches are found, the application will print "No matches found"
- All edge cases should be handled appropriately

## Proposed Algorithm
I propose a variation of the 2-sum problem algorithm. The significant difference is that the numbers we consider (players height) can be repeated. This will impact the complexity as the algorithm will work better or worse depending not on the size of the set but on the sample distribution. A higher concentration in the distribution of heights of the players will mean a higher probability of an scenario where we could need to pair all the players of the dataset which will be always a $O (n^2)$ . Fortunately, is not the case of our dataset:

![Distribution](https://user-images.githubusercontent.com/54406272/182401477-a55ddd35-c20b-4152-9907-29a95bfad089.png)


As we can see the higher concentration is around 79. Thus, the worst case scenario will be probably around target input $2 * 79 ≈ 158$.
Empirically I found it was 159.

### Algorithm steps
**1-** Iterates the dataset creating a frequency dictionary with the different heights as key and the correspondent players who have that height as value. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $O(n)$ *where n is the number of players in the dataset* .

**2-** Creates a sorted list of the different heights taking the keys of the dictionary which are unique. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $O(c_1 log(c_1))$ *where* $c_1$ *is the number of unique heights in the data set*.

**3-** Iterates the sorted list of different heights until the height is greater than the input number/2. For each iteration check if the target input number minus the current height is present in the dictionary of height frequencies.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $O(c_2)$

&nbsp;&nbsp;&nbsp;&nbsp;**3.1-** - As the two numbers $(A,B)$ that adds up to the given input number are found in the dictionary we generate the combination between the two lists of players and printed it.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $O(P_1P_2)$ *where* $P_1$ *is the number of players with height* $A$ *, and* $P_2$ *is the number of players with height* $B$.

The complexity of the algorithm is approximately: 

&nbsp;&nbsp;&nbsp;&nbsp; $O (n)+O(C_1log(C_1))+O(C_2)O(P_1P_2)$

*In other words:*

&nbsp;&nbsp;&nbsp;&nbsp; $O(C_2P_1P_2)$

*where*

&nbsp;&nbsp;&nbsp;&nbsp; $nlog(n) < C_2P_1P_2 < n^2$

**Please be aware that the complexity could vary depending on the sample's distribution of heights.**
## Edge Cases
Handled edge cases found were:
* Wrong input type: String, float.
* input number out of range.  

## Execution

The program is written in python 3.9.7

You can run the file nba2sum.py from terminal to run the main program. 
After running it, insert the target sum number and press enter. 
It will display all the combinations.

![image](https://user-images.githubusercontent.com/54406272/182400493-eb25ed28-a8d5-4ee0-912d-0c0f8c9084dd.png)

You can run the unit test file unittesting.py

![image](https://user-images.githubusercontent.com/54406272/182401358-cb633691-60d5-4c36-9d4a-321a987ed532.png)

