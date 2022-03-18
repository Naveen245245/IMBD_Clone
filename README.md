# IMBD_Clone
Rest API of IMBD clone

URLS for rest API of IMBD clone project:
--------------------------------------------------------
admin/
list/ [name='movie-list']
<int:pk> [name='movie_details']
^stream/$ [name='streamplatform-list']
^stream\.(?P<format>[a-z0-9]+)/?$ [name='streamplatform-list']
^stream/(?P<pk>[^/.]+)/$ [name='streamplatform-detail']
^stream/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='streamplatform-detail']
^$ [name='api-root']
^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
stream/<int:pk>/review-create [name='review-create']
stream/<int:pk>/review [name='review-list']
stream/review/<int:pk> [name='review-detail']
