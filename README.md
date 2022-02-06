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
```
