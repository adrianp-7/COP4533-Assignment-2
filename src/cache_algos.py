from typing import List, Tuple

def read_input_file(path: str) -> Tuple[int, List[int]]:
    """
    Read cache capacity and request sequence from a file.

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



def main():
    # Change the path to point to your input file
    input_path = "../tests/sample_input.txt"

    k, requests = read_input_file(input_path)


if __name__ == "__main__":
    main()