from typing import List, Tuple

def read_input_file(path: str) -> Tuple[int, List[int]]:
    """
    Read cache capacity and request sequence from a file

    Returns:
        k: cache capacity
        requests: list of integer requests
    """
    with open(path, "r") as f:
        # First line: k m
        first_line = f.readline().strip()
        if not first_line:
            raise ValueError("Input file is empty or missing first line.")

        parts = first_line.split()
        if len(parts) < 2:
            raise ValueError("First line must contain k and m.")

        k = int(parts[0])

        # m isn't strictly needed, but it can be read for validation
        m = int(parts[1])

        # Second line (or rest of file): requests
        rest = f.read().split()
        if len(rest) < m:
            raise ValueError("Not enough requests provided in input file.")

        requests = list(map(int, rest[:m]))

    return k, requests


def fifo_evict(k: int, requests: List[int]) -> int:
    """
    FIFO cache eviction

    Args:
        k: cache capacity
        requests: sequence of requested item IDs

    Returns:
        Number of cache misses
    """
    cache = []          # will store items in insertion order
    misses = 0

    for r in requests:
        if r in cache:
            # Cache hit: nothing to change for FIFO
            continue
        # Cache miss
        misses += 1
        if len(cache) < k:
            # Space available: just insert
            cache.append(r)
        else:
            # Cache full: evict the oldest inserted item (front of list)
            cache.pop(0)
            cache.append(r)

    return misses

def lru_evict(k: int, requests: List[int]) -> int:
    """
    LRU evicts the item that was least recently used
    We keep a list where the end of the list is the most recently used
    """
    cache = []          # store items; order represents recency (oldest at index 0)
    misses = 0

    for r in requests:
        if r in cache:
            # Cache hit: move this item to the end (most recently used)
            cache.remove(r)
            cache.append(r)
        else:
            # Cache miss
            misses += 1
            if len(cache) < k:
                # Space available: just add item as most recently used
                cache.append(r)
            else:
                # Cache full: evict least recently used (front)
                cache.pop(0)
                cache.append(r)

    return misses

def optff_evict(k: int, requests: List[int]) -> int:
    """
    For each miss when the cache is full:
      look at each item in the cache
      find when each will be requested next in the future
      evict the one whose next use is farthest in the future
      (or the one that will never be used again)
    """
    cache = []
    misses = 0
    m = len(requests)

    for i, r in enumerate(requests):
        if r in cache:
            # Cache hit: do nothing
            continue

        # Cache miss
        misses += 1

        if len(cache) < k:
            # Space available: insert the item
            cache.append(r)
        else:
            # Cache full: choose victim by farthest-in-future rule
            # For each item in cache, find its next use index
            farthest_next_index = -1
            victim = None

            for item in cache:
                try:
                    # find index of next occurrence of this item
                    next_index = requests.index(item, i + 1)
                except ValueError:
                    # item never used again = best candidate to evict
                    victim = item
                    break
                # Keep track of the item with the farthest next use
                if next_index > farthest_next_index:
                    farthest_next_index = next_index
                    victim = item

            # Evict the chosen victim
            cache.remove(victim)
            cache.append(r)

    return misses

def main():
    # Change the path to point to your input file
    input_path = "../tests/sample_input.txt"

    k, requests = read_input_file(input_path)
    fifo_misses = fifo_evict(k, requests)
    lru_misses = lru_evict(k, requests)
    optff_misses = optff_evict(k, requests)

    # Print in the specified format
    print(f"FIFO: {fifo_misses}")
    print(f"LRU: {lru_misses}")
    print(f"OPTFF: {optff_misses}")


if __name__ == "__main__":
    main()