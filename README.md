<h1>MSc Workflow and Documentation System</h1> <br>

The MSc Workflow and Documentation System is a crucial tool for streamlining and automating workflows, as well as organizing documents in the academic field.<br>
 
<h1>Installation Instructions</h1>

<p>Before starting, ensure you have Python and Django installed.</p>

<h2>Install Python:</h2>
<p>Visit <a href="https://www.python.org/downloads/" target="_blank">Python Downloads</a> for installation instructions.</p>

<h2>Install Django:</h2>
<p>Run the following command in your terminal:</p>
<pre><code>pip install Django</code></pre>

<h2>Cloning the Repository</h2>
<h3>Clone the Repository:</h3>
<pre><code>git clone https://github.com/darpankattel/msc-workflow-document-ms.git</code></pre>

<h3>Navigate to the Project Directory:</h3>
<pre><code>cd msc-workflow-document-ms</code></pre>

<h2>Configuration Steps</h2>
<p>No extra configuration is needed. The project is designed to work seamlessly without additional setup.</p>

<h2>Running the Project Locally</h2>

<h3>Set Up a Virtual Environment:</h3>
<p>If you don't have <code>virtualenv</code>, install it:</p>
<pre><code>pip install virtualenv</code></pre>

<p>Create and activate a virtual environment:</p>
<pre><code>python3.6 -m venv env
# OR
python -m venv env -p "path to Python 3.6.5"
source env/bin/activate  # On Windows: env\Scripts\activate</code></pre>

<h3>Install Dependencies:</h3>
<p>Use the <code>requirements.txt</code> file to install all necessary dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>Run the Server:</h3>
<p>Start the Django development server with:</p>
<pre><code>python manage.py runserver</code></pre>
 
