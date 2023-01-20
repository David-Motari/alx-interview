#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
from sys import stdin


if __name__ == "__main__":
    stts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    count = 1
    file_size = 0

    def get_line(line):
        """
        Parse line and grab data from it
        """
        try:
            read_line = line.split()
            stts_code = read_line[-2]
            if stts_code in stts.keys():
                stts[stts_code] += 1
            return int(read_line[-1])
        except Exception:
            return 0

    def print_stats():
        """
        print stats
        """
        print("File size: {}".format(file_size))
        for key in sorted(stts.keys()):
            if stts[key]:
                print("{}: {}".format(key, stts[key]))

    try:
        for line in stdin:
            file_size += get_line(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
