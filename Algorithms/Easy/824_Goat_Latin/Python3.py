class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        for i, word in enumerate(sentence.split(" ")):
            temp = []

            if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                temp.append(word)
            else:
                temp.append(word[1 : ] + word[0])
            
            temp.append("ma")
            temp.append("a" * (i+1))
            result.append("".join(temp))
        
        return " ".join(result)
