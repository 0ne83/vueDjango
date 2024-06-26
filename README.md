# vueDjango

vueDjango is a full-stack web application project boilerplate that integrates the Django framework for the backend with Vue.js for the frontend. This combination leverages the robust capabilities of Django's server-side processing with the dynamic, reactive user interfaces provided by Vue.js.

## Features

- **Django Backend**: Utilizes Django for handling server-side logic, database interactions, and serving APIs.
- **Vue.js Frontend**: Provides a responsive and interactive user interface.
- **REST API**: Implements RESTful APIs for seamless communication between the frontend and backend.
- **Authentication**: Includes user authentication and authorization mechanisms.
- **Modular Structure**: Clean separation of frontend and backend code for maintainability and scalability.

## Prerequisites

- Python 3.x
- Node.js and npm
- Vue CLI
- Django

## Getting Started

### Backend Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/0ne83/vueDjango.git
    cd vueDjango/backend
    ```

2. **Create a virtual environment and activate it**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**

    ```bash
    python manage.py migrate
    ```

5. **Start the Django server**

    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the frontend directory**

    ```bash
    cd ../frontend
    ```

2. **Install dependencies**

    ```bash
    npm install
    ```

3. **Start the Vue development server**

    ```bash
    npm run serve
    ```

## Project Structure

```
vueDjango/
│
├── backend/                  # Django backend
│   ├── manage.py             # Django management script
│   ├── myapp/                # Django application
│   └── ...                   # Other backend files
│
└── frontend/                 # Vue.js frontend
    ├── public/               # Public assets
    ├── src/                  # Source files
    ├── package.json          # npm package configuration
    └── ...                   # Other frontend files
```

## Deployment

### Backend Deployment

1. **Collect static files**

    ```bash
    python manage.py collectstatic
    ```

2. **Configure your production server (e.g., Gunicorn, Nginx)**

### Frontend Deployment

1. **Build for production**

    ```bash
    npm run build
    ```

2. **Serve the static files using a web server (e.g., Nginx)**

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Vue.js](https://vuejs.org/)
