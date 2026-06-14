class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        
        # 创建一个hash table，存储已经遍历过的数字(num)以及它对应的下标(index)
        hash_map = {}

        # 使用枚举拿到下标和数字
        for i, num in enumerate(nums):
            
            # 这个算法把a + b = target 转换成了目标数字减去当前数字等于我们需要的数字need
            need = target - num

            # 检查 need 这个数字是否已经存在在hash table中，如果存在直接return两数下标
            # 第一次遍历时hash table为空，因此 if 判断不会成立，会把当前数字(num)作为 key，当前下标(i)作为 value 存入 hash_map。
            if need in hash_map:
                # 第二次遍历的时候，在存入之前先进行匹配。

                # 计算need
                # ↓
                # 判断need是否存在
                # ↓
                # 存在就return
                # ↓
                # 不存在才存入当前num

                #==================

                # 返回两个数字对应的下标：
                # hash_map[need] 是之前保存的下标(value)，
                # i 是当前数字的下标。
                return [hash_map[need], i]
            
            # 如果if判断失效则存入key和value进入hash table作为下次判断need是否存在的依据
            hash_map[num] = i