#!/usr/bin/python3

"""
This module contains a script that reads stdin line by line
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
    - total_size (int): Total file size computed from the input.
    - status_counts (dict): Dictionary containing counts of specific status
    codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def process_lines(lines):
    """
    Process lines to compute total file size and status code counts.

    Args:
    - lines (list): List of strings representing input lines.

    Returns:
    - total_size (int): Total file size computed from the input.
    - status_counts (dict): Dictionary containing counts of specific status
    codes.
    """
    total_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

    return total_size, status_counts


lines = []
try:
    for i, line in enumerate(sys.stdin, start=1):
        lines.append(line.strip())
        if i % 10 == 0:
            total_size, status_counts = process_lines(lines)
            print_statistics(total_size, status_counts)
            lines = []
except KeyboardInterrupt:
    total_size, status_counts = process_lines(lines)
    print_statistics(total_size, status_counts)
