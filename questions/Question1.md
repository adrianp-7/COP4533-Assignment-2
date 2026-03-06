# Question 1: Empirical Comparison

## Results

|Input File| k | m  | FIFO | LRU | OPTFF |
|----------|---|----|------|-----|-------|
| File 1   | 3 | 60 | 26   | 23  | 18    |
| File 2   | 3 | 63 | 63   | 63  | 43    |
| File 3   | 4 | 68 | 21   | 21  | 17    |

---
## Analysis

### Does OPTFF always have the fewest misses?

Yes, OPTFF achieved the fewest misses on every test file. Being an optimal algorithm with full knowledge of the future request sequence, it always evicts the item whose next use is farthest away. OPTFF recognizes that each item will return soon and instead evicts items farther out in the cycle, while FIFO and LRU are essentially blind and miss on every single request.

### How does FIFO compare to LRU?

The results are more nuanced across these three files:

- **File 1:** LRU outperforms FIFO (23 vs. 26 misses).
- **File 2:** Both tie at 63 misses, every request is a miss.
- **File 3:** Both tie at 21 misses.

