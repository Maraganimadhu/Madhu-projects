# To-Do List Web App

## Overview
This is a feature-rich To-Do List web application built using **HTML, CSS, JavaScript, Flask, and MySQL**. The app allows users to create, manage, and organize tasks efficiently while providing authentication and task filtering options.

## Features
- **User Authentication**: Register, Login, Logout, and Guest Login
- **CRUD Operations**: Add, Edit, Delete, and View tasks
- **Task Organization**:
  - Categorized tasks (To-Start, In-Progress, Completed)
  - Date-based task sorting and filtering
  - Unique task title enforcement
- **User Interface**:
  - Dropdown menu for selecting task lists
  - Task display in a table format with serial numbers
  - Centered input fields for easy task entry
- **Navigation & UI Enhancements**:
  - Animated navigation buttons (Home, About, Contact Us, Review, Login)
  - "Work in Progress" image on homepage
  - "Create" button to navigate to the To-Do list page
  - Responsive design for mobile compatibility (Upcoming V1.1)
- **Dashboard**:
  - Kanban-style layout for task management
  - Profile Management
- **Additional Sections**:
  - Product Overview, Design Process, Target Audience, Workflow Diagram, UI Style Guide, Sketching & Wireframes, Visual Design V1.0

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Flask
- MySQL
- Node.js (optional, for frontend enhancements)

### Setup Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```
2. **Set Up a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Database Configuration**
   - Create a MySQL database.
   - Update `config.py` with database credentials.
   - Run migrations to set up tables.

5. **Run the Application**
   ```sh
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage
- **Sign Up / Log In** to access your personalized task list.
- **Create, edit, and delete tasks** as needed.
- **Filter tasks by date** using the provided controls.
- **Manage tasks** across different statuses in the Kanban dashboard.

## Future Enhancements
- Mobile-responsive version (V1.1)
- Dark mode theme
- Task reminders & notifications
- Collaborative task sharing

## Contributing
Feel free to fork the repository and submit pull requests with improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).

---
### Screenshots
_Add screenshots or GIFs here to showcase the app!_

