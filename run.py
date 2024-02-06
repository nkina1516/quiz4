#import module1.thing1 as hi
from module1 import thing1 as hello
from module2 import thing2 as hey
from module3 import thing3 as yo

def demo() -> None:
    
    hello.hello_world()
    hello.whatsnum1()
    hey.hello_world()
    hey.whatsnum2()
    yo.hello_world()
    yo.whatsnum3()

if __name__ =="__main__":
    demo()

