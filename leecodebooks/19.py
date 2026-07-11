‘’‘
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

小心dummy point 错误！！
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

‘’‘

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            print("err: We can not found anything in this list")
            return None  #  修改为 None
            # 1. 计算链表的总长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        p = head        # p 用来遍历原链表
        k = 0           # k 代表当前原链表节点的下标（从 0 开始）
        # 1. 创建一个哑节点，它的 next 指向真正的头节点 head
        # 这样即使你要删除第一个节点，也可以通过 dummy.next 顺利处理
        dummy = ListNode(1)
        current = dummy
        if (length == n):
            return None  #  修改为 None
        # 2. 遍历接下来的元素，把它们连成链表
        for k in range(1, length):
            # 这里我们需要创建一个新节点，并把它连在 current 的后面。
            if (k== (length-n)):
                if (length == (n+1)):
                    return dummy
                else:
                    # new_node = self.ListNode(head[k+2],k+2) 直接跳到后面两个，加上去，就可以返回了
                    p=p.next
                    continue
                        
            else:
                p=p.next
                new_node = ListNode(p.val)
                current.next =  new_node
                current=current.next
        return dummy



       
