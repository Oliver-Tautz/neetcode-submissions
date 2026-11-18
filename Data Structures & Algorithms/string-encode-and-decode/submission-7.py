import json

class Solution:


    def encode(self, strs: List[str]) -> str:
        print(strs)
        return json.dumps(strs)
    def decode(self, s: str) -> List[str]:
        return json.loads(s)