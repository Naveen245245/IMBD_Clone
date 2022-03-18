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
	
[movie-details](http://127.0.0.1:8000/<int:pk>/) **get, put and delete methods** function based views
	
[streamplatform](http://127.0.0.1:8000/stream) **retrive, list and post methods** using viewsets.ModelViewSet
	
[review-create](http://127.0.0.1:8000/stream/<int:pk>/review-create) **post method** to perform create review using generics CreateAPIView

[review-list](http://127.0.0.1:8000/stream/<int:pk>/review) **get method** to get reviews using generics List view

[review-detail](http://127.0.0.1:8000/stream/review/<int:pk>) **Retrive UPdate Destroy APIview** using generics

4.you can extend this project By completing front end to It 

5.Connect with me on LinkedIN 
[Naveen](https://www.linkedin.com/in/naveen-vp-541300154/)
