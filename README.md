### Rest API of IMBD clone
---
1. Steps to run in your system
	* git clone 
	* create vitual environment
	```python
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver
	```
2.[open the url](http://127.0.0.1:8000/admin)
	* add some dummy details to api in admin panel


3.URLs which I used in project

[movie-list](http://127.0.0.1:8000/list/) **get, post methods** using viewsets.ModelViewSet

```python

[
    {
        "id": 1,
        "title": "Pushpa",
        "description": "Sukumar",
        "active": true,
        "created": "2022-02-05T11:16:18.756975Z",
        "platform": 2
    },
    {
        "id": 2,
        "title": "RRR",
        "description": "Raju",
        "active": true,
        "created": "2022-02-05T11:16:43.817626Z",
        "platform": 1
    },
    {
        "id": 3,
        "title": "Republic",
        "description": "Deva",
        "active": true,
        "created": "2022-02-05T11:23:47.247753Z",
        "platform": 3
    },
    {
        "id": 4,
        "title": "Pelli",
        "description": "Deva",
        "active": true,
        "created": "2022-02-05T11:39:52.085114Z",
        "platform": 3
    }
]
```

	
[movie-details](http://127.0.0.1:8000/<int:pk>/) **get, put and delete methods** function based views
```javascript
{
    "id": 2,
    "title": "RRR",
    "description": "Raju",
    "active": true,
    "created": "2022-02-05T11:16:43.817626Z",
    "platform": 1
}
```
	
[streamplatform](http://127.0.0.1:8000/stream) **retrive, list and post methods** using viewsets.ModelViewSet
```python

[
    {
        "id": 1,
        "watchedlist": [
            {
                "id": 2,
                "title": "RRR",
                "description": "Raju",
                "active": true,
                "created": "2022-02-05T11:16:43.817626Z",
                "platform": 1
            }
        ],
        "name": "Netflex",
        "about": "Highh Budget",
        "website": "http://Netflex.com"
    },
    {
        "id": 2,
        "watchedlist": [
            {
                "id": 1,
                "title": "Pushpa",
                "description": "Sukumar",
                "active": true,
                "created": "2022-02-05T11:16:18.756975Z",
                "platform": 2
            }
        ],
        "name": "Amazon",
        "about": "Average budget",
        "website": "http://amazon.com"
    },
    {
        "id": 3,
        "watchedlist": [
            {
                "id": 3,
                "title": "Republic",
                "description": "Deva",
                "active": true,
                "created": "2022-02-05T11:23:47.247753Z",
                "platform": 3
            },
            {
                "id": 4,
                "title": "Pelli",
                "description": "Deva",
                "active": true,
                "created": "2022-02-05T11:39:52.085114Z",
                "platform": 3
            }
        ],
        "name": "zee2.0",
        "about": "lowbudget",
        "website": "http://zee.com"
    },
    {
        "id": 4,
        "watchedlist": [],
        "name": "Disney",
        "about": "Nice for kids",
        "website": "http://desney.com"
    },
    {
        "id": 6,
        "watchedlist": [],
        "name": "Hotstar",
        "about": "IPL",
        "website": "http://hotstar.com"
    }
]
```
	
[review-create](http://127.0.0.1:8000/stream/<int:pk>/review-create) **post method** to perform create review using generics CreateAPIView

[review-list](http://127.0.0.1:8000/stream/<int:pk>/review) **get method** to get reviews using generics List view
```python
[
    {
        "id": 1,
        "review_user": "naveen",
        "rating": 8,
        "description": "Sukumar catched pulse",
        "active": true,
        "created": "2022-02-06T03:10:09.127630Z",
        "update": "2022-02-06T03:10:09.127630Z"
    },
    {
        "id": 3,
        "review_user": null,
        "rating": 5,
        "description": "Netflix platform is amazing",
        "active": true,
        "created": "2022-03-18T01:23:51.636312Z",
        "update": "2022-03-18T01:23:51.636312Z"
    }
]
```

[review-detail](http://127.0.0.1:8000/stream/review/<int:pk>) **Retrive UPdate Destroy APIview** using generics
```python
 {
        "id": 3,
        "review_user": null,
        "rating": 5,
        "description": "Netflix platform is amazing",
        "active": true,
        "created": "2022-03-18T01:23:51.636312Z",
        "update": "2022-03-18T01:23:51.636312Z"
    }
```

4.you can extend this project By completing front end to It 

5.Connect with me on LinkedIN 
[Naveen](https://www.linkedin.com/in/naveen-vp-541300154/)
