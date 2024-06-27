# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int1 = None
        int2 = None
        max_len = 0

        len1 = len(l1)
        len2 = len(l2)
        l1_reversed = l1.reverse()
        l2_reversed = l2.reverse()
        if len1 > len2:
            max_len = len1
            l2.extend([0] * (len1 - len2))
        elif len2 > len1:
            max_len = len2
            l1.extend([0] * (len2 - len1))

        for elem1, elem2 in zip(l1, l2):
            if int1 != None and int2 != None:
                int1 = int1 * 10 + elem1
                int2 = int2 * 10 + elem2
            else:
                int1, int2 = (elem1, elem2)

        result = int1 - int2
        relist = []

        for i in range(max_len):
            result, unit = (result // 10, result % 10)
            relist.append(unit)
            

        return relist.reverse()



#342
#+
#465
#---
#807
#
#  9,9,9,9,9,9,9
#+
#  0,0,0,9,9,9,9
#1 0 0 0 9 9 9 8
