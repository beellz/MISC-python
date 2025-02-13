#!/usr/bin/env python3

import json

def return_networks():
    # returning dummy ip 
    return [
        "192.168.1.0/24",
        "10.0.0.0/16",
        "172.16.0.0/12"
    ]


def main():
    # running main function with dummy output and json dumps
    networks = return_networks()
    print(json.dumps(networks))


if __name__ == "__main__":
    main()
