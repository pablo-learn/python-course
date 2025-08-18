import multiprocessing

def proccess_data(data):
    print(f"Procesando datos: {data}")
    return data

if __name__ == "__main__":
    numbers = range(10000)
    with multiprocessing.Pool() as pool:
        results = pool.map(proccess_data, numbers)
        print(results)