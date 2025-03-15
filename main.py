import argparse
import os
from helpers import genRandomLetters


def main():
    parser = argparse.ArgumentParser(description="Process filename")
    parser.add_argument("filename",help="Path to the file")
    args = parser.parse_args()
    text = genRandomLetters(args.filename,1000)
    print(text)

    return

    
if __name__=='__main__':
    main()