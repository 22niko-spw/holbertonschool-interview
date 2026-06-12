#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    i = 0
    while i < len(data):
        byte = data[i] & 0xFF

        if byte >> 7 == 0:
            num_bytes = 1
        elif byte >> 5 == 0b110:
            num_bytes = 2
        elif byte >> 4 == 0b1110:
            num_bytes = 3
        elif byte >> 3 == 0b11110:
            num_bytes = 4
        else:
            return False

        for j in range(1, num_bytes):
            if i + j >= len(data):
                return False
            continuation = data[i + j] & 0xFF
            if continuation >> 6 != 0b10:
                return False

        i += num_bytes
    return True
