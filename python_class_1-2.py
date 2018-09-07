import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class UserInfo:
    def __init__(self, name, phone):  # 클래스 생성자
        self.name = name
        self.phone = phone

    def print_info(self):
        print("---------------------")
        print("Name: " + self.name)
        print("phone: " + self.phone)
        print("---------------------")

    def __del__(self):  # 메모리 누수방지
        print("delete!")


user1 = UserInfo("Kim", "010-2760-7777")
user2 = UserInfo("Park", "010-9928-7777")

print(id(user1))  # 인스턴스 주소값 확인
print(id(user2))

# user1.set_info("Kim", "010-2760-7777")
# user2.set_info("Park", "010-9928-7777")

user1.print_info()
user2.print_info()

print(user1.__dict__)  # 인스턴스 네임스페이스 확인
print(user2.__dict__)

print(user1.phone, user1.name)
