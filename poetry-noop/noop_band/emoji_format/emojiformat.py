"""
(maybe) format a noop emoji
"""

import emoji

class EmojiFormat:
    def __init__(self, emoji_name):
        self._emojiname = emoji_name

    def themoji(self):
        return emoji.emojize(self._emojiname)
