import matplotlib.pyplot as plt
from typing import Protocol # for type hints
#from matplotlib.artist import Artist

class HashFertile(Protocol):
    """Define a type to be used for annotating figtree() with type hints.

    The type only needs to implement the get_children() and __hash__() methods.
    Objects of this type must be hashable since they may be used as a dict key.
    get_chindren(): There is a LBYL-style check on it, so the function will not blow up
    if the method is not implemented."""

    def __hash__(self) -> int: ...
    def get_children(self) -> list: ...

def figtree(obj : HashFertile) -> dict | HashFertile:  # or use the Artist type here
    """Return all children of the obj object, then their children, etc
    recursively, as a dict. Useful for quick checking what a Figure
    or an Axes comprises."""

    if hasattr(obj, 'get_children') and callable(get_children := obj.get_children):
        branch = dict()
        if len(children := get_children()) < 1:
            return obj
        re_children = list()
        for child in children:
            re_children.append(figtree(child))
        branch[obj] = re_children
        return branch
    else:
        return obj

# A usage example
'''
fig, _ = plt.subplots()
tree = figtree(fig)

from pprint import pp
pp(tree[fig], depth=5)
'''
