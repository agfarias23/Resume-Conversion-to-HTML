def open_file(file):
    '''Opens the resume file, trims whitespace from beginning and end of each element, returns cleaned resume list'''

    # open the file and store lines as a list
    resume = open(file) # opens the resume file
    resume_lst = resume.readlines() #reads all lines in the file as a list
    resume.close() #closes the file object

    #take each list and clean it so that it can be easily read later on
    clean_resume = []  #create empty list
    for line in resume_lst: #strips out extra spaces or hidden characters in each element of list
        line = line.strip() #trims whitespace from beginning and end of element
        if line !="":
            clean_resume.append(line) #adds cleaned elements to clean_resume list

    #returns cleaned resume
    return clean_resume

def detect_name(file_name):
    '''Returns first line (name) and raises runtime error if name doesn't start with a capital letter'''

    name = str(file_name[0]).strip()

    if (name[0].isalpha() == False) or (name[0] != name[0].upper()): #checks to see if first character in first line (name) is an uppercase letter
        raise RuntimeError("The first letter in the resume name does begin with a capital letter.") #if not uppercase letter, raises error
    else:#if is uppercase letter, returns first line (name)
        return name

def detect_email(file, look_for = '@'): #sets default variable of look_for to '@'
    '''Finds the email address in the resume by looking for a line that has the @ character. Checks to make
    sure that that the last four characters of the email are either '.com' or '.edu'. Makes sure the email
    string begins with a normal lowercase English character between the ‘@’ and the ending. Makes sure
    that there are no digits or number in email address '''

    #Finds the email address in the resume by looking for a line that has the @ character and assigns to variable 'email_name'
    email_name = '' #creates empty email string
    for line in file:
        if look_for in line:
            email_name = str(line).strip() #trims whitespace from beginning and end of string

    #Checks to make sure that that the last four characters of the email are either '.com' or '.edu'. If not, returns 'None'
    if email_name.endswith('.com') == False and email_name.endswith('.edu') == False:
        return

    #Makes sure the email string begins with a normal lowercase English character between the ‘@’ and the ending. If not, returns 'None'
    look_for_index = email_name.index(look_for) #finds index of the '@' character
    if email_name[look_for_index + 1].isalpha(): #if statement referencing the index following the '@' character
        if email_name[look_for_index + 1] == email_name[look_for_index + 1].upper(): #if the character is upper case, returns 'None'
            return

    #Makes sure there are no numbers in the email. If there are, returns 'None'
    for char in email_name[0: len(email_name)]:
        if char.isnumeric() == True:
            return

    #Returns e-mail address if it passess these tests
    return email_name

def detect_courses(file, look_for = 'Courses'):
    '''Finds the 'Courses' line in the resume ('file'). Then extracts the line that contains that word ignoring
    any random punctuation'''

    for line in file: #looks at each element in the resume list
        if look_for in line: #checks if that line contains 'Courses'
            courses = line[7:len(line)].strip() #take everything after the word 'Courses' trimming trailing whitespace

            courses = courses.split(',')
            cleaned_courses = []
            for course in courses:
                cleaned_courses.append(course.strip())

            courses = ", ".join(cleaned_courses)

            if courses[1].isalpha(): #if first digit of remaining string is a letter, return remaining string
                return courses
            else:
                for char in courses: #for each element in string, continue until a letter is found
                    if char.isalpha():
                        return courses[courses.index(char):len(courses)] #once letter found, return remaining string


def detect_projects(file, look_for_1 = 'Projects', look_for_2 = '----------'): #sets look_for_1 default to 'Projects'
                                                                               #sets look_for_2 default to '----------'
    '''Looks for 'Projects and '----------' in the resume file and pulls out the projects that are listed in the
       lines between these two items'''

    for line in file: #looks at each line in the file
        if look_for_1 in line: #identifies where 'Projects' is located (indexed)
            start_index = file.index(line) #sets this to the beginning of the position to be used later

    for line in     file: #looks at each line in the file
        if look_for_2 in line: #identifies where '----------' is located indexed
            end_index = file.index(line) #sets this to the end of the position to be used later

    try:
        projects = file[start_index + 1 : end_index] #creates list of projects using aforementioned start and end indices
        projects_new =[]
        for item in projects: #for every project (if not empty), append it to a list
            if item != '':
                projects_new.append(item.strip())
        return projects_new #returns clean list of projects
    except: #if there is an error in finding the 'look_for' items '1' and '2' then returns None
        return

