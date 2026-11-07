
import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

ORANGE = 15844367

BANNER_URL = "https://media.discordapp.net/attachments/1513949300411994202/1568418750468849734/image.png.webp?ex=6aefbf49&is=6aee6dc9&hm=f97490ca44d60097531f548706a569e064bbcfa85d36a9d0d31678b42ea7e7f9&=&format=webp"

REGULATION_URL = "https://docs.google.com/document/d/15ja1u5uvGlupNFsZyLETHYZfZzDGfWoG3LqdQJVcfeo/edit?usp=sharing"

DATABASE_URL = "https://docs.google.com/spreadsheets/d/1zsOTyVMecjjdoh1X_BtcuYd5Mc6ESQWf_4ovVQIQOks/edit?gid=0#gid=0"

embeds = [
    {
        "color": ORANGE,
        "image": {
            "url": BANNER_URL
        }
    },
    {
        "title": "REGULATION",
        "url": REGULATION_URL,
        "description": (
            "Our regulations explain how to operate while on duty as TSU.\n\n"
            "They include vehicle, uniform, and callsign regulations, "
            "as well as other valuable information."
        ),
        "color": ORANGE,
        "footer": {
            "text": "TRAFFIC SERVICES UNIT • OFFICIAL INFORMATION"
        }
    },
    {
        "title": "TSU CHAIN OF COMMAND",
        "description": (
            "The following positions make up the division's Chain of Command.\n\n"
            "```text\n"
            "TCO  |  Traffic Coordinator\n"
            "SUP  |  Supervisor\n"
            "INS  |  Inspector\n"
            "SGT  |  Sergeant\n"
            "SOF  |  Senior Officer\n"
            "OFR  |  Officer\n"
            "OIT  |  Officer in Training\n"
            "```\n"
            "Please follow the appropriate Chain of Command "
            "when seeking assistance or raising concerns."
        ),
        "color": ORANGE,
        "footer": {
            "text": "TRAFFIC SERVICES UNIT • CHAIN OF COMMAND"
        }
    },
    {
        "title": "TSU DATABASE",
        "url": DATABASE_URL,
        "description": (
            "Our database is a roster/list of people who are in our division.\n\n"
            "If you're not listed, or your information is not listed correctly, "
            "please reach out to a Supervisor or the Traffic Coordinator."
        ),
        "color": ORANGE,
        "footer": {
            "text": "TRAFFIC SERVICES UNIT • DIVISION RECORDS"
        }
    }
]

payload = {
    "username": "TSU | Information Hub",
    "embeds": embeds,
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

    if response.status_code in (200, 204):
        print("TSU Information Hub sent successfully!")
    else:
        print("Discord Error:", response.status_code)
        print(response.text)

except requests.RequestException as error:
    print("Failed to send:", error)
