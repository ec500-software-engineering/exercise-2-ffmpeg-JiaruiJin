from pytest import approx
import subprocess
import json

def ffprobe(file) -> dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    file])
    return json.loads(meta)

def test_duration():
    fnin = 'videoplayback.mp4'
    fnout = 'videoplayback.mp4_480.mp4'

    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    assert orig_duration == approx(duration_480)
