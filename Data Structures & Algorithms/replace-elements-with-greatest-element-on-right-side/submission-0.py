class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        left = 0
        #right = left +1
        res = []
        #greatest = 0
        while left < len(arr):
            greatest = 0
            if left != len(arr)-1:
                right = left + 1
                for index in range(right,len(arr)):
                    greatest = max(greatest, arr[index])
                res.append(greatest)
                left +=1
                greatest = 0
            else:
                res.append(-1)
                break
        return res
        


        