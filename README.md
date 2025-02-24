# 🎬 FLIX - Movie Rating App  

<div style="text-align: center;">
    <img src="pack/assets/Flix.gif" alt="FLIX Logo" width="600px">
</div>

A **Flask-powered** web application where users can **browse, rate, and review movies**! 🚀 Built with **Flask, SQLAlchemy, Jinja2, and Bootstrap** to deliver a seamless user experience.  

> Special thanks to **Prof. Mukund Jha Sir** for the guidance and inspiration! 🙌  

---

## 🌟 Features  

✔️ **User Authentication** (Login/Register) 🔐  
✔️ **Browse & Search Movies** 🔎  
✔️ **Rate Movies on a 1-10 Scale** ⭐  
✔️ **Write & Read Reviews** 📝  
✔️ **View Personal Rating History** 📜  
✔️ **Responsive & Beautiful UI** 🎨  

![Flix App Demo](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGZuNHhtdXI2eTRqc252cXZxZjg4OXVsbXB0aHIzb28yZGhienNnayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tmH5eUto7WumOdTvRG/giphy.gif)  

---

## 🚀 Tech Stack  

| Technology | Version |
|------------|---------|
| Flask | 3.0.0 |
| SQLAlchemy | 3.1.1 |
| Flask-Bcrypt | 4.0.1 |
| Flask-WTF | 1.2.1 |
| SQLite | Latest |
| Jinja2 | Latest |

---

## 🔥 Installation & Setup  
```bash
✅ Step 1: Clone the Repository  

git clone <your-repository-url>
cd Flask-Project

✅ Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

✅ Step 3: Install Dependencies

pip install -r requirements.txt

✅ Step 4: Run the Application

python run.py

💡 The app will be live at: http://localhost:5000

📂 Project Structure

Flask-Project/
├── pack/
│   ├── __init__.py      # Application initialization
│   ├── models.py        # Database models
│   ├── routes.py        # Route handlers
│   ├── forms.py         # Form definitions
│   ├── utils.py         # Utility functions
│   ├── templates/       # HTML templates
│   ├── assets/
│   │   ├── flix-logo.png  # FLIX logo
├── static/
│   ├── css/             # Stylesheets
│   ├── images/          # Media files
│   ├── gifs/            # Animated GIFs
├── requirements.txt     # Project dependencies
└── run.py              # Application entry point

📜 Database Models

📌 User (Registerdb): Stores user authentication data
📌 Movie: Contains title, description, and release date
📌 Rating: Stores user ratings and reviews

🌍 Routes & Endpoints

📍 /register - User Registration
📍 /login - User Login
📍 /home - Movie Listing Page
📍 /movie/<id> - Movie Details & Ratings
📍 /my-ratings - User’s Rating History
📍 /search - Search for Movies


🤝 Contributing

🔥 Fork the repository
🔥 Create a new branch: git checkout -b feature/new-feature
🔥 Commit changes: git commit -m "Added cool feature"
🔥 Push: git push origin feature/new-feature
🔥 Open a Pull Request



🎬 Enjoy FLIX! 🍿✨

🚀 Give it a Star ⭐ on GitHub if you like it!

# Flask_final
