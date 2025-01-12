# Company Management System – Back End

## Overview
This project is a **Company Management System** built using Django and Django REST Framework. It provides a backend API for managing companies, departments, employees, and projects. The system also includes a workflow for handling employee performance reviews and implements role-based access control (RBAC) to ensure secure data handling.

## Features
- **CRUD Operations**: Create, read, update, and delete records for companies, departments, employees, and projects.
- **Employee Performance Review Workflow**: A structured process for scheduling, feedback collection, and approvals.
- **Role-Based Access Control (RBAC)**: Different levels of access for Admin, Manager, and Employee roles.
- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT).
- **Auto-Calculated Fields**: Fields like `days_employed`, `number_of_departments`, `number_of_employees`, and `number_of_projects` are automatically calculated.


## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Django 5.1 or higher
- Django REST Framework
- PostgreSQL (or SQLite for development)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/company-management-system.git
   cd company-management-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - For SQLite (default):
     ```bash
     python manage.py migrate
     ```
   - For PostgreSQL:
     - Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials.
     - Run migrations:
       ```bash
       python manage.py migrate
       ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API**:
   - The API will be available at `http://localhost:8000/api/`.

---

## Implementation Details

### Data Models
- **User**: Custom user model with roles (Admin, Manager, Employee).
- **Company**: Represents a company with auto-calculated fields for departments, employees, and projects.
- **Department**: Represents a department within a company.
- **Employee**: Represents an employee with auto-calculated `days_employed`.
- **Project**: Represents a project with assigned employees.
- **PerformanceReview**: Represents an employee's performance review with a workflow for stages and transitions.

### Workflow: Employee Performance Review
The performance review workflow includes the following stages:
1. **Pending Review**: Employee is flagged for review.
2. **Review Scheduled**: A review meeting is scheduled.
3. **Feedback Provided**: Feedback is documented.
4. **Under Approval**: Feedback is under managerial review.
5. **Review Approved**: Feedback is approved.
6. **Review Rejected**: Feedback is rejected and requires rework.

Transitions between stages are controlled by the `PerformanceReviewTransitionView` API endpoint.

### Security Measures
- **Role-Based Access Control (RBAC)**:
  - Admins have full access.
  - Managers can manage employees and performance reviews.
  - Employees have read-only access to their own data.
- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT). Tokens are required for all API requests.

---

## API Documentation

### Authentication
- **Obtain JWT Token**:
  - **Endpoint**: `POST /api/token/`
  - **Request Body**:
    ```json
    {
        "username": "your-username",
        "password": "your-password"
    }
    ```
  - **Response**:
    ```json
    {
        "access": "your-access-token",
        "refresh": "your-refresh-token"
    }
    ```

- **Refresh JWT Token**:
  - **Endpoint**: `POST /api/token/refresh/`
  - **Request Body**:
    ```json
    {
        "refresh": "your-refresh-token"
    }
    ```
  - **Response**:
    ```json
    {
        "access": "your-new-access-token"
    }
    ```

### Endpoints
#### Companies
- **List Companies**: `GET /api/companies/`
- **Create Company**: `POST /api/companies/`
- **Retrieve Company**: `GET /api/companies/{id}/`
- **Update Company**: `PUT /api/companies/{id}/`
- **Delete Company**: `DELETE /api/companies/{id}/`

#### Departments
- **List Departments**: `GET /api/departments/`
- **Create Department**: `POST /api/departments/`
- **Retrieve Department**: `GET /api/departments/{id}/`
- **Update Department**: `PUT /api/departments/{id}/`
- **Delete Department**: `DELETE /api/departments/{id}/`

#### Employees
- **List Employees**: `GET /api/employees/`
- **Create Employee**: `POST /api/employees/`
- **Retrieve Employee**: `GET /api/employees/{id}/`
- **Update Employee**: `PUT /api/employees/{id}/`
- **Delete Employee**: `DELETE /api/employees/{id}/`

#### Projects
- **List Projects**: `GET /api/projects/`
- **Create Project**: `POST /api/projects/`
- **Retrieve Project**: `GET /api/projects/{id}/`
- **Update Project**: `PUT /api/projects/{id}/`
- **Delete Project**: `DELETE /api/projects/{id}/`

#### Performance Reviews
- **List Performance Reviews**: `GET /api/performance-reviews/`
- **Create Performance Review**: `POST /api/performance-reviews/`
- **Retrieve Performance Review**: `GET /api/performance-reviews/{id}/`
- **Update Performance Review**: `PUT /api/performance-reviews/{id}/`
- **Delete Performance Review**: `DELETE /api/performance-reviews/{id}/`
- **Transition Review Stage**: `POST /api/performance-reviews/{id}/transition/`

---

## Check List
- [x] CRUD operations for companies, departments, employees, and projects.
- [x] Employee performance review workflow.
- [x] Role-based access control (RBAC).
- [x] JWT authentication.
- [x] Auto-calculated fields.
- [x] Unit and integration tests.

---

## Assumptions and Considerations
- **Database**: SQLite is used for development, but PostgreSQL is recommended for production.
- **Permissions**: Admins have full access, managers can manage employees and reviews, and employees have read-only access to their own data.
- **Performance Reviews**: Only managers can transition review stages.

---

## Security Measures
- **JWT Authentication**: All API endpoints require a valid JWT token.
- **Role-Based Access Control (RBAC)**: Different roles have different levels of access.
- **Data Protection**: Sensitive data (e.g., passwords) is hashed and stored securely.

---

## How to Access API Documentation
Access the Swagger UI at `http://localhost:8000/swagger/`.

---