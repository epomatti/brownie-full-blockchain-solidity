# Solidity + Brownie

## Setup

```bash
$ sudo apt-get install python3-venv
$ python3 -m venv env
$ . env/bin/activate
$ pip install --upgrade pip
$ pip install eth-brownie
```

## Account config

Set the `.env` file:

```env
PRIVATE_KEY=<key>
```

## Running it

```bash
brownie compile
```

```bash
npm install ganache --global
```

```bash
brownie run scripts/deploy.py --network rinkeby
brownie run scripts/deploy_fundme.py --network ganache-local
brownie run scripts/deploy_fundme.py --network mainnet-fork-dev
```

Mainnet-fork:

```bash
brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/<YOUR KEY>' accounts=10 mnemonic=brownie port=8545
