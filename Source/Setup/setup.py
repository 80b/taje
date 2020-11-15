import os
print("Setting up Taje...")
yorn = input("Would you like Taje to ping a role when someone uses it? Y/N: ")


if yorn == "Y":
	
	setup_file = open("PingFile.txt", "w+")
	pingme = input("What is your id? Format: <@YOURID>: ")
	
	setup_file.write(pingme)
	setup_file.close()
	print("Done!")
else:
	pass

print("Installing requirements...")
os.system("pip install discord-webhook")
print("Done.")
