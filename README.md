
# Customizing Artist API using DRF

This repo contain a Django Rest Framework API which are used to create a new artist, retrive a artist by thier name, or by thier work type("YT", "IG") etc.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Shivam1272/drf_artists_api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd drf_artists_api
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux or MacOS
    venv\Scripts\activate  # Windows
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (for accessing the admin panel):

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The API will be available at http://localhost:8000/.

## API Endpoints

- ### Register User
  - Endpoint: `/api/register/`
  - Method: `POST`
  - Request body:

  ```json
  {
      "username": "yourusername",
      "firstname": "Your",
      "lastname": "Name",
      "work_type": "YT",
      "link": "https://youtube.com/yourusername",
      "password": "yourpassword"
  }
  ```
  
- ### Obtain Authentication Token
  - Endpoint: `/api/token/`
  - Method: `POST`
  - Request body:
  ```json
  {
      "username": "yourusername",
      "password": "yourpassword"
  }
  ```
  
- ### Get Works
  - Endpoint: `/api/works/`
  - Method: `GET`
  - Headers:
  ```bash
  Authorization: Token yourauthtoken
  ```
 I used POSTMAN for testing Here are the steps:

<img width="892" alt="image" src="https://github.com/Shivam1272/drf_artists_api/assets/96972819/f436038a-631b-436b-b580-3743d8ae8a75">

- ### Get Artist
  - Endpoint: `/api/artists/`
  - Method: `GET`
  - Headers:
  ```bash
  Authorization: Token yourauthtoken
  ```

- ### Query

  * Endpoint: `/api/works?work_type=YT`
      - Method: `GET`
      - Headers:
  
      ```plaintext
      Authorization: Token yourauthtoken
      ```
  
  * Endpoint: `/api/works?artist=username`
      - Method: `GET`
      - Headers:
  
      ```plaintext
      Authorization: Token yourauthtoken
      ```

## Admin Panel

Access the admin panel at http://localhost:8000/admin/ with the superuser credentials.


### Additional Notes
- Replace placeholders like `yourusername`, `yourpassword`, and yourauthtoken with actual values.
- Customize the project as needed based on your specific requirements.
