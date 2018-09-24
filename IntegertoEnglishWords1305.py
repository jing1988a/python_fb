class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        t1= ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        t2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        t3=["Thousand", "Million", "Billion"]
        layer=-1
        ans=[]
        if num==0:
            return "Zero"
        while num>0:
            cur=num%1000
            temp=[]
            if cur>100:
                idx=cur//100
                cur%=100
                temp.append(t1[idx])
                temp.append("Hundred")
            if cur>19:
                idx=cur//10
                cur%=10
                temp.append(t2[idx])
            if cur!=0:
                temp.append(t1[cur])
            if temp:
                if layer!=-1:
                    temp.append(t3[layer])
                ans.append(' '.join(temp))
            layer+=1
            num//=1000
        return ' '.join(reversed(ans))