def surround_block(tag, text):
    '''Surrounds the given text with the given HTML tag and returns the string'''

    #String for the starting tag
    start_tag = ['<', tag, '>']
    start_tag = "".join(start_tag)

    #String for the ending tag
    end_tag = ['</', tag, '>']
    end_tag = "".join(end_tag)

    #Casts text into a list so that te function can insert the start and end tags at the 0 and last indices.
    #We use the 'try' block here to account for non-string being passed through
    try:
        text_list = list(text) #casts to list
        text_list.insert(len(text_list), end_tag) #inserts end_tag at end
        text_list.insert(0, start_tag) #inserts start_tag at beginning

        #Joins text back into a string and returns that string
        text_string = "".join(text_list)
        return text_string

    #If a non-string is pass through the function as 'test', then return an error
    except:
        return 'Error'

def create_email_link(email_address):
    '''Creates an email link with the given email address'''
    if '@' in email_address:
        email_address_alias =  email_address.replace('@','[aT]')
    return '<a href="mailto:{}">{}</a>'.format(email_address, email_address_alias)

def write_basic_info(name_str, email_str):
    '''Takes the name info from the resume and adds appropriate tags. Converts e-mail from resume into hyperlink'''
    if email_str is None:
        return 'Error - no data'
    name = surround_block('h1', name_str)
    email = surround_block('p', ("Email: " + create_email_link(email_str)))
    name_email = '\n' + name + '\n' + email + '\n'
    basic_info = surround_block('div', name_email)
    return basic_info

def write_projects(projects_lst):
    ''''Takes the project list from the resume and adds appropriate html tags, returning string with tags and projects.'''

    #Starts list of stings with the necessary opening text and tags
    projects = ['<div>','\n<h2>Projects</h2>', '\n<ul>\n']

    #Surrounds projects with necessary tags, puts on separate line, and uses try block to avoid non-string error
    try:
        for i in projects_lst:
            proj = surround_block('li', i)
            projects.append(proj)
            projects.append('\n')
        ending = ['</ul>', '\n</div>']
        projects.extend(ending)

        #Casts projects and tags into a string and returns that string
        projects = "".join(projects)
        return projects

    #If projects_lst is not a list then returns an error
    except:
        return 'Error - no data'

def write_courses(courses_str):
    '''Takes the project list from the resume and adds appropriate html tags, returning string with tags and projects.'''

    try:
        #Starts list of strings with the necessary opening text and tags
        courses = ['<div>','\n<h3>Courses</h3>','\n']

        #Surrounds projects with necessary tags, puts on separate line
        course_str = surround_block('span', courses_str)
        courses.append(course_str)
        courses.append('\n</div>')

        #Casts 'courses' list into string and returns that string
        courses = "".join(courses)
        return courses

    except:
        return "Error"

def main():
    resume = open_file("resume.txt") #opens file as resume
    #Reads through all text and assigns it to 'text'
    text = write_basic_info(detect_name(resume), detect_email(resume)) + '\n' + write_projects(detect_projects(resume)) + '\n' + write_courses(detect_courses(resume)) + '\n</div>\n</body>\n</html>'

    #Opens html file and writes 'text' to the file
    html_file = open('resume_template.html', 'r+')
    html_file_resume = open('resume.html','w')
    lines = html_file.readlines()
    html_file_resume.seek(0)
    html_file_resume.truncate()
    del lines[-1]
    del lines[-1]
    lines.extend(text)
    html_file_resume.writelines(text)
    # html_file.writelines("</body>")
    # html_file.writelines("</html>")

    #Closes html_file
    html_file.close()


if __name__ == '__main__':
    main()
