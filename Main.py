################# Resume Parsying System ################
#########################################################
#################    Mohamed Abdelazim   ################
#########################################################
#################      ID: 215165        ################  

import spacy  ## for natural language processing
import nltk  ## for natural language processing tasks
import re  ## for regular expressions
from pdfminer.high_level import extract_text  ## extract text from PDF documents

nltk.download('punkt')  ## Downloading resource for tokenization
nltk.download('averaged_perceptron_tagger')  ## Downloading resource for part-of-speech tagging
nltk.download('maxent_ne_chunker')  ## Downloading the 'maxent_ne_chunker' resource for named entity recognition
nltk.download('words')  ## Downloading resource for word corpus
nltk.download('stopwords')  ## Downloading resource for stop word removal

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')  ## Loading the English language model for spaCy

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)  ## Using the 'extract_text' function to extract text from a PDF document

# Extract names using Named Entity Recognition (NER)
def extract_names(txt):
    doc = nlp(txt)  ## Applying spaCy's NER model on the text
    person_names = []  ## Creating an empty list to store person names
    count = 0  ## Counter to keep track of extracted names

    for ent in doc.ents:  ## Iterating over the named entities in the document
        if ent.label_ == 'PERSON':  ## Checking if the named entity is a person
            person_names.append(ent.text)  ## Adding the person name to the list
            count += 1  ## Incrementing the counter
            if count == 2:  ## Stop extracting after the first two names
                break

    return person_names[:2]  ## Returning only the first two names

# Extract job titles using Named Entity Recognition (NER)
def extract_job_titles(txt):
    doc = nlp(txt)  ## Applying spaCy's NER model on the text
    job_titles = []  ## Creating an empty list to store job titles

    for ent in doc.ents:  ## Iterating over the named entities in the document
        if ent.label_ == 'JOB_TITLE':  ## Checking if the named entity is a job title
            job_titles.append(ent.text)  ## Adding the job title to the list

    return job_titles  ## Returning the list of job titles

# Extract phone numbers using regular expressions
def extract_phone_number(resume_text):
    phone_numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', resume_text)  ## Using regular expressions to find phone numbers
    return phone_numbers  ## Returning the list of phone numbers

# Extract emails using regular expressions
def extract_emails(resume_text):
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', resume_text)  ## Using regular expressions to find email addresses
    return emails  ## Returning the list of email addresses

# Extract skills using keyword matching
def extract_skills(input_text, requirements):
    stop_words = set(nltk.corpus.stopwords.words('english'))  ## Creating a set of stop words
    word_tokens = nltk.tokenize.word_tokenize(input_text)  ## Tokenizing the input text into words

    # Remove stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]  ## Removing stop words from the tokens

    # Remove punctuation
    filtered_tokens = [w for w in filtered_tokens if w.isalpha()]  ## Removing non-alphabetic tokens

    # Generate bigrams & trigrams
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))  ## Generating bigrams and trigrams

    # Create a set to keep results
    found_skills = set()  ## Creating an empty set to store found skills

    # Search for each token in the requirements
    for token in filtered_tokens:  ## Iterating over the filtered tokens
        if token.lower() in requirements:  ## Checking if the token matches any requirement
            found_skills.add(token)  ## Adding the skill to the set

    # Search for bigram, trigram in requirements
    for ngram in bigrams_trigrams:  ## Iterating over the generated bigrams and trigrams
        if ngram.lower() in requirements:  ## Checking if the ngram matches any requirement
            found_skills.add(ngram)  ## Adding the skill to the set

    return found_skills  ## Returning the set of found skills

# Extract years of experience using regular expressions
def extract_years_of_experience(resume_text):
    years_exp = re.findall(r'\d+ year[s]? of experience', resume_text)  ## Using regular expressions to find years of experience
    return years_exp  ## Returning the list of years of experience

if __name__ == '__main__':
    text = extract_text_from_pdf('Test.pdf')  ## Extracting text from a PDF document named 'Test.pdf'
    names = extract_names(text)  ## Extracting names from the extracted text
    phone_numbers = extract_phone_number(text)  ## Extracting phone numbers from the extracted text
    emails = extract_emails(text)  ## Extracting email addresses from the extracted text
    skills = extract_skills(text, [])  ## Extracting skills from the extracted text (empty requirements list)
    names = extract_names(text)  ## Extracting names again from the extracted text
    job_titles = extract_job_titles(text)  ## Extracting job titles from the extracted text
    years_exp = extract_years_of_experience(text)  ## Extracting years of experience from the extracted text

    if names:
        print('Name:', ' '.join(names))  ## Printing the extracted names

    if phone_numbers:
        print('Phone Numbers:', ', '.join(phone_numbers))  ## Printing the extracted phone numbers

    if emails:
        print('Emails:', ', '.join(emails))  ## Printing the extracted email addresses

    if job_titles:
        print('Job Titles:', ', '.join(job_titles))  ## Printing the extracted job titles

    if years_exp:
        print('Years of Experience:', ', '.join(years_exp))  ## Printing the extracted years of experience

#Motion GFX Skills
    main_requirements_section1 = [
        'Motion Graphics',
        'Animation',
        'Animator',
        'Adobe',
        'After Effects',
        'Adobe After Effects',
        'AE',
        'Blender',
        '3D'
    ]

# IMG GFX Skills
    main_requirements_section2 = [
        'Photoshop',
        'Adobe Photoshop',
        'PS',
        'Illustrator',
        'Visualizer',
        'Figma',
        'AI',
        'Canva',
        'Graphic Design',
        'Illustrate'
    ]
    
#Communication Skills
    side_requirements = [
        'communication skills',
        'verbal communication',
        'written communication',
        'active listening',
        'presentation skills',
        'interpersonal skills',
        'negotiation skills',
        'conflict resolution',
        'teamwork',
        'leadership',
        'empathy',
        'cultural awareness',
        'time management',
        'attention to detail',
        'customer service',
        'problem-solving',
        'decision-making',
        'adaptability',
        'creativity',
        'innovation',
        'persuasion',
        'networking',
        'public speaking',
        'diplomacy',
        'collaboration',
        'relationship building',
        'emotional intelligence',
        'clarity',
        'conciseness',
        'confidence',
        'respectfulness',
        'tactfulness',
        'professionalism',
        'responsiveness',
        'follow-up',
        'feedback',
        'coaching',
        'mentoring',
        'delegation',
        'motivation',
        'accountability',
        'trustworthiness',
        'integrity',
        'honesty',
        'ethical'
    ]

    skills = extract_skills(text, main_requirements_section1 + main_requirements_section2 + side_requirements)  
    ## Extracting skills from the extracted text with given requirements

    if skills:
        print('Skills:', ', '.join(skills))  ## Printing the extracted skills

    section1_score = len(skills.intersection(main_requirements_section1))  ## Calculating the score for section 1 requirements
    section2_score = len(skills.intersection(main_requirements_section2))  ## Calculating the score for section 2 requirements

    if section1_score >= 1 and section2_score >= 1:  ## Checking if the scores meet the main requirements
        match_score = (section1_score + section2_score) / (len(main_requirements_section1) + len(main_requirements_section2)) * 8  
        ## Calculating the match score
    else:
        match_score = 0

    print('Match Score:', match_score)  ## Printing the match score

    if match_score < 5:  ## Checking if the match score is below the threshold
        print("This applicant doesn't fit the requirements") 
