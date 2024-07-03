import os

verList = os.listdir("C:\\Program Files (x86)\\Roblox\\Versions")

path = ""

for i in verList:
    prefix = i.split("-")[0]
    
    if prefix == "version":
        path = "C:\\Program Files (x86)\\Roblox\\Versions\\" + i
        
        if "RobloxPlayerBeta.exe" in os.listdir(path):
            break

os.chdir(path)
os.system("start RobloxPlayerBeta.exe")