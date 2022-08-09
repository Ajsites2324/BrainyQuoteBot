from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝗛𝗲𝗺𝗹𝗼 𝗕𝗮𝗯𝘆 {}

𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 {} 𝗼𝘂𝗿 𝗳𝗮𝗻𝘁𝗮𝘀𝘁𝗶𝗰 𝗕𝗿𝗮𝗶𝗻𝗹𝘆 𝗾𝘂𝗼𝘁𝗲 𝗯𝗼𝘁.

𝗬𝗼𝘂 𝗰𝗮𝗻 𝘀𝗲 𝗺𝗲 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵 𝗾𝘂𝗼𝘁𝗲𝘀 𝗼𝗻 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝘁𝗼𝗽𝗶𝗰𝘀 𝗮𝗻𝗱 𝗴𝗿𝗲𝗮𝘁 𝗽𝗲𝗼𝗽𝗹𝗲 𝗮𝗻𝘆 𝘁𝗶𝗺𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁. 𝗧𝗼 𝘂𝘀𝗲 𝗵𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝗺𝗲 𝗽𝗿𝗲𝘀𝘀 𝗼𝗻 '𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘' 𝗯𝗲𝗹𝗼𝘄.

┏❖ 𝗕𝗼𝘁 𝗰𝗿𝗲𝗮𝘁𝗲𝗱 𝗯𝘆  
┗ ☞ @PAPA_BOL_SAKTEHO

┏❖ 𝗙𝗲𝗲𝗹𝗶𝗻𝗴𝘀  
┗ ☞ @ABOUT_AJEET
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Search a Quote ✨", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Search a Quote ✨", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/AJEET_BOTS")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MODERN_ELEMENTS")],
    ]

    # Help Message
    HELP = """
**✨ Inline Mode ✨**
 
**1) Search Quotes**
Just pass the topic/name on which you wanna search quotes.
Example : `@BrainQuoteroBot Albert Einstein`

**2) Quote of the Day**
To get 'Quote of the Day' pass `#q` or `#qod`. You will get that for 5 different topics.
Example : `@BrainQuoteroBot #qod`

**3) Random Quote**
To get a single random quote pass `#r` or `#random`.
Example : `@BrainQuoteroBot #random`

**4) A Single Quote**
By default, when you will use 1st option, you will get 20-30 quotes. But if you want only 1 random quote of that topic, use `#1` in end.
Example : `@BrainQuoteroBot Sushant Singh Rajput #1`

More features in development. Keep track by joining @AJEET_BOTS .
    """

    # About Message
    ABOUT = """
**𝗔𝗕𝗢𝗨𝗧 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧** 

𝗔 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗤𝘂𝗼𝘁𝗲 𝗯𝗼𝘁 𝗯𝘆 @ABOUT_AJEET

𝗠𝗼𝗿𝗲 𝗯𝗼𝘁𝘀 : [𝗖𝗹𝗶𝗰𝗸 𝗵𝗲𝗿𝗲](https://t.me/ajeet_bots)

𝗦𝗼𝘂𝗿𝗰𝗲 𝗰𝗼𝗱𝗲 : [𝗖𝗹𝗶𝗰𝗸 𝗵𝗲𝗿𝗲](https://t.me/papa_bol_sakteho)

𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺](docs.pyrogram.org)

𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [𝗣𝘆𝘁𝗵𝗼𝗻](www.python.org)

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : [𓆩〭⃛〬𓆩〭⃛〬➤⃝✖‿✖•Ajͥeeͣtͫ](https://t.me/papa_bol_sakteho)
    """
