class Hashtable:

    def __init__(self, lst=None):
        if lst:
            self._hashtable = self.hashing(lst)

    @classmethod
    def hashing(cls, lst):
        """"
        Hash-function.
        
             group's number           count watched elements the group
           /                         /
        20000: [{22341: True, ...}, 0]
                   \
                    original value
        """
        # c = 20000
        # r = lambda x: x % c  # remainder
        # k = lambda x: int((x - r(x)) / c)  # coefficient
        # group = lambda x: k(x) * c
        hashtable = {cls.group(x): [] for x in lst}
        for x in lst:
            hashtable[cls.group(x)].append(x)
        return hashtable

    @property
    def hashtable(self):
        return self._hashtable

    @hashtable.setter
    def hashtable(self, lst):
        self._hashtable = self.hashing(lst)
        return self._hashtable

    def shrink_ht(self):
        """
        Shrink inner hashtable.
        """
        c = 20000
        keys = [*self.hashtable]
        for key in keys:
            obj = self.hashtable[key]
            if len(obj) == 1:
                if not key - c in self.hashtable and \
                        not key + c in self.hashtable:
                    self.hashtable.pop(key)

    @classmethod
    def group(cls, x):
        c = 10000
        r = lambda x: x % c  # remainder  # * x/abs(x)
        k = lambda x: int((x - r(x)) / c)  # coefficient
        groups = lambda x: k(x) * c if x >= 0 else (k(x) + 1) * c
        return groups(x)

if __name__ == "__main__":
    lst = [1, 20000, 12314241, -1, -10001, -15000]
    ht = Hashtable(lst)
    print(ht.hashtable)
