Instructions: 
git clone https://github.com/Ashvith20/Fastapi-Groq.git
create your virtual environment -  python -m venv myvenv 
create .env file and create OPENAI_API_KEY=your groq api key
Use command ------> uvicorn main:app --reload
Once the server is running, click the port number (e.g., http://127.0.0.1:8000) shown in the terminal to open the app in your browser.
Once the server is running, you can access the interactive API docs at:
Swagger UI: http://127.0.0.1:8000/docs
click on POST/Generate endpoint - click try it yourself
Enter any question as prompt
click Execute
