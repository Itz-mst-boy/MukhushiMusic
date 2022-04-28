# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


from pyrogram.types import (CallbackQuery, InlineKeyboardButton,

                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Alexa import db_mem

def url_markup(videoid, duration, user_id, query, query_type):

    buttons = [

        [

            InlineKeyboardButton(

                text="❮",

                callback_data=f"slider B|{query_type}|{query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎵",

                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎥",

                callback_data=f"Choose {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="❯",

                callback_data=f"slider F|{query_type}|{query}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="🔎 ᴍᴏʀᴇ ʀᴇsᴜʟᴛs",

                callback_data=f"Search {query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🗑 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ",

                callback_data=f"forceclose {query}|{user_id}",

            ),

        ],

    ]

    return buttons

def url_markup2(videoid, duration, user_id):

    buttons = [

        [

            InlineKeyboardButton(

                text="🎵 ᴘʟᴀʏ ᴍᴜsɪᴄ",

                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",

            ),

            InlineKeyboardButton(

                text="🎥 ᴘʟᴀʏ ᴠɪᴅᴇᴏ",

                callback_data=f"Choose {videoid}|{duration}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="🗑 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ",

                callback_data=f"forceclose {videoid}|{user_id}",

            )

        ],

    ]

    return buttons

def search_markup(

    ID1,

    ID2,

    ID3,

    ID4,

    ID5,

    duration1,

    duration2,

    duration3,

    duration4,

    duration5,

    user_id,

    query,

):

    buttons = [

        [

            InlineKeyboardButton(

                text="1️⃣", callback_data=f"Yukki {ID1}|{duration1}|{user_id}"

            ),

            InlineKeyboardButton(

                text="2️⃣", callback_data=f"Yukki {ID2}|{duration2}|{user_id}"

            ),

            InlineKeyboardButton(

                text="3️⃣", callback_data=f"Yukki {ID3}|{duration3}|{user_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="4️⃣", callback_data=f"Yukki {ID4}|{duration4}|{user_id}"

            ),

            InlineKeyboardButton(

                text="5️⃣", callback_data=f"Yukki {ID5}|{duration5}|{user_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="<", callback_data=f"popat 1|{query}|{user_id}"

            ),

            InlineKeyboardButton(

                text="🗑 ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"

            ),

            InlineKeyboardButton(

                text=">", callback_data=f"popat 1|{query}|{user_id}"

            ),

        ],

    ]

    return buttons

def search_markup2(

    ID6,

    ID7,

    ID8,

    ID9,

    ID10,

    duration6,

    duration7,

    duration8,

    duration9,

    duration10,

    user_id,

    query,

):

    buttons = [

        [

            InlineKeyboardButton(

                text="6️⃣",

                callback_data=f"Yukki {ID6}|{duration6}|{user_id}",

            ),

            InlineKeyboardButton(

                text="7️⃣",

                callback_data=f"Yukki {ID7}|{duration7}|{user_id}",

            ),

            InlineKeyboardButton(

                text="8️⃣",

                callback_data=f"Yukki {ID8}|{duration8}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="9️⃣",

                callback_data=f"Yukki {ID9}|{duration9}|{user_id}",

            ),

            InlineKeyboardButton(

                text="𝟷𝟶🔟",

                callback_data=f"Yukki {ID10}|{duration10}|{user_id}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="<", callback_data=f"popat 2|{query}|{user_id}"

            ),

            InlineKeyboardButton(

                text="🗑 ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"

            ),

            InlineKeyboardButton(

                text=">", callback_data=f"popat 2|{query}|{user_id}"

            ),

        ],

    ]

    return buttons

def secondary_markup(videoid, user_id):

    buttons = [

        [

            InlineKeyboardButton(text="💥 ᴄʜᴀɴɴᴇʟ 💞", url=f"https://t.me/mukhushi_official"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 ᴍᴏʀᴇ ᴍᴇɴᴜ", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text=" ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/lets_playmusic_bot?startgroup=true"),

        ],

    ]

    return buttons

def secondary_markup2(videoid, user_id):

    buttons = [

        [

            InlineKeyboardButton(text="💥 ᴡᴏʀʟᴅᴡɪᴅᴇ ғʀɪᴇɴᴅ ᴢᴏɴᴇ 💞⁩", url=f"https://t.me/worldwide_friend_zone"),

        ],

        [

            InlineKeyboardButton(text="❤️ sᴜᴘᴘᴏʀᴛ ❤️", url=f"https://t.me/mukhushi_official"),

        ],

    ]

    return buttons

def primary_markup(videoid, user_id, current_time, total_time):

    if videoid not in db_mem:

        db_mem[videoid] = {}

    db_mem[videoid]["check"] = 2

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥 ᴡᴏʀʟᴅᴡɪᴅᴇ ғʀɪᴇɴᴅ ᴢᴏɴᴇ 💞", url=f"https://t.me/worldwide_friend_zone"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 ᴍᴏʀᴇ ᴍᴇɴᴜ", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text="ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/lets_playmusic_bot?startgroup=true"),

        ],

    ]

    return buttons

def timer_markup(videoid, user_id, current_time, total_time):

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥ᴡᴏʀʟᴅᴡɪᴅᴇ ғʀɪᴇɴᴅ ᴢᴏɴᴇ 💞", url=f"https://t.me/worldwide_friend_zone"),

        ],

        [

            InlineKeyboardButton(

                text="🔗 ᴍᴏʀᴇ ᴍᴇɴᴜ", callback_data=f"other {videoid}|{user_id}"

            ),

            InlineKeyboardButton(text="ᴀᴅᴅ  ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/lets_playmusic_bot?startgroup=true"),

        ],

    ]

    return buttons

def audio_markup(videoid, user_id, current_time, total_time):

    if videoid not in db_mem:

        db_mem[videoid] = {}

    db_mem[videoid]["check"] = 2

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥 sᴜᴘᴘᴏʀᴛ 💞", url=f"https:/t.me/mukhushi_official"),

        ],

        [InlineKeyboardButton(text="ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/lets_playmusic_bot?startgroup=true")],

    ]

    return buttons

def audio_timer_markup_start(videoid, user_id, current_time, total_time):

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{total_time} ------------------ {current_time}",

                callback_data=f"timer_checkup_markup {videoid}|{user_id}",

            )

        ],

        [

            InlineKeyboardButton(text="💥 ᴡᴏʀʟᴅᴡɪᴅᴇ ғʀɪᴇɴᴅ ᴢᴏɴᴇ💞⁩", url=f"https://t.me/worldwide_friend_zone"),

        ],

        [InlineKeyboardButton(text="ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/lets_playmusic_bot?startgroup=true")],

    ]

    return buttons

audio_markup2 = InlineKeyboardMarkup(

    [

        [

            InlineKeyboardButton(text="💥 ᴡᴏʀʟᴅᴡɪᴅᴇ ғʀɪᴇɴᴅ ᴢᴏɴᴇ 💞", url=f"https://t.me/worldwide_friend_zone"),

        ],

        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/lets_playmusic_bot?startgroup=true")],

    ]

)
