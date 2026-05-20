> [!abstract] Теория
>
> 
>- **str -> int**: `int("100")` -> `100` (для математики). **Важно:** строка должна состоять только из цифр, иначе будет ошибка! ⚠️
>     
>- **str -> list**: `list("abc")` -> `['a', 'b', 'c']` (разбивка на символы).
>  
>   Методы:
> - **upper()** - поднимает все символы до верхнего регистра
>   ```python
>my_str = 'hello world'
>uppercase_my_str = my_str.upper()
>print(uppecase_my_str) # HELLO WORLD
>
> - **strip()** - возвращает новую строку без указанных начальных и конечных символов. Если аргумент не указан, удаляются начальные и конечные пробелы.
>```python
my_str = "   hello world   "
trimmed_my_str = my_str.strip()
print(trimmed_my_str) # "hello world"
>```
>
> - **replace()** - - `replace(old, new)`: возвращает новую строку, в которой все вхождения `old` заменены на `new`. 
>```python
my_str = "Hello World"
replaced_my_str = my_str.replace('hello', 'hi)
print(replaced_my_str) # hi World
>```
>
>
>
>
> - **split()** - `split(separator)`: разбивает строку по указанному разделителю на список строк. Если разделитель не указан, строка разбивается по пробелам.
>```python
my_str = 'hello world'
>
>split_words = my_str.split()
>print(split_words)  # ['hello', 'world']
>```
> - **join()** - - `join(iterable)`: объединяет элементы итерируемого объекта в строку с разделителем.
> ```python
>my_list = ['hello', 'world']
>
>joined_my_str = ' '.join(my_list)
>print(joined_my_str)  # hello world
>```
> - **count()** - `count(substring)`: возвращает количество вхождений подстроки в строку.
> ```python
>my_str = 'hello world'
>
o_count = my_str.count('o')
print(o_count)  # 2
>```
> - isupper() - проверяет все ли символы  в верхнем регистре
>-  **ord()** — перевод из текста в цифру.
>    
>- **chr()** — перевод из цифры в текст.
  >  
>- **Заглавные:** 65–90.
>    
>- **Строчные:** 97–122.
  >  
>- **Важно:** Символ `'5'` и число `5` — это разные вещи. `ord('5')` — это 53, а не 5.