# vtt-timeshift

Adjust the timestamps on a [.VTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (transcript)
to accommodate for cropping the beginning of the source video

:warning: This is not well-tested. Double-check the results yourself.  PRs welcome.

## Setup

```bash
git clone git@github.com:andytuba/vtt-timeshift
cd vtt-timeshift
virtualenv -p python3 .
pip install -r requirements.txt
```

## Usage

Put your `transcript.vtt` file in the `vtt_files/` directory

In your terminal:

```bash
source bin/activate
python shift_it.py --time 00:05:23.010 vtt_files/transcript.vtt

```
to timeshift all the captions back 5 minutes, 23.01 seconds. _If the video is padded at the beginning, instead of cropped, add a `--padded` argument, like `python shift_it.py --padded --time etc`_

The timeshifted version of the .vtt file will be placed in the `output/` directory (unless you specify a `--output path/to/file.vtt`).
