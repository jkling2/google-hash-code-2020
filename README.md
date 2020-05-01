# google-hash-code-2020
Here, I provide my code from the extended round of the 2020's Google Hash Code Challenge.

The total score is **26,863,352**.

## Problem Statement
TODO

## Usage
```bash
usage: main.py [-h] --file {A,B,C,D,E,F} --algo {1,2,3,4,5,6}
```
The program requires a valid file and a valid algorithm. 

Valid file names are **A**, **B**, **C**, **D**, **E**, and **F**.

Valid algorithm numbers are **1**, **2**, **3**, **4**, **5**, **6**. They correspond to the following algorithm name:
* 1: GREEDY - greedy algorithm that determines the best library based on the total score a library has, considering the days left.
* 2: GREEDY_SIGN_UP_TIME - based on the greedy algorithm, further considering the library's sign-up-time 
* 3: GREEDY_TOTAL_BOOKS - based on the greedy algorithm, further considering the library's total books used
* 4: GREEDY_USED_BOOKS - based on the greedy algorithm, further considering the library's used books
* 5: AVERAGE_BOOK_SCORE - algorithm that determines the best library based on the average book score
* 6: BOOK_OCCURRENCE - algorithm that determines the best library based on the book occurrences

In order to reproduce the scores, use the following table:

| File | Algorithm | Score      |
|------|-----------|------------|
| A    | any       | 21         |
| B    | 2, 4, 6   | 5822900    |
| C    | 2         | 5683819    |
| D    | 6         | 5039450    |
| E    | 2         | 5039763    |
| F    | 2         | 5277399    |
|      | Total     | 26,863,352 |
