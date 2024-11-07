# Automated Content Posting and Social Sharing

## Overview
This project automates the process of detecting new articles from a JSON feed, generating a summary, creating an AI-driven image, and posting the content to a mock social media channel. It also stores user engagement data in an SQLite database and exposes a simple REST API endpoint to retrieve the top 3 articles based on engagement metrics.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Postman Collection](#postman-collection)
- [API Documentation](#api-documentation)
- [Screenshot](#screenshot)
- [License](#license)

## Technologies Used
- **Python**: Programming language for backend and automation.
- **Flask**: Web framework for building the RESTful API.
- **SQLite**: Lightweight database to store engagement data.
- **stable diffusion**: oUsed for generating AI-driven images based on article keywords trial only 4 image generation .
- **Flask-SQLAlchemy**: For SQLite integration in the Flask app.

## Installation

### Prerequisites
- **Python** (version 3.7+ recommended)
- **SQLite** (included in Python standard library)
- **OpenAI API Key** (for DALL-E image generation)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Akhancode/automate_content.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd automate_content
    ```

3. **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Set up environment variables**:
    Create a `.env` file in the root directory with the following variables:
    ```plaintext
    STABILITY_API_KEY = api_key
    ```

7. **Run the server**:
    ```bash
    flask run
    ```

8. **Access the application**: By default, the server will run on [http://localhost:5000](http://localhost:5000).

## Usage

1. **Monitor JSON Feed**: The script will automatically detect new articles from a local JSON feed (`feed.json`). You can simulate adding new articles to this file to trigger the automation.

2. **Automated Content Processing**: Each new article will have a summary generated, an AI-driven image created, and then a mock post to a social media channel (just prints ).

3. **Engagement Data**: User engagement (views, shares, etc.) will be simulated and stored in an SQLite database for tracking purposes.

4. **REST API**: A simple API is exposed to retrieve the top 3 articles based on engagement data.

### API Endpoints

 - [Explore the API with Postman](https://www.postman.com/restless-moon-684338/workspace/lcx-assessment/collection/30275964-dbc92cec-9daf-41b7-894c-377117887a20?action=share&creator=30275964)
 - [![Screenshot-2024-11-07-134246.png](https://i.postimg.cc/fTGMMkL1/Screenshot-2024-11-07-134246.png)](https://postimg.cc/PPQg4X1M)
  
Example response:
```json
{
    "top_3_by_shares": [
        {
            "article_url": "https://example.com/full-article",
            "id": 12,
            "image_url": "image_url",
            "shares": "shares",
            "summary": "summary",
            "title": "title",
            "views": "views"
        },
        {
            "article_url": "https://example.com/full-article",
            "id": 17,
            "image_url": "kdjfk",
            "shares": 91,
            "summary": "xiz",
            "title": "xyz-130",
            "views": 10
        },
        {
            "article_url": "https://example.com/full-article",
            "id": 6,
            "image_url": "kdjfk",
            "shares": 9,
            "summary": "xiz",
            "title": "xyz-10",
            "views": 10
        }
    ],
    "top_3_by_views": [
        {
            "article_url": "https://example.com/full-article",
            "id": 12,
            "image_url": "image_url",
            "shares": "shares",
            "summary": "summary",
            "title": "title",
            "views": "views"
        },
        {
            "article_url": "https://example.com/full-article",
            "id": 5,
            "image_url": "kdjfk",
            "shares": 6,
            "summary": "xiz",
            "title": "xyz-9",
            "views": 10
        },
        {
            "article_url": "https://example.com/full-article",
            "id": 6,
            "image_url": "kdjfk",
            "shares": 9,
            "summary": "xiz",
            "title": "xyz-10",
            "views": 10
        }
    ]
}
