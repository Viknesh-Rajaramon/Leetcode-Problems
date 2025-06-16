class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.lstrip()
        is_upper = False
        
        result = ["#"]
        for i, c in enumerate(caption):
            if c == " ":
                is_upper = True
                continue
            
            if is_upper:
                result.append(c.upper())
                is_upper = False
            else:
                result.append(c.lower())

            if len(result) == 100:
                break

        return "".join(result)
