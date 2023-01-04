import os
import sys
import time
import random
import platform

def print_help(args: list) -> None:
	"""
	It prints the usage of the program and exits if the number of arguments is not 4 or if the first argument is --help
	
	:param args: the arguments passed to the program
	:type args: list
	"""
	print("usage:\tpython3 rand.py [--option] [nbr_of_tests] [stack_len]");
	if (len(args) != 4):
		exit(1);
	if (args[1] == "--help"):
		print("\tOptions (string)\t : --generate, --print, --test, --visual");
		print("\tnumber_of_test (int > 0) : how many tests to run");
		print("\tstack_len (int > 0)\t : the len of the stack to generate");
		exit(1);

def generator(i: int) -> str:
	"""
	It takes an integer and returns a string of random numbers separated by spaces
	
	:param i: the number of elements in the list
	:type i: int
	:return: A string of numbers separated by spaces.
	"""
	ret = ""
	lst = random.sample(range(0,i),i)
	for j in lst:
		ret += f"{str(j)} "
	return ret.rstrip(' ');

def get_os() -> str:
	"""
	It returns the path to the checker executable, depending on the operating system
	:return: The path to the checker program.
	"""
	os_name = platform.system().lower();
	if (os_name == "linux"):
		return ("./checker_linux")
	return "./checker_Mac"

def command_runner(args: str, os_name: str, option: str, script_name: str):
	"""
	It runs the command line arguments
	
	:param args: The arguments to be passed to the push_swap program
	:type args: str
	:param os_name: The name of the executable file
	:type os_name: str
	:param option: The option you want to use
	:type option: str
	:param script_name: The name of the script
	:type script_name: str
	"""
	if (option == "--generate"):
		print(args);
	elif (option == "--print"):
		print(args);
		os.system(f"./push_swap {args} | {os_name} {args} | cat -e");
	elif (option == "--test"):
		os.system(f"./push_swap {args} | {os_name} {args} | grep 'KO\|Error'");
	elif (option == "--mouvements"):
		os.system(f"./push_swap {args} | wc -l");
	else:
		print(f"usage: python3 {script_name} [number] [range] [--option]");
		exit(1);

def parse(args: list) -> tuple:
	"""
	It checks if the arguments are valid
	
	:param args: list of arguments passed to the program
	:type args: list
	:return: A tuple containing the option, the number of queens and the size of the board.
	"""
	available_options = ["--generate", "--print", "--test", "--mouvements"];

	if (len(args) != 4):
		print_help(args);
	if (args[1] == "--help"):
		print_help(args);
	if ((args[1] not in available_options) or args[2].isdecimal() == False or args[3].isdecimal() == False):
		print_help(args);
	
	return (args[1], int(args[2]), int(args[3]));

if __name__ == "__main__":
	os_name: str = get_os();
	script_name: str = sys.argv[0];

	option: str
	nbr_of_tests: int
	stack_len: int

	option, nbr_of_tests, stack_len = parse(sys.argv);
	for i in range(nbr_of_tests + 1):
		stack = generator(stack_len);
		command_runner(stack, os_name, option, script_name);
