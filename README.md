# Arbutus Cloud Computing Guide

Aurthor: Sky Kehan Sheng

Description: A tutorial repository for logging into Arbutus, Compute Canada's OpenStack cloud platform, and managing object storage with S3.

## Documentation

**Full Tutorial is hosted here:** [http://www.skysheng.io/awp-arbutus-login/](http://www.skysheng.io/awp-arbutus-login/)

### Documentation Sections

- **[Getting Started](tutorial/getting-started.qmd)** - Prerequisites and installation
- **[Arbutus Authentication](tutorial/arbutus-auth.qmd)** - Setting up OpenStack authentication
- **[S3 Storage Setup](tutorial/s3-setup.qmd)** - Configuring s3cmd for object storage
- **[S3 Operations](tutorial/s3-operations.qmd)** - Working with buckets and files
- **[Command Cheatsheet](tutorial/cheatsheet.qmd)** - Quick reference for common commands

## Using the Makefile

This project includes a Makefile to simplify common tasks:

```bash
# View all available commands
make help

# Run Docker container with the environment
make docker

# Update environment.yml from your conda environment
make update

# Generate cross-platform conda-lock files
make lock

# Update environment.yml and generate lock files (both update + lock)
make env
```

**Common workflow:**
1. Run `make docker` to start the containerized environment
2. Use `make env` to update dependencies after modifying the environment

## Additional Resources

- [OpenStack CLI Guide](https://docs.alliancecan.ca/wiki/OpenStack_command_line_clients)
- [Digital Research Alliance of Canada Documentation](https://docs.computecanada.ca/)
- [OpenStack Client Documentation](https://docs.openstack.org/python-openstackclient/latest/)
- [s3cmd setup](https://docs.alliancecan.ca/wiki/Accessing_object_storage_with_s3cmd)
