#!/usr/bin/python3
'''A script for passing HTTP logs.
'''
import re
import sys


status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
'''Stats for the supported status codes.
'''
total_file_size = 0
'''The cummulative sum of the file sizes in each HTTP log.
'''
fp = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)',
    r'(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)',
    r'(?P<request>[^"]*)',
    r'(?P<status_code>\d+)',
    r'(?P<file_size>\d+)'
)
'''The pattern for each field in the log.
'''
log_fmt = '{} - \\[{}\\] "{}" {} {}'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
'''The regex pattern for the log.
'''


def print_statistics():
    '''Prints the accumulated statistics of the HTTP log.
    '''
    global total_file_size
    global status_codes_stats
    stats = []
    stats.append('File size: {:d}'.format(total_file_size))
    num = 0
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            stats.append('{:s}: {:d}'.format(status_code, num))
    print('\n'.join(stats), flush=True)


def get_metrics(line):
    '''Retrieves the metrics from a given HTTP log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
    '''
    global total_file_size
    global status_codes_stats
    resp_match = re.fullmatch(log_fmt, line.rstrip().lstrip())
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        if status_code in status_codes_stats.keys():
            status_codes_stats[status_code] += 1
        total_file_size += file_size


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    while True:
        try:
            line = input()
            get_metrics(line)
            line_num += 1
            if (line_num % 10 == 0) and (line_num > 0):
                print_statistics()
        except EOFError:
            print_statistics()
            break
        except KeyboardInterrupt:
            print_statistics()
            break


if __name__ == '__main__':
    run()
