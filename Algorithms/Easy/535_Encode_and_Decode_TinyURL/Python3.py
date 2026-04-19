import random
import string

class Codec:

    def __init__(self):
        self.hash_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        prefix = "http://tinyurl.com/"
        while True:
            hash = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            if hash not in self.hash_map:
                self.hash_map[prefix+hash] = longUrl
                return prefix + hash
        


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
