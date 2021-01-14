# https://docs.python.org/3/whatsnew/3.9.html
# https://realpython.com/python39-new-features/

# New Features

# Dictionary Merge & Update Operators (PEP 584)
print("Dictionary Merge & Update Operators (PEP 584)")
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
print(f"d1 | d2 = {d1 | d2}")
print(f"d2 | d1 = {d2 | d1}")
print()

# New String Methods to Remove Prefixes and Suffixes
print("New String Methods to Remove Prefixes and Suffixes")
print("test message".removeprefix("te"))
print("test message".removesuffix("ge"))
print()

# Type Hinting Generics in Standard Collections
print("Type Hinting Generics in Standard Collections")
def words_len_calc(words: list[str]) -> dict[str, int]:
    out_d = dict()
    for w in set(words):
        out_d[w] = len(w)
    
    return out_d

print(words_len_calc("one two three four five".split()))
print()

# Annotated Type Hints
from typing import Annotated, get_type_hints

def speed(distance: Annotated[float, "feet"], time: Annotated[float, "seconds"]) -> Annotated[float, "miles per hour"]:
    """Calculate speed as distance over time"""
    fps2mph = 3600 / 5280  # Feet per second to miles per hour
    return distance / time * fps2mph

print(get_type_hints(speed))
print()