import requests

ip = requests.get("https://api.ipify.org").text
print("Your IP is:", ip)
input("Press Enter to close uwu...")
