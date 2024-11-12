# insert_questions.py
import os
import django


from swot_test.models import Question  # Import the model

# Define the data as a list of dictionaries with all 19 questions
question_data = [
    {
        "question_text": "Picture yourself in a scenario where you need to calculate percentages and estimate costs in your head quickly. How confident do you feel in your ability to make quick calculations?",
        "option_a": "I feel confident in my ability to handle numbers and quickly calculate percentages and estimate costs.",
        "option_b": "I'm not particularly confident in my ability to handle math.",
        "attribute": "Data and Numbers",
    },
    {
        "question_text": "Imagine, you're at a networking event, and someone starts discussing investment avenues and market trends. How interested are you to join the conversation and learn more?",
        "option_a": "I'm interested to join the conversation, give my own inputs and learn more about investment strategies and market trends.",
        "option_b": "I'm not particularly interested in joining the conversation.",
        "attribute": "Data and Numbers,Mathematics",
    },
    {
        "question_text": "You're participating in a group discussion where you need to present your ideas. How confident are you in your communication skills to express yourself effectively?",
        "option_a": "I express myself freely and feel good about talking with others.",
        "option_b": "Public speaking and speaking my heart makes me nervous and anxious.",
        "attribute": "Communication Skills",
    },
    {
        "question_text": "You're involved in selling a product where you need to convince others to buy it. How skilled do you feel in convincing people?",
        "option_a": "I can come up with new innovative ideas and strategies to convince people.",
        "option_b": "I don't think I would be comfortable or impactful when it comes to convincing people.",
        "attribute": "Communication Skills",
    },
    {
        "question_text": "You're leading a team on a project and need to delegate tasks effectively. How confident are you in your ability to manage and guide others?",
        "option_a": "I am sure about my ability to manage and guide others effectively.",
        "option_b": "I am not entirely confident in my ability to lead and delegate tasks.",
        "attribute": "Leadership Skills,Data and Numbers",
    },
    {
        "question_text": "How interested are you in exploring Marketing, Finance, HR, Operations, and business as a whole?",
        "option_a": "Want to explore business as a whole.",
        "option_b": "Not really thought into it. Business does not interest me.",
        "attribute": "Leadership Skills,Data and Numbers",
    },
    {
        "question_text": "Do you like reading and enjoy studying theory subjects?",
        "option_a": "Yes, I like reading, and it helps me understand the subject properly.",
        "option_b": "No, I prefer practical experiences.",
        "attribute": "Reading and Theory",
    },
    {
        "question_text": "Overall, are you interested in knowing more about current affairs and politics by reading newspapers?",
        "option_a": "Yes, I like to be updated about current affairs.",
        "option_b": "Not really; none of the above interests me.",
        "attribute": "Reading and Theory",
    },
    {
        "question_text": "Do you consider yourself an avid traveler and not being homesick?",
        "option_a": "Yes, I enjoy travelling, and it helps me get my mind off everything.",
        "option_b": "I like travelling while making sure it's not that frequent.",
        "attribute": "Tech Savvy",
    },
    {
        "question_text": "Do you consider yourself a very helpful person who likes to do good to others, resolve their problems, and be involved in NGO activities?",
        "option_a": "Yes, I love helping people out. Money does not really change anything for me, and I like getting involved in NGO activities.",
        "option_b": "I am highly ambitious but also kind at heart while prioritizing my financial situation more.",
        "attribute": "Empathetic",
    },
    {
        "question_text": "Do you enjoy studying biology and finding out how living organisms work, from genes to the human body?",
        "option_a": "Yes, I love studying biology and understanding how living organisms function, starting from genes to the other intricacies of the human body.",
        "option_b": "Not really. Biology is complex, and it puzzles me.",
        "attribute": "Biology,Empathetic",
    },
    {
        "question_text": "You're trying to understand how a complicated machine works by taking it apart and finding new ways to fix it. How excited are you to learn more about physics and technology?",
        "option_a": "I am excited to understand the mysteries behind the forces of nature and the possibilities brought about by Technology.",
        "option_b": "No, Physics and Technology are not really my field.",
        "attribute": "Tech Savvy",
    },
    {
        "question_text": "Are you interested in researching and digging deeper into subjects of your interest through reading or using search engines such as Google, reading articles, or watching videos on platforms like YouTube?",
        "option_a": "Yes, I have the habit of researching and diving deep into any topics of my interest.",
        "option_b": "Not really. I get confused when I see too much information in one place.",
        "attribute": "Research Oriented",
    },
    {
        "question_text": "You're in chemistry class, studying chemical formulas. Do you find it fascinating and enjoy learning how these formulas are used to make medicines?",
        "option_a": "Yes, I find chemistry fascinating, especially learning about chemical formulas and reactions that are used to make medicines.",
        "option_b": "Chemistry isn't really my thing.",
        "attribute": "Chemistry,Research Oriented",
    },
    {
        "question_text": "Are you passionate about culinary arts, and how motivated are you to continuously improve your cooking techniques and create memorable dining experiences for others?",
        "option_a": "Cooking is my passion, and I'm always looking for ways to improve my dishes!",
        "option_b": "I like to eat and am not really into cooking.",
        "attribute": "Creative,Artistic",
    },
    {
        "question_text": "You're looking at new ideas in art and design, trying to draw things that inspire you. How excited are you to unleash your creativity?",
        "option_a": "I'm thrilled to explore new ideas and let my creativity flow by creating innovative designs.",
        "option_b": "I usually prefer readymade ideas and cannot think creatively.",
        "attribute": "Artistic",
    },
    {
        "question_text": "Are you interested in knowing and working in the field of sports, fitness, food, and exercise?",
        "option_a": "Yes, I can see myself working in this field.",
        "option_b": "I would be interested to know about this only for general knowledge. I do not wish to pursue a career field relating to the same.",
        "attribute": "Sport",
    },
    {
        "question_text": "Are you interested in working in the film industry as a director, editor, actor, or screenwriter? Do you think you have the creative mind to work in the movies?",
        "option_a": "Yes, I am a great storyteller, and I like watching movies. I would like to know more about it.",
        "option_b": "No, Not at all. I don’t possess enough creativity to be a part of the film industry.",
        "attribute": "Creative",
    },
    {
        "question_text": "What level of interest do you have in experiencing new places, serving guests in hotels, and immersing yourself in different cultures?",
        "option_a": "I'm itching to travel, serve guests, and soak in new cultures!",
        "option_b": "Exploring new places and serving guests isn't my cup of tea.",
        "attribute": "Empathetic,Hospitality",
    },
]

