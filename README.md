# awesome-project

A Python project called awesome-project

## Features

- **CLI Application** with Typer framework
- **Rich terminal output** with colors and formatting
- **Interactive commands** with help and configuration
- **Global installation** support via pipx
- **Modern Python tooling** (uv, ruff, black, mypy, pytest)
- **Pre-commit hooks** for code quality
- **GitHub Actions** CI/CD workflows
- **Comprehensive testing** with coverage reports
- **Version management** with automated bumping
- **Professional project structure** following best practices

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/ryannikolaidis/awesome-project.git
cd awesome-project

# Install dependencies
make install-dev
```

### Global Installation
Install awesome_project globally using pipx (recommended):

```bash
# Build and install globally
make install-package

# Or manually:
make build
pipx install .
```

After installation, you can use the `awesome-project` command from anywhere.

### Uninstall

```bash
make uninstall-package
# Or: pipx uninstall awesome_project
```
## Usage

```bash
# Show help
awesome-project --help

# Say hello
awesome-project hello
awesome-project hello --name Alice
awesome-project hello --name Bob --loud

# Show application info
awesome-project info

# Manage configuration
awesome-project config
awesome-project config --show
```

## Development

### Setup

```bash
# Install development dependencies
make install-dev

# Install pre-commit hooks
uv run pre-commit install
```

### Common Commands

```bash
# Run tests
make test

# Run linting
make lint

# Fix formatting
make tidy

# Run all checks
make check

# Build documentation
make docs

# Build and serve docs locally
make docs-serve

# Build package
make build

# Install globally
make install-package

# Bump version
make version-dev
```

### Testing

```bash
# Run tests with coverage
make test-cov
```

## Documentation

This project uses [Sphinx](https://www.sphinx-doc.org/) for documentation generation.

### Building Documentation

```bash
# Build HTML documentation
make docs

# Build and serve locally (opens in browser at http://localhost:8080)
make docs-serve

# Clean documentation build files
make clean
```

### Editing Documentation

Documentation source files are in the `docs/` directory:

- `docs/index.rst` - Main documentation page
- `docs/installation.rst` - Installation instructions
- `docs/usage.rst` - Usage examples and tutorials
- `docs/api.rst` - Auto-generated API reference

### GitHub Pages Deployment

Documentation is automatically built and deployed to GitHub Pages when you push to the `main` branch. The docs will be available at:

`https://ryannikolaidis.github.io/awesome-project/`

To enable GitHub Pages:
1. Go to your repository Settings → Pages
2. Select "GitHub Actions" as the source
3. Push to main branch to trigger the first build

## Docker

```bash
# Build image
make docker-build

# Run container
make docker-run
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
