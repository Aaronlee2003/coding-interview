class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(map(str, digits))
        number=int(result)+1
        results= list(map(int, str(number)))
        return results

        