# Insert each question into the database
for entry in question_data:
   Question.objects.create(**entry)


print("All questions inserted successfully.")




from swot_test.models import StrengthWeakness  # Replace 'your_app_name' with your actual app name

entries = [
    {
        "attribute": "Data and Numbers",
        "at_strength": "Being good with data and numbers helps you analyze information effectively, make informed decisions, and solve complex problems.",
        "at_weakness": "You feel unsure while making calculations and not on your feet. You tend to struggle with quantitative concepts.",
        "profile": "The candidate's main interest appears to be in activities that involve data analysis and numbers. They excel in tasks requiring precise calculations and meticulous attention to detail, enjoying the challenge of solving complex problems with accuracy."
    },
    {
        "attribute": "Communication Skills",
        "at_strength": "Having strong communication skills allows you to interact effectively with peers, teachers, and professionals. You can present ideas clearly, collaborate efficiently, and resolve conflicts.",
        "at_weakness": "You experience the need to overexplain, difficulty expressing your thoughts, and limited participation in group activities.",
        "profile": "Their strong communication skills enable them to clearly articulate complex information, making them effective in collaborative environments and public discussions. They are confident in expressing their ideas and facilitating productive conversations."
    },
    {
        "attribute": "Creative",
        "at_strength": "Being creative sparks innovation, problem-solving, and thinking outside the box. This leads to unique solutions and approaches to challenges.",
        "at_weakness": "You may experience rigid thinking, difficulty adapting to new situations, and limited ability to generate novel ideas.",
        "profile": "Their creativity shines through in tasks that allow them to express themselves by conceiving and designing innovative ideas. They are likely inclined towards artistic and imaginative activities, finding joy in creating unique and original concepts."
    },
    {
        "attribute": "Leadership Skills",
        "at_strength": "Possessing leadership skills enables you to inspire and motivate others, take initiative, and organize group tasks or projects effectively.",
        "at_weakness": "You might struggle with leading a group in an organization, sometimes encounter conflicts within group settings, and find decision-making challenging.",
        "profile": "Leadership is another prominent strength, indicating confidence in managing and guiding others towards achieving common goals. They are adept at delegating tasks, providing direction, and motivating team members to reach their full potential."
    },
    {
        "attribute": "Tech Savvy",
        "at_strength": "Tech-savvy means mastering the computer and its use, as well as new software or tools, among other things. They refine work output, problem-solving, and flexibility to work in various technology settings.",
        "at_weakness": "Due to heavy reliance on technology, you might face challenges such as losing fundamental skills or being disoriented by frequent technological changes.",
        "profile": "The candidate demonstrates a high level of empathy, showing genuine concern for others and the ability to understand and address diverse perspectives and needs. They excel in building strong relationships and providing support to those around them."
    },
    {
        "attribute": "Reading and Theory",
        "at_strength": "Your mastery of reading and theory enhances your understanding of complex texts, arguments, and abstract concepts, which is essential for academic research and critical analysis.",
        "at_weakness": "You feel impatient when reading long texts, and after some time, it gets boring.",
        "profile": "They enjoy reading and studying theoretical subjects, which helps them grasp complex concepts deeply and thoroughly. Their preference for in-depth learning supports a strong foundational knowledge and a comprehensive understanding of their interests."
    },
    {
        "attribute": "Empathetic",
        "at_strength": "Empathy fosters strong interpersonal relationships, understanding of diverse perspectives, and offering support to peers in need.",
        "at_weakness": "You experience misunderstandings and can't relate to others' feelings.",
        "profile": "The candidate demonstrates a high level of empathy, showing genuine concern for others and the ability to understand and address diverse perspectives and needs. They excel in building strong relationships and providing support to those around them."
    },
    {
        "attribute": "Chemistry",
        "at_strength": "Learning chemistry helps one comprehend the different matters that make up the compounds, which possess definite properties and the different changes that can occur to alter these properties. It is essential to the careers of associated areas such as pharmaceuticals, environmental science, and material engineering.",
        "at_weakness": "You may have a problem understanding some reactions and equations in chemistry, some new techniques in the lab, or safety measures to be taken.",
        "profile": "They find chemistry fascinating, particularly in understanding chemical reactions and processes, and how these can be applied to create various products and medicines. They appreciate the role of chemistry in solving real-world problems."
    },
    {
        "attribute": "Research Oriented",
        "at_strength": "Having a research-oriented mindset encourages curiosity, critical thinking, and the ability to find credible sources of information.",
        "at_weakness": "You may struggle with finding credible information and organizing data effectively.",
        "profile": "With a strong inclination towards research-oriented activities, they enjoy diving deep into subjects, conducting thorough investigations, and uncovering new insights and knowledge. Their curiosity drives them to explore and understand complex topics."
    },
    {
        "attribute": "Biology",
        "at_strength": "Understanding biology facilitates comprehension of living organisms, ecosystems, and biological processes. It's foundational for various fields, such as medicine, environmental science, and biotechnology.",
        "at_weakness": "You might struggle to understand fundamental principles, apply knowledge to real-world scenarios, and pursue related careers.",
        "profile": "They have a keen interest in studying living organisms, understanding biological processes from genetic functions to complex systems, and exploring the intricacies of life. They are fascinated by the mechanisms that drive biological diversity and health."
    },
    {
        "attribute": "Artistic",
        "at_strength": "You are able to think creatively, visualize ideas, and express emotions or concepts in unique and attractive ways.",
        "at_weakness": "You may struggle to think outside the box or come up with imaginative ideas and solutions.",
        "profile": "They love expressing themselves through various forms of art. High creative and imaginative skills. Artistic people love drawing, painting, and creating new things, developing innovative solutions and approaches to artistic challenges, whether in concept development, execution, or presentation."
    },
    {
        "attribute": "Mathematic",
        "at_strength": "You have a strong aptitude for understanding mathematical concepts, enabling you to solve problems efficiently, recognize patterns, and think logically.",
        "at_weakness": "You may feel overwhelmed by complex mathematical concepts and struggle with advanced topics.",
        "profile": "The candidate shows a strong proficiency in mathematics, demonstrating an ability to analyze quantitative data and apply mathematical reasoning. They find enjoyment in mathematical challenges and likely seek opportunities to further develop their skills in this area."
    },
    {
        "attribute": "Hospitality",
        "at_strength": "You excel in creating a welcoming and comfortable environment for others, showing empathy and attentiveness to their needs.",
        "at_weakness": "You may feel overwhelmed in high-stress environments, or find it challenging to stay patient and focused with difficult clients.",
        "profile": "The candidate demonstrates a natural inclination toward hospitality, finding satisfaction in serving others and creating positive experiences. They are likely skilled at managing interactions, addressing individual needs, and building rapport with clients or guests."
    },
    {
        "attribute": "Sport",
        "at_strength": "You have a strong sense of discipline, physical agility, and teamwork, enabling you to perform well in sports and physical activities.",
        "at_weakness": "You may struggle with maintaining motivation for regular training, or find high-pressure situations stressful.",
        "profile": "The candidate has a passion for sports and physical activities, demonstrating commitment, teamwork, and resilience in competitive environments. They find fulfillment in setting and achieving athletic goals, and are motivated by challenges that test their physical abilities and perseverance."
    }
]

