# Diagnosis Codes API

<img src="https://github.com/OlayinkaPeter/diagnosisAPI/blob/master/shot_.png" width="100%">
<img src="https://github.com/OlayinkaPeter/diagnosisAPI/blob/master/shot__.png" width="100%">

## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.7](https://www.python.org/downloads/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. Clone the repo:

    ```
    $ git clone https://github.com/OlayinkaPeter/diagnosisAPI.git
    $ cd diagnosisAPI
    ```

2. Setup a virtual environment and install the requirements:

    ```
    $ virtualenv --python=python3 env --no-site-packages
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

3. Create a PostgreSQL user with the username and password `postgres` and create a database called `diagnosis_db`:

    ```
    $ createuser --interactive --pwprompt
    $ createdb diagnosis_db
    ```

4. Export the required environment variables:

    ```
    $ export FLASK_APP=app.py
    ```

5. Execute the migrations to create the `diagnosis` table:

    ```
    $ flask db migrate
    $ flask db upgrade
    ```

6. Run the Flask API:

    ```
    $ flask run
    ```

7. Navigate to `http://localhost:5000` to view the API usage data.