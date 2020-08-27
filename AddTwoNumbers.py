# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        result_arr = []
        carry_over = False

        while True:
            
            digit1 = l1.val
            digit2 = l2.val

            # print(digit1, ' is digit1')
            # print(digit2, ' is digit2')
            
            result_array_item = digit1 + digit2
            
            if carry_over:
                result_array_item += 1
            
            # if more than one digit, carry over
            if result_array_item > 9:
                result_array_item = result_array_item % 10
                carry_over = True
            
            result_arr.append(result_array_item)        

            if l1.next is not None:
                l1 = l1.next
                l2 = l2.next
                
            else:
                break
        
        print(result_arr, ' is result_arr')
        
        
        result = ListNode()
        current = result
            
        while len(result_arr) > 0:
            current.val = result_arr[0]
            result_arr.pop(0)

            if len(result_arr) == 0:
                continue

            else:
                current.next = ListNode()
                current = current.next

        return result