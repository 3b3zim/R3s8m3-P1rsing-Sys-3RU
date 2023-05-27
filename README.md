### Hi there 👋

RESUME
PARSING SYSTEM

Made & introduced by: Mohamed Abdelazim
- AI LVL 3 - ID: 215165
- Course: Computational Perception
- Professor: Dr. Esraa A. Afify
- Teaching Assistant: Dr. Mustafa Gamal Muhammad


Documentation
Table of Contents
1. Introduction
2. System Overview
3. Dependencies
4. System Components
 • Extracting Text from PDF
 • Extracting Names using Named Entity Recognition (NER)
 • Extracting Job Titles using Named Entity Recognition (NER)
 • Extracting Phone Numbers using Regular Expressions
 • Extracting Emails using Regular Expressions
 • Extracting Skills using Keyword Matching
 • Extracting Years of Experience using Regular Expressions
5. Usage
6. Example
7. Conclusion
8. Future Enhancements

1. Introduction
The process of hiring and evaluating job
applicants can be time-consuming and
labor-intensive for recruiters and hiring
managers. With the increasing number of
resumes received for each job posting,
it becomes challenging to manually review
and extract relevant information from each
document.
This is where the Resume Parsing System comes into play.
Traditionally, resume parsing has been a manual and error-prone task, requiring
recruiters to sift through numerous resumes to identify qualified candidates.
However, with advancements in machine learning and text processing,
it is now possible to develop automated systems that can quickly and accurately
extract relevant information from resumes.
By automating the resume parsing process, recruiters can significantly reduce the
time and effort involved in reviewing applications.
They can focus their attention on evaluating candidates who meet the specified
requirements and possess the desired skills, saving valuable time and resources.
Additionally, the Resume Parsing System can provide consistent and objective
evaluations, eliminating potential biases that may arise from manual processing.




2. System Overview
Key components of the system include text extraction, named entity recognition
(NER), regular expression matching, and keyword matching.
These components work together to extract information such as names, contact
details, job titles, skills, and years of experience from resumes in PDF format.
.
Benefits of the Resume Parsing System include
time efficiency, accuracy, consistency, and
objective evaluation. The automated approach
reduces the time required for manual review,
ensuring a faster and more efficient screening
process. The system's automated extraction and
evaluation minimize human errors and biases,
promoting consistent and fair candidate assessment.
Moreover, the system enhances candidate
selection by identifying individuals who
possess the desired skills, experience, and
qualifications. Recruiters can make
informed decisions based on the extracted
information and the match score calculated
by the system. This facilitates efficient
candidate evaluation and selection.
The Resume Parsing System is a valuable
tool for streamlining the recruitment process, improving efficiency, and optimizing
candidate evaluation. With its automated capabilities and advanced techniques,
the system empowers recruiters to effectively manage a large volume of resumes
and identify the most qualified candidates.




3. Dependencies
The Resume Parsing System requires the following dependencies:
• Python 3.x
• spacy
• nltk
• pdfminer.six
You can install these dependencies using the following command:
Copy code
pip install spacy nltk pdfminer.six
Additionally, you need to download the required resources for nltk by running the
following commands:
arduinoCopy code
nltk.download('punkt') nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker') nltk.download('words')
nltk.download('stopwords')



4. System Components
The Resume Parsing System consists of the following components:
1. Extracting Text from PDF
The extract_text_from_pdf(pdf_path) function extracts text from a PDF document
given its file path. It utilizes the extract_text function from the pdfminer library to
perform the extraction.

2. Extracting Names using Named Entity Recognition (NER)
The extract_names(txt) function uses spaCy's named entity recognition (NER)
model to extract person names from the given text. It iterates over the named
entities in the document and checks for entities labeled as 'PERSON'. It returns the
first two names found.

3. Extracting Job Titles using Named Entity Recognition (NER)
The extract_job_titles(txt) function uses spaCy's NER model to extract job titles from
the given text. It iterates over the named entities in the document and checks for
entities labeled as 'JOB_TITLE'. It returns a list of job titles found.

