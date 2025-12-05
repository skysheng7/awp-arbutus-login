# Arbutus Cloud Computing Guide

A tutorial repository for logging into Arbutus, Compute Canada's OpenStack cloud platform, and managing object storage with S3.

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/skysheng7/awp-arbutus-login.git
cd awp-arbutus-login
```

2. Create and activate the conda environment:
```bash
conda-lock install -n arbutus conda-lock.yml
conda activate arbutus
```

## Documentation

📚 **Full documentation is available as Quarto website files in the repository root.**

### Documentation Sections

- **[Getting Started](tutorial/getting-started.qmd)** - Prerequisites and installation
- **[Arbutus Authentication](tutorial/arbutus-auth.qmd)** - Setting up OpenStack authentication
- **[S3 Storage Setup](tutorial/s3-setup.qmd)** - Configuring s3cmd for object storage
- **[S3 Operations](tutorial/s3-operations.qmd)** - Working with buckets and files
- **[Command Cheatsheet](tutorial/cheatsheet.qmd)** - Quick reference for common commands

## Additional Resources

- [OpenStack CLI Guide](https://docs.alliancecan.ca/wiki/OpenStack_command_line_clients)
- [Digital Research Alliance of Canada Documentation](https://docs.computecanada.ca/)
- [OpenStack Client Documentation](https://docs.openstack.org/python-openstackclient/latest/)
- [s3cmd setup](https://docs.alliancecan.ca/wiki/Accessing_object_storage_with_s3cmd)
