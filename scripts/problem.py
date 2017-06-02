import sys
from urllib2 import urlopen


def main(argv):

    # Check that all arguments are integers
    try:
        problems = [int(item) for item in argv]
    except ValueError:
        print('Error: Usage is \'python problem <problem-number>\'')
        sys.exit(1)

    for problem_number in problems:
        pass
        # TODO: Make request to euler
        # TODO: Parse title and capitalize first letters
        # TODO: Parse out question info
        # TODO: Split string into lines less than 80 char long
        # TODO: Create problem directory
        # TODO: Copy README and code skeleton over
        # TODO: R eplace README title with problem title
        # TODO: Replace README description with problem description
        # TODO: Enhancement. Generate method in code template


if __name__ == '__main__':
    main(sys.argv[1:])
