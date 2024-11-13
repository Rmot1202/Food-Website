
# Food Menu Website 

This is a Flask-based web application that features a responsive food menu, dynamic content fetched from the **Spoonacular API**, and an integrated chatbot powered by **OpenAI's GPT-3.5-turbo**. The chatbot enhances user interaction by providing automated responses for inquiries.

## Features

### Web Pages
- **Home Page**: Displays a carousel with featured dishes and a "Food of the Day" section.
- **Menu Page**: Shows a grid of dishes fetched from the Spoonacular API, including images and a "See Recipe" button.
- **About Page**: Provides the business history, mission statement, and team introductions with an inspirational quote.
- **Contact Page**: Features a contact form for inquiries and a star rating system for feedback.

### Chatbot Integration
- A chatbot interface allows users to interact and receive responses for questions and guidance.
- The `/chat` route handles chat requests using OpenAI's API and responds dynamically.

## Technologies Used
- **Python**: The main programming language.
- **Flask**: The web framework used for serving HTML templates and handling API requests.
- **HTML5/CSS3/JavaScript**: For the frontend structure, styling, and interactivity.
- **Bootstrap 5.3.2**: Ensures responsive design and UI components.
- **OpenAI GPT-3.5-turbo**: Powers the chatbot for generating intelligent responses.
- **Spoonacular API**: Supplies dynamic data for the food menu.
- **dotenv** (optional): For managing environment variables securely.

## Getting Started

### Prerequisites
- **Python 3.7+**
- **Flask**: Install via `pip install flask`.
- **OpenAI API Key**: Ensure you have an OpenAI API key set up in your environment.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/food-menu-website.git
   cd food-menu-website
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**:
   Create a `.env` file in the project root with the following line:
   ```bash
   OPENAI_API_KEY=your-actual-api-key
   ```

5. **Run the Flask app**:
   ```bash
   python chat.py
   ```

6. **Access the website**:
   Open your web browser and go to `http://127.0.0.1:5000`.

### Project Structure
```
├── template
│   ├── Home.html
│   ├── about.html
│   ├── contact.html
│   ├── menu.html
├── chat.py
├── requirements.txt
└── README.md
```

### Environment Variables
Ensure your environment includes:
- **OPENAI_API_KEY**: Your OpenAI API key.

### Security Note
**Do not** hardcode sensitive information like API keys. Use environment variables or a `.env` file managed by `python-dotenv`.

## How to Use

### Chatbot
- Navigate to the **Contact Page**.
- Interact with the chatbot interface by typing in your message.
- The chatbot will respond or display a modal prompt for further assistance.

### Contact Form
- Use the form on the **Contact Page** to submit inquiries and rate your experience.

## Future Enhancements
- Add user authentication and session management.
- Store user ratings and contact form submissions in a database.
- Implement more advanced chatbot features like multi-turn dialogue memory.

