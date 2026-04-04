class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            length = len(s)
            encode_str += str(length) + "#" + s
        
        return encode_str

    def decode(self, s: str) -> List[str]:
        message = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            message.append(s[j + 1:j + 1 + length])

            i = j + 1 + length
        
        return message
            