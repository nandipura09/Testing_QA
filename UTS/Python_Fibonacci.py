import sys

# Fungsi untuk memvalidasi input n pada fungsi Fibonacci
def validate_number_for_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    elif n <= 0:
        raise ValueError("Input must be a positive integer")

# Fungsi rekursif untuk menghitung bilangan Fibonacci ke-n
def fibonacci(n):
    # Validasi input terlebih dahulu
    validate_number_for_fibonacci(n)
    
    # Kasus dasar: Fibonacci(1) = 0, Fibonacci(2) = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Perhitungan Fibonacci menggunakan rekursi
        return fibonacci(n - 1) + fibonacci(n - 2)

# Fungsi untuk menghasilkan array bilangan Fibonacci dalam rentang start hingga end
def fibonacci_array(start, end):
    # Validasi input untuk start dan end
    validate_number_for_fibonacci(start)
    validate_number_for_fibonacci(end)
    
    # Validasi bahwa start harus kurang dari atau sama dengan end
    if start > end:
        raise ValueError("end must be after start")
    
    fib_array = []  # Inisialisasi array kosong untuk hasil Fibonacci
    for i in range(start, end + 1):
        # Menghitung Fibonacci ke-i dan menambahkannya ke dalam array
        fib_array.append(fibonacci(i))
    return fib_array

if __name__ == '__main__':
    # Mengambil argumen dari baris perintah
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # Memanggil fungsi fibonacci_array dengan argumen dari baris perintah
    result = fibonacci_array(start, end)
    
    # Mencetak hasil array Fibonacci
    print(result)
