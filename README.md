🏋️ Fitness Tracker

📌 Description
Fitness Tracker is a full-stack application that helps users log workouts, manage nutrition, and track progress toward their fitness goals.
The backend is built with Django & Django REST Framework (DRF), providing secure and scalable APIs, while the frontend templates use TailwindCSS for a clean and responsive UI.


🚀 Features
🔐 User Authentication – Register, log in, and manage sessions securely with JWT
🏃 Workout Management – Add, update, and track workouts & exercises
🍎 Nutrition Tracking – Log meals and monitor calorie intake
📊 Progress Tracking – View summaries and progress reports over time
⚡ Modern UI – Tailwind-powered responsive templates


🛠️ Tech Stack
1. Backend:
   Python:  [Python 3.13](https://www.python.org/) 
   Django: [Django 5](https://www.djangoproject.com/) 
   Django REST Framework:  [Django REST Framework](https://www.django-rest-framework.org/)  
2. Frontend:
   Django Templates + TailwindCSS
3. Database:
   SQLite (default, can switch to PostgreSQL/MySQL)
4. Auth: 
   JWT (JSON Web Tokens) via DRF SimpleJWT: [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) 



📂 Project Structure
fitness_tracker/
│── accounts/         # User authentication & profiles  
│── workouts/         # Workout & exercise management  
│── nutrition/        # Nutrition tracking  
│── summaries/        # Progress & analytics  
│── templates/        # HTML templates (UI with TailwindCSS)  
│── fitness_tracker/  # Main project settings  


## Installation
1. Clone the repository:
   git clone https://github.com/NkatDesta/fitness-tracker.git


⚙️ Installation & Setup

1. Clone the repository
   git clone https://github.com/NkatDesta/fitness-tracker.git
   cd fitness-tracker

2. Create & activate virtual environment
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Mac/Linux

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations
   python manage.py migrate

5. Create superuser (admin access)
   python manage.py createsuperuser


6. Run development server
   python manage.py runserver
7. Now open: http://127.0.0.1:8000/


🔗 API Endpoints (Examples)
##Authentication
Method   	Endpoint	            Description	        Status
POST	    /api/auth/register/	   Register new user  	✅
POST	      /api/auth/login/   	Obtain JWT token	   ✅

##Workouts
Method	   Endpoint      	Description         	Status
GET    	/api/workouts/ 	List all workouts  	 ✅
POST  	/api/workouts/    Create new workout	 ✅

##Nutrition
Method	  Endpoint      	Description       	   Status
GET	  /api/nutrition/  	List meals & calories	 ✅

##Progress
Method   	Endpoint	                Description         	Status
GET	  /api/summaries/progress/ 	View user progress     	✅
