[contributors-url]: https://github.com/omnivector-solutions/flexlm-simulator/graphs/contributors
[forks-url]: https://github.com/omnivector-solutions/flexlm-simulator/network/members
[stars-url]: https://github.com/omnivector-solutions/flexlm-simulator/stargazers
[issues-url]: https://github.com/omnivector-solutions/flexlm-simulator/issues
[license-url]: https://github.com/omnivector-solutions/flexlm-simulator/blob/master/LICENSE
[website]: https://www.omnivector.solutions
[product-screenshot]: images/screenshot.png

[Contributors][contributors-url] •
[Forks][forks-url] •
[Stargazers][stars-url] •
[Issues][issues-url] •
[MIT License][license-url] •
[Website][website]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/omnivector-solutions/flexlm-simulator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">flexlm-simulator</h3>

  <p align="center">
    A License manager simulator project for testing license integration in user applications.
    <br />
    <a href="https://github.com/omnivector-solutions/flexlm-simulator/issues">Report Bug</a>
    ·
    <a href="https://github.com/omnivector-solutions/flexlm-simulator/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Prerequisites](#prerequisites)
- [Build](#build)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project
The flexlm-simulator is an application that simulates lmutil output for use in the development of applications which interface to the license servers.

## Prerequisites
Snapcraft

    sudo snap install snapcraft --classic

## Build
Use snapcraft to build and install the snap.

    snapcraft --use-lxd

## Installation
Use the `snap install` command to install the built snap.

    sudo snap install flexlm-simulator_0.1_amd64.snap --dangerous

## Usage
Once the snap is installed, visit `http://<your-computer-ip-address>:9999` to see the simulated license usage output.

## Built With
- [snapcraft](https://snapcraft.io)

## License
Distributed under the MIT License. See `LICENSE` for more information.


## Contact
Omnivector Solutions - [www.omnivector.solutions][website] - <info@omnivector.solutions>

Project Link: [https://github.com/omnivector-solutions/charm-centos7](https://github.com/omnivector-solutions/charm-centos7)
