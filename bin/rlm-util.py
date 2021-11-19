#!/usr/bin/env python3
"""
File that will be called by the license-manager-agent in the report function.

It will hit the /licenses-in-use/ endpoint and will generate the report in the same format as the rlm,
this way we can use the same rlm parser in the license-manager-agent.
"""
import requests
from jinja2 import Environment, FileSystemLoader

# You must modify this value to reflect the ip address and port that the
# license-manager-simulator is listening on in your environment.
#
# The format of the value is: `http://<ip-address>:<port>`
URL = "http://localhost:8000"


def get_server_data():
    license = requests.get(URL + "/licenses/").json()[0]
    return {
        "license_name": license.get("name"),
        "total_licenses": license.get("total"),
        "in_use": license.get("in_use"),
        "licenses_in_use": license.get("licenses_in_use"),
    }


def generate_license_server_output() -> None:
    """Print output formatted to stdout."""
    source = "rlm.out.tmpl"
    license_information = get_server_data()

    template = Environment(loader=FileSystemLoader(".")).get_template(source)
    print(template.render(**license_information))


if __name__ == "__main__":
    generate_license_server_output()
