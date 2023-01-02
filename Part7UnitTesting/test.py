import unittest
import main

class TestMainClass(unittest.TestCase):
    def setUp(self):
        print('This will run and set everything before each test')

    def test_multiply_main(self):
        print('test1')
        param_x = 4
        test_result = main.multiply_by_7(param_x)
        self.assertEqual(test_result, 28)

    def test_multiply_main2(self):
        print('test2')
        param_x = '4'
        test_result = main.multiply_by_7(param_x)
        self.assertEqual(test_result, 28)


    def test_multiply_main3(self):
        print('test3')
        param_x = 'string'
        test_result = main.multiply_by_7(param_x)
        self.assertIsInstance(test_result, ValueError)


    def test_multiply_main4(self):
        print('test4')
        ''' Test number 4 where we stest when the param_x is equal to None'''
        param_x = None
        test_result = main.multiply_by_7(param_x)
        #self.assertEqual(test_result, 0)
        self.assertEqual(test_result, 'None is not allowed, please use number next time')

    def tearDown(self):
        print('This will run after each test is completed')
unittest.main()






























