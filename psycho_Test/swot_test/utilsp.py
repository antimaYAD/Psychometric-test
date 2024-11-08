from .models import CareerFields, StrengthWeakness

def generate_swot_report_final(responses):
    # Dictionary mapping question IDs to strengths/weaknesses
    skill_dict = {
        1: "Data and Numbers",
        3: "Communication Skills",
        5: "Leadership Skills",
        10: "Empathetic",
        13: "Research oriented",
        16: "Artistic",
        4: "Creative",
        11: "Biology",
        12: "Tech Savvy",
        14: "Chemistry",
        7: "Reading and Theory"
    }

    # Initialize lists for strengths and weaknesses
    strengths = []
    weaknesses = []

    # List of responses (example format)
    yes_questions = [response["question_id"] for response in responses if response["selected_option"].lower() == "yes"]
    no_questions = [response["question_id"] for response in responses if response["selected_option"].lower() == "no"]
    
    print(yes_questions)
    
    # Categorize strengths and weaknesses based on the answers
    for question_id in yes_questions:
        if question_id in skill_dict:
            strengths.append(skill_dict[question_id])
    
    for question_id in no_questions:
        if question_id in skill_dict:
            weaknesses.append(skill_dict[question_id])

    # Example: Categorize career fields based on the responses
    career_fields = []

    if 2 in yes_questions:
        career_fields.append("Finance")
        
    if {1, 2}.issubset(set(yes_questions)):
        career_fields.append("Finance/Economics")
    
    if {3, 4}.issubset(set(yes_questions)):
        career_fields.append("Marketing/English Literature/Journalism")
    
    if {5, 6}.issubset(set(yes_questions)):
        career_fields.append("Business Management")
        
    if 5 in yes_questions or 6 in yes_questions:
        career_fields.append("Business Management")
    
    if {7, 8}.issubset(set(yes_questions)):
        career_fields.append("Law, Political Science, Civil Services")
    
    if 9 in yes_questions and 12 in yes_questions:
        career_fields.append("Pilot/Merchant Navy")
    
    if {10, 11}.issubset(set(yes_questions)):
        career_fields.append("Doctor and other paramedical fields")
    
    if 7 in yes_questions and 10 in yes_questions:
        career_fields.append("Psychology")
    
    if {13, 14}.issubset(set(yes_questions)):
        career_fields.append("Pharmacy/Biochemistry")
    
    if {11, 13}.issubset(set(yes_questions)):
        career_fields.append("Biotechnology/Biological Sciences")
    
    if 19 in yes_questions:
        career_fields.append("Hotel management")
    
    if 15 in yes_questions:
        career_fields.append("Culinary arts, Hotel management")
    
    if 16 in yes_questions:
        career_fields.append("Design")
    
    if 1 in yes_questions and 16 in yes_questions:
        career_fields.append("Architecture")
    
    if 17 in yes_questions:
        career_fields.append("Dietetics and Nutrition, Sports Science, Sports Management")
    
    if 12 in yes_questions:
        career_fields.append("Engineering")
    
    if 18 in yes_questions:
        career_fields.append("Film and Cinematics")
        
    if  not yes_questions :
        career_fields.append("Business Management")

    # Fetch career fields from the database
    all_careers_fields = []
    for career in career_fields:
        try:
            fields = CareerFields.objects.get(field_name=career)
            all_careers_fields.append({
                'field_name': fields.field_name,
                'description': fields.description,
                'opportunities': fields.opportunity,
                'threats': fields.threat,
                'example1': fields.example1,
                'example2': fields.example2
            })
        except CareerFields.DoesNotExist:
            print(f"Career field '{career}' not found in the database.")

    # Initialize dictionary to store strength details
    all_strengths = []
    for strength in strengths:
        strength_obj = StrengthWeakness.objects.filter(attribute=strength).first()
        if strength_obj:
            all_strengths.append({
                 "attribute": strength_obj.attribute,
                 "strength": strength_obj.at_strength,
                    "profile_description": strength_obj.profile

            })
    
    # Initialize dictionary to store weakness details
    all_weaknesses = []
    for weakness in weaknesses:
        weakness_obj = StrengthWeakness.objects.filter(attribute=weakness).first()
        if weakness_obj:
            all_weaknesses.append({
                "attribute": weakness_obj.attribute,
                "weakness": weakness_obj.at_weakness
            })

    # Prepare final SWOT report
    swot_report = {
        "strengths": all_strengths,
        "weaknesses": all_weaknesses,
        "career_fields": all_careers_fields
    }
    
    return swot_report
