#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    A method that determines if a given data set
    represents a valid UTF-8 encoding.
    """

    def is_start_byte(byte):
        """Helper function to check if a given byte is a valid start byte"""
        return (byte & 0b10000000) == 0b0

    def is_following_byte(byte):
        """Helper function to check if a given byte is a valid following byte
        """
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data to check each byte
    i = 0
    while i < len(data):
        # Check the number of bytes for the current character
        if is_start_byte(data[i]):
            num_bytes = 1
            if (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
                num_bytes = 2
            elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
                num_bytes = 3
            elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
                num_bytes = 4

            # Check if the following bytes are valid
            for j in range(i + 1, i + num_bytes):
                if j >= len(data) or not is_following_byte(data[j]):
                    return False

            i += num_bytes
        else:
            return False

    return True
