#compile with pyinstaller "Roblox Launcher.exe" --onefile --noconsole

import os
import shutil

verList = os.listdir("C:\\Program Files (x86)\\Roblox\\Versions")

path = ""

latestModified = 0.0

#check for older versions
for i in verList:
    prefix = i.split("-")[0]
    
    if prefix == "version":
        path = "C:\\Program Files (x86)\\Roblox\\Versions\\" + i
        
        if(os.path.getmtime(path) >= latestModified):
            latestModified = os.path.getmtime(path)

#remove older versions
for i in verList:
    prefix = i.split("-")[0]
    
    if prefix == "version":
        path = "C:\\Program Files (x86)\\Roblox\\Versions\\" + i
        
        if(os.path.getmtime(path) != latestModified):
            shutil.rmtree(path)
        

#run roblox
verList = os.listdir("C:\\Program Files (x86)\\Roblox\\Versions")

path = ""

for i in verList:
    prefix = i.split("-")[0]
    
    if prefix == "version":
        path = "C:\\Program Files (x86)\\Roblox\\Versions\\" + i

        if "RobloxPlayerBeta.exe" in os.listdir(path):
            break

if(path != ""):
    os.chdir(path)
    os.system("start RobloxPlayerBeta.exe")