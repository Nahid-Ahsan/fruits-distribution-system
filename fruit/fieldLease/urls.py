from django.urls import path
from .views import BookFieldView, FieldList


urlpatterns = [
    path('fieldlist/', FieldList.as_view(), name='fruit-list'),
    path('book/<int:field_id>/', BookFieldView.as_view(), name='book-field'),
]




"""

{
    "farmer": 1,  
    "acres_requested": 2.5,
    "start_date": "2023-11-15",
    "end_date": "2023-12-15",
    "contact_email": "nahid@example.com",
    "contact_phone": "017234567890"
}

"""


# get : http://127.0.0.1:8000/field/fieldlist/
# post : http://127.0.0.1:8000/field/book/1/