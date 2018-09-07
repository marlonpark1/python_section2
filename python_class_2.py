import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class SelfTest:
    def function1():  # self 없는 인스턴스 호출 에러발생, 클래스 직접 호출 가능
        print("function1 called!")

    def function2(self):
        # print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))
f.function2()
print(SelfTest.function1())
