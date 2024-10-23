# Item Management API with Django REST Framework

This project is a simple Django application designed to help you understand how to write REST APIs and perform CRUD operations using Django and Django REST Framework. The API allows for the creation, retrieval, updating, and deletion of items, each with a first name, description, and price.

## Features

- **Create** item (POST)
- **Retrieve** all items (GET)
- **Retrieve** specific item by ID (GET)
- **Update** item details (PUT)
- **Delete** item (DELETE)

## Technologies Used

- Django
- Django REST Framework
- SQLite (default database)

## Getting Started

### Prerequisites

Make sure you have Python and pip installed. This project is built with:

- Python 3.x
- Django 4.x
- Django REST Framework

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/item-management-api.git
   cd item-management-api
   ```

2. **Install the required packages:**

   ```
   pip install django djangorestframework
            ```

3. **Run migrations:**

   ```
   python manage.py migrate
   

4. **Run the server:**

   ```
   python manage.py runserver
   

### API Endpoints

1. **Create Item**
   - **URL:** \`/api/items/\`
   - **Method:** \`POST\`
   - **Body:**
     ```json
     {
       "first_name": "Item Name",
       "description": "Description of the item",
       "price": 19.99
     }
     ```

2. **Retrieve All Items**
   - **URL:** \`/api/items/\`
   - **Method:** \`GET\`

3. **Retrieve Specific Item**
   - **URL:** \`/api/items/<id>/\`
   - **Method:** \`GET\`

4. **Update Item**
   - **URL:** \`/api/items/<id>/\`
   - **Method:** \`PUT\`
   - **Body:**
     ```json
     {
       "first_name": "Updated Item Name",
       "description": "Updated description",
       "price": 24.99
     }
     ```

5. **Delete Item**
   - **URL:** \`/api/items/<id>/\`
   - **Method:** \`DELETE\`

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
