gang_members = []

def add_member(name, age, gang):
    new_member = {"name": name,
         "age": age,
          "gang": gang}
    gang_members.append(new_member)
    return new_member # เช้ดว่าเพิ่มถูกรึป่าว

def show_members():
    return gang_members


while True:
    a = int(input("ผู้ใช้ต้องการทำอะไร 1.เพื่อเพิ่มสมาชิก 2.เพื่อดูสมาชิกทั้งหมด 3.เพื่อออกจากระบบ: "))
    if a == 1:
        name = input("Name: ")
        age = input("Age: ")
        gang = input("Gang: ")
        add_member(name, age, gang)
    elif a == 2:
        print(show_members())
    else:
        print("กำลังออกจากระบบ")
        break

        
    
