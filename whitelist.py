#!/usr/bin/env python3

import os
import json
import subprocess

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
L1_URL = "https://sepolia.proxy.pontem.network"
ADDRESSES_PATH = "src/evm.whiteList.json"
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xA2Aa3247B75923173Da2e6C4cc93dd5790030a6d")


def get_addresses():
    print("Getting addresses")
    with open(ADDRESSES_PATH) as addresses_file:
        addresses = json.load(addresses_file)
    print("Succesfully got addresses!")
    return addresses


def whitelist_addresses(addresses: str, contract_address: str, trues: str):
    print("Whitelisting addresses...")
    command = f"cast send {contract_address} 'whitelist(address[],bool[])' '[{addresses}]' '[{trues}]' --rpc-url {L1_URL} --private-key {PRIVATE_KEY}"
    subprocess.call(command, shell=True)
    print("Succesfully whitelisted!")


def main():
    addresses = get_addresses()
    addresses_str = ",".join(addresses)
    trues = ("true," * len(addresses))[:-1]
    whitelist_addresses(addresses_str, CONTRACT_ADDRESS, trues)


if __name__ == "__main__":
    main()
