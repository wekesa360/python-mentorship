# Microsoft Codility Technical Assessment

# s = "ababa"
# def dist_substring(s):
#     count_set = set()
#     i = 0 #index
#     substring_count = 1
#     for j in range(len(s)):
#         if s[j] not in count_set:
#             count_set.add(s[j])
#             i += 1
#         else:
#             count_set = set()
#             count_set.add(s[i])
#             substring_count += 1
#             i += 1
#     print(substring_count)
        
        
# blocks = [1,1,6,7,8,3,1]
# def solution(blocks):
#     n = len(blocks)
#     position_apart = 0
#     for i in range(n):
#         j = i 
#         # move left while blocks are less than or equal to current block
#         while j > 0 and blocks[j-1] >= blocks[j]:
#             j -= 1
#         low = j
#         j = i
#         # move right while blocks are less than or equal to current block
#         while j < n-1 and blocks[j+1] >= blocks[j]:
#             j += 1
#         high = j
#         position_apart = max(position_apart, high - low )
#     return position_apart + 1

# print(solution(blocks))