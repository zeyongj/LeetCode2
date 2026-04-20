class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        li=[]
        for i in num:
            if i!=0:
                li.append(i)
        li.sort()
        st1=""
        st2=""
        if len(li)==4:
            st1=st1+li[0]+li[2]
            st2=st2+li[1]+li[3]
            return int(st1)+int(st2)        