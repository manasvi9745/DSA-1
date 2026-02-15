class Solution(object):
    def nextLargerNodes(self, head):
        if not head or not head.next:
            return [0]
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        n=len(l)
        res=[0]*n
        s=[]
        for i in range(n):
            while s and l[i]>l[s[-1]]:
                x=s.pop()
                res[x]=l[i]
            s.append(i)
        return res