
import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

payload = {
    "username": "TSU Database",
    "embeds": [
        {
            "title": "TSU Database",
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

print("Sent!" if response.status_code == 204 else response.text)
