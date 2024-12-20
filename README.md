# Vacations Management System - Part II

This project is the second part of a three-part series focused on building a Vacations Management System. In this phase, the goal is to implement both the backend and the frontend using Flask, HTML, CSS, JavaScript, and Bootstrap. The backend connects to a MySQL database, and the system functionality builds upon the foundation set in Part I. This phase includes creating the user interface and adding advanced functionality to the system, including role-based access.

## Project Overview

The Vacations Management System allows users to view vacations, like/unlike vacations, and provides administrative controls for managing the vacations. The system supports two types of roles:

1. **Admin**: Can view, add, update, and delete vacations.
2. **User**: Can view vacations and like or unlike them.

This part focuses on expanding the application by adding a complete front-end, building upon the previous backend setup using Flask.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Virtual Environment**: Python virtual environment with `requirements.txt` for dependencies

## Project Structure

The project is organized into several key components:

- **Backend (`src/`)**:
  - **App (`src/app.py`)**: The main Flask application file that starts the server and registers all the blueprints. It also handles error pages for 404 and 500 errors.
  - **Facades (`src/facades/`)**: Contains facade logic to handle interactions between the frontend and backend logic layer. Includes:
    - `countries_facade.py`, `likes_facade.py`, `roles_facade.py`, `users_facade.py`, `vacations_facade.py`.
  - **Logic Layer (`src/logic/`)**: Implements the business logic for managing users, vacations, roles, likes, and countries. Includes:
    - `countries_logic.py`, `likes_logic.py`, `roles_logic.py`, `users_logic.py`, `vacations_logic.py`.
  - **Models Layer (`src/models/`)**: Contains data models representing users, roles, countries, vacations, likes, and status codes. Includes:
    - `countries_model.py`, `error_model.py`, `likes_model.py`, `role_model.py`, `status_code.py`, `users_model.py`, `vacations_model.py`.
  - **Views (`src/views/`)**: Contains view functions to handle HTTP requests and responses for different routes. Includes:
    - `api_view.py`, `contact_view.py`, `counties_view.py`, `home_view.py`, `users_view.py`, `vacations_view.py`.
  - **Utilities (`src/utils/`)**: Contains utility files such as:
    - `app_config.py` (application configuration), `cyber_hash.py` (hashing passwords), `dal.py` (database interaction), `logger.py` (logging), `image_handler.py` (handling image uploads).

- **Frontend (`src/templates/` and `src/static/`)**:
  - **Templates (`src/templates/`)**: Contains HTML files for various pages in the system:
    - **Layout and Error Pages**:
      - `layout.html`: Base layout for all pages.
      - `404_page_not_found.html`: Custom 404 error page.
      - `500_server_error.html`: Custom 500 error page.
    - **User-Related Pages**:
      - `login.html`: User login page.
      - `register.html`: User registration page.
      - `auth_hello_users.html`: Displays greeting and authentication options.
    - **Vacation Management Pages**:
      - `all_vacations.html`: Displays all available vacations for users and admins.
      - `add_new_vacation.html`: Admin page for adding a new vacation.
      - `update_vacation.html`: Admin page for updating an existing vacation.
      - `vacation_info.html`: Detailed view for a specific vacation.
    - **Country Management**:
      - `add_new_country.html`: Admin page for adding a new country.
    - **Home and Contact Pages**:
      - `home.html`: The homepage of the website.
      - `contact_us.html` and `contact_us_target.html`: Contact form and confirmation pages.
  - **Static (`src/static/`)**: Holds CSS, JavaScript, and image files used in the project.
    - **CSS (`src/static/css/style.css`)**: Defines the styling for the entire application.
    - **JavaScript (`src/static/js/main.js`)**: Contains JavaScript code for various client-side functionalities, such as form handling, dynamic content updates, and confirmation prompts.
    - **Images (`src/static/`)**: Contains folders like `background_images`, `home_gallery_images`, `icons`, `data_base_images`, and `logos` for various assets used in the web application.

## Database Structure

The database consists of the following tables:

1. **Roles (`roles`)**:
   - `role_id` (Primary Key)
   - `role_name` (Admin, User)

