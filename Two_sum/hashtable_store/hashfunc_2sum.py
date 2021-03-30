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
        c = 20000
        r = lambda x: x % c  # remainder
        k = lambda x: int((x - r(x)) / c)  # coefficient
        group = lambda x: k(x) * c
        hashtable = {group(x): [{x: True}, 0] for x in lst}
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
            obj = [self.hashtable[key][0]]
            if len(obj) == 1:
                if not key - c in self.hashtable and \
                        not key + c in self.hashtable:
                    self.hashtable.pop(key)

if __name__ == "__main__":
    lst = [1, 20000, 12314241]
    ht = Hashtable(lst)
    ht.shrink_ht()
    print(ht.hashtable)
