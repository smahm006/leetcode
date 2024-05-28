class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        newnums = set()
        for num in nums:
            if num in newnums:
                return True
            newnums.add(num)
        return False
    
if __name__=="__main__": 
    sol = Solution()
    test = [925,467,318,353,-250,-707,-481,809,-718,982,-42,-550,530,951,-807,-184,813,-2,-666,368,705,-541,-669,447,-116,56,-172,-305,-137,-599,-269,-347,-811,479,-250,-960,-307,135,-60,-97,441,-962,-212,-321,60,278,-394,50,968,-868,-768,882,615,-531,991,795]
    print(sol.containsDuplicate(test))
