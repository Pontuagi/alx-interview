#!/usr/bin/python3

"""
UTF-8 Validation module
"""


def validUTF8(data):
    """
    A function to validate UTF-8 enconding

    Args
    - data: The data to validate

    Return
    - True if data is valid UTF-8 encoding, else False
    """
    # Number of bytes to validate after the current one
    bytes_to_validate = 0

    for num in data:
        # Checking if the current number is a continuation byte
        if bytes_to_validate > 0:
            # If the current number is not in the format 10xxxxxx, return False
            if not (num >> 6 == 0b10):
                return False
            bytes_to_validate -= 1
        else:
            # Count the number of bytes to validate
            if num >> 7 == 0:
                # Single byte character
                bytes_to_validate = 0
            elif num >> 5 == 0b110:
                # Two byte character
                bytes_to_validate = 1
            elif num >> 4 == 0b1110:
                # Three byte character
                bytes_to_validate = 2
            elif num >> 3 == 0b11110:
                # Four byte character
                bytes_to_validate = 3
            else:
                # Invalid UTF-8 format
                return False

    # If all bytes are properly validated, return True
    return bytes_to_validate == 0
