# genai-starter

This project provides a starter template for building a GenAI application focused on generating and managing text embeddings using Google Generative AI.

---

## End-to-End App Development Steps

### 1. Project Structure & Initialization
- Organize code in a package structure under `src/genai_start/`.
- Ensure each module has an `__init__.py` file.
- Create a `tests/` directory for unit tests.

### 2. Environment & Configuration
- Store API keys and sensitive configs in a `.env` file.
- Use the `config.py` module to load environment variables.
- Add `.env` to `.gitignore` to keep secrets safe.

### 3. Core Functionality
- Implement embedding logic in `101_text_embedding.py`.
- Include functions for:
  - Generating embeddings.
  - Saving/loading embeddings.
  - Error handling and logging.

### 4. Packaging
- Ensure `setup.py` and `setup.cfg` are configured for distribution.
- Test package installation locally with `pip install .`.

### 5. Testing
- Write unit tests for all major functions (using `pytest` or `unittest`).
- Place tests in the `tests/` directory.

### 6. Documentation
- Add docstrings to all functions and classes.
- Update this `README.md` with:
  - Project overview
  - Installation instructions
  - Usage examples
  - Testing instructions

### 7. Dockerization
- Create a `Dockerfile` to containerize the app.
- Build and test the Docker image locally.
- Use `docker-compose.yml` to run multiple scripts/services if needed.

### 8. Automation
- Add a Makefile or shell scripts for common tasks (test, build, run).
- Optionally set up CI/CD for automated testing and building.

### 9. Distribution
- (Optional) Publish to PyPI for easy installation via `pip`.
- Tag releases in version control.

### 10. Deployment & Usage
- Deploy the Docker container to your preferred environment (local/cloud).
- Test the end-to-end workflow: input → embedding → output.

---

## Quickstart

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd genai-starter
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file with your API keys and configs.

4. **Run the embedding script:**
    ```sh
    python -m genai_start.101_text_embedding
    ```

5. **Run with Docker:**
    ```sh
    docker compose up
    ```

---

## Project Structure

genai-starter/ │
├── src/ │ └── genai_start/ │ 
                ├── init.py │ 
                ├── 101_text_embedding.py │ 
                └── config.py 
├── data/ │ 
            └── embeddings/ │ 
                            └── text_embeddings/ 
├── tests/ 
├── setup.py 
├── setup.cfg 
├── Dockerfile 
├── docker-compose.yml 
├── requirements.txt 
└── README.md