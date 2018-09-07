import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class NameTest:
    total = 0


print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after : ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()
print(id(n1), " VS ", id(n2))
print(dir())
print(n1.__dict__)  # 네임스페이스 확인
print(n2.__dict__)
n1.total = 77
print(n1.__dict__)

print(n1.total)
print(n2.total)
print(n1.next)  # next 네임스페이스에 없으면 오류 발생
