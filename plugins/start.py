from pyrogram import client, filters, StopPropagation


@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
