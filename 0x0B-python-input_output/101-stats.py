#!/usr/bin/python3
"""
import sys module
"""


import sys


"""
Prints the computed statistics.
"""


def print_statistics(total_file_size, status_code_counts):
    """
    Args:
        total_file_size (int): The total file size.
        status_code_counts (dict): A dictionary
        containing counts of status codes.

    Raises:
        None

    Returns:
        None
    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(status_code, ":", count)


"""
Reads input line by line from stdin, computes metrics, and prints statistics.
"""


def process_input():
    """
    Args:
        None

    Raises:
        None

    Returns:
        None
    """
    total_file_size = 0
    status_code_counts = {}

    try:
        line_count = 0

        # Read input line by line from stdin
        for line in sys.stdin:
            # Remove leading/trailing whitespace and split the line by spaces
            line_parts = line.strip().split()

            # Ignore lines that do not have the expected number of parts
            if len(line_parts) != 9:
                continue

            # Extract file size from line_parts and update total file size
            file_size = int(line_parts[-1])
            total_file_size += file_size

            # Extract status code from line_parts and update status code counts
            status_code = line_parts[-3]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
                print()

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_file_size, status_code_counts)


if __name__ == '__main__':
    process_input()
