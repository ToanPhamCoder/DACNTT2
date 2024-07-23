## Setup

1. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your MongoDB connection string:

    ```env
    MONGODB_URL=mongodb://localhost:27017/bhx?retryWrites=true&w=majority
    ```

4. Run the application:

    ```sh
    python run.py
    ```

## Endpoints

- `GET /home/` - Welcome endpoint
- `GET /category/` - Get frequent categories
- `GET /products/` - Get frequent products
- `GET /products/search?name={name}` - Search products by name
-