2. **Users (`users`)**:
   - `user_id` (Primary Key)
   - `first_name`, `last_name`, `email`, `password`
   - `role_id` (Foreign Key)

3. **Countries (`countries`)**:
   - `country_id` (Primary Key)
   - `country_name`

4. **Vacations (`vacations`)**:
   - `vacation_id` (Primary Key)
   - `country_id` (Foreign Key)
   - `description`, `start_date`, `end_date`, `price`, `image_file`

5. **Likes (`likes`)**:
   - `user_id` (Foreign Key)
   - `vacation_id` (Foreign Key)

The database must include two roles (Admin and User), two users (one Admin and one User), at least 10 countries, and 12 vacations. The `likes` table should be empty initially.

## Features Implemented

1. **Database Setup**:
   - Creation of tables and setting up relationships.
   - Initial data population (roles, users, countries, vacations).

2. **Frontend Pages**:
   - **Registration Page**: Allows new users to register. All fields are required, email validation is performed, and passwords must be at least 4 characters long.
   - **Login Page**: Allows registered users to log in with their email and password. Incorrect details will display an error message.
   - **Vacations Page**: Accessible only to logged-in users. Displays vacations in cards, showing vacation details and the number of likes. Users can like or unlike vacations.
   - **Admin Page**: Accessible only to admins. Allows adding, editing, or deleting vacations, with confirmation prompts for deletion.
   - **Add/Edit Vacation Pages**: Allows admins to add or edit vacation details, including image uploads.
   - **Add New Country Page**: Allows admins to add new countries.
   - **Contact Page**: Displays contact information and allows users to get in touch.

3. **Business Logic**:
   - User Management: Register users, verify login credentials, validate unique emails.
   - Vacation Management: Add, update, delete vacations, retrieve vacations sorted by start date.
   - Like Management: Add/remove likes for specific vacations.

4. **API Endpoints**:
   - Provides RESTful API endpoints to retrieve vacation information in JSON format, supporting both single vacation queries and full vacation list queries (`api_view.py`).

5. **Navigation**:
   - Main menu navigation changes based on the user type (Admin or regular user).
   - Logged-in users can log out, view vacations, and like/unlike vacations.
   - Admin users have additional options to manage vacations.

6. **JavaScript Functionalities**:
   - Handles client-side actions like confirming vacation deletion, dynamic image gallery updates, and managing like/unlike interactions.

7. **Error Handling**:
   - Custom error pages for `404 Page Not Found` and `500 Server Error` are implemented, and errors are logged using `logger.py`.

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/hagarhorvitz/freedom_project_part2.git
   cd freedom_part2
   ```

2. Set up the virtual environment:
   ```bash
   python -m venv freedomVE
   source freedomVE/bin/activate  # On Windows: freedomVE\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Import the provided SQL schema (`freedom_database_mysql.sql`) and data into your MySQL server.

4. Run the Flask application:
   - Ensure `app.py` is in the correct location (`src/` directory or root as applicable).
   ```bash
   python src/app.py
   ```

## .gitignore

The following files and directories are ignored in the Git repository:
- `/freedomVE`: The virtual environment folder.
- `.env`: Environment variables file.
- `/src/tests`: Test files directory.

## Requirements

The required Python packages are listed in `requirements.txt`. Here are the main dependencies:
- `Flask==3.0.3`
- `mysql-connector-python==8.3.0`
- `python-dotenv==1.0.1`
- `Jinja2==3.1.4`
- `Werkzeug==3.0.3`
- `blinker`, `click`, `colorama`, `dnspython`, `email_validator`, `idna`, `itsdangerous`, `MarkupSafe`

## Notes

- This part of the project adds a complete frontend using HTML, CSS, JavaScript, and Bootstrap, building upon the backend foundation.
- The admin role and some initial data are hardcoded for this part of the project.
- Make sure the `app.py` file exists and is in the correct directory before running the application.

## Future Development

This project is the second of three phases:
1. **Part I**: Backend foundation with Flask and MySQL.
2. **Part II**: Full-stack development using Flask for both backend and frontend (current).
3. **Part III**: Advanced full-stack development with Django for the backend and React for the frontend.

## Author
This project is part of the Full Stack Python Web Development course.

## License
This project is for educational purposes only and follows the terms provided by the course.

