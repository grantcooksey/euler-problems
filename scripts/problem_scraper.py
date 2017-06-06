"""Web Scraper to pull new down problem from Project Euler.

This module is to assist in generating the problems rather than copying
and pasting from Project Euler's website and provide some standardization
between problems. The problem description is
scraped from the problem page and is formatted and placed into a template
README. The problem description is split into lines less than LINE_LENGTH
and attempts to not split words in half unless dealing with long words.
See `Note`. A new directory for the problem is placed in `problems` and the
README and a bruteforce code template are placed in the directory. The
naming convention for the directory is `problem<problem_number>`. If the
directory already exists, the problem is skipped.

Note:
    When formatting the README, words longer than 30 characters are split
    between two lines. If the long word runs over the second line after
    the first split, it is not split again.

Example:
    To pull down problem 37 and generate the README and template::

        $ python problem_scraper.py 37

    For multiple problems::

        $ python problem_scraper.py 37 48 52

Attributes:
    LINE_LENGTH (int): Maximum length of character per line. See ``Note``for
        when dealing with long words.
    LONG_WORD (int): Length of word to consider splitting in two between lines.

Todo:
    * Don't split urls
    * Format math equations
    * Generate method in code template

"""
import sys
import os
from urllib2 import urlopen, URLError
from lxml import html

LINE_LENGTH = 80
LONG_WORD = 30


def split_into_lines(s):
    """Splits lines into >= LINE_LENGTH characters long lines

    Note:
        Words longer than 30 characters are split between two lines. If the
        long word runs over the second line after the first split, it is not
        split again.

    Args:
        s (str): Text to split.

    Returns:
        str: Text split by appropriate newline chars.

    """
    text = str()

    for line in s.split('\n'):
        words = line.split(' ')
        new_line = str()
        for i in range(len(words)):
            if len(new_line + words[i] + ' ') > LINE_LENGTH:
                if len(words[i]) > LONG_WORD:  # Long words are split
                    split_index = LINE_LENGTH - len(new_line)
                    text += new_line + words[i][:split_index] + '\n'
                    words[i] = words[i][split_index:]
                else:
                    text += new_line + '\n'
                new_line = str()
            new_line += words[i] + ' '
        text += new_line + '\n\n'

    return text


def make_request(problem_number):
    """Pulls content from the Project Euler website.

    Args:
        problem_number (int): Problem number to pull down.

    Returns:
        HTML element.

    """
    url = 'https://projecteuler.net/problem=' + str(problem_number)

    # Make request to euler
    try:
        page = urlopen(url, timeout=5)
        content = html.fromstring(page.read())
    except URLError:
        print('Error: The request to {0} did not complete.'.format(url))
        sys.exit(1)

    return content


def parse_problem(content):
    """Parses the title and problem description.

    Args:
        content: HTML element from a Project Euler problem description.

    Returns:
        str: Title of problem.
        str: Problem description.

    """
    # Parse title and capitalize first letters
    title = content.xpath('//h2/text()')[0].title()

    # Parse out question info
    el = content.xpath('//div[@class="problem_content"]/child::*')
    description_long = '\n'.join(x.text for x in el)

    return title, description_long


def new_problem(problem_number):
    """Checks is problem does not exist in collection of problems.

    The purpose of this function is avoid overwriting problems.
    If a directory or file named `problem<problem_number>`
    exists in `problems`, a problem template should not be generated.

    Args:
        problem_number (int): Problem to check.

    Returns:
        bool: True if problem has not been attempted or previously created,
            else False.

    """
    path = '../problems/problem{0}'.format(problem_number)
    return not os.path.exists(path)


def main(argv):
    # Change module's working directory to the module's own directory
    os.chdir(sys.path[0])

    # Check that all arguments are integers
    try:
        problems = [int(item) for item in argv]
    except ValueError:
        print('Error: Usage is \'python problem <problem-number>\'')
        sys.exit(1)

    for problem_number in problems:
        if new_problem(problem_number):
            content = make_request(problem_number)

            # Parse out question description and title
            title, description_long = parse_problem(content)

            # Split string into lines less than 80 char long
            description = split_into_lines(description_long)

            # TODO: Create problem directory
            # TODO: Copy README and code skeleton over
            # TODO: Replace README title with problem title
            # TODO: Replace README description with problem description

if __name__ == '__main__':
    main(sys.argv[1:])
