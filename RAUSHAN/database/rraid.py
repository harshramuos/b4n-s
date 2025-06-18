from RAUSHAN.database import cli

collection = cli["RAUSHAN"]["rraid"]


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