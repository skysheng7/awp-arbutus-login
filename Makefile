.PHONY: help update lock env clean docker

# Default conda environment name
ENV_NAME ?= arbutus

# Default root directory
ROOT_DIR ?= .

# Default yml file name
YML_NAME ?= environment.yml

# Platforms to lock for (leave empty to use conda-lock default multi-platform)
# Note: win-64 excluded by default because s3cmd requires Unix (__unix dependency)
# To include Windows, remove s3cmd from environment.yml or make it platform-specific
PLATFORMS := linux-64 osx-64 osx-arm64

help:
	@echo "Available targets:"
	@echo "  make update    - Export conda environment to environment.yml with version numbers"
	@echo "  make lock      - Generate conda-lock.yml for all platforms"
	@echo "  make env       - Update environment.yml and generate lock files (default)"
	@echo "  make clean     - Remove generated lock files"
	@echo "  make docker    - Run Docker container with arbutus_python service"
	@echo ""
	@echo "Variables:"
	@echo "  ENV_NAME       - Conda environment name (default: arbutus)"
	@echo "  ROOT_DIR       - Root directory (default: .)"
	@echo "  YML_NAME       - YML file name (default: environment.yml)"
	@echo ""
	@echo "Example:"
	@echo "  make all ENV_NAME=myenv"

update:
	@echo "Exporting $(ENV_NAME) environment to $(YML_NAME) (from history)..."
	conda export -n $(ENV_NAME) --from-history > $(YML_NAME)
	@echo "Adding version pins to $(YML_NAME)..."
	python scripts/00-update-environment-yml.py \
		--root_dir="$(ROOT_DIR)" \
		--env_name="$(ENV_NAME)" \
		--yml_name="$(YML_NAME)"

lock:
	@echo "Generating conda-lock.yml for platforms: $(PLATFORMS)..."
	conda-lock lock --file $(YML_NAME) $(foreach platform,$(PLATFORMS),--platform $(platform))

env: update lock
	@echo "Done! Updated $(YML_NAME) and generated conda-lock.yml for all platforms."

clean:
	@echo "Cleaning generated lock files..."
	rm -f conda-lock.yml conda-*.lock

docker:
	@echo "Running Docker container with arbutus_python service..."
	docker compose run --rm arbutus_python

