## 🛠 Практика: Примеры кода (Было / Стало)

### Пример 1: Принцип (S) — Единственная ответственность
**Задача:** Зарегистрировать пользователя и отправить приветственное письмо.

❌ **Без SOLID (Плохо: класс делает две разные работы):**
```python
class UserManager:
    def register_user(self, username, email):
        # 1. Работа с Базой Данных
        print(f"Сохраняем пользователя {username} в БД...")
        
        # 2. Работа с Сетью (Отправка писем)
        print(f"Отправляем email на {email}: Добро пожаловать!")
````

Почему это плохо: Если поменяется провайдер email-рассылок, нам придется лезть в класс UserManager и менять его. А если мы там случайно опечатаемся, мы сломаем регистрацию!

✅ **По SOLID (Два класса — две задачи):**

```python
# Класс 1: Занимается ТОЛЬКО базой данных
class UserRepository:
    def save(self, username):
        print(f"Сохраняем {username} в БД...")

# Класс 2: Занимается ТОЛЬКО почтой
class EmailService:
    def send_welcome_email(self, email):
        print(f"Отправляем email на {email}")

# Оркестратор
repo = UserRepository()
email_sender = EmailService()

repo.save("Sergey")
email_sender.send_welcome_email("sergey@mail.com")
```

### Пример 2: Принцип (O) — Open-Closed (Открыт для расширения, закрыт для изменения)
```python
### Пример 2: Принцип (O) — Open-Closed (Открыт для расширения, закрыт для изменения) **Рабочий кейс:** Интернет-магазин. Нам нужно считать скидки для разных типов пользователей (Обычный, VIP, Черная Пятница). 

❌ **Без SOLID (Свалка из IF-ов):**  

class DiscountCalculator: 
def calculate(self, user_type, amount):
	if user_type == "regular":
		return amount 
	elif user_type == "vip": 
		return amount * 0.8
	elif user_type == "black_friday": 
		return amount * 0.5

```
Почему это проблема: Завтра маркетологи придумают скидку "Новогодняя". Тебе придется **изменять** старый, рабочий, оттестированный класс DiscountCalculator. Ты можешь случайно удалить кусок кода и сломать скидки VIP-клиентам. Класс не "Закрыт".

✅ **По SOLID (Паттерн Стратегия):**

```python
from abc import ABC, abstractmethod 
# 1. Создаем общий стандарт для скидок 
class DiscountStrategy(ABC): 

	@abstractmethod 
	def get_discount(self, amount):
		pass 
# 2. Каждая скидка — это отдельный независимый класс 
class VipDiscount(DiscountStrategy):
	def get_add(self, amount):
		return amount * 0.8 
		
class BlackFridayDiscount(DiscountStrategy): 
	def get_discount(self, amount): 
		return amount * 0.5 
# 3. Калькулятор теперь ЗАКРЫТ для изменений. Ему всё равно, какая сейчас акция. 
class DiscountCalculator: 
	def calculate(self, discount_strategy: DiscountStrategy, amount):
		return discount_strategy.get_discount(amount) 
		# Завтра просят Новогоднюю скидку? Мы просто создаем НОВЫЙ файл с классом NewYearDiscount. # Старый код мы даже не открываем!

```

### Пример 3: Принцип (L)   — Liskov Substitution (Подстановка Лисков)

**Рабочий кейс:** Работа с базами данных (БД). В архитектуре есть основная БД (Мастер) и запасная БД для чтения (Реплика).

❌ **Без SOLID (Класс-наследник подкладывает свинью):**
```python
class DataBase:
	def read_data(self):
	print("Читаем данные...")
	
	def write_data(self):
	print("Записываем данные...")
	
	
# Создаём реплику (она только для чтения). Наследуем её от основной БД.
class ReadOnlyReplica(Database):
	def write_data(self):
	# Наследник ломает поведение родителя!
		raise NotImplementedError("В Реплику писать нельзя,она только для чтения")
		
# --- Логика сервера ---
	def save_user_profile(db: Database):
	db.wirte_data() # Если мы подсунем ReadOnlyReplica, сервер упадёт.
