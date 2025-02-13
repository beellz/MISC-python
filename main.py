#!/usr/bin/env python3
import json
import argparse
import ipaddress
import sys


def return_networks():
    # returning dummy ip 
    return [
        "192.168.1.0/24",
        "10.0.0.0/16",
        "172.16.0.0/12"
    ]



def collisions_checker(file_path):
    #try and except to check if the path given is correct or the path provided has the file 
    try:
        with open(file_path, 'r') as f:
            networks = json.load(f)
    except FileNotFoundError:
        print("File Not Found")
        print("Please Check the Path or the File")
        sys.exit(0)  # Exit with status code 0
    except json.JSONDecodeError: # Anything other than json file
        print("File Not Found")
        print("Please Check the Path or the File")
        sys.exit(0)  # Exit with status code 0

    # looping to check the collision 
    collisions = []
    for i in range(len(networks)):
        for j in range(i + 1, len(networks)):
            network1 = ipaddress.ip_network(networks[i])
            network2 = ipaddress.ip_network(networks[j])
            if network1.overlaps(network2):
                collisions.append((networks[i], networks[j])) 
    return collisions


def main():

    parser = argparse.ArgumentParser(description='IP Tools')
    parser.add_argument('--check-collision', metavar='FILE', help='Check for IP networks collisions')
    args = parser.parse_args()

    if args.check_collision:
        collisions = collisions_checker(args.check_collision)
        if collisions:
            print("Colliding networks:")
            for net1, net2 in collisions:
                print(f"{net1} collides with {net2}")
        else:
            print("No collisions found.")
    else:
        networks = return_networks()
        print(json.dumps(networks))




if __name__ == "__main__":
    main()
