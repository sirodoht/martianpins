import requests
from background_task import background
from django.core.mail import send_mail


@background(schedule=1)
def ipfs_add(file_name):
    requests.get("http://localhost:5001/api/v0/add?arg=" + file_name)


@background(schedule=1)
def ipfs_pin_add(ipfs_hash):
    print(f"pin add for '{ipfs_hash}'")
    requests.get("http://localhost:5001/api/v0/pin/add?arg=" + ipfs_hash)
