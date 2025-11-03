from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        li: list = self.store[key]
        left: int = 0
        right: int = len(li) - 1
        result: str = ""
        while left <= right:
            mid: int = left + (right - left) // 2
            if li[mid][0] <= timestamp:
                result: str = li[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result


a = TimeMap()
a.set("foo", "bar", 1)
print(a.get("foo", 1))
print(a.get("foo", 3))
a.set("foo", "bar2", 4)
print(a.get("foo", 4))
print(a.get("foo", 5))
