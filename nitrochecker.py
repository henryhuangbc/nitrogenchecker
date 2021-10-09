import random, string
import webbrowser
import time
import requests


with open("Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" _Valid | {} ".format(line.strip("\n")))
            open("Working.txt")
            r.write("")
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))