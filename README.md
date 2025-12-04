# Arbutus Cloud Computing Guide

A tutorial repository for logging into Arbutus, Compute Canada's OpenStack cloud platform.

## Prerequisites

### Install Virtual Environment

0. Prerequisite: 

* [**Miniforge**](https://conda-forge.org/download/) installed
* `conda-lock` installed
    * You can install `conda-lock` using `conda install conda-lock`
* You have applied and got an account with [Digital Research Alliance of Canada](https://www.alliancecan.ca/en/our-services/advanced-research-computing/account-management/apply-account)
* You have applied and got an account with [Arbutus](https://docs.google.com/forms/d/e/1FAIpQLSeU_BoRk5cEz3AvVLf3e9yZJq-OvcFCQ-mg7p4AWXmUkd5rTw/viewform)
* You can login to [Arbutus](https://arbutus.cloud.computecanada.ca/auth/login/?next=/)

1. Clone this repository

```bash
git clone https://github.com/skysheng7/awp-arbutus-login.git
cd awp-arbutus-login
```
2. To recreate the conda environment:

```bash
conda-lock install -n arbutus conda-lock.yml
```

Alternatively, if you prefer to use the `environment.yml` file directly:
```bash
conda env create -f environment.yml
```

3. Activate the environment

```bash
conda activate arbutus
```

4. Login to Arbutus

Login to [Arbutus](https://arbutus.cloud.computecanada.ca/auth/login/?next=/) ➡️ Click on "API Access" on the left panel ➡️ Click on "Download OpenStack RC File" ➡️ Click on "OpenStack RC File" in the drop down menu. 

Rename the downloaded file to be `def-ubcawp-dev-openrc.sh`. Please note I've put this file in the `.gitignore` file so this will not be tracked and accidently pushed to github. 

> ⚠️ DO NOT share your OpenStack RC File with anyone. Never push this to GitHub.

In your terminal, source the OpenStack credentials script:

```bash
source def-ubcawp-dev-openrc.sh
```

You will be prompted to enter your OpenStack password. Enter your password when prompted (it won't be displayed on screen for security).

### 5. Verify your login

After sourcing the script, verify that you're authenticated by checking your OpenStack credentials:

```bash
openstack token issue
```

Or list available resources:

```bash
openstack server list
```

## Additional Resources

- [Compute Canada Documentation](https://docs.computecanada.ca/)
- [OpenStack Client Documentation](https://docs.openstack.org/python-openstackclient/latest/)