"""
# 클래스

클래스는 객체를 표현하기 위한 문법입니다.
예를 들어 게임을 만든다고 하면 기사, 마법사, 궁수, 사제 등 직업별로 클래스를 만들어서 표현할 수 있습니다.

물론 집, 자동차, 나무 등도 클래스로 표현할 수 있습니다.
특히 프로그래밍에서는 현실 세계에 있는 개념들뿐만 아니라 컴퓨터 안에서만 쓰이는 개념들도 클래스로 만들어서 표현합니다. 웹 브라우저에서 내용이 길어지면 보이는 스크롤 바, 프로그램에서 주로 볼 수 있는 버튼, 체크 박스 등이 대표적입니다.

지금까지 나온 기사, 마법사, 궁수, 사제, 집, 자동차, 나무, 스크롤 바,
버튼, 체크 박스처럼 특정한 개념이나 모양으로 존재하는 것을 객체(object)라고 부릅니다.
그리고 프로그래밍으로 객체를 만들 때 사용하는 것이 클래스입니다.

그럼 게임의 기사 캐릭터를 클래스로 표현하려면 무엇이 필요할까요? 간단합니다.
일단 게임 캐릭터는 체력, 마나, 물리 공격력, 주문력 등이 필요합니다.
그리고 기사 캐릭터는 칼로 베기, 찌르기 등의 스킬이 있어야 합니다.

여기서 체력, 마나, 물리 공격력, 주문력 등의 데이터를 클래스의 속성(attribute)이라
부르고, 베기, 찌르기 등의 기능을 메서드(method)라고 부릅니다.

이렇게 프로그래밍 방법을 객체지향(object oriented) 프로그래밍이라고 합니다.
객체지향 프로그래밍은 복잡한 문제를 잘게 나누어 객체로 만들고, 객체를 조합해서 문제를 해결합니다.
따라서 현실 세계의 복잡한 문제를 처리하는데 유용하며
기능을 개선하고 발전시킬 때도 해당 클래스만 수정하면 되므로 유지 보수에도 효율적입니다.

지금까지 숫자 1, 2, 3 문자 'a', 'b', 'c', 리스트, 딕셔너리 등을 조합해서 프로그램을 만들었는데
사실 파이썬에서는 이 모든 것이 객체입니다. 이번에는 클래스를 사용해서 객체를 표현하고 만드는 방법을 알아보겠습니다.

## 클래스와 메서드 만들기

클래스는 class에 클래스 이름을 지정하고 :(콜론)을 붙인 뒤 다음 줄부터 def로 메서드를 작성하면 됩니다. 여기서 메서드는 클래스 안에 들어있는 함수를 뜻합니다.

클래스 이름을 짓는 방법은 변수와 같습니다. 보통 파이썬에서는 클래스의 이름은 대문자로 시작합니다. 그리고 메서드 작성 방법은 함수와 같으며 코드는 반드시 들여쓰기를 해야 합니다(들여쓰기 규칙은 if, for, while과 같습니다). 특히 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 합니다.

```
class 클래스이름:
    def 메서드(self):
        코드
```
"""

class MyClass:
    def hello(self):
        # print("안녕하세요!")
        print("안녕히계세요!")

mc = MyClass()  # 함수마냥 '실행' -> 생성
mc.hello() # -> 해당 클래스에 소속(소유)된 기능

"""그럼 이 클래스를 사용해봐야겠죠? 다음과 같이 클래스에 ()(괄호)를 붙인 뒤 변수에 할당합니다.

* `인스턴스 = 클래스()`
# 클래스 B를 통해서 객체 A를 만들면, (A) A라는 객체는, 클래스 B에 의해서 생성된 인스턴스다.
"""


"""Person으로 변수 james를 만들었는데 이 james가 Person의 인스턴스(instance)입니다.
클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 합니다.

### 메서드 호출하기

이제 메서드를 호출해보겠습니다. 메서드는 클래스가 아니라 인스턴스를 통해 호출합니다. 다음과 같이 인스턴스 뒤에 .(점)을 붙이고 메서드를 호출하면 됩니다.

* `인스턴스.메서드()`
"""
# 문자열, 리스트 => 객체.(기능)()


"""인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 부릅니다.

### 파이썬에서 흔히 볼 수 있는 클래스

지금까지 사용한 int, list, dict 등도 사실 클래스입니다.
우리는 이 클래스로 인스턴스를 만들고 메서드를 사용했습니다.
"""



