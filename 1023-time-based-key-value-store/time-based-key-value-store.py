class TimeMap:

    def __init__(self):
        self.key_timstamps = dict()
        self.key_hash = dict()

    def find(self, key:int ,timestamp:int):
        if key not in self.key_timstamps:
            return -1
        return bisect.bisect_right(self.key_timstamps[key], timestamp) - 1

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_timstamps:
            self.key_timstamps[key] = []
            self.key_hash[key] = dict()

        index = self.find(key, timestamp)
        if index == -1 or self.key_timstamps[key][index] != timestamp:
            self.key_timstamps[key].insert(index + 1, timestamp)

        self.key_hash[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_timstamps:
            return ""

        index = self.find(key, timestamp)
        if index == -1:
            return ""

        return self.key_hash[key][self.key_timstamps[key][index]]