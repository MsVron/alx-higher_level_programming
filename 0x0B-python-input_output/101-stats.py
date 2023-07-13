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
This script reads input log lines from stdin,
computes metrics, and prints statistics.

The expected input format is as follows:
<IP Address> - [<Timestamp>] "<HTTP Method> <URL> <HTTP Version>"
<Status Code> <File Size>

The script calculates the total file size and counts
the occurrences of each status code.

Example usage: ./101-generator.py | ./101-stats.py
"""

"""
Prints the computed statistics.
"""


def print_statistics(total_file_size, status_code_counts):
    """
    Args:
        total_file_size (int): The total file size.
        status_code_counts (dict): A dictionary containing
        counts of status codes.

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
    Returns:
        None
    """
    total_file_size = 0
    status_code_counts = {}

    try:
        line_count = 0

        for line in sys.stdin:
            match = re.match(r".*\s(\d+)$", line)
            if match:
                file_size = int(match.group(1))
                total_file_size += file_size

            match = re.match(r".*\".*?\" (\d+)", line)
            if match:
                status_code = match.group(1)
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
                print()

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)


if __name__ == '__main__':
    process_input()
