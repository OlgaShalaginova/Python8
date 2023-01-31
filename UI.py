def get_value():
    last_name = str(input("Введите фамилию: "))
    first_name = str(input("Введите имя: "))
    mid_name = str(input("Введите отчество: "))
    phone_number = str(input("Введите номер телефона: "))
    department = str(input("Введите номер класса: "))
    return last_name, first_name, mid_name, phone_number, department

def view_data():
    last_name = str(input("Введите фамилию: "))
    return last_name

def import_data():
    file_name = str(input("Введите имя файла: "))
    return file_name