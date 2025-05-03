# Ejercicio 1: Sales by match

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

### Example
```
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
```
> There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

### 📌 Function Description
Complete the ``sockMerchant`` function.

``sockMerchant`` has the following parameters:

- ``int n``: the number of socks in the pile
- ``int ar[n]``: the colors of each sock

### 🔁 Returns

- ``int``: the number of pairs

### 📥 Input Format

The first line contains an integer ``n``, the number of socks represented in ``ar``.

The second line contains ``n`` space-separated integers, ``ar[i]``, the colors of the socks in the pile.

### ⚠️ Constraints

- ``1 ≤ n ≤ 100``
- ``1 ≤ ar[i] ≤ 100 where 0 ≤ i < n``

### 🧾 Sample Input
```
9
10 20 20 10 10 30 50 10 20
```

### ✅ Sample Output
```
3
```

### 💬 Explanation

![image](https://github.com/user-attachments/assets/ac3f10f3-01bb-4d08-bca6-efcfd10abbc1)

There are three pairs of socks.

# Ejercicio 2: Jumping on the Clouds

There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting position to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

### Example
```
c = [0, 1, 0, 0, 0, 1, 0]
```

Index the array from 0...6. The number on each cloud is its index in the list, so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: ``0 → 2 → 4 → 6 or 0 → 2 → 3 → 4 → 6``.
The first path takes ``3`` jumps while the second takes ``4``.
Return: ``3``

### 📌 Function Description
Complete the ``jumpingOnClouds`` function in the editor below.

``jumpingOnClouds`` has the following parameter(s):

- ``int c[n]``: an array of binary integers

### 🔁 Returns
- ``int``: the minimum number of jumps required

### 📥 Input Format
The first line contains an integer ``n``, the total number of clouds.

The second line contains ``n`` space-separated binary integers describing clouds ``c[i]`` where ``0 ≤ i < n``.

### ⚠️ Constraints

- ``2 ≤ n ≤ 100``
- ``c[i] ∈ {0, 1}``
- ``c[0] = c[n − 1] = 0``

### Output Format
Print the minimum number of jumps needed to win the game.

### 🧾 Sample Input
```
7
0 0 1 0 0 1 0
```

### ✅ Sample Output
```
4
```

### 💬 Explanation

The player must avoid ``c[2]`` and ``c[5]``. The game can be won with a minimum of ``4`` jumps:

![image](https://github.com/user-attachments/assets/b345088a-fde3-482b-a419-b1176ad3abec)

# Ejercicio 3: Repeated String

Given a string ``s`` of lowercase English letters that is repeated infinitely many times, and an integer ``n``, the task is to find and print the number of letter a's in the first ``n`` letters of the infinite string.

### Example
```
s = 'abcac'
n = 10
```

The infinite repeated string would be: ``abcacabcac...``
The substring we consider is the first 10 characters: ``abcacabcac``
There are 4 occurrences of the letter ``a`` in that substring.

### 📌 Function Description
Complete the ``repeatedString`` function with the following signature:

``repeatedString`` has the following parameters:
- ``s``: a string to repeat
- ``n``: the number of characters to consider

### 🔁 Returns
- ``int``: the frequency of letter a in the substring

### 📥 Input Format
The first line contains a single string ``s``.

The second line contains an integer ``n``.

### ⚠️ Constraints

- ``1 ≤ ∣𝑠∣ ≤ 100``
- ``1 ≤ n ≤ 10^12``
- For 25% of the test cases. ``n>= 10^6``

### 🧾 Sample Input

```
aba
10
```

### ✅ Sample Output
```
7
```

### 💬 Explanation

The first ``n = 10`` letters of the infinite string are abaabaabaa. Because there are ``7`` a's, we return ``7``.

The first ``n = 10`` letters of the infinite string are ``abaabaaaba``.
Because there are ``7`` a's, we return ``7``.

# Ejercicio 4: Counting Valleys
An avid hiker keeps meticulous records of their hikes. During their last hike, which consisted of exactly steps steps, each step was recorded as either an uphill (U) or a downhill (D) step. Hikes always start and end at sea level, and each step represents a one-unit change in altitude.

### Definitions
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.

A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of steps, this program counts and prints the number of valleys traversed during the hike.

### Example
```
steps = 8
path = "DDUUUUDD"
```

### 📌 Function Description
Implement the function countingValleys with the following parameters:

- ``int steps``: the number of steps in the hike
- ``string path``: a string consisting of U and D characters describing the path

### 🔁 Returns
- ``int``: the number of valleys traversed

### 📥 Input Format
An integer steps, the number of steps in the hike.

A string path of length steps, describing the steps taken.

### ⚠️ Constraints

- ``2 ≤ steps ≤ 10^6``
- ``path[i] ∈ {U, D}``

### 🧾 Sample Input
```
8
UDDDUDUU
```

### ✅ Sample Output
```
1
```

### 💬 Explanation
If we represent _ as sea level, an upward step as /, and a downward step as \, the hike can be visualized as:

```
_/\      _
   \    /
    \/\/
```

The hiker enters and leaves one valley.
