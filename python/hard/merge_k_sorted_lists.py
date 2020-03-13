class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge_2_lists(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            temp = list1
            temp.next = self.merge_2_lists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.merge_2_lists(list1, list2.next)
        return temp

    def merge_k_lists(self, lists) -> ListNode:
        if len(lists) < 2:
            return lists[0]
        lists.append(self.merge_2_lists(lists[0], lists[1]))
        return self.merge_k_lists(lists[2:])


s = Solution()
a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)

a.next = c
c.next = e

b.next = d
d.next = f

node = s.merge_k_lists([a, b])
while node.next:
    print(node.val)
    node = node.next
