
import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

# TSU document links
REGULATION_URL = "https://docs.google.com/document/d/1wOzU3Y3ia7nrEf3XZw7HqKS1Zwtx8qQh3ou223Vb4aM/edit?usp=sharing"

GOVERNMENT_URL = "https://rcmp.ca/en/traffic-safety/about"

DATABASE_URL = "https://docs.google.com/spreadsheets/d/1zsOTyVMecjjdoh1X_BtcuYd5Mc6ESQWf_4ovVQIQOks/edit?gid=0#gid=0"

ORANGE = 15844367

# 1. Regulation
regulation = {
    "title": "Regulation",
    "url": REGULATION_URL,
    "description": (
        "Our regulations explain how to operate while on duty as TSU.\n"
        "They include vehicle, uniform, and callsign regulations, "
        "as well as other valuable information."
    ),
    "color": ORANGE
}

# 2. TSU Government Website
government = {
    "title": "TSU Government Website",
    "url": GOVERNMENT_URL,
    "description": (
        "This is the official government website that explains "
        "the role of TSU and how they operate. "
        "Please take the time to review this."
    ),
    "color": ORANGE
}

# 3. TSU Chain of Command
chain_of_command = {
    "title": "TSU Chain of Command",
    "description": (
        "**TCO | Traffic Coordinator**\n"
        "**SUP | Supervisor**\n"
        "**INS | Inspector**\n"
        "**SGT | Sergeant**\n"
        "**SOF | Senior Officer**\n"
        "**OFR | Officer**\n"
        "**OIT | Officer in Training**"
    ),
    "color": ORANGE
}

# 4. TSU Database
database = {
    "title": "TSU Database",
    "url": DATABASE_URL,
    "description": (
        "Our database is a roster/list of people who are in our division.\n"
        "If you're not listed, or your information is not listed correctly, "
        "please reach out to a Supervisor or the Traffic Coordinator."
    ),
    "color": ORANGE
}

# Send everything in ONE Discord message
payload = {
    "username": "TSU Information",
    "embeds": [
        regulation,
        government,
        chain_of_command,
        database
    ],
    "allowed_mentions": {
        "parse": []
    }
}

try:
    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        timeout=20
    )

    if response.status_code == 204:
        print("TSU Information sent successfully!")
    else:
        print("Discord Error:", response.status_code)
        print(response.text)

except requests.RequestException as error:
    print("Failed to send:", error)
