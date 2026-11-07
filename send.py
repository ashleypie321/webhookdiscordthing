
import os
import requests

# Discord webhook secret
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

# TSU LINKS
REGULATION_URL = "https://docs.google.com/document/d/1wOzU3Y3ia7nrEf3XZw7HqKS1Zwtx8qQh3ou223Vb4aM/edit?usp=sharing"

GOVERNMENT_URL = "https://rcmp.ca/en/traffic-safety/about"

DATABASE_URL = "https://docs.google.com/spreadsheets/d/1zsOTyVMecjjdoh1X_BtcuYd5Mc6ESQWf_4ovVQIQOks/edit?gid=0#gid=0"

# TSU BANNER

BANNER_URL = "https://media.discordapp.net/attachments/1513949300411994202/1568418750468849734/image.png.webp?ex=6aefbf49&is=6aee6dc9&hm=f97490ca44d60097531f548706a569e064bbcfa85d36a9d0d31678b42ea7e7f9&=&format=webp"
# ORANGE COLOUR
ORANGE = 15844367

# 1. BANNER
banner = {
    "color": ORANGE,
    "image": {
        "url": BANNER_URL
    }
}

# 2. REGULATION
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

# 3. GOVERNMENT WEBSITE
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

# 4. CHAIN OF COMMAND
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

# 5. DATABASE
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

# SEND EVERYTHING IN ONE DISCORD MESSAGE
payload = {
    "username": "TSU Information",
    "embeds": [
        banner,
        regulation,
        government,
        chain_of_command,
        database
    ],
    "allowed_mentions": {
        "parse": []
    }
}

# SEND WEBHOOK
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
