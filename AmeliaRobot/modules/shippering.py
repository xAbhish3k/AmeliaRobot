from AmeliaRobot import pbot as app
from AmeliaRobot.utils.errors import capture_err
from AmeliaRobot.utils.dbfunc import get_couple, save_couple
from pyrogram import filters
import random
from datetime import datetime


# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(' ')
    return dt_list


def dt_tom():
    a = str(int(dt()[0].split('/')[0]) + 1)+"/" + \
        dt()[0].split('/')[1]+"/" + dt()[0].split('/')[2]
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())


@app.on_message(filters.command("couples") & ~filters.edited)
@capture_err
async def couple(_, message):
    if message.chat.type == "private":
        await message.reply_text("This command only works in groups.")
        return
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in app.iter_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                await message.reply_text("Not enough users")
                return
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await app.get_users(c1_id)).mention
            c2_mention = (await app.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**
{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await app.send_message(
                message.chat.id,
                text=couple_selection_message
            )
            couple = {
                "c1_id": c1_id,
                "c2_id": c2_id
            }
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected['c1_id'])
            c2_id = int(is_selected['c2_id'])
            c1_name = (await app.get_users(c1_id)).first_name
            c2_name = (await app.get_users(c2_id)).first_name
            couple_selection_message = f"""Couple of the day:
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await app.send_message(
                message.chat.id,
                text=couple_selection_message
            )
    except Exception as e:
        print(e)
        message.reply_text(e)



__help__ = """
 ❍ /couples - To Choose Couple Of The Day
 
 @MissAlissaBot🇱🇰

 """
__mod_name__ = "Couples👩‍❤️‍👨"
