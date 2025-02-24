from pack import app,db, bcrypt
from flask import render_template,redirect,url_for,flash,session,request
from pack.models import Registerdb, Movie, Rating
from pack.forms import Register,Login, RatingForm, SearchForm
from pack.utils import login_req
from datetime import datetime
from sqlalchemy import or_

@app.route('/Register',methods=['GET','POST'])
def register():
    f=Register()
    if f.validate_on_submit():
        obj=Registerdb.query.filter_by(email=f.email.data).first()
        if obj:
            flash("Email already Registered")
            pass
        else:
            i1 = Registerdb(name=f.name.data,email=f.email.data,passhash=f.password.data)
            db.session.add(i1)
            db.session.commit()
            session['user_id']=int(Registerdb.query.filter_by(email=f.email.data).first().id)
            session.modified = True 
            return redirect(url_for('home'))
    if f.errors != {}:
        for i in f.errors.values():
            flash(i)
            print(i)
    return render_template('register.html',form=f)

@app.route('/login', methods=['GET', 'POST'])
def login():
    f=Login()
    if f.validate_on_submit():
        obj=Registerdb.query.filter_by(email=f.email.data).first()
        if obj:
            if obj.checkpass(f.password.data):
                session['user_id']=int(obj.id)
                session['email']=obj.email
                session.modified = True 
                print(f"✅ Session Set: {session.get('user_id')}, {session.get('email')}") 
                flash('Successfully signed in')
                return redirect(url_for('home'))
            else:
                flash('Incorrect Password')
        else:
            flash("Email Not Registered")
            return redirect(url_for('login'))
    if f.errors != {}:
        for i in f.errors.values():
            flash(i)
            print(i)
    return render_template('login.html',form=f)

@app.route('/')
@app.route('/home')
@login_req
def home():
    search_form = SearchForm()
    print(f"🔍 Checking Session: {session.get('user_id')}")  # Debugging print
    if 'user_id' not in session:
        flash("Session expired, please log in again.")
        return redirect(url_for('login'))
    movies = Movie.query.all()
    return render_template('home.html', movies=movies, search_form=search_form)


@app.route('/Logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('login'))



@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
@login_req
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = RatingForm()
    search_form = SearchForm()
    
    # Get existing rating if any
    user_rating = Rating.query.filter_by(
        user_id=session['user_id'],
        movie_id=movie_id
    ).first()
    
    # If form is submitted and valid
    if form.validate_on_submit():
        if user_rating:
            # Update existing rating
            user_rating.rating = form.rating.data
            user_rating.review = form.review.data
            user_rating.date_posted = datetime.utcnow()
            flash('Your rating has been updated!', 'success')
        else:
            # Create new rating
            rating = Rating(
                rating=form.rating.data,
                review=form.review.data,
                user_id=session['user_id'],
                movie_id=movie_id
            )
            db.session.add(rating)
            flash('Your rating has been added!', 'success')
        
        db.session.commit()
        return redirect(url_for('movie_detail', movie_id=movie_id))

    # Pre-populate form if rating exists
    elif request.method == 'GET' and user_rating:
        form.rating.data = user_rating.rating
        form.review.data = user_rating.review

    return render_template('movie_detail.html', 
                         movie=movie,
                         form=form,
                         user_rating=user_rating,
                         search_form=search_form)

@app.route('/my_ratings')
@login_req
def my_ratings():
    search_form = SearchForm()
    user_id = session.get('user_id')
    ratings = Rating.query.filter_by(user_id=user_id).order_by(Rating.date_posted.desc()).all()
    return render_template('my_ratings.html', 
                         ratings=ratings, 
                         search_form=search_form)

@app.route('/search')
@login_req
def search():
    search_form = SearchForm()
    query = request.args.get('search_query', '')
    if query:
        movies = Movie.query.filter(
            or_(
                Movie.title.ilike(f'%{query}%'),
                Movie.description.ilike(f'%{query}%')
            )
        ).all()
    else:
        movies = []
    
    return render_template('search_results.html', 
                         movies=movies, 
                         query=query, 
                         search_form=search_form)



