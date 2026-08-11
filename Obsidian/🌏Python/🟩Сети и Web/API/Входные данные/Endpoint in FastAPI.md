
1. **HTTP** — это **язык общения** . Как именно запаковать конверт.
    
2. **API (Application Programming Interface)** — cписок того, что вообще можно попросить у твоего сервера.
    
3. **FastAPI**(фреймворк) — инструмент, который читает HTTP-конверт, смотрит в меню (API), делает работу и отдает ответ.
    

То есть: **FastAPI создает API, которое общается по протоколу HTTP.**


В веб-разработке мы постоянно общаемся с сервером. Чтобы сервер понимал, чего мы от него хотим, мы используем разные **HTTP-методы**.

Представьте, что ваше API — это **архив с документами**.

1. **GET** — Вы просите библиотекаря показать документ.
    
2. **POST** — Вы приносите новый документ и просите положить его в архив.
    
3. **PUT** — Вы просите заменить старую папку на новую целиком.
    
4. **PATCH** — Вы просите подправить пару строчек в документе (например, исправить опечатку).
    
5. **DELETE** — Вы просите выбросить документ в шредер.
    


Для начала создадим "базу данных" (обычный список) и модель данных, чтобы FastAPI знал, как выглядит наш пользователь.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Модель данных (схема)
# Она гарантирует, что пользователь всегда имеет имя и возраст
class User(BaseModel):
    id: int
    name: str
    age: int

# 2. Наша "База данных"
users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]
```


 5 главных методов API в FastAPI
## 1️⃣ GET — Получение данных

**Смысл:** "Просто покажи мне данные, я ничего не буду менять".  
Это самый частый запрос. Мы используем декоратор @app.get.

```python 
@app.get("/users")
def get_all_users():
    """Возвращает список всех пользователей"""
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает конкретного пользователя по ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    # Если не нашли — выдаем ошибку 404
    raise HTTPException(status_code=404, detail="User not found")
```

## 2️⃣ POST — Создание данных

**Смысл:** "Вот новые данные, сохрани их".  
Данные отправляются в **теле запроса** (body). FastAPI автоматически проверит, соответствуют ли они схеме User. Используем @app.post.

```python
@app.post("/users")
def create_user(user: User):
    """Добавляет нового пользователя"""
    # Превращаем модель Pydantic в словарь и добавляем в список
    users_db.append(user.dict())
    return {"message": "User created", "user": user}
```

## 3️⃣ PUT — Полное обновление

**Смысл:** "Замени старую запись вот этой новой".  
Важно: PUT обычно подразумевает, что мы передаем объект **целиком**. Если вы передадите только имя, а возраст забудете — возраст сотрется (или будет ошибка). Используем @app.put.
```python 
@app.put("/users/{user_id}")
def update_user_complete(user_id: int, updated_user: User):
    """Полностью заменяет пользователя с указанным ID"""
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            # Полная замена элемента списка
            users_db[index] = updated_user.dict()
            return {"message": "User updated completely", "user": updated_user}
    
    raise HTTPException(status_code=404, detail="User not found")
```

## 4️⃣ PATCH — Частичное обновление

**Смысл:** "Измени только то, что я прислал".  
Это более гибкий метод. Например, пользователь хочет сменить только имя, а возраст оставить прежним.  
Для этого нам понадобится отдельная модель, где все поля необязательны (Optional). Используем @app.patch.

```python 
# Модель для обновления (все поля могут быть пустыми)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

@app.patch("/users/{user_id}")
def update_user_partial(user_id: int, user_update: UserUpdate):
    """Обновляет только переданные поля"""
    for user in users_db:
        if user["id"] == user_id:
            # Если прислали имя — обновляем имя
            if user_update.name is not None:
                user["name"] = user_update.name
            # Если прислали возраст — обновляем возраст
            if user_update.age is not None:
                user["age"] = user_update.age
            return {"message": "User updated partially", "user": user}
            
    raise HTTPException(status_code=404, detail="User not found")
```

## 5️⃣ DELETE — Удаление

**Смысл:** "Удали эту запись навсегда".  
Самый простой метод. Обычно мы просто удаляем объект и сообщаем об успехе. Используем @app.delete.

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Удаляет пользователя по ID"""
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index] # Удаляем из списка
            return {"message": f"User {user_id} deleted"}
            
    raise HTTPException(status_code=404, detail="User not found")
```