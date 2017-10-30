import unittest
import math


def skip1(val):
    if val == 1:
        return lambda fn: fn
    return unittest.skip('value is not 1')



class Test1(unittest.TestCase):
    def test_int(self):
        self.assertEqual(int('11'), 11)
        with self.assertRaises(ValueError):
            int('1.1')

    def test_pow(self):
        self.assertEqual(math.pow(2, 3), 8)

    def test_ceil(self):
        self.assertEqual(math.ceil(1.4), 2)

    @unittest.skip('Test1.notest')
    def test_notest(self):
        self.assertEqual(1, 0)

    @unittest.skipIf(__name__ == 'unit', 'not unit')
    def test_t1(self):
        pass

    @skip1(2)
    def test_1(self):
        pass

    @unittest.skipUnless(__name__ == 'unit2', 'is not unit2')
    def test_t2(self):
        pass


    @unittest.expectedFailure
    def test_intstr(self):
        int('str')

    def setUp(self):
        print('start test')

    def tearDown(self):
        print('finish test')


@unittest.skip('NoTest')
class NoTest(unittest.TestCase):
    def test_any(self):
        pass


def suite():
    s = unittest.TestSuite()
    s.addTest(Test1('test_int'))
    return s

if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())
