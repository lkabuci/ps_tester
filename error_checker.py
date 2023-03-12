import re
from typing import List
import subprocess

# def test_non_integers(args):
#     if not is_all_integers(args):
#         process = subprocess.Popen(
#                 ["./push_swap", args],
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE
#                 )
#         _, error = process.communicate()
#         if error.decode().strip() == "Error":
#             exit(0)
#         print("No \"Error\" in the stderr for non integers elements")
#         exit(1)
#     return True
# 
# def test_duplicates(args):
#     if (is_duplicated(args)):
#         process = subprocess.Popen(
#                 ["./push_swap", args],
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE
#                 )
#         _, error = process.communicate()
#         if error.decode().strip() == "Error":
#             exit(0)
#         print("No \"Error\" in the stderr for duplicated elements")
#     return True

