from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from config import auth, fdb

app = Flask(__name__)
app.secret_key = "seginf"

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not session.get("user"):
      return redirect(url_for("login"))
    return f(*args, **kwargs)
  return decorated_function

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            account_info = auth.get_account_info(user['idToken'])
            print("logged")
            if account_info['users'][0]['emailVerified']:
                # Email is verified, allow user to log in
                print("Email is verified")
                session['user'] = user['localId']
                return redirect(url_for('dashboard'))
                print("Redirecting to dashboard")
            else:
                # Email is not verified, redirect user to a page informing them to verify their email
                return render_template('login.html', message='El correo no ha sido verificado')
        except Exception as e:
            return render_template('login.html', message='El correo o la contraseña son incorrectos')
    else:
        return render_template('login.html')

#Logout
@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for("login"))


#Registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        phone_number = request.form['phone_number']

        if password == confirm_password:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                fdb.child("users").child(user['localId']).set({
                    "email": email,
                    "phone_number": phone_number
                })

                auth.send_email_verification(user['idToken'])

                return redirect('/')
            except Exception as e:
                return render_template('register.html', error=str(e))
        else:
            return render_template('register.html', message="Passwords do not match.")
    else:
        return render_template('register.html')

#Reseteo de contraseña
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        try:
            auth.send_password_reset_email(email)
            return render_template('reset_password.html', message='Email de reseteo de contrasena enviado con exito')
        except:
            return render_template('reset_password.html', error='El correo no esta registrado')

    return render_template('reset_password.html')

#Pagina principal (tabla)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)