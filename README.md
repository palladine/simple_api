# simple_api
(Python / Django)

Запросы к api - **/api**

Реализованы три метода:
 - **getbooks** (список книг)
 - **getauthors** (список авторов)
 - **getbookinfo** (информация о книги)
 

 
#### **/getbooks**
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
         "year": 1987  
       },  
       {  
         "id": 2,  
         "name": "Преступление и наказание",  
         "author": "Достоевский Ф.М.",  
         "year": 1996  
       },  
       {  
         "id": 3,  
         "name": "Война и мир",  
         "author": "Толстой Л.Н.",  
         "year": 1992  
       }  
  ],  
}  
```




 