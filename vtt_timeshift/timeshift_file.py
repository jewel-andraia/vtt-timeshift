import datetime
import os
import webvtt

from vtt_timeshift.vtt_timestamp import argparse_vtt_timestamp
from vtt_timeshift.vtt_timestamp import timeshift_vtt
from vtt_timeshift.vtt_timestamp import timeshift_vtt_timestamp


TIMEDELTA_FORMAT = '{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}'

def timeshift_file(filename, shift_by, padded, output):
    if output is None:
        _, tail = os.path.split(filename)
        basename, ext = os.path.splitext(tail)
        output = "output/{basename}_{padded}{shift_by}{ext}".format(
            basename=basename,
            padded='+' if padded else '',
            shift_by=TIMEDELTA_FORMAT.format(**shift_by[0]),
            ext=ext
        )

    vtt = webvtt.read(filename)
    vtt = timeshift_vtt(vtt, shift_by[1], padded)
    vtt.save(output)


