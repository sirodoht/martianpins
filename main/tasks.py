import requests
from background_task import background


@background(schedule=1)
def ipfs_add(ipfs_file_path):
    with open(ipfs_file_path, "rb") as f:
        response = requests.get(
            f"http://localhost:5001/api/v0/add?arg=" + ipfs_file_path,
            files={"path": f.read()},
        )
        if response.status_code == 200:
            print("IPFS add for " + ipfs_file_path)
            ipfs_pin_add(response.json()["Hash"])


@background(schedule=1)
def ipfs_pin_add(ipfs_hash):
    response = requests.get("http://localhost:5001/api/v0/pin/add?arg=" + ipfs_hash)
    if response.status_code == 200:
        for p in response.json()["Pins"]:
            print(f"Pin add for {p}")

@background(schedule=1)
def ipfs_pin_rm(ipfs_hash):
    response = requests.get("http://localhost:5001/api/v0/pin/rm?arg=" + ipfs_hash)
    if response.status_code == 200:
        for p in response.json()["Pins"]:
            print(f"Pin rm for {p}")
    else:
        print(f"Error: Pin rm for {ipfs_hash}.")
        print(f"Error: Status code {response.status_code}.")
