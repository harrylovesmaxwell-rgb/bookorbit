'''

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

'''

class Solution:
    class ListNode:
        def __init__(self, val, index,originalindex):
            self.val = val          # 数值
            self.index= index
            self.originalindex=originalindex
            self.next = None        #下一个指针指向哪里
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            print("err: We can not found numbers in this list")
            return []
            
        # 1. 创建头节点（此时它的当前下标和原始下标都是 0）
        head = self.ListNode(nums[0], 0,0)
        current = head
        
        # 2. 遍历接下来的元素，把它们连成链表
        for k in range(1, len(nums)):
            # 这里我们需要创建一个新节点，并把它连在 current 的后面。
            # 应该如何写这两行代码？
            new_node = self.ListNode(nums[k],k,k)
            current.next =  new_node
            
            # 别忘了让 current 指针也向后移动一步
            current = current.next
            # 外层指针 i 从头节点开始

        # 2. 把链表节点放入一个 Python 列表中，方便排序
        nodes_list = []
        curr = head
        while curr is not None:
            nodes_list.append(curr)
            curr = curr.next
            
        
        # --- 接下来：初始化前后对撞双指针 ---
        left = 0 ## INIT 初始最左边
        right = len(nodes_list) - 1 ## INIT 初始最右边
        # 建立一個 List，裡面包含多個 Tuple（數列對）
        ans_number_pairs = []
        while left < right:
            current_sum = nodes_list[left].val + nodes_list[right].val
            # 🤔 思考时间：
            # 如果 current_sum == target，说明找到了！我们应该返回哪两个属性？
            # 如果 current_sum < target，说明数字太小了，左指针 left 应该怎么移动？
            # 如果 current_sum > target，说明数字太大了，右指针 right 应该怎么移动？
            if (current_sum == target):
                ans_number_pairs.append((nodes_list[left].originalindex+1,nodes_list[right].originalindex+1))
                return ans_number_pairs[0]
            else:
                if (current_sum < target):
                    left=left+1
                    continue
                else:
                    if(current_sum > target):
                        right =right-1
# 3️⃣ 步骤三：排序我们使用了 Python 自带的 sort() 排序。计算机科学中，最优的通用排序算法（如 Timsort、归并排序）的时间复杂度公式为：$$T_3(N) = c_3 \times N \log_2 N$$💡 这部分是整体开销最大的地方，复杂度为 $O(N \log N)$。这是最关键的地方！在 while left < right: 循环中：初始时，左右指针的距离是 $N - 1$。每次执行循环体，要么 left += 1，要么 right -= 1。也就是说，每一步两个指针之间的距离都会雷打不动地减少 1。当它们相遇时（距离变为 0），循环绝对终止。因此 food 循环体最多只会执行 $N - 1$ 次，而且里面没有任何嵌套循环：

#conclusion
# 在大 $\mathcal{O}$ 阶算法复杂度分析中，当 $N$ 变得非常大时，低阶项（如 $N$）的影响力远小于高阶项。因此我们只保留增长最快的那一项：$$O(N) + O(N) + O(N \log N) + O(N) = O(N \log N)$$
                
