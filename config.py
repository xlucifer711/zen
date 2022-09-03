## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BADBVW6spHGdVgy0wZ3yYPatrD9_WRnQ3E_4NgflE9ziB4zx_2KwOpBgZGNWMENv45LOgSl0cL8y3zvizqOm7Zhna7hJAg4QH81B8R1WZ_bZXvygVWDMFXGmIEqLXg0Y8EIrRqj-4a47UoAXKG6tGWQh7xWdbfWRnhCPuWpZYc1uX-9IOVcYhhI3uAUpQIGR80y9a24pxg5UktI4L42sRQ2ehTq61WnwtpmBrNq854F-v9QOhpILtBUtF92gfeSb5TNZyf23NHZ3SOA6XcVw_A-B8-quP3h7uwEdmhnzF_JiRIlFPr9RpaCjYz-RVvPkI6x4uhQc_GZ9Fg21pJxiNek0AAAAAUQT7O4A")
BOT_TOKEN = getenv("BOT_TOKEN", "5471797925:AAFtxBzhHC-GhRp8FGGGKgb6wIVYOCr3tkY")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "pokemon")
OWNER_USERNAME = getenv("OWNER_USERNAME", "wjj_u")
ALIVE_NAME = getenv("ALIVE_NAME", "zein")
BOT_USERNAME = getenv("BOT_USERNAME", "z_09bot")
OWNER_ID = getenv("OWNER_ID", "1355571767")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AQOOX2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "q_k_2")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1355571767").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/95859dbf2c9cb0db433df.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/7e7e8007c9cee7ed710be.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
