# simple_api
(Python / Django)

Запросы к api POST-методом - **/api**

Реализованы три метода:
 - **getbooks** (список книг)
 - **getauthors** (список авторов)
 - **getbookinfo** (информация о книги)
 
  
    
      
      
 
#### **Метод getbooks**
Пример запроса:  
```json  
{  
  "method": "getbooks",  
  "data": {}  
}
```

Ответ:
```json  
{  
  "status": 1,  
  "data": [  
       {  
         "id": 1,  
         "name": "Евгений Онегин",  
         "author": "Пушкин А.С.",  
       },  
       {  
         "id": 2,  
         "name": "Преступление и наказание",  
         "author": "Достоевский Ф.М.",  
       },  
       {  
         "id": 3,  
         "name": "Война и мир",  
         "author": "Толстой Л.Н.",  
       }  
  ],  
}  
```
  
    
    
#### **Метод getbookinfo**  
Пример запроса:  
```json  
{  
  "method": "getbookinfo",  
  "data": {  
        "id": [1,2]  
  }  
}
```

Ответ:  
```json  
{
  "status": 1,
  "data": [
       {
         "id": 1,
         "name": "Евгений Онегин",
         "author": "Пушкин А.С.",
         "year": 1987
       },
       {
         "id": 2,
         "name": "Преступление и наказание",
         "author": "Достоевский Ф.М.",
         "year": 1996
       }
  ],
}  
```
  
    
    
#### **Метод getauthors**  
Пример запроса:  
```json  
{  
  "method": "getautors",  
  "data": {}  
}
```
Ответ:  
```json  
{
  "status": 1,
  "data": [
       {
         "id": 1,
         "name": "Пушкин А.С."
       },
       {
         "id": 2,
         "name": "Достоевский Ф.М."
       },
       {
         "id": 3,
         "name": "Толстой Л.Н."
       }
  ],
}
```
  
    
    
#### **Ответ при ошибке в запросе**  
В ответе присутствует статус и код ошибки, например:  
```json  
{
  "status": 0,
  "code": 702,
  "error": "no such method"
}
```  


Api может расширятся добавление заголовков, новых методов и параметров методов в запросе.  

