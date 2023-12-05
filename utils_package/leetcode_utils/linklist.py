class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(nums):
    if not nums:
        return None

    prev = ListNode(nums[0])
    prev_head = prev

    for num in nums[1:]:
        temp = ListNode(num)
        prev.next = temp
        prev = temp

    return prev_head

def show_list(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

