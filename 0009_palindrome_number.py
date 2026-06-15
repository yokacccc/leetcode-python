class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 先检查x是否为负数，如果x为负数，palindrome必定为false，因为-121的回文是121-
        if x < 0:
            return False

        # 设置原始数和翻转数，用来最后进行比较返回bool
        original = x
        reverse = 0

        # 使用while循环遍历提取翻转数
        while x > 0:
            # digit为提取的个位数
            # 取模 10 会得到 x 除以 10 后的余数，也就是个位数
            digit = x % 10
            # 这一步是把提取出来的个位数拼接到 reverse 的末尾
            # 当第一次提取时，reverse为0所以0 * 10 等于0，只把个位赋值给reverse
            # 当第二次提取时，reverse为提取的个位数，reverse * 10 把数字移到十位，并加上提取的第二个数，以此往复
            reverse = reverse * 10 + digit
            # 设置while循环结束条件，每次把x / 10并向下取整直到x = 0结束循环。
            x //= 10
        
        # 当while循环结束时已经提取完reverse数字，比较原始数字并且输出bool
        return original == reverse