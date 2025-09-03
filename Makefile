# ==============================================================================
# Makefile for Project Automation
#
# Provides a unified interface for common development tasks, such as running
# the application, formatting code, and running tests.
#
# Inspired by the self-documenting Makefile pattern.
# See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# ==============================================================================

# Default target when 'make' is run without arguments
.DEFAULT_GOAL := help

# Specify the Python executable and main Streamlit file name
PYTHON := ./.venv/bin/python
STREAMLIT_APP_FILE := ./src/main.py

# ==============================================================================
# HELP
# ==============================================================================

.PHONY: help
help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ==============================================================================
# ENVIRONMENT SETUP
# ==============================================================================

.PHONY: setup
setup: ## Project initial setup: install dependencies and create .env file
	@echo "🐍 Installing python dependencies with uv..."
	@uv sync
	@echo "📄 Creating environment file..."
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..." ; \
		cp .env.example .env; \
		echo "✅ .env file created."; \
	else \
		echo "✅ .env already exists. Skipping creation."; \
	fi
	@echo "💡 You can customize the .env file for your specific needs."


# ==============================================================================
# APPLICATION
# ==============================================================================

.PHONY: run
run: ## Launch the Streamlit application with development port
	@if [ ! -f .env ]; then \
		echo "❌ Error: .env file not found. Please run 'make setup' first."; \
		exit 1; \
	fi
	@echo "🚀 Starting Streamlit app on development port..."
	@export $$(cat .env | grep -v '^#' | grep -v '^$$' | xargs) && PYTHONPATH=. STREAMLIT_SERVER_PORT=$${DEV_PORT:-8503} streamlit run $(STREAMLIT_APP_FILE)

.PHONY: run-prod
run-prod: ## Launch the Streamlit application with production port
	@if [ ! -f .env ]; then \
		echo "❌ Error: .env file not found. Please run 'make setup' first."; \
		exit 1; \
	fi
	@echo "🚀 Starting Streamlit app on production port..."
	@export $$(cat .env | grep -v '^#' | grep -v '^$$' | xargs) && PYTHONPATH=. STREAMLIT_SERVER_PORT=$${HOST_PORT:-8501} streamlit run $(STREAMLIT_APP_FILE)

# ==============================================================================
# CODE QUALITY
# ==============================================================================

.PHONY: format
format: ## Automatically format code using Black and Ruff
	@echo "🎨 Formatting code with black and ruff..."
	@black .
	@ruff check . --fix

.PHONY: lint
lint: ## Perform static code analysis (check) using Black and Ruff
	@echo "🔬 Linting code with black and ruff..."
	@black --check .
	@ruff check .

# ==============================================================================
# TESTING
# ==============================================================================

 .PHONY: test
test: build-test e2e-test ## Run the full test suite

 .PHONY: build-test
build-test: ## Run build tests
	@echo "Running build tests..."
	@$(PYTHON) -m pytest tests/build -s

 .PHONY: e2e-test
e2e-test: ## Run end-to-end tests
	@echo "Running end-to-end tests..."
	@$(PYTHON) -m pytest tests/e2e -s