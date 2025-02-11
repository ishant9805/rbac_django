# RBAC_Django

Role-Based Login System with Authentication & Authorization


## Prerequisites

- Python 3.10.5
- PostgreSQL
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Create a virtual environment:
   ```bash
   py -m venv venv
   ```

3. Activate the virtual environment:
     ```bat
     venv\Scripts\activate
     ```


4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration

The project uses PostgreSQL as its database. You can just edit the setup.bat file in root directory.

## Running the Server

Simply run the setup script:
```bash
setup.bat
```

## Project Structure
```
project/
│
├── slate_root/           # Main project directory
│   ├── slate_root/      # Main project app
|   ├── users/           # rbac system
│   └── manage.py        # Django management script
│
├── postman_collection.json # Postman collection for api testing
├── requirements.txt     # Project dependencies
├── setup.bat           # Windows setup script
└── README.md          # Project documentation
```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Django-Rest-Framework](https://www.django-rest-framework.org/) - REST Api
- [PyJWT](https://www.django-rest-framework.org/) - JWT authentication

## Authors

- Ishant Kumar - [ishant9805](https://github.com/ishant9805)
