import pytest

import ds.preprocessing
import ds.tests.wallet as wallet


def yes(func):
    def wrapper():
        func()

    return wrapper


@yes
def test_fib():
    assert ds.preprocessing.fib(0) == 0
    assert ds.preprocessing.fib(1) == 1
    assert ds.preprocessing.fib(34) == 5702887


@pytest.mark.slow
@pytest.mark.crazy
def test_rfib():
    assert ds.preprocessing.rfib(0) == 0
    assert ds.preprocessing.rfib(1) == 1
    assert ds.preprocessing.rfib(34) == 5702887


@pytest.fixture()
def empty_wallet():
    """
    :return: wallet instance with balance zero
    """
    return wallet.Wallet()


def test_default_initial(empty_wallet):
    assert empty_wallet.check_balance() == 0


@pytest.mark.parametrize("deposit, withdraw, balance", [
    (100, 50, 50),
    (1000, 50, 950)

])
def test_deposit(empty_wallet, deposit, withdraw, balance):
    empty_wallet.deposit(deposit)
    empty_wallet.withdraw(withdraw)
    assert empty_wallet.check_balance() == balance


def test_insufficient_balance(empty_wallet):
    with pytest.raises(Exception):
        empty_wallet.withdraw(10)
