MSc Workflow and Documentation System

The MSc Workflow and Documentation System is a crucial tool for streamlining and automating workflows, as well as organizing documents in the academic field.

Installation Instructions: 
Before you begin, make sure you have Python and Django installed. You'll also need the 
project's dependencies listed in the requirements.txt file. Run the following commands in your 
terminal: 
Install Python (if not already installed) 
# Visit https://www.python.org/downloads/ for installation instructions 
# Install Django (if not already installed) 
pip install Django 
Cloning the Repository: 
To get started, clone the project repository using the following commands: 
# Clone the repository 
git clone https://github.com/darpankattel/msc-workflow-document-ms.git 
# Navigate to the project directory 
cd msc-workflow-document-ms 
Configuration Steps: 
No additional configuration steps are required for this project. It's designed to work seamlessly 
without any complex setup. 
Running the Project Locally: 
To run the project locally, follow these steps: 
a. Install Virtual Environment: 
If you haven't installed the venv module, use the following command: 
3 | P a g e 
Documentation Release 1.0 
pip install virtualenv 
b. Create and Activate Virtual Environment: 
Create a virtual environment named "env" and activate it: 
python3.6 -m venv env 
# ORRRRRR 
Python –m venv env –p “your python path to python 3.6.5” 
source env/bin/activate   # On Windows: env\Scripts\activate 
Install Requirements: 
Install the project dependencies using the requirements.txt file: 
pip install -r requirements.txt 
Run the Server: 
Start the Django development server: 
python manage.py runserver 
 
 
