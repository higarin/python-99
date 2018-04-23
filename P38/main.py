import sys
import timeit

sys.path.append('../')

number = 100


def test_totient_phi():
    print('P34 {}'.format(
        timeit.timeit('totient_phi(10090)', number=number, setup='from P34.main import totient_phi')))


def test_totient_phi_improved():
    print('P37 {}'.format(
        timeit.timeit('totient_phi(10090)', number=number, setup='from P37.main import totient_phi')))


if __name__ == "__main__":
    test_totient_phi()
    test_totient_phi_improved()
