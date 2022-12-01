from scripts.helpful_scripts import get_account
from brownie import ETHDonLolo, network, config
from web3 import Web3

ETH_AMOUNT_REQUEST = 0.01


def deploy():
    account = get_account()
    ethDonLolo = ETHDonLolo.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("ETHDonLolo contract has been deployed!")
    return ethDonLolo


def requestDonation(ethAmount=ETH_AMOUNT_REQUEST):
    account = get_account()
    ethDonLolo = ETHDonLolo[-1]
    name = "Lolo"
    github = "https://github.com/Lolo-VRS"
    reason = "The first request of donation :)"
    ethAmount = Web3.toWei(ethAmount, "ether")
    donationRequest_tx = ethDonLolo.sendDonationRequest(
        name, github, reason, ethAmount, {"from": account}
    )
    donationRequest_tx.wait(1)
    print(f"{name} donation has been added to the list")


def removeDonation():
    account = get_account()
    ethDonLolo = ETHDonLolo[-1]
    removeDonationRequest_tx = ethDonLolo.removeDonationRequest({"from": account})
    removeDonationRequest_tx.wait(1)
    print("Donation has been deleted!")


def main():
    deploy()
    requestDonation()
    removeDonation()
