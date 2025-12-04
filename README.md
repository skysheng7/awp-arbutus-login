# Arbutus Cloud Computing Guide

A tutorial repository for logging into Arbutus, Compute Canada's OpenStack cloud platform.

## Prerequisites

Before you begin, ensure you have:

* [**Miniforge**](https://conda-forge.org/download/) installed
* `conda-lock` installed (install with `conda install conda-lock`)
* An account with [Digital Research Alliance of Canada](https://www.alliancecan.ca/en/our-services/advanced-research-computing/account-management/apply-account)
* An account with [Arbutus](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform)
* The ability to login to [Arbutus](https://arbutus.cloud.computecanada.ca/auth/login/?next=/)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/skysheng7/awp-arbutus-login.git
cd awp-arbutus-login
```

2. Create the conda environment using one of the following methods:

**Using conda-lock (recommended):**
```bash
conda-lock install -n arbutus conda-lock.yml
```

**Or using environment.yml directly:**
```bash
conda env create -f environment.yml
```

3. Activate the environment:

```bash
conda activate arbutus
```

## Authentication Setup

1. Download your OpenStack RC file:
   - Login to [Arbutus](https://arbutus.cloud.computecanada.ca/auth/login/?next=/)
   - Click on "API Access" on the left panel
   - Click on "Download OpenStack RC File"
   - Click on "OpenStack RC File" in the dropdown menu

2. Rename the downloaded file to `def-ubcawp-dev-openrc.sh` and place it in the repository root directory.

   > ⚠️ **Security Warning:** DO NOT share your OpenStack RC File with anyone. Never push this to GitHub. This file is already included in `.gitignore` to prevent accidental commits.

3. Source the OpenStack credentials script:

```bash
source def-ubcawp-dev-openrc.sh
```

You will be prompted to enter your OpenStack password. Enter your password when prompted (it won't be displayed on screen for security).

## Verification

Verify that you're authenticated by running the following commands:

**List available Docker images:**
```bash
openstack image list
```

**List available servers:** It might return an empty list
```bash
openstack server list
```

## Additional Resources

- [OpenStack CLI Guide](https://docs.alliancecan.ca/wiki/OpenStack_command_line_clients)
- [Digital Research Alliance of Canada Documentation](https://docs.computecanada.ca/)
- [OpenStack Client Documentation](https://docs.openstack.org/python-openstackclient/latest/)
