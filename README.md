# MyPersonalPortfolio

A personal portfolio website built with Django to showcase my projects and skills.

## ✨ Features

- Home Page: Overview of my portfolio and showcased projects.
- About Page: Detailed information about my skills, interests, and journey.
- Local Bootstrap Hosting: Utilizes Bootstrap CSS and JS served directly from the project's static files.
- Responsive Design: Built with Bootstrap components for a mobile-first approach.
- Project Management: Dedicated Django app to manage portfolio projects.

## 🚀 Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Git

### Installation

1.  Clone the repository:
    ```bash
    git clone [YOUR_GITHUB_REPOSITORY_URL]
    cd MyPortfolio1
    ```

2.  Create and activate a virtual environment:
    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run database migrations:
    ```bash
    python manage.py migrate
    ```

5.  Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your username, email, and password.

6.  Run the development server:
    ```bash
    python manage.py runserver
    ```
    The website will be accessible at `http://127.0.0.1:8000/`.

## 🗺️ Routes

-   / (Root): The main home page, displaying an overview of projects.
-   /about/: A dedicated page providing information about me and my skills.

## 🛠️ Built With

-   [Django](https://www.djangoproject.com/) - The web framework used
-   [Bootstrap 5](https://getbootstrap.com/) - Frontend framework for responsive design

## 🤝 Contributing

Feel free to fork this repository, create your own portfolio, and modify it as needed.

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details (you can add a LICENSE file later if you wish).