#!/usr/bin/env python3
"""
File that will be called by the license-manager-agent in the report function.

It will hit the /licenses-in-use/ endpoint and will generate the report in the same format as the LS-Dyna,
this way we can use the same LS-Dyna parser in the license-manager-agent.
"""
import requests
from jinja2 import Environment, FileSystemLoader

# You must modify this value to reflect the ip address and port that the
# license-manager-simulator is listening on in your environment.
#
# The format of the value is: `http://<ip-address>:<port>`
URL = "http://localhost:8000"


def get_server_data():
    """Get license information form the server."""
    license = requests.get(URL + "/licenses/").json()[-1]

    license_information = {
        "license_name": license.get("name").upper(),
        "total_licenses": license.get("total"),
        "in_use": license.get("in_use"),
        "free": int(license.get("total")) - int(license.get("in_use")),
        "licenses_in_use": license.get("licenses_in_use"),
    }

    if len(license_information["licenses_in_use"]) > 0:
        used = "-"
    else:
        used = 0
    license_information["used"] = used

    return license_information


def generate_license_server_output():
    """Print output formatted to stdout."""
    source = "lsdyna.out.tmpl"
    license_information = get_server_data()

    template = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True).get_template(
        source
    )
    print(template.render(**license_information))


if __name__ == "__main__":
    generate_license_server_output()
