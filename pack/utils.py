from functools import wraps
from flask import session,flash,redirect,url_for


def login_req(func):
    @wraps(func)
    def function(*a,**b):
        print(f"🔍 DEBUG: Session Data Before Check - {session}")  
        if 'user_id' not in session:
            flash('⚠️ Login first to continue')
            print("🔍 DEBUG: User not logged in. Redirecting to login page.") 
            return redirect(url_for('login'))
        print("✅ User is logged in! Proceeding to the requested page.")
        return func(*a,**b) 
    return function