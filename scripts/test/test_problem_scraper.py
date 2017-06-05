from unittest import TestCase
from problem_scraper import split_into_lines, make_request, parse_problem


class TestSplitIntoLines(TestCase):
    def test_split_into_lines_37(self):
        text = 'The number 3797 has an interesting property. Being prime ' + \
            'itself, it is possible \nto continuously remove digits ' + \
            'from left to right, and remain prime at each \nstage: 3797, ' + \
            '797, 97, and 7. Similarly we can work from right to left: ' + \
            '3797, \n379, 37, and 3. \n\nFind the sum of the only eleven ' + \
            'primes that are both truncatable from left to \nright and ' + \
            'right to left. \n\nNOTE: 2, 3, 5, and 7 are not considered ' + \
            'to be truncatable primes. \n\n'
        x, description = parse_problem(make_request(37))
        parsed_test = split_into_lines(description)
        self.assertEqual(parsed_test, text)

    def test_split_into_lines_37_long(self):
        text = 'The number aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
               'aaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 3797' \
               ' has an interesting property. Being prime \nitself, it is ' \
               'possible to continuously remove digits from left to right,' \
               ' and \nremain prime at each stage: 3797, 797, 97, and 7. S' \
               'imilarly we can work from \nright to left: 3797, 379, 37, ' \
               'and 3. \n\nFind the sum of the only eleven primes that are ' \
               'both truncatable from left to \nright and right to left. \n' \
               '\nNOTE: 2, 3, 5, and 7 are not considered to be truncatable' \
               ' primes. \n\n'
        x, description = parse_problem(make_request(37))
        long_word = ' ' + ''.join('a' for a in range(100))
        description = description[:10] + long_word + description[10:]
        print(description)
        self.assertEqual(split_into_lines(description), text)
