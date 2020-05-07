# google-hash-code-2020: Qualification Round - Google Books
Here, I provide my code from the extended round of the 2020's Google Hash Code Challenge.

The total score is **26,863,352**.

## Problem Statement
Digitalizing Books requires scanning them in the library they are located at. The challenge is to scan as many books as possible in the given amount of time over all available libraries considering each book's value. Each library needs a certain amount of days to register for the scanning process (sign-up time). This sign up process cannot be done in parallel for multiple libraries. After that a library can scan a certain amount of books per day. Once registered, libraries can scan books in parallel. Each books has a certain numerical value that counts towards the total score. Books can be located in multiple libraries, however, they only need to be scanned once, hence they count only once towards the total score.

The full problem can be found on [Google Hash Code Archive](https://codingcompetitions.withgoogle.com/hashcode/archive).

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
