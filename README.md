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

## Usage
You can add/remove Licenses from the license-server using the `http://localhost:8000/docs`, There
is possible to make requests directly with the browser into the API, with examples.


To be able to generate the output from the server in the same format as the `lmutil`, we have the
`license_manager_simulator/template_files` folder, there is the `lms-util.py` file. To be able to use
it is necessary to install `jinja2` and `requests`, and it is necessary to keep the `flexlm.out.tmpl`
in the same folder as the `lms-util.py`


We also have the `application.sh` script in the root of the repository, it is a simple bash script
that is intended to run in slurm as a job that uses the licenses from the API. It is just a dummy
application for test that create a license_in_use in the API, sleeps, then delete the
license_in_use.
Just run with `./application.sh` and it is possible to specify the number of licenses in the first
args and the user_name in the second args, but they are optional and defaults to `42` and
`user$RANDOM` respectively.

## License
Distributed under the MIT License. See `LICENSE` for more information.


## Contact
Omnivector Solutions - [www.omnivector.solutions][website] - <info@omnivector.solutions>

Project Link: [https://github.com/omnivector-solutions/license-manager-simulator](https://github.com/omnivector-solutions/license-manager-simulator)
