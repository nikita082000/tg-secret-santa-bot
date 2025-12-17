import os
import sys


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("BOT_TOKEN is not set in environment variables")
    sys.exit(1)


config = AttrDict({
    "telegram": AttrDict({
        "token": BOT_TOKEN,
        "log_chat": False,   # логувати chat_id (не обовʼязково)
    }),

    "santa": AttrDict({
        "min_participants": 2,
        "max_participants": 100,
        "allow_self_gifting": False,
    }),

    "ui": AttrDict({
        "language": "en",
    }),
})
