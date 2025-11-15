📧 Mail Matrix – Unified Messaging Dashboard

Mail Matrix is a centralized email management system built using Python Django.
It allows users to send, receive, view, search, and organize internal mails through a clean and responsive dashboard.

🚀 Features
🔐 User Authentication

User registration

Login / Logout

Secure Django session management

📨 Mail Management

Compose and send mails

Inbox (received mails)

Sent mails

Delete mails

Mark mails as read

Search by subject or sender

🖥️ Dashboard Interface

Sidebar navigation

Mobile responsive UI using Bootstrap 5

Clean and modern layout

🛠️ Backend Technology

Django (latest stable version)

SQLite / MySQL

Django ORM

Models:

sender

receiver

subject

body

timestamp

is_read

🌐 Deployment Ready

Fully configured for Vercel

Includes:

vercel.json

requirements.txt

Static files support settings

📁 Project Structure
Mail-Matrix/
│── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
│── mail_dashboard/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
│── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── inbox.html
│   ├── sent.html
│   ├── compose.html
│
│── static/
│── staticfiles/
│── manage.py
│── vercel.json
│── requirements.txt
│── README.md

⚙️ Installation (Local Development)
1. Clone the Repository
git clone https://github.com/Harshkumar50/Mail-Matrix.git
cd Mail-Matrix

2. Create Virtual Environment
python -m venv .venv


Activate:

Windows:

.venv\Scripts\activate


Mac / Linux:

source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Start Server
python manage.py runserver


Visit:
http://127.0.0.1:8000/

🚀 Deploy on Vercel
1. Install Vercel CLI
npm install -g vercel

2. Deploy Project
vercel

3. For Future Deployments
vercel --prod

🔧 Required Environment Variables (optional)

If using a .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=mailmatrix

🛡️ Security

Password hashing

CSRF protection

Form validation

Only authenticated users access dashboard

Sender/receiver validation for mail access

📸 Future Enhancements (Optional)

Attachments support

Multi-user groups

Mail archiving

Notification system

Admin analytics panel

👨‍💻 Author

Harsh Kumar
GitHub: https://github.com/Harshkumar50

Project: Mail Matrix – Unified Messaging Dashboard
