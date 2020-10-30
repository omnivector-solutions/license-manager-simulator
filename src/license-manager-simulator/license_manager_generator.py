#!/usr/bin/env python3
"""FlexLM Generator."""
import os

from pathlib import Path
from random import randint

from jinja2 import Environment, FileSystemLoader


TOTAL_LICENSES = 1000
MAX_JOBS = 50
LICENSE_MAX_PER_JOB = 50
USERS = ['jxezha', 'jbemfv', 'ratrta', 'ratrat']


def generate_jobs():
    """Generate a list of jobs using less then the TOTAL_LICENSES."""
    def gen_jobs_and_licenses():
        """Generate a combination of random license allocations."""
        accum_jobs = list()
        for i in range(0, randint(0, MAX_JOBS)):
            accum_jobs.append(
                {
                    'job_id': i,
                    'license_allocations': randint(0, LICENSE_MAX_PER_JOB)
                }
            )
        return accum_jobs

    jobs = gen_jobs_and_licenses()

    while sum(job['license_allocations'] for job in jobs) > TOTAL_LICENSES:
        jobs = gen_jobs_and_licenses()

    return jobs


def gen_flexlm_output() -> None:
    """Render the flexlm output file."""
    source = 'flexlm.out.tmpl'
    target = Path(f"{os.environ['SNAP_COMMON']}/flexlm.out")

    loader = FileSystemLoader(f"{os.environ['SNAP']}")
    rendered_template = Environment(loader=loader).get_template(source)

    if target.exists():
        target.unlink()

    target.write_text(
        rendered_template.render(
            {'jobs': generate_jobs(), 'total_licenses': TOTAL_LICENSES}
        )
    )


if __name__ == "__main__":
    gen_flexlm_output()
