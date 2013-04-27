
__________________________________
ABOUT THIS PROJECT & ORGANIZATION:

This project is a website for Connecting Countries Adopt-A-School (CCAAS), a charity aimed at improving sanitation conditions at schools in rural Kenya.
The charity is located in Hamilton, Ontario, Canada. It's main programs are:

Sanitation Latrine Building - is our primary program. Through fundraising, Canadian “partner schools” have helped to finance the building of almost 100 latrines since 2005.  Why is adequate sanitation so fundamentally important for Kenyan schools?  With the building of proper latrines, student absences due to illnesses brought on by poor sanitation are reduced; toilet wait times lessen resulting in more class time, and students acquire an improved level of privacy, safety and dignity.  

Pen Pal Letter Program - links Canadian and Kenyan students allowing them to build friendships and exchange cultural information. Canadian students are matched with students from Central Kenyan Schools and thus a friendship begins. Thousands of letters are exchanged each school year. In addition to enhancing mutual cultural understanding, this program builds literacy skills, furthers global citizenship education, and allows fundraising to be more personal. Most importantly, children from both countries enjoy this program and have fun with it.  

Clean Hands - is based upon the sanitation-education link. This program augments the Kenyan Ministry of Health and Education’s focus to improve the health of students. Clean Hands teaches Kenyan school children the importance of hand washing and proper techniques. It also provides access to soap and water through hand washing stations to help stop the spread of preventable disease. Healthy children attend school more regularly.

Continuing Support - conceived by Ontario Pen Pal students. This program allows Canadian students to continue to support their Kenyan friends’ education by raising money to fund the purchase necessary school supplies. Over 5000 notebooks, more than 400 textbooks and countless numbers of pencils have found their way to our Kenyan classrooms.

This website aims to be the cornerstone of information for Connecting Countries Adopt-A-School. The goal is to create a strong online presence for CCAAS, ultimately educating visitors about the organization and the surrounding issues, and pushing for donations. 

___________________
TECHNICAL OVERVIEW:

This project is built using Django with the Mezzanine CMS and (soon) Cartridge Shopping Cart.

From the root of this project you will find the basics of a Django project, static media (css, js, graphics), a requirements file (requirments/project.txt), Django templates, and the "mainsite" Django app which encompasses all the Django/Mezzanine models, page processors, template tags, etc.. 

**************************
How To Build This Project:

Working knowledge of Git, Python, and Django are expected. 

1. First clone the repo into some folder on your machine.

Next I use virtualenv to setup my environment, but it is not necessary. 


2. Make a new virtualenv:
$ sudo virtualenv <pathtoenv>


3. Simply activate the environment:
$ source <pathtoenv>/bin/activate

Now basically anything you do with Python is within the scope of this virtualenv. So now we can install our required Python packages for this project.
These packages will be placed under <pathtoenv>/lib/python2.x/site-packages and will not conflict with packages installed on your machine outside this virtual environment.


4. Install required packages (pip is the easiest way to go for this):
$ pip install -r  requirements/project.txt 
This will automatically get any packages needed for this project.


5. Head back to the directory you placed the project repo.


6. We are now setup and ready to go. To run the website simple enter:
$ python manage.py runserver