for entry in entries:
    StrengthWeakness.objects.create(**entry)
    
    
    
from swot_test.models import CareerFields

# Data to insert
fields_data = [
    {
        'field_name': 'Finance',
        'description': 'Finance is an area of economic activity related to the use and provision of capital and funds, as an organization or an individual acquires, allocates, invests, and manages money. Professionals in finance are spread across all types of occupations, including banking, investment or corporate finance, and financial planning. The field involves having analytical capabilities, understanding, and focusing on the details and legal and regulatory compliance issues related to financial instruments.',
        'opportunity': 'Advances in financial technology, such as blockchain and AI, are transforming financial services, offering more efficient and accessible solutions. Increasing globalization provides opportunities for financial professionals to engage with diverse markets and investment opportunities.',
        'threat': 'Frequent changes in financial regulations, continuous adaptation, market uncertainty.',
        'example1': 'By setting aside a portion of your allowance or income, you will learn about the importance of savings, budgeting, setting financial goals.',
        'example2': 'The fund manager of a mutual fund company allocating the amount invested by investors to various financial instruments such as the stock market, debt instruments such as bonds, real estate etc, making sure that he/she gives maximum returns to investors.',
        'strength_weakness': 'Data and Numbers'
    },
    {
        'field_name': 'Finance/Economics',
        'description': 'Finance is the dynamic industry where you can manage money and everything related to money, i.e. investments, bonds, and risks, to optimise your overall wealth growth. Economics plays a very important role within societies, delving into market dynamics, policy impacts, and global economic systems. Both disciplines are pillars of modern commerce, influencing business strategies, governmental policies, and individual financial decisions. Professionals in these fields shape the economic landscape, steering toward stability, growth, and prosperity.',
        'opportunity': 'Opportunities to work in international finance and investment, leveraging diverse markets and opportunities. Access to innovative financial tools and platforms for analysis, trading, and investment. Increasing need for financial advisors, analysts, and consultants.',
        'threat': 'Market fluctuations, financial crises, regulatory compliance, risk of job loss due to automation.',
        'example1': 'Saving money in a piggy bank or opening a savings account at a bank represents basic financial principles.',
        'example2': 'By setting aside a portion of your allowance or income, you will learn about the importance of savings, budgeting, setting financial goals, and future savings for needs such as buying a toy or saving for college.',
        'strength_weakness': 'Mathematic'
    },
    {
        'field_name': 'Marketing/English Literature/Journalism',
        'description': 'Marketing is creativity + strategy aimed at attracting the audience\'s attention and driving consumer behavior. Drawing from disciplines like English Literature and Journalism, marketers craft compelling narratives, engaging content, and persuasive campaigns to connect products or services with consumers\' desires and aspirations. English Literature helps marketing with its access to human emotions and storytelling techniques. Together, they form a mix that shapes brand identities, influences public perceptions, and drives business success in an ever-evolving marketplace.',
        'opportunity': 'Opportunities to work in digital marketing, content creation, and storytelling. Growing demand for brand managers and strategists. Leveraging data-driven insights to optimize marketing campaigns.',
        'threat': 'High competition in the digital landscape, disruption of traditional media, maintaining credibility in journalism.',
        'example1': 'Reading product reviews or watching advertisements on social media platforms.',
        'example2': 'Whether deciding on a new phone, a book to read, or a movie to watch, individuals are exposed to persuasive messaging and storytelling techniques.',
        'strength_weakness': 'Communication Skills'
    },
    {
        'field_name': 'Business Management',
        'description': 'Business Management is the art and science of managing resources, people, and processes to achieve organizational goals effectively and efficiently. It contains a broad spectrum of functions, including strategic planning, operations management, human resource management, and financial oversight. With a focus on leadership, innovation, and adaptability, business managers work through different complexities to drive growth within their organizations.',
        'opportunity': 'Opportunities to start and scale businesses, demand for business consultants, multinational expansion opportunities.',
        'threat': 'Fluctuating market conditions, competition for skilled professionals, disruption from startups.',
        'example1': 'Planning a family outing or organizing a school event.',
        'example2': 'Assigning roles for a group project or creating a budget for a trip.',
        'strength_weakness': 'Leadership Skills'
    },
    {
        'field_name': 'Law, Political Science, Civil Services',
        'description': 'Law, Political Science, and Civil Services are interconnected fields that shape governance and justice while safeguarding democratic principles. The law governs society by establishing rights, obligations, and legal frameworks, ensuring order and fairness. Political Science analyses power dynamics, institutions, and policies. Civil services are the administrative backbone of governments, responsible for implementing policies, delivering public services, and promoting the welfare of citizens.',
        'opportunity': 'Opportunities to serve in government agencies, demand for specialized legal expertise, work as lobbyists or advocates influencing policy.',
        'threat': 'Political uncertainty, disruptive legal tech solutions, public trust challenges.',
        'example1': 'Participating in a student council election or resolving a conflict among friends demonstrates the application of legal and political principles in everyday life.',
        'example2': 'By electing representatives, debating issues, and enforcing rules, individuals engage in democratic processes, governance structures, and conflict-resolution mechanisms.',
        'strength_weakness': 'Reading and Theory'
    },
    {
        'field_name': 'Pilot/Merchant Navy',
        'description': 'Pilots and Merchant Navy professionals are the unsung heroes of global transportation, navigating skies and seas to ensure the safe and efficient movement of people and goods. Pilots command aircraft with precision, skill, and expertise, guiding passengers to their destinations across continents and cultures. Merchant Navy officers oversee the operation and navigation of commercial vessels, navigating vast oceans and intricate waterways to deliver essential commodities and sustain global trade. With a commitment to safety and professionalism, these professionals overcome challenges, weather storms, and bridge distances, helping to connect the world.',
        'opportunity': 'Explore different cultures and destinations, access to advanced navigation systems, career advancements in aviation and maritime industries.',
        'threat': 'Potential automation reducing demand, adaptation to new technologies.',
        'example1': 'Planning a road trip or coordinating vacation travel arrangements.',
        'example2': 'From mapping out routes and scheduling stops to ensuring vehicle maintenance and safety protocols.',
        'strength_weakness': 'Tech Savvy'
    },
    {
        'field_name': 'Doctor and other paramedical fields',
        'description': 'Doctors and psychologists are dedicated to healing, understanding, and enhancing human health and well-being. Doctors diagnose and treat physical ailments to alleviate suffering and promote preventive care to improve longevity and quality of life. With empathy, expertise, and scientific rigor, professionals in these fields empower individuals to overcome adversity, achieve holistic wellness, and lead fulfilling lives, bridging the gap between body and mind to cultivate health and happiness.',
        'opportunity': 'Expansion of telehealth, mental health recognition, medical research and public health innovation.',
        'threat': 'Healthcare inequities, high stress and burnout, evolving regulations impacting practice.',
        'example1': 'Offering emotional support to a friend or practicing self-care during stressful times reflects basic principles of psychology and healthcare.',
        'example2': 'Suggesting medicines at home in emergency situations.',
        'strength_weakness': 'Empathetic, Biology'
    },
    

    {
        'field_name': 'Psychology',
        'description': 'Psychology can be defined as the scientific discipline that focuses on the human mind and its functions and activities. It covers a vast area of interest in students, including but not limited to cognition, affective processes, growth and development, individual differences, and interpersonal relationships. It seeks to define how people practically experience the world, not only in relation to ideas but also feelings and actions, as well as the psychology behind these donations. Clinical and social Psychologists employ research techniques like experiments, questionnaires, and observations in order to generate hypotheses relevant to peoples behavior.',
        'opportunity': 'Expansion of teletherapy and digital mental health platforms, advancements in research and neuroscience.',
        'threat': 'Stigma and barriers to accessing mental health services, limited intervention reach.',
        'example1': 'Understanding the reasons behind anxiety and using deep breathing and mindfulness techniques to reduce stress is an everyday application of psychology in daily life.',
        'example2': 'In counseling, psychologists use cognitive-behavioral techniques to help clients overcome challenges like depression or anxiety, enabling them to lead more fulfilling professional lives.',
        'strength_weakness': 'Reading and Theory, Empathetic'
    },
    {
        'field_name': 'Pharmacy/Biochemistry',
        'description': 'Pharmacy and Biotechnology remain at the forefront of healthcare innovation, bringing new discoveries, developing and delivering life-saving medicines and therapies, and playing a vital role in patient care and public health. A biotechnologist basically deals with research and development regarding living organisms, cells, and biological systems to develop treatments, diagnostic tools, and sustainable solutions to global outbreaks.',
        'opportunity': 'Work in pharmaceutical companies, personalized medicine, and biotech startups.',
        'threat': 'Regulatory challenges, clinical trials, patent disputes, high development costs.',
        'example1': 'Taking medications or using natural remedies for common ailments illustrates the practical applications of pharmacy and biotechnology in everyday life.',
        'example2': 'Pharmacists counseling patients on medication management, including proper dosage and potential side effects, highlights the practical application of pharmacy in ensuring effective and safe treatment plans.',
        'strength_weakness': 'Chemistry, Research Oriented'
    },
    {
        'field_name': 'Biotechnology/Biological Sciences',
        'description': 'Biotechnology mostly revolves around the molecular mechanisms of cells and the ecological dynamics of ecosystems. Living organisms, genetic engineering, and biochemical processes to develop novel products, treatments, and technologies with applications ranging from medicine and agriculture to environmental remediation and industrial manufacturing. Biological scientists explore the diversity, evolution, and interconnectedness of life forms, shedding light on fundamental questions about existence, adaptation, and sustainability. With curiosity, innovation, and interdisciplinary collaboration, these disciplines pave the way for groundbreaking discoveries and transformative solutions to global challenges.',
        'opportunity': 'Develop biodegradable materials, renewable energy, conservation and biodiversity efforts.',
        'threat': 'Potential ecological impacts of biotechnology applications, gene flow, ecosystem disruption.',
        'example1': 'By cultivating plants, observing ecosystems, and recycling organic materials, individuals engage in hands-on learning experiences that foster an appreciation for biodiversity and ecological processes.',
        'example2': 'Using genetically modified crops to improve yield and resistance to pests is a practical application of biotechnology, demonstrating its impact on agriculture and food security.',
        'strength_weakness': 'Biology, Research Oriented'
    },
    {
        'field_name': 'Hotel Management',
        'description': 'Hotel Management is the art and science of handling hospitality chores, starting from luxurious accommodations to memorable dining experiences and impressive guest service. It encompasses a diverse array of functions, including operations management, revenue optimization, guest relations, and culinary arts. With a focus on customer satisfaction, operational excellence, and innovation, hotel managers create welcoming environments, personalized services, and unforgettable moments that delight guests and foster loyalty.',
        'opportunity': 'Growth in international travel and tourism, adoption of technology for personalized guest experiences.',
        'threat': 'Competition among hotels and booking platforms, customer loyalty challenges.',
        'example1': 'Planning a family vacation or booking accommodations for a business trip.',
        'example2': 'From researching hotels and amenities to making reservations and checking in/out, individuals experience firsthand the guest-centric approach, efficiency, and professionalism expected in the hospitality industry.',
        'strength_weakness': 'Hospitality'
    },
    {
        'field_name': 'Culinary Arts',
        'description': 'Culinary Arts converge to create extraordinary dining experiences and elevate hospitality standards to new heights. Culinary artists master the art of cooking, blending flavors, and creating visually stunning dishes that tantalize the senses and evoke emotions. They craft culinary journeys that delight guests, celebrate local flavors, and showcase culinary creativity and innovation. Through passion, craftsmanship, and a dedication to excellence, they transform meals into memories and hotels into culinary destinations.',
        'opportunity': 'Culinary tourism and innovative dining experiences, catering to multicultural preferences.',
        'threat': 'Labor shortages impacting service quality, operational efficiency.',
        'example1': 'You have a passion for cooking and like experimenting with different objects and ingredients when creating new recipes.',
        'example2': 'Learning how to bake different types of bread and cakes, experimenting with unique flavor combinations and decoration styles, reflects the creativity and precision in culinary arts.',
        'strength_weakness': 'NULL'
    },
    {
        'field_name': 'Design',
        'description': 'Design as a field includes various disciplines, such as Communication, Product, and Fashion design, which shape our visual culture and immersive experiences. Designers craft visual identities, products, and environments that resonate with audiences, blending aesthetics, functionality, and user experience to evoke emotions and convey messages. Designers push the boundaries of creativity, innovation, and expression, enriching our lives with beauty, meaning, and inspiration.',
        'opportunity': 'Emerging technologies enabling innovative storytelling, global distribution via streaming platforms.',
        'threat': 'High competition due to content volume, difficult recognition for new creators.',
        'example1': 'Branding and Packaging, Interior design, Website Designing, Fashion Designing.',
        'example2': 'Creating a visual identity for a new brand, developing engaging multimedia content for advertisements, or crafting an innovative set design for a short film.',
        'strength_weakness': 'Artistic'
    },
    {
        'field_name': 'Architecture',
        'description': 'Architecture is the art and science of designing shelters and spaces that inspire and enrich human living. Architects blend creativity, technical expertise, and environmental stewardship to conceive and realize built environments that harmonize with their surroundings, meet human needs, and reflect cultural values. From iconic skyscrapers to sustainable communities, architectural marvels shape our cities.',
        'opportunity': 'Sustainable materials and green building techniques, integration of technology in architecture.',
        'threat': 'Economic downturns impacting construction projects and financial stability.',
        'example1': 'Taj Mahal, Antilia.',
        'example2': 'Skyscraper.',
        'strength_weakness': 'Artistic, Data and Number'
    },
    {
        'field_name': 'Dietetics and Nutrition, Sports Science, Sports Management',
        'description': 'The intersection of Dietetics and Nutrition, Sports Science, and Sports Management forms a comprehensive field focused on optimizing athletic performance through tailored nutrition plans, evidence-based training techniques, and effective management strategies for athletes, teams, and sporting organizations.',
        'opportunity': 'Comprehensive approach to athlete health, performance analytics, personalized nutrition plans.',
        'threat': 'Resource and budget constraints affecting comprehensive support in sports.',
        'example1': 'A coach maintains the performance of the player by going through his performance analytics.',
        'example2': 'In sports management, overseeing the logistics of organizing a major sporting event involves coordinating venue arrangements, teams, and event logistics.',
        'strength_weakness': 'Sports'
    },
    
    {
        "field_name": "Engineering",
        "description": "Engineering is a vast and diverse discipline that applies mathematics and science to develop solutions for real-life challenges across fields such as construction, machinery, and technology. Major branches include civil, mechanical, electrical, chemical, and computer engineering, all of which focus on innovation and improvement of products and systems. Engineering professionals contribute significantly to sectors like infrastructure, production, technology, and healthcare, enhancing the quality and functionality of everyday life.",
        "opportunity": "Advances in AI, robotics, and nanotechnology, along with sustainable energy system design.",
        "threat": "Rapidly evolving technology requires constant learning and adaptation.",
        "example1": "A mechanical engineer designing a new machine prototype.",
        "example2": "A civil engineer overseeing the construction of bridges and highways.",
        "strength_weakness": "Tech Savvy"
    },
    
    {
        "field_name": "Film and Cinematics",
        "description": "Film and Cinematics explores the art, history, theory, and technical aspects of filmmaking, including camera work, editing, sound, and storytelling. This field values creativity, technical skills, cultural understanding, and the power of film as a social and artistic medium. It includes roles such as cinematographer, director, producer, and scriptwriter, who work to produce compelling visual stories and advance film techniques.",
        "opportunity": "Integration of VR, AR, and AI to enhance cinematic experiences, along with expanding global streaming distribution.",
        "threat": "Intense competition driven by content saturation in the digital age.",
        "example1": "A director creating a short film using VR technology.",
        "example2": "A filmmaker experimenting with augmented reality to create immersive cinematic experiences.",
        "strength_weakness": "Creative"
    }
]


    


# Insert data into the database
for field in fields_data:
    CareerFields.objects.create(**field)

print("Data inserted successfully.")





