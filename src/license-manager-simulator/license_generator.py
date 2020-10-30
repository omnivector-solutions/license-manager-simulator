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
    def generate_jobs_and_license_allocations():
        """Generate a combination of random license allocations."""
        return [
            {
                'job_id': job_id,
                'license_allocations': randint(0, LICENSE_MAX_PER_JOB)
            }
            for job_id in range(0, randint(0, MAX_JOBS))
        ]

    jobs = generate_jobs_and_license_allocations()

    while sum(job['license_allocations'] for job in jobs) > TOTAL_LICENSES:
        jobs = generate_jobs_and_license_allocations()

    return jobs


def generate_license_server_output() -> None:
    """Render the license server output to a file."""
    source = 'flexlm.out.tmpl'
    target = Path(f"{os.environ['SNAP_COMMON']}/flexlm.out")

    loader = FileSystemLoader(f"{os.environ['SNAP']}")
    template = Environment(loader=loader).get_template(source)

    if target.exists():
        target.unlink()

    target.write_text(
        template.render(
            {'jobs': generate_jobs(), 'total_licenses': TOTAL_LICENSES}
        )
    )


if __name__ == "__main__":
    generate_license_server_output()
