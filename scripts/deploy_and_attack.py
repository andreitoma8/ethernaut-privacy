from scripts.helpful_scripts import get_account
from brownie import Attacker


def main():
    account = get_account()
    attack = Attacker.deploy(
        "0x87620365BDB5Dc1d31EBf1A9E18C8a401bd729B6", {"from": account}
    )
    print("Attack contract deployed!")
    tx = attack.attack(
        "0xa46ae0fe9f6ee363a55e0f3e331df82ca673ace8eabf40411a5d79f21563a1b2",
        {"from": account},
    )
    tx.wait(1)
    print("Attack began!")
