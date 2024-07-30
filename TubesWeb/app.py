from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Pembeli, Pesanan, Produk, Pembayaran, Alamat

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# @app.before_first_request
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        kata_sandi = request.form['kata_sandi']
        telepon = request.form.get('telepon')

        pembeli_baru = Pembeli(nama=nama, email=email, kata_sandi=kata_sandi, telepon=telepon)
        db.session.add(pembeli_baru)
        db.session.commit()
        flash('Registrasi berhasil! Silakan login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        kata_sandi = request.form['kata_sandi']

        pembeli = Pembeli.query.filter_by(email=email, kata_sandi=kata_sandi).first()
        if pembeli:
            flash('Login berhasil!')
            return redirect(url_for('profile', id=pembeli.id))
        else:
            flash('Login gagal. Silakan coba lagi.')
    return render_template('login.html')

@app.route('/profile/<int:id>')
def profile(id):
    pembeli = Pembeli.query.get_or_404(id)
    return render_template('profile.html', pembeli=pembeli)

@app.route('/product')
def product():
    produk = Produk.query.all()
    return render_template('product.html', produk=produk)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Tangani pengiriman formulir di sini
        # Proses data dan redirect atau tampilkan konfirmasi
        return redirect(url_for('finish'))
    return render_template('checkout.html')

@app.route('/finish')
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)
