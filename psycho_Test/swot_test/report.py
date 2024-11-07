from .models import Question, Student, CareerFields,

def analyze_responses_and_select_career_fields(data):
    # Extract user details from the request
    user_details = data['user_details']
    name = user_details.get('name')
    email = user_details.get('email')
    phone = user_details.get('phone')
    alt_phone = user_details.get('alt_phone')

    # Create or update the student record
    student, created = Student.objects.get_or_create(
        email=email,
        defaults={
            'name': name,
            'phone': phone,
            'alt_phone': alt_phone
        }
    )

    # Extract and process responses
    responses = data['responses']
    strengths = []
    weaknesses = []

    for response in responses:
        question_id = response['question_id']
        selected_option = response['selected_option'].lower()

        # Retrieve the question from the database
        try:
            question = Question.objects.get(id=question_id)
            if selected_option == 'yes':
                strengths.append(question.attribute)
            else:
                weaknesses.append(question.attribute)
        except Question.DoesNotExist:
            print(f"Question with ID {question_id} not found")

    # Remove duplicates
    strengths = list(set(strengths))
    weaknesses = list(set(weaknesses))

    # Map strengths to career fields
    career_fields = []
    for strength in strengths:
        fields = CareerFields.objects.filter(strengthweakeness__icontains=strength)
        for field in fields:
            if field.field_name not in [f['field_name'] for f in career_fields]:
                career_fields.append({
                    'field_name': field.field_name,
                    'description': field.descriotion,
                    'opportunities': field.oppurtunity
                })

    # Return the analysis
    analysis_result = {
        "student": {
            "name": student.name,
            "email": student.email
        },
        "analysis": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "career_fields": career_fields
        }
    }

    return analysis_result
