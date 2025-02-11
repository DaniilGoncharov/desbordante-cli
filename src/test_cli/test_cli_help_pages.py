import pytest
from click.testing import CliRunner

from src.cli import desbordante_cli, Algorithm, Task


@pytest.fixture
def runner():
    return CliRunner()


def test_main_help_page(runner, snapshot):
    result = runner.invoke(desbordante_cli, '--help').output
    snapshot.assert_match(result, 'main_help')


@pytest.mark.parametrize('algo', list(Algorithm))
def test_algos_help_pages(runner, snapshot, algo):
    result = runner.invoke(desbordante_cli, f'--algo={algo} --help').output
    snapshot.assert_match(result, f'{algo}')


@pytest.mark.parametrize('task', list(Task))
def test_tasks_help_pages(runner, snapshot, task):
    result = runner.invoke(desbordante_cli, f'--task={task} --help').output
    snapshot.assert_match(result, f'{task}')
