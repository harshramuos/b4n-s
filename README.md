# 𝗔𝗟𝗣𝗛𝗔 𝗨𝗦𝗘𝗥𝗕𝗢𝗧

<p align="center">⚡️𝗔 𝗣𝗢𝗪𝗘𝗥𝗙𝗨𝗟 𝗜𝗗 𝗨𝗦𝗘𝗥𝗕𝗢𝗧⚡️</p>

<h1 align="center"
### 🚩🚩 जय बजरंग बली 🚩🚩
<h1 align="center"
  
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://readme-typing-svg.herokuapp.com?color=FF0085&width=620&lines=🍁+🚩+𝗣𝗢𝗪𝗘𝗥𝗘𝗗+𝗕𝗬+𝗥𝗔𝗨𝗦𝗛𝗔𝗡+𝗞𝗜𝗡𝗚+𝗔𝗥𝗔+🚩+🍁"></b></h3>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h1 align="center"><b>𝐓ᴇᴀᴍ 𝐏ᴜʀᴠɪ 𝐁ᴏᴛs</b></h1>
<p align="center"><a href="https://ll_ALPHA_BABY_lll"><img src="https://files.catbox.moe/mlwgfu.jpg" width="400"></a></p>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ / ʀᴇɴᴅᴇʀ 」─
</h3>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/TEAMPURVI/ALPHA_USERBOT"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-green?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>




<p align="center"## 𝖣𝖤𝖯𝖫𝖮𝖸 𝖳𝖮 𝖱𝖤𝖭𝖣𝖤𝖱

[![DEPLOY TO RENDER](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/TEAMPURVI/ALPHA_USERBOT)

## String Session

<p align="center"><a href="https://t.me/StringFatherRobot"> <img src="https://img.shields.io/badge/String%20Session-black?style=for-the-badge&logo=replit" width="220" height="38.45"/></a></p>


![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=TEAMPURVI&repo=ALPHA_USERBOT&theme=flag-india)


<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://t.me/PURVI_SUPPORT"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<a href="(https://t.me/https://t.me/+Q25anL0Ckuk5NzM1"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>


- <b> sᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋs ᴛᴏ [𝖳HE PURVI MUSIC™](https://github.com/TEAMPURVI) ғᴏʀ [𝖳HE PURVI MUSIC™](https://github.com/TEAMPURVI/PURVI_MUSIC) </b>
from pyrogram import Client, filters
import asyncio
import random

# Credentials
api_id = 29994788
api_hash = "fde39a82c05d1ea6aba52b4b36b2e205"
session_string = "BQFwyZ4AeZaMWP7t2fbFwjzPC5yi2rSqnI6H9UP9r4odkMORSv_0NyA6JiYH6ck9CSbPIQ2PJOvyZCeolC-6Udc4ITvTEVD22r2aw6LYq9BpplKWhPp1dOM6EeY--JsxFGGsQg-hvz0-2kJ_8XqejrLqYJTfQN0O7tVRk4HYLWK40Yym0Dl_wD2QUivJzEfaNmCakGXdPPwyl2I0178rdxNu3FuaX3safWYi_XWu8DHQWwr_rylZi-wkLCO0ODp0X2cBCcn-6okxVtCMPH6nHDWTQpAY3VDggECMvcrIhGlwpz3C4yaYPdHYRKUADgqrCNIgw9-3GufYOtJF-1DDc3d8hkbvfAAAAAFytaGUAA"

# Gali list
gali_list = [
    "Tere jaise to keyboard ke button bhi ignore karte hain",
    "Aukaat me reh be!",
    "Tere jese 404 error jese milte hain",
    "Bohot bakwas karta hai tu",
    "Maa ka code bhi tujhe reject kar de",
    "Shakal dekh apni pehle",
]

app = Client(name="userbot", api_id=api_id, api_hash=api_hash, session_string=session_string)


@app.on_message(filters.command("raid", prefixes=".") & filters.me)
async def reply_raid(client, message):
    if not message.reply_to_message:
        await message.reply("⚠️ Reply kis pe karun bhai? Pehle kisi message pe reply karo.")
        return

    try:
        count = int(message.command[1]) if len(message.command) > 1 else 5
    except ValueError:
        count = 5

    reply_msg = message.reply_to_message

    for i in range(count):
        gali = random.choice(gali_list)
        await reply_msg.reply_text(gali)
        await asyncio.sleep(0.5)

    await message.delete()


print("✅ Userbot reply raid is running...")
app.run()
