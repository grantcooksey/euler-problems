import sys
from urllib2 import urlopen, URLError
from lxml import html


def split_into_lines(s):
    text = str()

    for line in s.split('\n'):
        words = line.split(' ')
        new_line = str()
        for i in range(len(words)):
            if len(words[i]) > 80:  # Long word on its own line
                text += new_line + '\n' + words[i] + '\n'
                new_line = str()
            if len(new_line + words[i] + ' ') > 80:
                text += new_line + '\n'
                new_line = str()
            new_line += words[i] + ' '
        text += new_line + '\n\n'

    return text


def make_request(problem_number):
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
    # Parse title and capitalize first letters
    title = content.xpath('//h2/text()')[0].title()

    # Parse out question info
    el = content.xpath('//div[@class="problem_content"]/child::*')
    description_long = '\n'.join(x.text for x in el)

    return title, description_long


def main(argv):
    # Check that all arguments are integers
    try:
        problems = [int(item) for item in argv]
    except ValueError:
        print('Error: Usage is \'python problem <problem-number>\'')
        sys.exit(1)

    for problem_number in problems:
        content = make_request(problem_number)

        # Parse out question description and title
        title, description_long = parse_problem(content)

        # Split string into lines less than 80 char long
        description = split_into_lines(description_long)

        # TODO: Create problem directory
        # TODO: Copy README and code skeleton over
        # TODO: Replace README title with problem title
        # TODO: Replace README description with problem description
        # TODO: Enhancement. Generate method in code template


if __name__ == '__main__':
    main(sys.argv[1:])
