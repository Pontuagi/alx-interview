#!/usr/bin/python3

"""
This module contains a script that reads stdin line by line
"""

import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    Prints the computed statistics.

    Args:
    - total_size (int): Total file size computed from the input.
    - status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def process_lines(lines):
    """
    Processes lines to compute total file size and status code counts.

    Args:
    - lines (list): List of strings representing input lines.

    Returns:
    - total_size (int): Total file size computed from the input.
    - status_counts (dict): Dictionary containing counts of status codes.
    """
    total_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[5])
                file_size = int(parts[6])
                total_size += file_size
                status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

    return total_size, status_counts


lines = []
try:
    for line in sys.stdin:
        lines.append(line.strip())
        if len(lines) >= 10:
            total_size, status_counts = process_lines(lines)
            print_statistics(total_size, status_counts)
            lines = []
except KeyboardInterrupt:
    total_size, status_counts = process_lines(lines)
    print_statistics(total_size, status_counts)