4. Extracting Phone Numbers using Regular Expressions
The extract_phone_number(resume_text) function uses regular expressions to
extract phone numbers from the resume text. It searches for patterns that match
phone number formats and returns a list of phone numbers found.


5. Extracting Emails using Regular Expressions
The extract_emails(resume_text) function uses regular expressions to extract email
addresses from the resume text. It searches for patterns that match email address
formats and returns a list of email addresses found.

6. Extracting Skills using Keyword Matching
The extract_skills(input_text, requirements) function extracts skills from the resume
text using keyword matching. It tokenizes the input text, removes stop words and
punctuation, generates bigrams and trigrams, and compares the tokens with a list
of requirements. It returns a set of found skills.

7. Extracting Years of Experience using Regular Expressions
The extract_years_of_experience(resume_text) function uses regular expressions to
extract years of experience from the resume text. It searches for patterns that
match the format "X year(s) of experience" and returns a list of years of experience
found.


5. Usage
To use the Resume Parsing System, follow these steps:
1. Ensure that you have installed the required dependencies and
downloaded the necessary resources for nltk.
2. Place the resume document in PDF format in the same directory as the
Python script.
3. Modify the code to specify the correct PDF file name in the line: text =
extract_text_from_pdf('Test.pdf').
4. Customize the main requirements and side requirements lists according
to the desired skills and qualifications.
5. Run the Python script.
6. The system will extract and print the relevant information from the
resume, including names, phone numbers, emails, job titles, years of
experience, and skills.
7. It will also calculate a match score based on the skills found and the
specified requirements.
8. Based on the match score, the system will provide feedback on whether
the applicant fits the requirements or not.


6. Example
Here's an example usage scenario of the Resume Parsing System:
Suppose we have a resume document named "Test.pdf" that we want to parse. We
have defined the main requirements for two sections: Motion GFX Skills and IMG
GFX Skills. We also have a list of side requirements for communication skills.
We run the script and obtain the following output:
yamlCopy code
Name: Mohamed Abdelazim Phone Numbers: +1234567890 Emails:
example@email.com Job Titles: Animator, Graphic Designer Years of Experience: 2
years of experience, 4 years of experience Skills: Motion Graphics, Animation, Adobe
After Effects, Photoshop, Illustrator Match Score: 6.0
Based on the extracted information and the match score, we can determine that
the applicant, Mohamed Abdelazim, has relevant skills in both Motion GFX and IMG
GFX. The match score indicates a good fit for the requirements.

7. Conclusion
The Resume Parsing System provides a convenient way to extract important
information from resumes and evaluate job applicants more efficiently. By
automating the initial screening process, it saves time and effort for recruiters and
enables them to focus on qualified candidates. The system can be further
customized and enhanced to meet specific requirements and integrate with
existing applicant tracking systems.



9. Future Enhancements
Here are some potential future enhancements for the Resume Parsing System:
1. Improve accuracy: Fine-tune the named entity recognition (NER) models
to better identify names and job titles.
2. Expand skills matching: Incorporate more advanced techniques, such as
semantic analysis or machine learning, to improve the skills extraction and
matching process.
3. Handle different resume formats: Extend the system to handle various
resume formats, such as DOCX or plain text, by incorporating additional
text extraction methods or libraries.
4. Integration with databases: Develop functionality to store the parsed
information in a database for further analysis and comparison with other
candidates.
5. GUI interface: Create a graphical user interface (GUI) to provide a userfriendly interaction for uploading resumes, displaying results, and
managing settings.
6. The system will be able to analyze the persona of the applicant and check
if it meets the company requirements & environment, ex: introvert or
extrovert?, Judgmental or nonjudgmental?, etc.…
7. The system can know anything about anyone, even his affairs by the way
he is typing & and choosing words, Colors, Fonts Type+ the type of his CV
8. -This could save muchhh time for the companies to choose the right
applicant! Without wasting time.
9. It can analyze any job position and rate the applicant with the
requirements.
10. Check his work experience if it really exits “It would work with social media
specialists”
11. Expect anything to make the progress of hiring much easier!
With these enhancements, the Resume Parsing System can become a powerful
tool for automating the recruitment process and selecting the best candidates
efficiently.
