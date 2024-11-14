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
    - On prefered:
      ```bash
      pip install virtualenv
      ```
      ```bash
      virtualenv venv
      ```
      OR
      
    - Or use this:
       ```bash
        python3 -m venv venv
        ```
   
    

5. **Activate the virtual environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

6. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

7. **Set up environment variables**:
    Create a `.env` file in the root directory with the following variables:
   
   - [Download env file ](https://drive.google.com/file/d/1vY-Z_xF3Jjzf6QnjP7yrvUSif0l71g82/view?usp=sharing)
 
    ```plaintext
   STABILITY_API_KEY : <SECRET>
    DEVELOPMENT : false / true
    LINKEDIN_APP_ID : <SECRET>
    LINKEDIN_API: <SECRET>
    X_CONSUMER_API_KEY: <SECRET>
    X_CONSUMER_API_SECRET: <SECRET>
    X_ACCESS_TOKEN_KEY: <SECRET>
    X_ACCESS_TOKEN_SECRET: <SECRET>
    X_CLIENT_SECRET: <SECRET>
    X_BEARER_TOKEN: <SECRET>
    ```

9. **Run the server**:
    ```bash
    set FLASK_APP=run.py
    ```
    ```bash
    flask run
    ```

10. **Access the application**: By default, the server will run on [http://localhost:5000](http://localhost:5000).

## User Instruction

1. Start the Flask Server
2. Open http://localhost:5000 in your web browser.
   
   -[![Screenshot-2024-11-14-141743.png](https://i.postimg.cc/zXdm5YgL/Screenshot-2024-11-14-141743.png)](https://postimg.cc/7fTtMcXD)

4. **Add a New Article**: On the web page, fill out the form fields to add a new article.
    - Submitting the form updates the article.json file

5. **Monitor Changes**: A Python script running in a separate thread monitors article.json for changes.
    This script detects new articles and triggers automated content processing, allowing the main thread (Flask server) to remain responsive.

6. **Check Console Logs**: Keep an eye on the terminal or console to see logs of the processing steps, including:
    - Summary generation
    - AI-driven image creation (if credits are available)
    - Simulated social media posts (printed in logs)
      
7. **Simulated Social Media Posts**: The script prints simulated LinkedIn and Twitter posts in the console.
    Following are the links to socialmedias.
    - [LinkedIn ](https://www.linkedin.com/in/f-schuppe-4b6588338/recent-activity/all/)
    - [X.com (Twitter) ](https://x.com/SchuppeFelicia)

   [![Screenshot-2024-11-14-142321.png](https://i.postimg.cc/JngyS25S/Screenshot-2024-11-14-142321.png)](https://postimg.cc/34XJv96Z)


## Usage

1. **Monitor JSON Feed**: The script will automatically detect new articles from a local JSON feed (`feed.json`). You can simulate adding new articles with **NOT EXISTING UNIQUE ID** to this file to trigger the automation. Please Note : Default values will not feed  as it may triggers the processing API and to Avoid Image Generation from getting Exhaust (only 10 credits) before testing  . Monitoring function will scan for change in JSON and all of this related to monitoring will run in seperate thread so the main thread remain open to REST api.

3. **Automated Content Processing**: Each new article will have a summary generated, an AI-driven image created, and then a mock post to a social media channel (just prints ).

4. **Engagement Data**: User engagement (views, shares, etc.) will be simulated and stored in an SQLite database for tracking purposes.

5. **REST API**: A REST API endpoint provides access to the top 3 articles based on engagement metrics.

   - **Default Behavior**: Returns the top 3 articles for both views and shares.
   - **Query Parameter**:
     - `type=most_viewed`: Returns the top 3 articles based on views only.
     - `type=most_shared`: Returns the top 3 articles based on shares only.

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
