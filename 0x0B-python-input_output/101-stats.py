#!/usr/bin/python3
"""
import sys module
"""


import sys

"""
import re module
"""

import re

"""
Prints the computed statistics.
"""


def print_statistics(total_file_size, status_code_counts):
    """
    Args:
        total_file_size (int): The total file size.
        status_code_counts (dict): A dictionary containing counts of status codes.

    Raises:
        None

    Returns:
        None
    """
    print("File size:", total_file_size)
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
            # Extract file size from the line using regular expression
            match = re.match(r".*\s(\d+)$", line)
            if match:
                file_size = int(match.group(1))
                total_file_size += file_size

            # Extract status code from the line using regular expression
            match = re.match(r".*\".*?\" (\d+)", line)
            if match:
                status_code = match.group(1)
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
