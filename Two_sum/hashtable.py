class Hashtable:

    def __init__(self, lst=None):
        if lst:
            self._hashtable = self.hashing(lst)

    @classmethod
    def hashing(cls, lst):
        """"
             group's number           count watched elements the group
           /                         /
        20000: [{22341: True, ...}, 0]
                   \
                    original value
        """
        hashtable = {cls.group(x): [] for x in lst}
        for x in lst:
            hashtable[cls.group(x)].append(x)
        return hashtable

    @property
    def hashtable(self):
        return self._hashtable

    @classmethod
    def group(cls, x, c=10000):
        """
        Hash-function.
        """
        r = lambda x: x % c  # remainder
        k = lambda x: int((x - r(x)) / c)  # coefficient
        groups = lambda x: k(x) * c if x >= 0 else (k(x) + 1) * c
        return groups(x)

if __name__ == "__main__":
    lst = [1, 20000, 12314241, -1, -10001, -15000]
    ht = Hashtable(lst)
    print(ht.hashtable)
