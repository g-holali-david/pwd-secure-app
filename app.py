from flask import Flask, render_template, request, redirect, session, flash, jsonify
from utils import redis_client, hash_password, verify_password
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Charge la configuration

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test-redis', methods=['GET'])
def test_redis():
    """Test de connexion à Redis."""
    try:
        if redis_client and redis_client.ping():
            return jsonify({"status": "success", "message": "Redis is connected!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if redis_client.hexists('users', username):
            flash('Ce nom d’utilisateur existe déjà.', 'danger')
            return redirect('/register')

        hashed_password = hash_password(password)
        redis_client.hset('users', username, hashed_password)

        flash('Inscription réussie ! Connectez-vous.', 'success')
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        stored_hash = redis_client.hget('users', username)

        if stored_hash and verify_password(stored_hash, password):
            session['loggedin'] = True
            session['username'] = username
            session['ip'] = request.remote_addr  # Stocker l'IP utilisateur
            flash('Connexion réussie !', 'success')
            return redirect('/dashboard')
        else:
            flash('Identifiants incorrects.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        total_users = len(redis_client.hkeys('users'))  # Nombre total d'utilisateurs

        return render_template('dashboard.html', username=session['username'], 
                               ip=session['ip'], total_users=total_users)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('ip', None)
    flash('Déconnecté avec succès.', 'info')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
