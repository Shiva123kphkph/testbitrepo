class script(object):
    START_TXT = """<b>HOW ARE YOU {} DUDE 🤩,Nice To Meet You🙌</b>
\n<i>𝖨'𝗆 𝗃𝗎𝗌𝗍 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗋𝖾 - 𝖿𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝖾𝖽 𝖺𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍</i>
\n<b><i>You Can't Use Me To Your Group Because Iam A Privet Bot..⚡️</i></b>"""
    HELP_TXT = """<b>HEY {} DUDE 🙋‍♂️</b>
\n<b>○ Sorry bruh... I can't help You because I'm a private bot🥲
○ You Can Check My status  Using This Command /Stats
○ Notice 📙:-

\n<i>○YOU CAN'T USE ME..⚡️</i>
○Dont Spam Me...🤒

©️MᴀɪɴᴛᴀɪɴᴇD Bʏ <a href='https://t.me/OGGY123kph'>𝑺ʜɪᴠᴀ 🇮🇳/🇵🇹</a></b>"""
    ABOUT_TXT = """ <code> IAM JUST A  Auto-Filter-Bot </code>🚶‍♂️⚠️

○ 𝑴𝒚 𝒏𝒂𝒎𝒆 : 𝐄𝐋𝐎𝐍 𝐌𝐔𝐒𝐊 🧛‍♂️
○ <b>𝑪𝒓𝒆𝒂𝒕𝒐𝒓 : <a href='https://t.me/OGGY123kph'>𝑺ʜɪᴠᴀ 🕵️‍♂️</a>
○ 𝑪𝒓𝒆𝒅𝒊𝒕𝒔 : <code>Everyone in this journey</code>
○ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚 : <a href='https://docs.pyrogram.org/'>𝑷ʏʀᴏɢʀᴀᴍ 📜</a>
○ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : <code>𝑷ʏᴛʜᴏɴ 3</code>
○ 𝑫𝒂𝒕𝒂 𝒃𝒂𝒔𝒆 : <a href='https://www.mongodb.com/'>𝑴ᴏɴɢᴏ 𝑫ʙ</a>
○ 𝑩𝒐𝒕 𝒔𝒆𝒓𝒗𝒆𝒓 : <a href='https://dashboard.heroku.com/apps'>𝑯ᴇʀᴏᴋᴜ</a>
○ 𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆 : <a href='https://t.me/joinchat/aYbIjDgZqY9lYjQ9'>👉 𝑪ʟɪᴄᴋ 𝑯ᴇʀᴇ</a>
○ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔 : <code>v1.0.1 [ 𝑩ᴇᴛᴀ ]</code>
\n\n🔖 𝑸𝒖𝒐𝒕𝒆 : <code>ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും</code></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
<b>Extra 🐶 Show Commands</b>

<b>𝖭𝖮𝖳𝖤: 𝗍𝗁𝖾𝗌𝖾 𝖺𝗋𝖾 𝗍𝗁𝖾 𝖾𝗑𝗍𝗋𝖺 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 𝗈𝖿 Rexie</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
<b>Film And Information</b>
\n<code>🎬 Ge𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """📂 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
⚡ TOTAL USERS : <code>{}</code>
🔖 TOTAL CHATS : <code>{}</code>
📜 USED STORAGE: <code>{}</code> MB
🎭 FREE STORAGE: <code>{}</code> MB"""
    LOG_TEXT_G = """#NewGroup
⚡ Group = {}(<code>{}</code>)
😳 Total Members = <code>{}</code>
🕵️‍♂️ Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
