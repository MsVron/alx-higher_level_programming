#!/usr/bin/python3

"""
sys module import
"""


import sys

"""
Print the computed statistics.
"""


def print_statistics(total_size, status_counts):
    """
    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary with status code counts.

    Returns:
        None
    """
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

"""
Parse a line and extract file size and status code.
"""
def parse_line(line):
    """
    Args:
        line (str): Input line to parse.

    Returns:
        tuple: Tuple containing file size and status code.
    """
    elements = line.split()
    file_size = int(elements[-1])
    status_code = elements[-2]
    return file_size, status_code

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        file_size, status_code = parse_line(line)
        total_size += file_size
        status_counts[int(status_code)] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)

except KeyboardInterrupt:
    print_statistics(total_size, status_counts)
