import argparse
import datetime
import re

TIMESTAMP_FORMAT = '%H:%M:%S.%f'
TIMESTAMP_REGEX = re.compile(r'^(?P<negative>-)?((?P<hours>\d+?):)?((?P<minutes>\d+?):)?(?P<seconds>\d+)(\.(?P<milliseconds>\d{,3}))?$')


def argparse_vtt_timestamp(arg_value):
    parts = TIMESTAMP_REGEX.match(arg_value)
    if not parts: 
        raise argparse.ArgumentTypeError

    parts = parts.groupdict()
    if parts['milliseconds']:
        # because parsing floats is bad amirite
        parts['milliseconds'] = parts['milliseconds'].ljust(3, '0')

    time_parts = dict(
        negative='',
        hours=0,
        minutes=0,
        seconds=0,
        milliseconds=0
    )

    negative = parts.pop('negative')
    coefficient = 1
    if negative:
        time_parts['negative'] = negative
        coefficient = -1

    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param) * coefficient
            time_parts[name] = int(param)
    time_delta = datetime.timedelta(**time_params)

    return (
        time_parts,
        time_delta
    )


def timeshift_vtt(vtt, timedelta, padded):
    for caption in vtt:
        caption.start = timeshift_vtt_timestamp(caption.start, timedelta, padded)
        caption.end = timeshift_vtt_timestamp(caption.end, timedelta, padded)
    return vtt

    
def timeshift_vtt_timestamp(vtt_timestamp, timedelta, padded):
    timestamp = datetime.datetime.strptime(vtt_timestamp, TIMESTAMP_FORMAT) 
    if padded:
        shifted_timestamp = timestamp + timedelta
    else:
        shifted_timestamp = timestamp - timedelta
    shifted_vtt_timestamp = shifted_timestamp.strftime(TIMESTAMP_FORMAT)
    return shifted_vtt_timestamp