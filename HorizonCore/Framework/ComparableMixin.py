class ComparableMixin(object):
    def _compare(self, other, method):
        try:
            return method(self._compareKey(), other._compareKey())
        except (AttributeError, TypeError):
            raise ValueError("Types cannot be compared. Values are of different types, or _compareKey not implemented")

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s, o: s != o)
