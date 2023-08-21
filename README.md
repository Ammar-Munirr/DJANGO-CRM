# CRM (Customer Relationship Management) Project in Django

Welcome to the CRM project! This Django-based application is designed to help manage customer relationships efficiently. It includes a range of features to streamline user interactions and handle various aspects of customer management.

## Key Features

1. **User Authentication:**
   - Users can easily create an account, log in, and log out.
   - Password recovery system implemented using console email handling.

2. **Authentication Handling:**
   - Complete authentication process for user security.

3. **User Profiles:**
   - User profiles are automatically created using signals when a new profile is registered.

4. **Lead Management:**
   - Sending email notifications when a new lead is created.

5. **User Interface:**
   - Utilizes Crispy Forms for improved form styling.
   - Tailwind CSS has been integrated to enhance the visual appeal.

6. **Class-Based Views:**
   - The project extensively uses Class-Based Views (CBVs) to organize and manage views.

## Requirements

Before you start the project, ensure you have the following dependencies installed:

- asgiref==3.7.2
- crispy-tailwind==0.5.0
- Django==4.2.3
- django-crispy-forms==2.0
- sqlparse==0.4.4

You can install these dependencies using the following command:

```bash
pip install asgiref==3.7.2 crispy-tailwind==0.5.0 Django==4.2.3 django-crispy-forms==2.0 sqlparse==0.4.4
``````
## Getting Started

Follow these steps to get the CRM project up and running:

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
    ``````
2. **Navigate to the Project Directory:**
    ```bash
    cd CRM
    ``````
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ``````
4. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ``````
5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ``````
6. **Access the Application:**
    ```bash
    http://127.0.0.1:8000/
    ```

## Contribute
Contributions are welcome! If you'd like to contribute to the project, feel free to submit pull requests or issues on the GitHub repository.