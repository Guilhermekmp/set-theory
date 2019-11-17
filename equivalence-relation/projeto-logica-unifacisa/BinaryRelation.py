#coding: utf-8


class BinaryRelation(object):
    """Template class for classes representing a Binary Relation."""

    def contains_ordered_pair(self, x, y):
        """
        This method returns a boolean value indicating if a given ordered pair belongs to the binary relation.
        Arguments:
        x - The first element of the ordered pair.
        y - The second element of the ordered pair.
        Return True if the ordered pair belongs to the binary relation, otherwise, return False.
        """
        pass

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        Arguments:
        S - The input set.
        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """
        pass
