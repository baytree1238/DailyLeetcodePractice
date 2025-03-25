class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        good_students_count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                good_students_count +=1
        return good_students_count
'''
https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
'''
