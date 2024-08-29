#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys
import signal

# Store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # Keep count of the number of lines processed


def print_metrics():
    """Print the current metrics."""
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes_dict.keys()):
        if status_codes_dict[key] > 0:
            print('{}: {}'.format(key, status_codes_dict[key]))


def handle_interrupt(signum, frame):
    """Handle keyboard interruption (CTRL + C) gracefully."""
    print_metrics()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()

        # Validate the line has the correct format
        if len(parts) < 7:
            continue

        status_code = parts[-2]
        file_size = parts[-1]

        # Update metrics if the status code is recognized
        if status_code in status_codes_dict:
            status_codes_dict[status_code] += 1

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        count += 1

        # Print metrics every 10 lines
        if count % 10 == 0:
            print_metrics()

except Exception as e:
    print("Error:", e, file=sys.stderr)

finally:
    print_metrics()
