import sys
import os

def my_cat():
    # sys.argv[0] is the script name, so we look at everything from index 1 onwards
    files = sys.argv[1:]

    if not files:
        print("Usage: python cat.py <file1> <file2> ...")
        return

    for file_path in files:
        # Check if the path exists and is a file
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as f:
                    # Print file content to standard output
                    print(f.read(), end='')
            except Exception as e:
                print(f"\ncat: {file_path}: {e}", file=sys.stderr)
        else:
            print(f"\ncat: {file_path}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    my_cat()
