import re
from typing import List

def is_all_integers(args: List[str]) -> bool:
    return all(re.match(r'^\s*-?\d+\s*$', number) for number in args)

def is_duplicated(args: List[str]) -> bool:
    return len(args) != len(set(args))

"""
TODO:
    * check when items are sorted the the outuput should be empty
    * check if only one item the output should be empty too
    * combine all the error inside a function
    * print the number of mouvements after sorting
    * if the range is between 1-3 ==> max 3
                              1-5 ==> max 7 ...

"""

