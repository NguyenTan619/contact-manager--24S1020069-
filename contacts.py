phonebook = []

def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

def add_contact():
    name = input("Nhập tên: ").strip()
    phone = input("Nhập số điện thoại: ").strip()
    if not name or not phone:
        print("Tên hoặc số điện thoại không được rỗng.")
        return
    # kiểm tra trùng (tuỳ yêu cầu, ở đây cho phép trùng)
    contact = {'name': name, 'phone': phone}
    phonebook.append(contact)
    print("Đã thêm liên hệ.")