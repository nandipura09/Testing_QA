import fibonacci  # Impor modul yang akan diuji
import unittest  # Impor modul unittest untuk pembuatan Unit Test

# Kelas TestFibonacci digunakan untuk menguji fungsi dalam modul fibonacci
class TestFibonacci(unittest.TestCase):

    def test_validate_number_for_fibonacci_with_non_integer_input(self):
        try:
            fibonacci.validate_number_for_fibonacci("hello")  # Menguji input non-integer
        except TypeError as e:
            self.assertEqual(str(e), "Input must be an integer")  # Memastikan pesan kesalahan sesuai

    # Test-case berikut adalah contoh kasus uji lainnya yang serupa dengan penjelasan di atas
    # ...

# Kelas TestValidator digunakan untuk menguji fungsi validasi input (validate_number_for_fibonacci)
class TestValidator(unittest.TestCase):

    def test_validate_number_for_fibonacci_with_non_integer_input(self):
        # Menguji input non-integer
        try:
            fibonacci.validate_number_for_fibonacci("hello")
        except TypeError as e:
            self.assertEqual(str(e), "Input must be an integer")

    # Test-case berikut adalah contoh kasus uji lainnya yang serupa dengan penjelasan di atas
    # ...

# Kelas TestFibonacciArray digunakan untuk menguji fungsi pembuatan array Fibonacci (fibonacci_array)
class TestFibonacciArray(unittest.TestCase):

    def test_fibonacci_array_with_non_integer_input(self):
        # Menguji input non-integer
        try:
            fibonacci.fibonacci_array("hello", 1)
        except TypeError as e:
            self.assertEqual(str(e), "Input must be an integer")

    # Test-case berikut adalah contoh kasus uji lainnya yang serupa dengan penjelasan di atas
    # ...

if __name__ == '__main__':
    unittest.main()  # Menjalankan semua Unit Test
