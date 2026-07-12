from typing import List
class Solution:
    
    class ListNode:
        def __init__(self,val,index):
            print("enter the Init in the class Listndoe")
            self.val = val
            self.index = index
            self.next = None
        def _build_and_sort_list(self, nums: List[int]):
            if not nums:
                return None,[]
            head=self.__class__(nums[0],0)
            current=head
            for k in range(1,len(nums)):
                new_code= self.__class__(nums[k],k)
                current.next = new_code
                current = current.next
            nodeslist = []
            curr = head
            while curr is not None:
                nodeslist.append(curr)
                curr = current.next
            print("enter the nodelist sort function")
            nodeslist.sort(key=lambda node:node.val)
            return head, nodeslist
            # ========== 新增中转方法 ==========
        '''
        Solution (外层类)
  └── ListNode (内部类)
       └── _build_and_sort_list (属于 ListNode 实例的方法)
        '''
    def print3values(self,left,middle,right):
        print("left:",left)
        print("middle:",middle)
        print("right:",right)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            print("err: We can not found numbers in this list")
            return []
        # 1. 创建头节点（此时它的当前下标和原始下标都是 0）
        head = self.ListNode(nums[0],0)
        current = head
        # 2. 遍历接下来的元素，把它们连成链表
        for k in range(1, len(nums)):
            # 这里我们需要创建一个新节点，并把它连在 current 的后面。
            # 应该如何写这两行代码？
            new_node = self.ListNode(nums[k],k)
            current.next =  new_node
            # 别忘了让 current 指针也向后移动一步
            current = current.next

        # 2. 把链表节点放入一个 Python 列表中，方便排序
        nodes_list = []
        curr = head
        while curr is not None:
            nodes_list.append(curr)
            curr = curr.next        
        ans_number_pairs= []
        left = 0 ## INIT 初始最左边
        middle= left+1 ## INIT 初始最左边 的右边一格子
        right = len(nodes_list)-1  ## INIT 初始最右边
        target = 0
        self.print3values(left,middle,right)
        while left < middle < right:
            ThreeSum = nodes_list[left].val + nodes_list[middle].val+nodes_list[right].val
            sum_last2values = nodes_list[middle].val + nodes_list[right].val
            if (ThreeSum == target):
                ans_number_pairs.append((nodes_list[left].val + nodes_list[middle].val+ nodes_list[right].val))
                left=left+1
                middle=left+1## INIT 初始最左边 的右边一格子
                right = len(nodes_list)-1  ## INIT 初始最右边
                self.print3values(left,middle,right)
                continue
            else:
                    if (ThreeSum < target):
                        if(sum_last2values > (target-nodes_list[left].val)):
                            middle=middle+1
                            self.print3values(left,middle,right)
                            continue
                        if(sum_last2values < (target-nodes_list[left].val)):
                            right=right-1
                            self.print3values(left,middle,right)
                        else:
                            print("error logic in this algorith")
        return ans_number_pairs

