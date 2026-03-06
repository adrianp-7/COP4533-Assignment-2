# COP4533 Assignment 2

- Arnav Bagmar
- Adrian Pelaez

---

## Running the Program

Python 3

```bash
python3 cache_algos.py <input_file>
```

**Example:**
```bash
python3 cache_algos.py tests/test_1.txt
```

**Output:**
```
FIFO  : 26
LRU   : 23
OPTFF : 18
```

---

## Input Format

The input file should have two lines:
- Line 1: two integers `k` (cache capacity) and `m` (number of requests)
- Line 2: `m` space-separated integers representing the request sequence

**Example:**
```
3 60
1 6 1 1 1 2 2 3 5 2 ...
```

---

## Assumptions

- All item IDs are positive integers
- Input files are well-formed and contain at least `m` requests on line 2
- No external dependencies beyond the Python 3 standard library

---

 ##Written Component

- [Question 1: Empirical Comparison](questions/Question1.md)
- [Question 2: Bad Sequence for LRU or FIFO](questions/Question2.md)
- [Question 3: Proof that OPTFF is Optimal](questions/Question3.md)