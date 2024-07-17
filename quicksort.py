import time
import tracemalloc
import random

# Implementación optimizada de QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Función para medir tiempo de ejecución y uso de memoria
def measure_performance(arr):
    start_time = time.time()
    tracemalloc.start()
    
    sorted_arr = quicksort(arr)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000  # convertir a milisegundos
    memory_usage = peak / 10**6  # convertir a MB
    
    return execution_time, memory_usage, sorted_arr

# Generar arrays de prueba
small_array = [random.randint(0, 1000) for _ in range(100)]
medium_array = [random.randint(0, 1000) for _ in range(300)]
large_array = [random.randint(0, 1000) for _ in range(500)]

# Medir rendimiento
small_time, small_memory, small_sorted = measure_performance(small_array)
medium_time, medium_memory, medium_sorted = measure_performance(medium_array)
large_time, large_memory, large_sorted = measure_performance(large_array)

# Resultados
print(f"Conjunto pequeño (100 elementos): Tiempo = {small_time:.2f} ms, Memoria = {small_memory:.6f} MB")
print(f"Conjunto mediano (300 elementos): Tiempo = {medium_time:.2f} ms, Memoria = {medium_memory:.6f} MB")
print(f"Conjunto grande (500 elementos): Tiempo = {large_time:.2f} ms, Memoria = {large_memory:.6f} MB")
