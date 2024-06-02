# https://leetcode.com/problems/count-days-without-meetings/description/
# 3169. Count Days Without Meetings
 
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort the meetings by their start times
        meetings.sort(key=lambda x: x[0])

        # Merge overlapping meetings
        merged = [meetings[0]]
        for current_meeting in meetings[1:]:
            last_meeting_end = merged[-1][1]
            if current_meeting[0] <= last_meeting_end:
                merged[-1][1] = max(last_meeting_end, current_meeting[1])
            else:
                merged.append(current_meeting)

        # Calculate the total number of days with meetings
        total_days_with_meetings = sum(end - start + 1 for start, end in merged)

        # Return the total number of days without meetings
        return days - total_days_with_meetings