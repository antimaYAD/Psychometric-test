from django.urls import path
from .views import GetQuestionView,SubmitResponsView,DwonloadreportView,StudentDetailView # Import the class directly from views

urlpatterns = [
    path("questions/", GetQuestionView.as_view(), name="get_questions"),
    path("submitresponses/",SubmitResponsView.as_view(), name="response_result"),
    path("dwonloadreport/",DwonloadreportView.as_view(), name="dwonloadreport"),
    path("studentdetails/",StudentDetailView.as_view(), name="student_detail"),
]
