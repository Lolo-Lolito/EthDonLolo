from scripts.deploy import deploy, requestDonation, removeDonation, ETH_AMOUNT_REQUEST
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network, exceptions, accounts
from web3 import Web3
import pytest


def test_can_donate_to_one_requester():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    accounts.clear()
    accounts.add()
    ethDonLolo = deploy()
    requestDonation(ethAmount=0.01)
    ethDonLolo.donateToRequester(
        account.address,
        {"from": get_account(index=1), "value": Web3.toWei(0.005, "ether")},
    )
    assert ethDonLolo.requesterToDonationRequest(account.address)[3] == Web3.toWei(
        0.005, "ether"
    )


def test_can_donate_to_all():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account_master = get_account()
    accounts.clear()
    accounts.add()
    accounts.add()
    account1 = get_account(index=0)
    account2 = get_account(index=1)
    ethDonLolo = deploy()
    account_master.transfer(account1, Web3.toWei(0.001, "ether"))
    account_master.transfer(account2, Web3.toWei(0.001, "ether"))
    ethDonLolo.sendDonationRequest(
        "Alice",
        "Alice Github",
        "Good reason",
        Web3.toWei(0.01, "ether"),
        {"from": account1},
    )
    ethDonLolo.sendDonationRequest(
        "Bob",
        "Bob Github",
        "Bad reason",
        Web3.toWei(0.01, "ether"),
        {"from": account2},
    )
    assert ethDonLolo.requesters(0) == account1.address
    assert ethDonLolo.requesters(1) == account2.address
    ethDonLolo.donateToAll(
        {"from": account_master, "value": Web3.toWei(0.01, "ether")},
    )
    assert ethDonLolo.requesterToDonationRequest(account1.address)[3] == Web3.toWei(
        0.005, "ether"
    )
    assert ethDonLolo.requesterToDonationRequest(account2.address)[3] == Web3.toWei(
        0.005, "ether"
    )
