#!/usr/bin/env python
###########################################
# Duino-Coin arduino miner version 0.5.2  #
# https://github.com/revoxhere/duino-coin #
#  copyright by MrKris7100 & revox 2019   #
###########################################

𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨=print
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡=str
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚=input
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌룤=open
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭=True
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗛥=int
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩=bytes
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ⶴ=range
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𧅈=hash
import socket,threading,time,random,configparser,sys,serial,hashlib,serial.tools.list_ports
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡑷=hashlib.sha1
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗷓=serial.Serial
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ݷ=serial.tools
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞡙=sys.exit
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﺁ=configparser.ConfigParser
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿=time.sleep
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𑂋=threading.Timer
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞡄=socket.socket
from pathlib import Path
def 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ꭿ():
 global 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﶽ,𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﶽ=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈=0
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𑂋(1.0,𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ꭿ).start()
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷=[0,0]
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﶽ=0
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈=0
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﺁ()
if not Path("ArduinoMinerConfig.ini").is_file():
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Initial configuration, you can edit 'ArduinoMinerConfig.ini' later\n")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Scanning ports...")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𪂗=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ݷ.list_ports.comports()
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ۑ=[]
 for 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐐤 in 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𪂗:
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ۑ.append(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐐤.device)
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Found COM ports: "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ۑ))
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ᗮ=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚("Enter your Arduino port (e.g: COM8): ")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𢾗=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚("Enter pool adddress (official: serveo.net): ")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗖾=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚("Enter pool port (official: 14808): ")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𠉁=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚("Enter username: ")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐲙=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗾚("Enter password: ")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶['pool']={"address":𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𢾗,"arduino":𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ᗮ,"port":𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗖾,"username":𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𠉁,"password":𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐲙}
 with 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌룤("ArduinoMinerConfig.ini","w")as configfile:
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶.write(configfile)
else:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶.read("ArduinoMinerConfig.ini")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ᗮ=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶["pool"]["arduino"]
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𢾗=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶["pool"]["address"]
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗖾=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶["pool"]["port"]
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𠉁=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶["pool"]["username"]
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐲙=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞢶["pool"]["password"]
while 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Connecting to pool...")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞡄()
 try:
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.connect((𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𢾗,𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗛥(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗖾)))
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Connected!")
  break
 except:
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Cannot connect to pool server. Retrying in 30 seconds...")
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿(30)
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿(0.025)
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Connecting to Arduino...")
try:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞺖=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗷓(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ᗮ,9600)
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Arduino connected!")
except:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Cannot connect to Arduino. Check your ArduinoMinerConfig.ini file.")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞡙()
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Logging in...")
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.send(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩("LOGI,"+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𠉁+","+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐲙,encoding="utf8"))
while 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭪=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.recv(1024).decode()
 if 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭪=="OK":
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Logged in!")
  break
 if 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭪=="NO":
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Invalid credentials!")
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.close()
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿(0.025)
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Started arduino mining thread...")
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿(1)
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ꭿ()
𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.send(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩("JOB",encoding="utf8"))
while 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭:
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.send(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩("JOB",encoding="utf8"))
 while 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭:
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.recv(1024).decode()
  if 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨:
   break
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𦷿(0.025)
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨.split(",")
 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Recived new job from pool. Diff: "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨[2])
 for 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﺗ in 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ⶴ(100*𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𗛥(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨[2])+1):
  𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𧅈=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡑷(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨[0]+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﺗ)).encode("utf-8")).hexdigest()
  if 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓈨[1]==𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𧅈:
   𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞺖.write(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈),encoding="utf8"))
   𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌륈=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𞺖.readline().decode('utf8').rstrip()
   𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.send(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳩(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﺗ),encoding="utf8"))
   while 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐭭:
    𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓏟=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐤡.recv(1024).decode()
    if 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓏟=="GOOD":
     𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]+1 
     𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Share accepted "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0])+"/"+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1])+" ("+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]/(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1])*100)+"%), "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﶽ)+" H/s")
     break
    elif 𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𓏟=="BAD":
     𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1]=𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1]+1 
     𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐳨("Share rejected "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0])+"/"+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1])+" ("+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]/(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[0]+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𡦷[1])*100)+"%), "+𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌𐰡(𨬓ﻭݕ𞺄ض힢𐬋ސ𧪂ﯭ凐샜ඍ㣻禾𐢝𐤣ߞ鬭ﭿﴮꍈ𐳰𠉡贐އﳃﺤ𡻌ﶽ)+" H/s")
     break
   break
# Created by pyminifier (https://github.com/liftoff/pyminifier)