"""파이썬에서는 자료형도 클래스입니다.
다음과 같이 type을 사용하면 객체(인스턴스)가 어떤 클래스인지 확인할 수 있습니다.

* `type(객체)`
"""

print(type(MyClass))  # <class 'type'>
print(type([])) # <class 'list'>
print(type({})) # <class 'dict'>


"""### 인스턴스와 객체의 차이점?

클래스는 객체를 표현하는 문법이라고 했는데,
클래스로 인스턴스를 만든다고 하니 좀 헷갈리죠? 사실 인스턴스와 객체는 같은 것을 뜻합니다.
보통 객체만 지칭할 때는 그냥 객체(object)라고 부릅니다.
하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부릅니다.
그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체입니다.
그리고 a와 b는 list 클래스의 인스턴스입니다.
"""



"""### 빈 클래스 만들기"""

# 내용이 없는 빈 클래스를 만들 때는 코드 부분에 pass를 넣어줍니다.

class Empty:
    pass # pass.

"""### 메서드 안에서 메서드 호출하기

메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다. self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 합니다.
"""

class FishBread:
    def eat(self):
        print("냠냠")

    def sound(self):
        print("붕어빵 먹는 소리")
        # self -> 이 클래스를 통해서 만들어진 객체(인스터스)가 갖고 있는 데이터와 기능
        self.eat()

bread = FishBread()
bread.sound()



"""### 특정 클래스의 인스턴스인지 확인하기

현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.

* `isinstance(인스턴스, 클래스)`
"""



"""isinstance는 주로 객체의 자료형을 판단할 때 사용합니다. 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없습니다. 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다."""





"""## 속성 사용하기

지금까지 클래스에서 메서드를 만들고 호출해보았습니다. 이번에는 클래스에서 속성을 만들고 사용해보겠습니다. 속성(attribute)을 만들 때는 `__init__` 메서드 안에서 self.속성에 값을 할당합니다.

```
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```
"""



"""```
__init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드입니다.
즉, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화합니다.

특히 이렇게 앞 뒤로 __(밑줄 두 개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데,
스페셜 메서드(special method) 또는 매직 메서드(magic method)라고 부릅니다.
앞으로 파이썬의 여러 가지 기능을 사용할 때 이 스페셜 메서드를 채우는 식으로 사용하게 됩니다.
```

```
속성은 __init__ 메서드에서 만든다는 점과 self에 .(점)을 붙인 뒤 값을 할당한다는 점이 중요합니다.
클래스 안에서 속성을 사용할 때도 self.hello처럼 self에 점을 붙여서 사용하면 됩니다.
```

### self의 의미

그런데 도데체 self는 뭘까요? self는 인스턴스 자기 자신을 의미합니다. 우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다. 여기서 `__init__`의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다. 그리고 self가 완성된 뒤 james에 할당됩니다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다. 그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.

### 인스턴스를 만들 때 값 받기

`__init__` 메서드에서 self 다음에 값을 받을 매개변수를 지정합니다. 그리고 매개변수를 self.속성에 넣어줍니다.

```
class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
```
"""



"""### 클래스의 위치 인수, 키워드 인수

클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다. 규칙은 함수와 같습니다. 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 합니다.
"""



"""키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 합니다."""



"""### 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기

지금까지 클래스의 인스턴스 속성은 `__init__` 메서드에서 추가한 뒤 사용했습니다. 하지만 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있습니다. 다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가합니다.
"""



# 이렇게 추가한 속성은 해당 인스턴스에만 생성됩니다.
# 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않습니다.

# 인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌
# 다른 메서드에서도 속성을 추가할 수 있습니다. 단, 이때는 메서드를 호출해야 속성이 생성됩니다.



"""## 클래스 속성과 인스턴스 속성 알아보기

속성에는 클래스 속성과 인스턴스 속성 두 가지 종류가 있습니다. `__init__` 메서드에서 만들었던 속성은 인스턴스 속성입니다.

### 클래스 속성 사용하기

```
class 클래스이름:
    속성 = 값
```
"""



"""put_bag 메서드에서 클래스 속성 bag에 접근할 때 self를 사용했습니다. 사실 self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 조금 모호합니다."""



"""그래서 클래스 속성에 접근할 때는 다음과 같이 클래스 이름으로 접근하면 좀 더 코드가 명확해집니다.

* `클래스.속성`
"""



