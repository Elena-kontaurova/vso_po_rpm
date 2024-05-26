import time

def calculate_excuton_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        excution_time = end_time - start_time
        print("Время выполнения:", excution_time, "секунд")
        return result
    return wrapper

@calculate_excuton_time
def test_function(a = None, b= None):
    count = 0
    for i in range(a, b):
        count += i
    return count

result = test_function(0, 4323870)