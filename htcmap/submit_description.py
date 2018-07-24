import collections


class SubmitDescription(collections.ChainMap):
    def __getitem__(self, key):
        s = super().__getitem__(key)

        for mapping in self.maps[1:]:
            s = s.replace('#', mapping.get(key, ''))

        return s
