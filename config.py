import os
import sys


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("BOT_TOKEN is not set in environment variables")
    sys.exit(1)


config = AttrDict({
    "bot": AttrDict({
        "token": BOT_TOKEN
    })
})