"""Person.bag이라고 하니 클래스 Person에 속한 bag 속성이라는 것을 바로 알 수 있습니다. 마찬가지로 클래스 바깥에서도 다음과 같이 클래스 이름으로 클래스 속성에 접근하면 됩니다."""



"""### 인스턴스 속성 사용하기"""



"""* 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
* 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

## 클래스 상속 사용하기

지금까지 클래스의 기본적인 사용 방법을 알아보았습니다. 이번에는 클래스 상속(inheritance)을 사용해보겠습니다.

상속은 무언가를 물려받는다는 뜻입니다. 그래서 클래스 상속은 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용하는 기능입니다. 여기서 기능을 물려주는 클래스를 기반 클래스(base class), 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 합니다.

보통 기반 클래스는 부모 클래스(parent class), 슈퍼 클래스(superclass)라고 부르고, 파생 클래스는 자식 클래스(child class), 서브 클래스(subclass)라고도 부릅니다.

클래스 상속은 생물 분류를 떠올리면 이해하기 쉽습니다. 예를 들어 조류, 어류는 공통된 조상인 척추동물로부터 물려받은 특성을 공유하면서 각자 고유한 특성을 가집니다. 척추를 가졌다는 특성은 변함이 없지만 날개를 가졌으면 조류, 물속에 살면 어류인 식입니다. 즉, 같은 계통으로 특성을 공유하며 전혀 상관없이 어류가 꽃식물의 특성을 가지지는 않습니다.

마찬가지로 클래스 상속도 기반 클래스의 능력을 그대로 활용하면서 새로운 클래스를 만들 때 사용합니다. 동물을 예로 들면 척추동물에서 포유류, 조류, 파충류 등을 만드는 식이죠.

그런데 그냥 새로운 클래스를 만들면 되지 왜 이런 상속 개념을 만들었을까요? 만약 새로운 기능이 필요할 때마다 계속 클래스를 만든다면 중복되는 부분을 반복해서 만들어야 합니다. 이럴 때 상속을 사용하면 중복되는 기능을 만들지 않아도 됩니다. 따라서 상속은 기존 기능을 재사용할 수 있어서 효율적입니다.

클래스 상속은 다음과 같이 클래스를 만들 때 ( )(괄호)를 붙이고 안에 기반 클래스 이름을 넣습니다.

```
class 기반클래스이름:
    코드

class 파생클래스이름(기반클래스이름):
    코드
```
"""



"""이처럼 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능을 추가할 수 있습니다. 특히 클래스 상속은 연관되면서 동등한 기능일 때 사용합니다. 즉, 학생은 사람이므로 연관된 개념이고, 학생은 사람에서 역할만 확장되었을 뿐 동등한 개념입니다.

## 기반 클래스의 속성 사용하기

이번에는 기반 클래스에 들어있는 인스턴스 속성을 사용해보겠습니다. 다음과 같이 Person 클래스에 hello 속성이 있고, Person 클래스를 상속받아 Student 클래스를 만듭니다. 그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해봅니다.
"""



"""```
실행을 해보면 에러가 발생합니다.
왜냐하면 기반 클래스 Person의 __init__ 메서드가 호출되지 않았기 때문입니다.
실행 결과를 잘 보면 'Student __init__'만 출력되었습니다.

즉, Person의 __init__ 메서드가 호출되지 않으면,
self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않습니다.
```

### super()로 기반 클래스 초기화하기

이때는 super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해줍니다. 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식입니다.

* `super().메서드()`
"""



"""### 기반 클래스를 초기화하지 않아도 되는 경우

`만약 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.`
"""



"""### 좀 더 명확하게 super 사용하기

super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다. 물론 super()와 기능은 같습니다.

* `super(파생클래스, self).메서드`
"""



"""## 메서드 오버라이딩 사용하기

이번에는 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드 오버라이딩에 대해 알아보겠습니다. 다음과 같이 Person의 greeting 메서드가 있는 상태에서 Student에도 greeting 메서드를 만듭니다.
"""



"""오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻입니다. 여기서는 Person 클래스의 greeting 메서드를 무시하고 Student 클래스에서 새로운 greeting 메서드를 만들었습니다.

그럼 메서드 오버라이딩은 왜 사용할까요? 보통 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용합니다.

기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있습니다. 다음과 같이 오버라이딩된 메서드에서 super()로 기반 클래스의 메서드를 호출해봅니다.
"""

