try:
    print(10/0)
except ZeroDivisionError as e:
    print("No se puede dividir por cero", e)
except Exception as e:
    print("Error", e)






