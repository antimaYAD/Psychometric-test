from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentDetail, Question
from django.core.mail import send_mail
from .serializer import QuestionSerializer,StudentDetailSerializer
from django.conf import settings
from.utilsp import generate_swot_report_final
from loguru import logger
import json
import boto3
# from .utils import generate_pdf_report

# Create your views here.
class GetQuestionView(APIView):
    def get(self, request):
       try: 
            questions = Question.objects.all()
            serialize = QuestionSerializer(questions,many=True)
            return Response({"questions_list":serialize.data},status=status.HTTP_200_OK) 
       except Exception as error:
           logger.error(f"Error fetching questions: {error}")  # Log the error message
           return Response({"error": "An error occurred while fetching questions."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
#Submit yor responses       
class SubmitResponsView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Parse the request body
            data = request.data
            user_details = data.get('user_detail')  # Use get to avoid KeyError
            responses = data.get('responses')
            
            if not user_details or not responses:
                return Response({"error": "Incomplete data provided."}, status=status.HTTP_400_BAD_REQUEST)
            
            #Save user_detail
          
            student = StudentDetail.objects.create(
                name=user_details['name'],
                email=user_details['email'],
                phone=user_details['phone'],
                alt_phone=user_details['alt_phone']
            )
            
            result = generate_swot_report_final(responses)
            
            student.save()
            
            return Response({"result":result,"student_detail":StudentDetailSerializer(student).data,"message": " You have completed the text sucessfilly"}, status=status.HTTP_200_OK)
            
        except Exception as error:
            logger.error(f"Error submitting responses: {error}")  # Log the error message
            return Response({"error": "An error occurred while submitting responses."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
class DwonloadreportView(APIView):
    def post(self, request):
        
        # Extract the PDF file path and student email from the request data
        pdf_file_path = request.data.get('pdf_file_path')
        student_email = request.data.get('student_email')

        # Validate the input
        if not pdf_file_path or not student_email:
            return Response(
                {"error": "PDF file path and student email are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Verify if the student exists

            # Upload the file to S3
            s3 = boto3.client('s3', 
                              aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                              aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
                              region_name=settings.AWS_S3_REGION_NAME)

            file_name = pdf_file_path.split('/')[-1]  # Get the file name from the path
            s3.upload_file(pdf_file_path, settings.AWS_STORAGE_BUCKET_NAME, file_name)

            # Construct the S3 file URL
            s3_file_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file_name}'

            # Save the link to the student's record
            student = StudentDetail.objects.get(email=student_email)
            student.pdf_link = s3_file_url
            student.save()

            # Return the download link
            return Response({"download_link": s3_file_url}, status=status.HTTP_200_OK)  
        except StudentDetail.DoesNotExist:
            return Response({"error": "Student with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            logger.error(f"Error uploading report: {error}")
            return Response({"error": "An error occurred while uploading the report."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
            
class StudentDetailView(APIView):
    def get(self, request):
        try:
            student = StudentDetail.objects.all()
            serialize = StudentDetailSerializer(student,many=True)
            return Response(serialize.data, status=status.HTTP_200_OK)
        except StudentDetail.DoesNotExist:
            return Response({"error": "Student with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            logger.error(f"Error fetching student details: {error}")  # Log the error message
            return Response({"error": "An error occurred while fetching student details."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)