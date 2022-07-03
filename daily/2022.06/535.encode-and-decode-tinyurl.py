"""
日期: 2022-06-29
题目: TinyURL 的加密与解密
链接: https://leetcode-cn.com/problems/encode-and-decode-tinyurl/
"""

from dataclasses import dataclass
from typing import *
from collections import *
class Codec:
    database = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = str(hash(longUrl))
        self.database[short] = longUrl
        return "http://tinyurl.com/" + str(short)

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        short = shortUrl.split("/")[-1]
        return self.database[short]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))