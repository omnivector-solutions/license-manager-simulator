[contributors-url]: https://github.com/omnivector-solutions/license-manager-simulator/graphs/contributors
[forks-url]: https://github.com/omnivector-solutions/license-manager-simulator/network/members
[stars-url]: https://github.com/omnivector-solutions/license-manager-simulator/stargazers
[issues-url]: https://github.com/omnivector-solutions/license-manager-simulator/issues
[license-url]: https://github.com/omnivector-solutions/license-manager-simulator/blob/master/LICENSE
[website]: https://www.omnivector.solutions

[Contributors][contributors-url] •
[Forks][forks-url] •
[Stargazers][stars-url] •
[Issues][issues-url] •
[MIT License][license-url] •
[Website][website]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/omnivector-solutions/license-manager-simulator">
    <img src=".images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">license-manager-simulator</h3>

  <p align="center">
    A License management simulator project for testing license integration in user applications.
    <br />
    <a href="https://github.com/omnivector-solutions/license-manager-simulator/issues">Report Bug</a>
    ·
    <a href="https://github.com/omnivector-solutions/license-manager-simulator/issues">Request Feature</a>
  </p>
</p>

[![.github/workflows/test_push.yaml](https://github.com/omnivector-solutions/license-manager-simulator/actions/workflows/test_push.yaml/badge.svg)](https://github.com/omnivector-solutions/license-manager-simulator/actions/workflows/test_push.yaml)

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project
The license-manager-simulator is an application that simulates `lmutil` output for use in the development of applications which interface to the license servers.

There are 2 parts: the API and the application to render the `lmutil` output.

## Installation
To install this project, just clone the repository, then:

```bash
$ pip install .
```
it will install all the dependencies to be able to run the API.

To run the API, use the `Makefile`:

```bash
$ make local
```
This will run the server at `http://localhost:8000`

## Prerequisites
For the `bin/lms-util.py` you may need to change the first line to match the python3 in the
environment that have requests and jinja2 installed, and also it is necessary to change the URL to
match the license-manager backend URL.

For the `job/application.sh` it may be necessary to change the URL to match the
license-manager-simulator backend.

It is necessary to add licenses to the slurm, run:
```bash
# sacctmgr add resource Type=license Clusters=osd-cluster Server=flexlm Names=fake_license.fake_feature Count=1000 ServerType=flexlm  PercentAllowed=100 -i
```

## Usage
You can add/remove Licenses from the license-server using the online interface at `http://localhost:8000/docs`. This helps you to make requests directly with the browser into the API, with examples.

To be able to generate the output from the server in the same format as the `lmutil`, we have the
`bin` folder, in there is the `lms-util.py` file. To be able to use
it is necessary to install `jinja2` and `requests`, and it is necessary to keep the `flexlm.out.tmpl`
in the same folder as the `lms-util.py`. Must replace the `lmutil` with `lms-util.py`, keeping the
`lmutil` name, and put the `flexlm.out.tmpl` in the same folder.

We also have the `job` folder, there is the `application.sh` it is a simple bash script
that is intended to run in Slurm as a job that uses the licenses from the API. It is just a dummy
application for test that creates a license_in_use in the API, sleeps, then deletes the
license_in_use. There is also the `batch.sh`, which is the script to be run via `sbatch`.

To run it, it is necessary to have both scripts available in the nodes and have licenses in the
cluster.

## License
Distributed under the MIT License. See `LICENSE` for more information.


## Contact
Omnivector Solutions - [www.omnivector.solutions][website] - <info@omnivector.solutions>

Project Link: [https://github.com/omnivector-solutions/license-manager-simulator](https://github.com/omnivector-solutions/license-manager-simulator)
