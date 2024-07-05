<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSc Workflow and Documentation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
        }
        code {
            background-color: #eaeaea;
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 1em;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            margin: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>MSc Workflow and Documentation System</h1>
        <p>The MSc Workflow and Documentation System is a crucial tool for streamlining and automating workflows, as well as organizing documents in the academic field.</p>

        <h2>Installation Instructions</h2>
        <p>Before starting, ensure you have Python and Django installed.</p>
        
        <h3>Install Python:</h3>
        <p>Visit <a href="https://www.python.org/downloads/">Python Downloads</a> for installation instructions.</p>
        
        <h3>Install Django:</h3>
        <pre><code>pip install Django</code></pre>

        <h2>Cloning the Repository</h2>
        <h3>Clone the Repository:</h3>
        <pre><code>git clone https://github.com/Baebabe/MSC_SE.git</code></pre>

        <h3>Navigate to the Project Directory:</h3>
        <pre><code>cd msc-workflow-document-ms</code></pre>

        <h2>Configuration Steps</h2>
        <p>No extra configuration is needed. The project is designed to work seamlessly without additional setup.</p>

        <h2>Running the Project Locally</h2>
        <h3>Set Up a Virtual Environment:</h3>
        <p>If you don't have virtualenv, install it:</p>
        <pre><code>pip install virtualenv</code></pre>

        <h3>Create and activate a virtual environment:</h3>
        <pre><code>
python3.6 -m venv env
# OR
python -m venv env -p "path to Python 3.6.5"
source env/bin/activate  # On Windows: env\Scripts\activate
        </code></pre>

        <h3>Install Dependencies:</h3>
        <p>Use the requirements.txt file to install all necessary dependencies:</p>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>Run the Server:</h3>
        <p>Start the Django development server with:</p>
        <pre><code>python manage.py runserver</code></pre>
    </div>
</body>
</html>
