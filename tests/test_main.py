"""Tests for awesome_project.main module."""

from typer.testing import CliRunner

from awesome_project.main import app

runner = CliRunner()


def test_hello_command():
    """Test hello command with default name."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout


def test_hello_command_with_name():
    """Test hello command with custom name."""
    result = runner.invoke(app, ["hello", "--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.stdout


def test_hello_command_loud():
    """Test hello command with loud option."""
    result = runner.invoke(app, ["hello", "--name", "Bob", "--loud"])
    assert result.exit_code == 0
    assert "HELLO BOB!" in result.stdout


def test_info_command():
    """Test info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "awesome-project" in result.stdout
    assert "0.1.0" in result.stdout


def test_config_command():
    """Test config command."""
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
    assert "Configuration created!" in result.stdout


def test_config_show():
    """Test config command with show option."""
    result = runner.invoke(app, ["config", "--show"])
    assert result.exit_code == 0
    assert "No configuration file found" in result.stdout


def test_help():
    """Test help output."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "A Python project called awesome-project" in result.stdout
