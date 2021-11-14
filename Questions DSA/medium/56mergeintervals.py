# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution:
    #Approach1:
    #Time Complexity:O(nlogn)
    #Space Complexity:O(N)
    def merge(self,intervals):
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x:x[0])
        mergeinterval= []
        for interval in intervals:
            if not mergeinterval  or mergeinterval[-1][1]<interval[0]:
                mergeinterval.append(interval)
            else:
                mergeinterval[-1][1] = max(mergeinterval[-1][1],interval[1])
        return mergeinterval
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
