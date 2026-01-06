# Superheroes API

## Project Overview
The Superheroes API is a Flask-based RESTful API for managing superheroes and their superpowers. Users can retrieve information about heroes, powers, and hero-power relationships, as well as update powers and add new hero powers.

This project was developed as part of a Flask API assessment.

---

## Features
- Retrieve a list of all heroes
- Retrieve a single hero by ID, including their powers
- Retrieve a list of all powers
- Retrieve a single power by ID
- Update a power's description
- Create a new hero-power relationship

---

## Technologies Used
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- SQLite (for the database)
- Postman (for API testing)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <YOUR_PRIVATE_REPO_URL>
cd superheroes-api

2. Create a virtual environment
python3 -m venv venv

3. Activate the virtual environment
On Linux / Mac
source venv/bin/activate

On Windows CMD
venv\Scripts\activate

On Windows PowerShell
venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Run migrations
flask db migrate -m "Initial migration"
flask db upgrade

6. Seed the database
python seed.py

7. Run the server
python app.py


The API will run at: http://127.0.0.1:5555

API Endpoints
Heroes

GET /heroes → List all heroes

GET /heroes/<id> → Retrieve hero by ID with powers

Powers

GET /powers → List all powers

GET /powers/<id> → Retrieve power by ID

PATCH /powers/<id> → Update a power's description

Hero Powers

POST /hero_powers → Create a new hero-power relationship

{
  "strength": "Average",
  "hero_id": 3,
  "power_id": 1
}

Data Validation

HeroPower.strength must be one of: Strong, Weak, Average

Power.description must be at least 20 characters

Testing

Use the provided Postman collection to test all routes:

Import challenge-2-superheroes.postman_collection.json into Postman

Run the requests and verify responses

Author

Zach Ndung'u

License

This project is licensed under the MIT License.