```
Почему это проблема: Принцип Лисков гласит: "Наследник не должен удивлять". Если функция ждет объект Database, она уверена, что у него работает метод write_data. А наша Реплика взрывается ошибкой.

✅ **По SOLID (Правильное разделение интерфейсов):**
```python
# РОдитель умеет только читать
class ReadableDatabase:
	def read_data(self):
	pass
	
# Наследник умеет и читать, и писать (расширяет, а не ломает!)
class WriteDatabase(ReadableDatabase):
	def write_data(self):
	pass
	
class ReadOnlyReplica(ReadableDataBase):
	pass # Реплике метод write_data просто не достался, и никто его от неё не ждёт!

```

### Пример 4:  Принцип (I) — Interface Segregation (Разделение интерфейса)

**Рабочий кейс:** Работа с облачными хранилищами (AWS, Яндекс.Облако, Локальный диск).

❌ **Без SOLID (Интерфейс "Швейцарский нож"):**
```python
#Огромный интерфейс для облака
class CloudProvider(ABC):
	@abstractmethod
	def store_file(self):
		pass
		
	@abstractmethod
	def setup_database(self):
		pass
		
# Если мы хотим сделать простое локальное хранилище (которе БД не поддерживает)
class LocalStorage(CloudProvider):
	def store_file(self):
		print("Файл сохранён на диск")
	
	def setup_database(self):
# Мы ВЫНУЖДЕНЫ реализовывать этот метод, хотя он нам не нужен!
		pass
```
Почему это проблема: Класс LocalStorage заставили тащить на себе лишний багаж.

✅ **По SOLID (Дробление интерфейсов):**

```python
# Разделяем огромный CloudProvider на маленькие кусочки 

class FileStorage(ABC):
	@abstractmethod
	def store_file(self):
		pass
	
class DataBaseHosting(ABC):
	@abstractmethod
	def setup_database(self):
		

# теперь классы берут только те интерфейсы,которые им РЕАЛЬНО нужны
class LocalStorage( FileStorage):
	def store_file(self):
		print("Файл сохранён на диск")

class AmazonAWS(FileStorage, DataBaseHosting):
		def store_file(self):
			pass
		def setup_database(self):
			pass 

```

### Пример 5:  Принцип (D) — Dependency Inversion Principle (принцип инверсии зависимостей)

**Задача:** Магазин должен принимать оплату через платежную систему.
❌ **Без SOLID (Смертельное сцепление):**
```python
class YandexKassa:
	def make_payment(self, amount):
		print(f"Оплата {amount} руб. через Яндекс.")
	
class Store:
	def checkout(self, amount):
		# Магазин жёстко зависит от конкретного Яндекса
		payment_system = YandexKassa()
		payment_system.make_payment(amount)

shop = Store()
shop.checkout(100)
```

Почему это катастрофа: Завтра бизнес скажет: "Мы уходим от Яндекса, подключай Tinkoff". Тебе придется "вскрывать" класс Store и переписывать весь код магазина. А если таких мест 50?

✅ **По SOLID (Инверсия зависимостей через Розетку):**
```python

from abc import ABC, abstractmethod

	# 1. Создаем "Розетку" (Абстракцию). Мы говорим: "У любой платежки должна быть кнопка pay"
	class PaymentGateAway(ABC):
		@abstractmethod
		def pay(self, amount):
			pass
	# 2. Делаем конкретные "вилки"(они подчиняются розетке)
	class YandexKassa(self, amount):
		print(f"Оплата {amount} руб. через Яндекс.")
		
	class TinkoffPay(self,amount):
		print(f"Оплата {amount} руб. через Тиньку.")
	
	# 3. Магазин больше не зависит от Яндекса. Он зависит от абстрактной "розетки"
	class Store:
		# При создании магазина мы просто передаём ему нужную платёжку извне
		def __init__(self, payment_system: PaymentGateAway):
			self.payment_system = payment_system
		
		def checkout(self, amount):
			self.payment_system.pay(amount) # Магазин жмёт на абстрактную pay
			
	# Теперь смена платёжки занимает минимум времени без измения кода магазина:
	tinkoff = TinkoffPay()
	shop = store(tinkoff)
	shop.checkout(100)
			

```