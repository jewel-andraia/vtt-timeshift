import argparse

from vtt_timeshift.vtt_timestamp import argparse_vtt_timestamp

def parse_args():
    parser = argparse.ArgumentParser(
        description='Timeshift (adjust the timestamps) of captions in a .VTT file',
    )
    parser.add_argument(
        'filename', 
        type=str, 
        help='path to vtt file'
    )
    parser.add_argument(
        '--output', 
        metavar='filename',
        required=False,
        type=str, 
        help='path to save timeshifted vtt file to'
    )
    parser.add_argument(
        '--time',
        metavar='shift',
        default='00:01:00.000',
        type=argparse_vtt_timestamp, 
        help='how far to shift, in the form HH:MM:SS.SSS or SS.SSS'
    )
    parser.add_argument(
        '--padded',
        action='store_true',
        default=False,
        help='was video padded at the beginning (instead of cropped)'
    )

    args = parser.parse_args()
    
    return args
    
