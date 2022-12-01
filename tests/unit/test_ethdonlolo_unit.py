from scripts.deploy import deploy, requestDonation, removeDonation, ETH_AMOUNT_REQUEST
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network, exceptions
from web3 import Web3
import pytest


def test_can_request_donation():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation()
    assert ethDonLolo.requesters(0) == account.address
    assert ethDonLolo.requesterToDonationRequest(account.address)[3] == Web3.toWei(
        ETH_AMOUNT_REQUEST, "ether"
    )


def test_can_request_be_removed():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation()
    removeDonation()
    with pytest.raises(exceptions.VirtualMachineError):
        ethDonLolo.requesters(0) == account.address


def test_only_one_request():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation()
    requestDonation()
    assert ethDonLolo.requesters(0) == account.address
    with pytest.raises(exceptions.VirtualMachineError):
        ethDonLolo.requesters(1) == account.address


def test_can_requester_modify_request():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation()
    requestDonation(ethAmount=0.02)
    assert ethDonLolo.requesterToDonationRequest(account.address)[3] == Web3.toWei(
        0.02, "ether"
    )


def test_can_donate_to_one_requester():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation(ethAmount=0.1)
    ethDonLolo.donateToRequester(
        account.address,
        {"from": get_account(index=1), "value": Web3.toWei(0.05, "ether")},
    )
    assert ethDonLolo.requesterToDonationRequest(account.address)[3] == Web3.toWei(
        0.05, "ether"
    )


def test_can_remove_requester_after_donation_goal():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    ethDonLolo = deploy()
    requestDonation(ethAmount=0.1)
    assert ethDonLolo.requesters(0) == account.address
    ethDonLolo.donateToRequester(
        account.address,
        {"from": get_account(index=1), "value": Web3.toWei(0.1, "ether")},
    )
    assert ethDonLolo.requesterToDonationRequest(account.address)[3] == 0
    with pytest.raises(exceptions.VirtualMachineError):
        ethDonLolo.requesters(0) == account.address


def test_can_donate_to_all():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account1 = get_account(index=1)
    account2 = get_account(index=2)
    ethDonLolo = deploy()
    ethDonLolo.sendDonationRequest(
        "Alice",
        "Alice Github",
        "Good reason",
        Web3.toWei(0.1, "ether"),
        {"from": account1},
    )
    ethDonLolo.sendDonationRequest(
        "Bob",
        "Bob Github",
        "Bad reason",
        Web3.toWei(0.1, "ether"),
        {"from": account2},
    )
    assert ethDonLolo.requesters(0) == account1.address
    assert ethDonLolo.requesters(1) == account2.address
    ethDonLolo.donateToAll(
        {"from": get_account(index=3), "value": Web3.toWei(0.1, "ether")},
    )
    assert ethDonLolo.requesterToDonationRequest(account1.address)[3] == Web3.toWei(
        0.05, "ether"
    )
    assert ethDonLolo.requesterToDonationRequest(account2.address)[3] == Web3.toWei(
        0.05, "ether"
    )
