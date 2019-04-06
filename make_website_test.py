import unittest

# C:\Users\Anthony\Documents\Wharton\Spring 2019\CIT590\Python\Homeworks

from make_website import * #imports all functions in make_website

class Test_Make_Website(unittest.TestCase):

    def setUp(self): #creates sample resume lists to test from
        self.test_1 = ['anthony Farias  ', 'Projects:','    Project 1', 'Project 2    ','----------','    agfe@wharton.upenn.com    ', 'Courses:::::     1234Bio, Chem, Math' ]
        self.test_2 = ['3nthony Farias  ','Projects:','  Project1',' Project 2','  agfe@wharton.upenn.edu      ','Courses    Bio,   Chem,   Math']
        self.test_3 = ['   Anthony Farias    ',' agfe@Wharton.upenn.edu  ']
        self.test_4 = ['Anthony Farias','agfe23@wharton.upenn.edu   ']
        self.test_5 = ['Anthony Farias','agfe@whart23.upenn.edu   ']
        self.test_6= []

    def test_open_resume_file(self):
        self.assertEqual(['Anthony Farias'], open_file('test_open.txt')) #tested on a sample *.txt file

    def test_detect_name(self):
        #Testing for runtime error w/ first letter as lower case letter
        self.assertRaises(RuntimeError, detect_name, 'self.test_1')

        #Testing for runtime error w/ first letter as non-letter
        self.assertRaises(RuntimeError, detect_name, 'self.test_2')

        #Testing for runtime error if file is empty list (i.e. nothing can be found for name)
        self.assertRaises(RuntimeError, detect_name, 'self.test_6')

        #Testing for correct output with first letter as uppercase letter and with spaces after and before name
        self.assertEqual('Anthony Farias', detect_name(self.test_3))

    def test_detect_email(self):
        #Testing for correctly formatted email ending with '.com' and with spaces before and after email.
        self.assertEqual('agfe@wharton.upenn.com', detect_email(self.test_1))

        #Testing for correctly formatted email ending with '.edu' and with spaces before and after email.
        self.assertEqual('agfe@wharton.upenn.edu', detect_email(self.test_2))

        #Testing for correctly formated email with normal lowercase English character between '@' and ending, by returning 'None'
        self.assertEqual(None, detect_email(self.test_3))

        #Testing for correctly formated email with no number in first part of e-mail, by returning 'None'
        self.assertEqual(None, detect_email(self.test_4,))

        #Testing for correctly formated email with no number in second part of e-mail, by returning 'None'
        self.assertEqual(None, detect_email(self.test_5,))

        #Testing that e-mail can be found, by returning 'None' if blank
        self.assertEqual(None, detect_email(self.test_6,))

    def test_detect_courses(self):

        #Testing that Courses will be found despite random punctuation or non-letters (before and after)
        self.assertEqual('Bio, Chem, Math', detect_courses(self.test_1))

        #Testing that courses will be found despite whitespace
        self.assertEqual('Bio, Chem, Math', detect_courses(self.test_2))

        #Testing that function returns None if 'Courses does not exist
        self.assertEqual(None, detect_courses(self.test_6))

    def test_detect_projects(self):

        #Testing the function returns correct projects, despite trailing white spaces
        self.assertEqual(['Project 1', 'Project 2'], detect_projects(self.test_1))

        #Testing that the function returns None if the list does not end with 10 minus signs
        self.assertEqual(None, detect_projects(self.test_2))

        #Testing that the function returns None, if no projects are listed
        self.assertEqual(None, detect_projects(self.test_3))

    def test_surround_block(self):

        #Test function
        self.assertEqual('<h1>The Beatles</h1>', surround_block('h1', 'The Beatles'))

    def test_create_email_link(self):

        #Test Function
        self.assertEqual('<a href="mailto:tom@seas.upenn.edu">tom[aT]seas.upenn.edu</a>', create_email_link('tom@seas.upenn.edu'))

    def test_write_basic_info(self):

        #Testing to see that the correct tags get put on basic info
        self.assertEqual('<div>\n<h1>Anthony Farias</h1>\n<p>Email: <a href="mailto:agfe@wharton.upenn.edu">agfe[aT]wharton.upenn.edu</a></p>\n</div>', write_basic_info('Anthony Farias', 'agfe@wharton.upenn.edu'))

        #Testing to see that the function returns 'Error' if non-string produced
        self.assertEqual('Error - no data', write_basic_info('Anthony Farias', None))

    def test_write_projects(self):

        #Testing to see that the correct tags get put on each project & whitespace trimmed
        self.assertEqual('<div>\n<h2>Projects</h2>\n<ul>\n<li>proj 1</li>\n<li>proj 2</li>\n<li>proj 3</li>\n</ul>\n</div>', write_projects(['proj 1',      'proj 2', 'proj 3']))

        #Testing to see that the function returns 'no data' if projects are not provided
        self.assertEqual('Error - no data', write_projects(None))

    def test_write_courses(self):

        #Testing to see that the correct tags get put on the courses list
        self.assertEqual('<div>\n<h3>Courses</h3>\n<span>course1, course2, course3</span>\n</div>', write_courses('course1, course2, course3'))

        #Testing to see that the function returns 'Error' in place of courses if no courses are provided
        self.assertEqual('<div>\n<h3>Courses</h3>\nError\n</div>', write_courses(None))

unittest.main()
