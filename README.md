# Portable-Roblox-Launcher
Allow launching sym linked Roblox in diskless setup after update even without superuser to change shortcut target.

THIS APPLICATION IS FREE AND NOT FOR SALE.

Roblox will be downloaded directly from installer itself and will not be provided by me. The only thing from me is the launcher, thus minimizing the risk of malwares. Tested on Windows 10 22H2 with CCBoot and PanCafe Pro. This should work on any Windows 10 installation and any diskless solution.

INSTRUCTIONS

  1. On your diskless server, install Roblox.

  2. Create a "Roblox" folder on your gamedisk and make "AppData\Local" and "Program Files (x86)" folders inside it.

  3. Move "C:\\Users\USERNAME\AppData\Local\Roblox" to "GAMEDISK\Roblox\AppData\Local" folder you created on step 2.

  4. Move "C:\\Program Files (x86)\Roblox" to "GAMEDISK\Roblox\Program Files (x86)" folder you created on step 2.

  5. Make a symbolic link for Roblox Folders. Open cmd as administrator. Type in
    
         mklink /d "C:\\Program Files (x86)\Roblox" "GAMEDISK\Roblox\Program Files (x86)\Roblox"
         
         mklink /d "C:\\Users\USERNAME\AppData\Local\Roblox" "GAMEDISK\Roblox\AppData\Local"

  6. In "GAMEDISK\Roblox\Program Files (x86)\Roblox", search for "RobloxPlayerBeta.exe" and copy the file to "GAMEDISK\Roblox"

  7. Rename "GAMEDISK\Roblox\RobloxPlayerBeta.exe" to "RobloxIcon.exe"

  8. Copy "Roblox.Launcher.exe" to "GAMEDISK\Roblox".

     a. Right click "Roblox.Launcher.exe" > Properties > Compatibility > Check "Run this program as an administrator" > Click "OK". (DO NOT SKIP THIS STEP. YOU WILL HAVE ISSUES ON ROBLOX UPDATE IF YOU SKIP THIS STEP.)

     b. Create a desktop shortcut of "Roblox.Launcher.exe" and change shortcut icon to "RobloxIcon.exe"

  9. Repeat Step 8 on super user client pc then save.

  10. To update, just open Roblox Launcher shortcut on your diskless server.
