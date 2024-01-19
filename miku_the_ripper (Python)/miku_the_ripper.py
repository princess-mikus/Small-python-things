# Made by Mikus the Ripper

from sys import argv
from os import remove
import hashlib
import time

def print_result(password, custom_out, outfile):
    if custom_out:
        outfile.write(password)
    else:
        print(password)

def basic_test(wordlist, hash, type):
    for i in range(len(wordlist)):
        h = hashlib.new(type)
        line = wordlist[i].rstrip("\n")
        line = line.encode("utf-8")
        h.update(line)
        new_hash = h.hexdigest()
        if new_hash == hash:
            return wordlist[i].rstrip("\n")
    return None
            
def combination_test(wordlist, hash, type):
    for i in range(len(wordlist)):
        for j in range(len(wordlist)):
            h = hashlib.new(type)
            line = wordlist[i].rstrip("\n") + wordlist[j].rstrip("\n")
            line = line.encode("utf-8")
            h.update(line)
            new_hash = h.hexdigest()
            if new_hash == hash:
                return wordlist[i].rstrip("\n") + wordlist[j].rstrip("\n")
    return None

def main():
    if len(argv) <= 2:
        print("Not enough arguments"), exit(2)
    
    # Dictionary ALWAYS imported from argv[1]
    try:
        dictionary = open(argv[1], "r")
    except IOError:
            print("Dictionary file not found"), exit(IOError)
    custom_out = False
    file_input = False
    outfile = ""
    type = None

    # Flag parsing
    for i in range(len(argv)):
        if argv[i] == "-o": # -o specifies the output file, if not prints to console
            try:
                outfile = open(argv[i + 1], "w")
            except IOError:
                print("Error creating outfile"), exit(IOError)
            custom_out = True
        if argv[i] == "-f": # -f indicates the input file in which the hash is stored. Maybe I'll add multiple line input support
            try:
                infile = open(argv[i + 1], "r")
            except IOError:
                print("Hash file not found"), exit(IOError)
            file_input = True
        if argv[i] == '-t': # Specificy which type of hash was used. Multiple algorithms can be given separated by a space in the same argument
            type = argv[i + 1].split(" ")
            for i in range(len(type)):
                if type[i].lower().replace("-", "") not in hashlib.algorithms_available:
                    print("Either not a type or not supported in your Python interpreter"), exit()

    if type is None:
        type = "SHA-1"

    # Gets the hash either from argument or from the file specified before
    if not file_input:
        hash = argv[2]
    else:
        hash = infile.read()

    wordlist = dictionary.readlines()
    # Get start of cracking time
    start = time.perf_counter()
    
    solved = False
    #for i in range(len(type)):
    password = basic_test(wordlist, hash, type)
    if password:
        print_result(password, custom_out, outfile)
        solved = True
    if not solved:
        password = combination_test(wordlist, hash, type)
    if not solved and password:
        print_result(password, custom_out, outfile)
        solved = True
    if not password and i not in range(len(type)):
        print("Miku can't rip the password :(")
        if custom_out:
            custom_out = False
            remove(outfile) 

    # Get endtime
    end = time.perf_counter()
    print(f"Program ran in {float(end - start)} seconds")
    if (file_input):
        infile.close()
    if (custom_out):
        outfile.close()
    dictionary.close()

if __name__ == '__main__':
	main()