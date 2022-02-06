from brownie import SimpleStorage, accounts, config


def read_contract():
    print(SimpleStorage[0])
    # Most recent deployment is -1
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
