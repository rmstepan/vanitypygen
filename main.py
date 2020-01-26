import bitcoin
import random
import time
import sys


def pattern_mine(pattern = "dft", startWith = False):
    secret_key = ""
    address = ""
    while 1:
        # generate the secret private key
        secret_key = bitcoin.random_key()

        # generate the address derived from private key
        address = bitcoin.privkey_to_address(secret_key)

        if bool(startWith):
            if address.startswith("1" + pattern): break
        else:
            if pattern in address: break

    print("Vanity address found: ", address)
    print("HEX private key: ", secret_key)

if __name__ == "__main__":
    start = time.time()
    pattern_mine(sys.argv[1], sys.argv[2])
    end = time.time() - start
    print("Elapsed time: ", end)
