#!/usr/bin/env python3
"""FlexlmSimulator web."""
import os

from pathlib import Path


def application(env, start_response):
    """Display flexlm-simulation."""
    flexlm_out = Path(f"{os.environ['SNAP_COMMON']}/flexlm.out")

    if flexlm_out.exists():
        output = flexlm_out.read_text()
    else:
        output = ""

    start_response('200 OK', [('Content-Type', 'plain/text')])
    return [output.encode()]
