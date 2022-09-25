import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo a string into a file')
    parser.add_argument('--file', required=True,
                        help='The file to which the string will be stored')
    parser.add_argument('str', help='the string to echo')

    args = parser.parse_args()
    str = args.str
    with open(args.file, 'w', encoding="utf-8", newline='') as f:
        f.write(str)
