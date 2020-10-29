#!/usr/bin/env python3
import json
import os
import random
import sqlite3

from pathlib import Path

from jinja2 import Environment, FileSystemLoader


#DB_NAME = 'flexlm_simulator.db'
#DB_PATH = Path(f"{os.environ['SNAP_COMMON']/{DB_NAME}")

#DB_CONN = sqlite3.connect(str(DB_PATH))


#def init_db():
#    c = DB_CONN.cursor()
#
#    # Create the Simulations table
#    c.execute(
#        "CREATE TABLE Simulations (PRIMARY KEY (simulation_id),"
#        "application_name text, num_jobs integer)"
#    )
#
#    # Create the Licensebookings table
#    c.execute(
#        "CREATE TABLE Licensebookings (PRIMARY KEY (license_booking_id), license_type text)"
#    )
#
#    # Create the Features table
#    c.execute(
#        "CREATE TABLE Features (feature_name text, num_available integer, "
#        "FOREIGN KEY (license_booking_id) REFERENCES Licensebookings(license__booking_id))"
#    )
#
#len(c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='simulations';''').fetchall())

TOTAL_LICENSES = 1000
MAX_JOBS = 50
LICENSE_MAX_PER_JOB = 50
USERS = ['jxezha', 'jbemfv', 'ratrta', 'ratrat']


def generate_jobs():
    def gen_jobs_and_licenses():
        accum_jobs = list()
        num_jobs = random.randint(0, MAX_JOBS)

        for i in range(0, num_jobs):
            accum_jobs.append(
                {
                    'job_id': i,
                    'license_allocations': random.randint(0, LICENSE_MAX_PER_JOB)
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

