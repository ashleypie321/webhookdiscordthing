
import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

DATABASE_URL = "https://docs.google.com/spreadsheets/d/1zsOTyVMecjjdoh1X_BtcuYd5Mc6ESQWf_4ovVQIQOks/edit?gid=0#gid=0"

payload = {
    "username": "TSU Database",
    "embeds": [
        {
            "title": "TSU Database",
            "url": DATABASE_URL,
            "description": (
                "Our database is a roster/list of people who are in our division.\n"
                "If you're not listed, or your information is not listed correctly, "
                "please reach out to a Supervisor or the Traffic Coordinator."
            ),
            "color": 15844367
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("TSU Database sent successfully!")
else:
    print("Error:", response.status_code, response.text)
