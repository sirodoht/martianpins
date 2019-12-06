import requests
from background_task import background

from main import models


@background(schedule=1)
def ipfs_add(ipfs_file_name, ipfs_file_path, user_id):
    with open(ipfs_file_path, "rb") as f:
        response = requests.get(
            f"http://localhost:5001/api/v0/add?arg=" + ipfs_file_path,
            files={"path": f.read()},
        )
        if response.status_code == 200:
            ipfs_hash = response.json()["Hash"]
            print(f"IPFS add for {ipfs_file_path}. Hash: {ipfs_hash}")

            # check if is already pinned
            ipfs_file, created = models.IPFSFile.objects.get_or_create(
                ipfs_hash=ipfs_hash
            )

            # create pin
            user = models.MartianUser.objects.get(id=user_id)
            models.Pin.objects.create(
                name=ipfs_file_name, ipfs_file=ipfs_file, user=user
            )

            if created:  # if created, then pin does not exist, so let's create one
                ipfs_pin_add(ipfs_hash)
        else:
            print(f"Error: IPFS add for {ipfs_file_path}.")
            print(f"Error: Status code {response.status_code}.")


@background(schedule=1)
def ipfs_pin_add(ipfs_hash):
    response = requests.get("http://localhost:5001/api/v0/pin/add?arg=" + ipfs_hash)
    if response.status_code == 200:
        for p in response.json()["Pins"]:
            print(f"Pin add for {p}")
    else:
        print(f"Error: Pin add for {ipfs_hash}.")
        print(f"Error: Status code {response.status_code}.")


@background(schedule=1)
def ipfs_pin_rm(ipfs_hash):
    response = requests.get("http://localhost:5001/api/v0/pin/rm?arg=" + ipfs_hash)
    if response.status_code == 200:
        for p in response.json()["Pins"]:
            print(f"Pin rm for {p}")
    else:
        print(f"Error: Pin rm for {ipfs_hash}.")
        print(f"Error: Status code {response.status_code}.")
