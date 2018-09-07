import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 클래스 변수, 인스턴스 변수


class Warehouse:
    stock_num = 0  # 클래스 변수

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)  # 인스턴스 네임스페이스 확인 -> 클래스 네임스페이스 확인

print(user1.stock_num)  # 인스턴스 변수는 공유불가능, 클래스 변수는 공유가능
print(user2.stock_num)
