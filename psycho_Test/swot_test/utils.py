from .models import Question,CareerFields,StrengthWeakness





def generate_swot_report(responses):
    print(responses, "======")
    strengths = dict()
    weaknesses = dict()
    
    # results = {1:["Data and Number"],2:["Mathematic"],3:["Communi}

    for response in responses:
        print(response)
        # Fetch the question using question_id from the response
    
        question = Question.objects.get(id=response['question_id'])
        print(question)  # For debugging purposes, print the question object

        # Ensure the attribute exists and is not None
        if question and question.attribute:
            # Split the comma-separated attributes into a list and strip extra whitespace
            attributes = [attr.strip() for attr in question.attribute.split(',')]
        else:
            # If attribute is None, assign an empty list
            attributes = []

        print(attributes) 


        strength_weaknesses = StrengthWeakness.objects.filter(attribute__in=attributes)  
        print(strength_weaknesses)
        
        for strength_weakness in strength_weaknesses: 
            if response['selected_option'].lower() == 'yes':
           
                if strength_weakness.attribute not in strengths:
                    strengths[strength_weakness.attribute] = { 
                        "strength": strength_weakness.at_strength,
                        "profile_description": strength_weakness.profile
                    }
            else:
               
                if strength_weakness.attribute not in weaknesses:
                    weaknesses[strength_weakness.attribute] = {
                        "weakness": strength_weakness.at_weakness
                    }
                    
    print(strengths)
    print(weaknesses)

    # Map strengths to career fields
    career_fields = []
    strength_keys = strengths.keys()  # Get keys from strengths for easy checking

    for field in CareerFields.objects.all():
        # Split the required attributes of the career field into a list
        if not field.strength_weakness:
         continue

    # Split the required attributes of the career field into a list
        required_attributes = [attr.strip() for attr in field.strength_weakness.split(',')]
        # required_attributes = [attr.strip() for attr in field.strength_weakness.split(',')]

        # Check if all required attributes are present in strengths.keys()
        if all(attr in strength_keys for attr in required_attributes):
            # If all required attributes are present, add the career field to the list
            career_fields.append({
                'field_name': field.field_name,
                'description': field.description,
                'opportunities': field.opportunity,
                'threats': field.threat,
                'example1': field.example1,
                "example2": field.example2
            })
            
    print(career_fields)

    analysis = {
        "strengths": strengths,  # Strengths keyed by specific attributes
        "weaknesses": weaknesses,  # Weaknesses keyed by specific attributes
        "career_fields": career_fields
    }

    return analysis

