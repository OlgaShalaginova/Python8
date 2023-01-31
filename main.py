import controller

def main():
    choice = int(input("Выберете действие:\n"
                       "1 Добавить контакт\n"
                       "2 Найти контакт\n"
                       "3 Экспорт контактов:\n "))
    if choice == 1:
        controller.new_contact()
    elif choice == 2:
        controller.get_contact()
    elif choice == 3:
        controller.export_contacts()

if __name__ == "__main__":
    main()