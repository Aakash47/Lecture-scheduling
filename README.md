## Lecture Scheduling Module

A Django-based system for managing and scheduling lectures, courses, and instructors with conflict prevention.

---

### Installation Guide

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Aakash47/Lecture-scheduling.git
   cd Lecture-scheduling
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**  
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Server**  
   ```bash
   python manage.py runserver
   ```

---

### URLs

- **Admin Dashboard**: `/admin-dashboard/`  
- **Add Instructor**: `/add-instructor/`  
- **Add Course**: `/add-course/`  
- **Schedule Lecture**: `/schedule-lecture/`  
- **Login**: `/login/`  
- **Logout**: `/logout/`  

---