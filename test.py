from colorama import init, Fore, Style
import re
import subprocess
from typing import List, Tuple
import unittest

executable = "./push_swap"

def is_all_integers(args: List[str]) -> bool:
    return all(re.match(r'^\s*-?\d+\s*$', number) for number in args)

def is_duplicated(args: List[str]) -> bool:
    return len(args) != len(set(args))

def get_executable_output(args: str) -> Tuple[str, str]:
    """
    return the (stdout, stderr) of a command "./push_swap $args"
    """
    process = subprocess.Popen(
            [executable, args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
    stdout, stderr = process.communicate()
    return (stdout.decode().strip(), stderr.decode().strip())




class TestGetExecutableOutput(unittest.TestCase):
    def ft_test(
            self,
            test_case: str,
            actual: Tuple[str, str],
            expected: Tuple[str, str],
            ) -> None:
        tests = [
            ["stdout", expected[0], actual[0]],
            ["stderr", expected[1], actual[1]],
        ]
        for test in tests:
            try:
                self.assertEqual(test[1], test[2])
            except AssertionError:
                print(Fore.RED + f"KO" + Style.RESET_ALL, end = "\t")
                print(f"case: \"{test_case}\", expected in {test[0]} \"{test[1]}\", found \"{test[2]}\"")
            else:
                print(Fore.GREEN + "OK" + Style.RESET_ALL)

    def test_doing_nothing(self):
        args = [
            "0 1 2 3 4 5",
            "-5 -2 -1 0 3 10",
            "00 001 0002 00003",
            "1",
            "              1",
            "-1",
            "2147483647",
            "-2147483648",
        ]
        expected = ("", "")
        for case in args:
            self.ft_test(case, get_executable_output(case), expected)

    def test_error_cases(self):
        args = [
            "",
            "a",
            "-",
            "+",
            "00000000a",
            "12-12",
            "09-",
            "     +",
            "     ",
            "1 2 2 3 4 5",
            "0 1 023 0000023 34 3",
            "0-1",
        ]
        for case in args:
            expected = ("", "Error")
            for case in args:
                self.ft_test(case, get_executable_output(case), expected)


if __name__ == "__main__":
    init()
    unittest.main()

"""
TODO:
    * check when items are sorted the the outuput should be empty
    * check if only one item the output should be empty too
    * combine all the error inside a function
    * print the number of mouvements after sorting
    * if the range is between 1-3 ==> max 3
                              1-5 ==> max 7 ...

"""

