import time
import common


def main():
    start = time.time()
    ans = 1/float(1000)  #TODO start problem here
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))
    common.hello()


if __name__ == '__main__':
    main()
