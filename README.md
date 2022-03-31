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
The license-manager-simulator is an application that simulates several license servers output for use in the development of applications which interface to the license servers.

There are 2 parts: the API to manage license information and the applications that simulate the license servers output.

License servers supported:

* FlexLM
* RLM
* LS-Dyna
* LM-X

## Installation
To install this project, clone the repository and use `docker-compose` to run it in containers:

```bash
$ docker-compose up
```
This will create a container for the API, and also a PostgreSQL container for the database.

The API will be available at `http://localhost:8000`.

## Prerequisites
To use the license-manager-simulator you must have `Slurm` and `license-manager-agent` charms deployed with `Juju`.
Instructions for this can be found at the [License Manager documentation](https://omnivector-solutions.github.io/license-manager/).

For each license server supported, there's a script that requests license information to the simulator API and a template
where the data will be rendered. These files need to be copied to the license-manager-agent machine.

Use the `prepare-environment.sh` script in the `bin` folder to copy the files to their correct location:

```bash
$ cd bin
$ ./prepare-environment.sh
```

It is necessary to add licenses to the slurm, run:
```bash
# sacctmgr add resource Type=license Clusters=osd-cluster Server=flexlm Names=fake_license.fake_feature Count=1000 ServerType=flexlm  PercentAllowed=100 -i
```

## Usage
You can add/remove licenses from the license server API using the online interface at `http://localhost:8000/docs`. This helps you to make requests directly with the browser into the API, with examples.

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
