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

4. Verification

Verify that you're authenticated by running the following commands:

**List available Docker images:**
```bash
openstack image list
```

5. Establish access to Arbutus Object Store

In order to manage your Arbutus Object Store, you need your own storage access ID & secret key. In terminal, create credentails using: 

```bash
openstack ec2 credentials create
```

6. Configure `s3cmd`

To configure the s3cmd tool, you will use the command: 

```bash
s3cmd --configure
```

Then make the following configurations using youre credential printed out in the terminal above:

```bash
Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.

Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key []: 20_DIGIT_ACCESS_KEY
Secret Key []: 40_DIGIT_SECRET_KEY
Default Region [US]:

Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint []: object-arbutus.cloud.computecanada.ca

Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used
if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket []: object-arbutus.cloud.computecanada.ca

Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password []:
Path to GPG program [/usr/bin/gpg]: 

When using secure HTTPS protocol all communication with Amazon S3
servers is protected from 3rd party eavesdropping. This method is
slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol []: Yes

On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name:
```

* You will be prompted for "Test access with supplied credentials?" --> Answer "y"
* You will be prompted for "Save settings? [y/N]" --> Answer "y"

## Additional Resources

- [OpenStack CLI Guide](https://docs.alliancecan.ca/wiki/OpenStack_command_line_clients)
- [Digital Research Alliance of Canada Documentation](https://docs.computecanada.ca/)
- [OpenStack Client Documentation](https://docs.openstack.org/python-openstackclient/latest/)
- [s3cmd setup](https://docs.alliancecan.ca/wiki/Accessing_object_storage_with_s3cmd)
