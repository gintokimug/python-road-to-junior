fake_tasks_db = [
    {"task_name": "Task 1"},
    {"task_name": "Task 2"},
    {"task_name": "Task 3"},
    {"task_name": "Task 4"},
    {"task_name": "Task 5"},
    {"task_name": "Task 6"},
    {"task_name": "Task 7"},
    {"task_name": "Task 8"},
    {"task_name": "Task 9"},
    {"task_name": "Task 10"},
]

# @app.get("/tasks")
# async def get_tasks(limit: int = 10, offset: int = 0, keyword : str | None = None):
#     sorted_list = []
#     if keyword is None:
#         return fake_tasks_db[offset : offset + limit]
#     else:
#         for task in fake_tasks_db:
#             if keyword.lower() in task["task_name"].lower():
#                 sorted_list.append(task)
#         return sorted_list[offset : offset + limit]


from fastapi import FastAPI

# Создаём приложение FastAPI
app = FastAPI()

# --------------------------------------------------------------
# Плохой пример (так НЕ работает для путей со слешами)
# --------------------------------------------------------------
@app.get("/bad/{file_name}")
def bad_example(file_name: str):
    # Если запросить /bad/images/logo.png, то FastAPI выбросит 404,
    # потому что он ожидает ОДИН параметр до следующего слеша.
    # В этом случае URL /bad/images/logo.png воспринимается как:
    #   - file_name = "images"
    #   - а "logo.png" вообще лишнее (некуда привязать)
    return {"error": "этот эндпоинт не примет путь со слешами"}

# --------------------------------------------------------------
# Хороший пример – используем конвертер :path
# --------------------------------------------------------------
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    """
    Эндпоинт для получения пути к файлу, который может содержать слеши.

    :param file_path: строка, включающая символы '/' как часть пути.
                      Например: "images/фото/лето/logo.png"
    """
    # Для наглядности напечатаем в консоль то, что получили
    print(f"Получен путь: {file_path}")

    # Возвращаем JSON-ответ
    return {
        "сообщение": "Путь к файлу успешно принят",
        "file": file_path,
        "длина_пути": len(file_path),
        "последний_сегмент": file_path.split("/")[-1]   # показывает имя файла
    }

# --------------------------------------------------------------
# Ещё один пример – два параметра: обычный + :path
# --------------------------------------------------------------
@app.get("/storage/{storage_name}/{remaining_path:path}")
def storage_file(storage_name: str, remaining_path: str):
    """
    Показывает, как сочетать обычный параметр и путь со слешами.
    /storage/photos/2024/07/example.jpg
    -> storage_name = "photos"
    -> remaining_path = "2024/07/example.jpg"
    """
    return {
        "хранилище": storage_name,
        "оставшийся_путь": remaining_path,
        "полный_путь": f"{storage_name}/{remaining_path}"
    }