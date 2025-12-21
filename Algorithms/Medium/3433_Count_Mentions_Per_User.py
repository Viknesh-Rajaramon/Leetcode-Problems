from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        result, last_online, all_num = [0] * numberOfUsers, [0] * numberOfUsers, 0

        events.sort(key = lambda x: (int(x[1]), x[0] == "MESSAGE"))
        for event_type, timestamp, data in events:
            if event_type == "MESSAGE":
                if data == "ALL":
                    all_num += 1
                elif data == "HERE":
                    timestamp = int(timestamp)
                    for i in range(numberOfUsers):
                        if last_online[i] <= timestamp:
                            result[i] += 1
                else:
                    for user_id in data.split():
                        result[int(user_id[2 : ])] += 1
            elif event_type == "OFFLINE":
                last_online[int(data)] = int(timestamp) + 60

        for i in range(numberOfUsers):
            result[i] += all_num

        return result
