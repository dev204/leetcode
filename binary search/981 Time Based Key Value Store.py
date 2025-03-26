'''
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the
most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp).
If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

'''

# we can use a hashmap with lists to store where input key will be key and for value we store (value, timestamp) as a list
# when we get, we get the array corresponding to the key, now we need to search for timestamp which is <= input timestamp
# since it's in sorted order we can then implement a bs on this array to find the timestamp
# tc O(1) for set and O(log n) for set where n is total values associated with a key
# sc will be O(n * m) where m is total number of keys and n is same as above total values associated with a key

class TimeMap:

    def __init__(self):
        self.store = {} # key : [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])

        l,r=0,len(values)-1
        while l<=r:
            m = l + (r-l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                #search in the right portion
                l = m + 1
            else:
                #search left portion
                r = m - 1
        return res
