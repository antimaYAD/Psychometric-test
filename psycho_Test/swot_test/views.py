from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentDetail, Question
from django.core.mail import send_mail
from .serializer import QuestionSerializer,StudentDetailSerializer
from django.conf import settings
from.utilsp import generate_swot_report_final
from rest_framework.parsers import MultiPartParser, FormParser
from . utils import send_report_email
from loguru import logger
from datetime import datetime
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
                grade=user_details['grade'],
                school_name= user_details['school_name'],
                phone=user_details['phone'],
                alt_phone=user_details['alt_phone'],
                email=user_details['email'],
                alt_email=user_details['alt_email'],
            )
            
            result = generate_swot_report_final(responses)
            
            student.save()
            
            return Response({"result":result,"student_detail":StudentDetailSerializer(student).data,"message": " You have completed the text sucessfilly"}, status=status.HTTP_200_OK)
            
        except Exception as error:
            logger.error(f"Error submitting responses: {error}")  # Log the error message
            return Response({"error": "An error occurred while submitting responses."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
class DwonloadreportView(APIView):
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # Extract file and student email from the request data
        student_email = request.data['student_email']
        pdf_file = request.FILES['pdf_file_path']
        print(pdf_file)
        # Validate the input
        if not pdf_file or not student_email:
            return Response(
                {"error": "PDF file and student email are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Verify if the student exists
            student = StudentDetail.objects.get(email=student_email)

            # Generate a unique filename for the PDF file
            unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"SWOT_Test_Report_{student_email}_{unique_id}.pdf"

            # Initialize the S3 client and upload the file
            s3 = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_S3_REGION_NAME
            )

            try:
                s3.upload_fileobj(
                    pdf_file,
                    settings.AWS_STORAGE_BUCKET_NAME,
                    file_name,
                    ExtraArgs={'ContentType': 'application/pdf'}
                )
            except Exception as upload_error:
                logger.error(f"Error uploading file to S3: {upload_error}")
                return Response({"error": "Failed to upload file to S3."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Construct the S3 file URL
            file_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{file_name}"

            # Save the link to the student's record
            student.pdf_link = file_url
            student.save()

            # Send an email to the student with the download link
            send_report_email(student_email, file_url)

            # Return the download link
            return Response({"download_link": file_url}, status=status.HTTP_200_OK)

        except StudentDetail.DoesNotExist:
            return Response(
                {"error": "Student with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            logger.error(f"Unexpected error: {error}")
            return Response(
                {"error": "An error occurred while processing the request."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
   
            
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
        
    def delete(self, request):
        try:
            data = request.data
            student = StudentDetail.objects.get(id=data["id"])
            
            if student.pdf_link:
            # Initialize a session using Amazon S3
                s3_client = boto3.client(
                    's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name=settings.AWS_S3_REGION_NAME
                )
                
                # Extract the file key (assuming s3_file contains the file path)
                file_key = student.pdf_link.split('/')[-1]  # Adjust this if your S3 URL structure is different
                
                # Delete the file from S3
                s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_key)
                logger.info(f"Deleted file {file_key} from S3 bucket.")
            
            # Now delete the student record from the database
                student.delete()
                logger.info(f"Deleted student record with id {data['id']}.")
                
            return Response({"message": "Student and associated file deleted successfully."}, status=status.HTTP_200_OK)

        except StudentDetail.DoesNotExist:
            logger.error(f"Student with ID {data['id']} does not exist.")
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as error:
            logger.error(f"Error occurred while deleting student or file: {error}")
            return Response({"error": "An error occurred while deleting student data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
              