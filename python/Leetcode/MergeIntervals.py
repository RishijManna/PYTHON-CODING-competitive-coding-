#https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merge=[]
        for i in intervals:
           
            if not merge or merge[-1][1]<i[0]:
                merge.append(i)
            elif merge[-1][1]>= i[0]:
                merge[-1][1]=max(merge[-1][1],i[1])
        return merge
