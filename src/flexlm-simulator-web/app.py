#!/usr/bin/env python3
import os
from pathlib import Path


def application(env, start_response):
    FLEXLM_OUT = Path(f"{os.environ['SNAP_COMMON']}/flexlm.out")

    if FLEXLM_OUT.exists():
        output = FLEXLM_OUT.read_text() 
    else:
        output = ""

    start_response('200 OK', [('Content-Type','plain/text')])
    return [output.encode()]
