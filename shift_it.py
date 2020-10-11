import sys

from vtt_timeshift.parse_args import parse_args
from vtt_timeshift.timeshift_file import timeshift_file

def __main__():
    args = parse_args()
    if args is None:
        sys.exit()
    timeshift_file(args.filename, args.time, args.padded, args.output)
    sys.exit()

if __name__ == "__main__":
    __main__()
