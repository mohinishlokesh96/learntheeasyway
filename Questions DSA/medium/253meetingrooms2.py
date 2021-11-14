# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.
class Solution:
    #Approach1:
    #Time Complexity:O(nlogn)
    #Space Complexity:O(1)
    def meetingroom(self,intervals):
        startingtime = [i[0] for i in intervals]
        endingtime = [i[1] for i in intervals]
        st = 0
        et = 0
        count = 0
        startingtime.sort()
        endingtime.sort()
        while st < len(intervals):
            if startingtime[st]>endingtime[et]:
                count-=1
                et+=1
            count+=1
            st+=1
        return count
sol = Solution()
print(sol.meetingroom([[0,30],[5,10],[15,20]]))
print(sol.meetingroom([[7,10],[2,4]]))