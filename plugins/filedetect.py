from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

@Client.on_message(filters.private & filters.reply)
async def refunc(client,message):
        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        	new_name = message.text
        	await message.delete()
        	media = await client.get_messages(message.chat.id,message.reply_to_message.message_id)
        	file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        	filename = file.file_name
        	types = file.mime_type.split("/")
        	mime = types[0]
        	mg_id = media.reply_to_message.message_id
        	try:
        		out = new_name.split(".")
        		out_name = out[1]
        		out_filename = out[0] + "."+ out_name
        		await message.reply_to_message.delete()
        		if mime == "video":
        			markup = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Document",callback_data = "doc"), 
        			InlineKeyboardButton("Video",callback_data = "vid") ]])
        		elif mime == "audio":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Document",callback_data = "doc")
        			,InlineKeyboardButton("Audio",callback_data = "aud") ]])
        		else:
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Document",callback_data = "doc") ]])
        		# dont chenge this message.reply_text     			        		
        		await message.reply_text(f"**Select OutPut Media Type :**\n**New FileName** :- ```{out_filename}```",reply_to_message_id=mg_id,reply_markup = markup)
        		
        	except:
        		try:
        			out = filename.split(".")
        			out_name = out[1]
        			out_filename= new_name + "."+ out_name
        		except:
        			await message.reply_to_message.delete()
        			await message.reply_text("**Error** :  No  Extension In File, Add OutPut Extension. Example : .mkv,.mp4, .m4a"
        			,reply_to_message_id=mg_id)
        			return
        		await message.reply_to_message.delete()
        		if mime == "video":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Document",callback_data = "doc")
        			,InlineKeyboardButton("Video",callback_data = "vid") ]])
        		elif mime == "audio":
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Document",callback_data = "doc")
        			,InlineKeyboardButton("Audio",callback_data = "aud") ]])
        		else:
        			markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Document",callback_data = "doc") ]])
        		# dont chenge this message.reply_text 
        		await message.reply_text(f"**Select OutPut Media Type :**\n**New FileName** :- ```{out_filename}```",
        		reply_to_message_id=mg_id,reply_markup = markup)
        		
