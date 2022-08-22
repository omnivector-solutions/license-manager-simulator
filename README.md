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

The API will be available at `http://localhost:8000/lm-sim`.

## Prerequisites
To use the license-manager-simulator you must have `Slurm` and `license-manager-agent` charms deployed with `Juju`.
Instructions for this can be found at the [License Manager documentation](https://omnivector-solutions.github.io/license-manager/).

For each license server supported, there's a script that requests license information to the simulator API and a template
where the data will be rendered. These files need to be copied to the `license-manager-agent` machine.

You also need to add licenses to the simulator API and to the Slurm cluster, and then copy an application file to the `slurmd` node to run a job.

To prepare your local `license-manager-agent` to use the simulator, run the simulator API, get its IP address and
pass it to the `make setup` command:

```bash
$ make setup lm_sim_ip=http://127.0.0.1:8000/lm-sim
```

After executing this command, you'll be able to submit jobs that use the simulated licenses.

## Usage
You can add/remove licenses from the license server API using the online interface at `http://localhost:8000/lm-sim/docs`. This helps you to make requests directly with the browser into the API, with examples.

There is an `application.sh` script that is intended to run in Slurm as a job that uses the licenses from the API. It is just a dummy
application for testing purposes that creates a license_in_use in the API, sleeps, then deletes the license_in_use.
There is also a `batch.sh` script to run the application via `sbatch`.

These files are seeded with the API IP address provided in the step above and available at `/tmp` folder in the `slurmd` node.

To submit the job, run:

```bash
$ juju ssh slurmd/leader sbatch /tmp/batch.sh
```

## License
Distributed under the MIT License. See `LICENSE` for more information.


## Contact
Omnivector Solutions - [www.omnivector.solutions][website] - <info@omnivector.solutions>

Project Link: [https://github.com/omnivector-solutions/license-manager-simulator](https://github.com/omnivector-solutions/license-manager-simulator)
