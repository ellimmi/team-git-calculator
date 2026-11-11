from basic_operations import add, subtract, multiply, divide
from advanced_operations import power, square_root, factorial

def main():
    print("=== Командный Инженерный Калькулятор (Git Lab) ===")
    
    while True:
        print("\nДоступные операции:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Возведение в степень (^)")
        print("6. Квадратный корень (√)")
        print("7. Факториал (!)")
        print("0. Выход")
        
        choice = input("\nВыберите действие (0-7): ").strip()
        
        if choice == '0':
            print("Программа завершена. До свидания!")
            break
            
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введите первое число (или основание): "))
                num2 = float(input("Введите второе число (или степень): "))
            except ValueError:
                print("Ошибка: Пожалуйста, вводите только числа!")
                continue
                
            try:
                if choice == '1': print(f"Результат: {add(num1, num2)}")
                elif choice == '2': print(f"Результат: {subtract(num1, num2)}")
                elif choice == '3': print(f"Результат: {multiply(num1, num2)}")
                elif choice == '4': print(f"Результат: {divide(num1, num2)}")
                elif choice == '5': print(f"Результат: {power(num1, num2)}")
            except ValueError as e:
                print(e)
                
        elif choice in ('6', '7'):
            try:
                num = float(input("Введите число для операции: "))
            except ValueError:
                print("Ошибка: Пожалуйста, вводите только числа!")
                continue
                
            try:
                if choice == '6': print(f"Результат: {square_root(num)}")
                elif choice == '7': print(f"Результат: {factorial(num)}")
            except ValueError as e:
                print(e)
        else:
            print("Ошибка: Неверный пункт меню! Попробуйте снова.")

if __name__ == "__main__":
    main()
    