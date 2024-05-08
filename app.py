from flask import Flask, render_template,request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import hashlib





app = Flask(__name__)
app.config['SECRET_KEY'] = "uygwyifyehcvbuibyibcvylisbvuibswvbyiswbgi;"

def db_conn():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Timothy123#",
        port = "5432")
    return conn




@app.route("/add-products", methods = [ 'POST'])
def add_products():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        prod_id = request.form.get("product_id")
        prod_name = request.form.get("product_name")
        product_description = request.form.get("product_description")
        product_category = request.form.get("product_category")
        product_owner = request.form.get("product_owner")
        product_price = request.form.get("product_price")
        product_image = request.files.get("product_image")
        if product_image:
            image_data = product_image.read()
        else:
            image_data = None
        if not prod_id:
            flash('Insert a Product ID', category = "error")
        elif not prod_name:
            flash('Insert a Product Name', category='error')
        elif not product_description:
            flash('Insert a Product Description', category='error')
        elif not product_category:
            flash('Insert a Product Category', category= 'error')
        elif not product_owner:
            flash('Insert a Product Owner', category= 'error')
        elif not product_price:
            flash('Insert a Product Price', category= 'error')
        elif not image_data:
            flash('Insert a Product Image', category= 'error')
        else:
            flash("Account created!", category="success")
        
        cur.execute('''INSERT INTO "BuyBest".product(prod_id, prod_name, prod_description, product_category, prod_owner, prod_price, prod_image) VALUES(%s, %s,%s,%s,%s,%s,%s)''', (prod_id, prod_name, product_description, product_category, product_owner, product_price, psycopg2.Binary(image_data)))
        conn.commit()
        cur.close()
        conn.close()
        redirect("/admin")
    return render_template('admin.html')

@app.route('/update-products')
def update_products():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        prod_id = request.form.get("product_id")
        prod_name = request.form.get("product_name")
        product_description = request.form.get("product_description")
        product_category = request.form.get("product_category")
        product_owner = request.form.get("product_owner")
        product_price = request.form.get("product_price")
        product_image = request.files.get("product_image")
        if product_image:
            image_data = product_image.read()
        else:
            image_data = None
        if not prod_id:
            flash('Insert a Product ID', category = "error")
        elif not prod_name:
            flash('Insert a Product Name', category='error')
        elif not product_description:
            flash('Insert a Product Description', category='error')
        elif not product_category:
            flash('Insert a Product Category', category= 'error')
        elif not product_owner:
            flash('Insert a Product Owner', category= 'error')
        elif not product_price:
            flash('Insert a Product Price', category= 'error')
        elif not image_data:
            flash('Insert a Product Image', category= 'error')
        else:
            flash("Account created!", category="success")
        
        cur.execute('''UPDATE "BuyBest".product SET prod_name=%s, prod_description=%s, product_category=%s, prod_owner=%s, prod_price=%s, prod_image=%s WHERE id=%s ''', (prod_name, prod_id, prod_name, product_description, product_category, product_owner, product_price, product_image))
        conn.commit()
        cur.close()
        conn.close()
        redirect(url_for('admin.html'))
    return render_template('admin.html')

@app.route('/delete-products')
def delete_products():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        prod_id = request.form.get("product_id")
        cur.execute('''DELETE "BuyBest".product WHERE prod_id=%s''', (prod_id,))
        conn.commit()
        cur.close()
        conn.close()
        redirect(url_for('admin.html'))
    return render_template('admin.html')


@app.route('/admin')
def admin():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "BuyBest".product ''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html',data= data)


@app.route('/cart')
def cart():
    if request.method == 'POST':
        userName = request.form.get("user_id")
        prod_id = request.form.get("product_id")
        quantity = request.form.get("quantity")
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('''INSERT INTO "BuyBest".cart(prod_id, userName, quantity) VALUES(%s, %s,%s,%s,%s,%s,%s)''', (userName,prod_id, quantity ))
        conn.commit()
        cur.close()
        conn.close()
        redirect(url_for('products'))
    return render_template("cart.html")

@app.route('/addcart')
def addCart():
    if request.method == 'POST':
        userName = request.form.get("user_id")
        prod_id = request.form.get("product_id")
        quantity = int(request.form.get("quantity"))
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('''INSERT INTO "BuyBest".cart(prod_id, userName, quantity) VALUES(%s, %s,%s)''', (userName,prod_id, quantity ))
        row = cur.fetchone()


        conn.commit()
        cur.close()
        conn.close()
        redirect(url_for('products'))
    return render_template("cart.html")


@app.route('/payment')
def payment():
    if request.method == 'POST':
        conn = db_conn()
        cur = conn.cursor()
        userName= request.form.get("userName")
        card_number= request.form.get("card_number")
        name_on_card = request.form.get("name_on_card")
        billing_address = request.form.get("billing address")
        expiry_date= request.form.get("expiry_date")
        cvv = request.form.get("cvv")
        shipping_address = request.form.get("shipping_address")
        if not userName:
            flash('Insert a Product ID', category = "error")
        elif not card_number:
            flash('Insert a Product Name', category='error')
        elif not name_on_card:
            flash('Insert a Product Category', category= 'error')
        elif not billing_address:
            flash('Insert a Product Owner', category= 'error')
        elif not expiry_date:
            flash('Insert a Product Price', category= 'error')
        elif not cvv:
            flash('Insert a Product Image', category= 'error')
        else:
            flash("Account created!", category="success")
        cur.execute('INSERT INTO "BuyBest".shipping(user_id, shipping_address)' 'VALUES(%s, %s)',(userName, shipping_address ))
        cur.execute('INSERT INTO "BuyBest".payment(user_id, card_number,name_on_card, billing_address ,expiry_date, cvv)' 'VALUES(%s, %s,%s,%s,%s,%s)',(userName, card_number, name_on_card, billing_address, expiry_date, cvv ))
        conn.commit()
        cur.close()
        conn.close()
        redirect(url_for('order_confirmation.html'))
    return render_template("payment.html")

@app.route('/products')
def products():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "BuyBest".product''' )
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return render_template('products.html', data = data)
    

@app.route('/product-description')
def product_description():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "BuyBest".product'''  )
    data = cur.fetchall()
    cur.close()
    conn.close()
    if 'logged_in' in session:
        return render_template('product_description.html', data = data)
    else:
        return redirect('/login')

@app.route('/order-confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        conn = db_conn()
        cur = conn.cursor()
        
        def hash_password(password):
                password_bytes = password.encode('utf-8')

                sha256 = hashlib.sha256()
                sha256.update(password_bytes)
                password_hash = sha256.hexdigest()
                return password_hash
        hashed_password = hash_password(password)

        cur.execute('''SELECT * FROM "BuyBest".users WHERE user_id= %s AND password= %s''', (username, hashed_password ))
        
        if len(username)< 4:
            flash('User name must be greater than 2 characters', category='error')
        elif len(password) < 7:
            flash('Passwords must be greater than 7 characters', category= 'error')
        else:
            flash("Login Successful!", category="success")
            return redirect("/products")
        conn.commit()
        cur.close()
        conn.close()
       
    return render_template('login.html')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/')
def logout():
    session['logged_in'] = False
    flash("Logout Successfully!", category="success")
    return render_template("welcome.html")

@app.route('/account')
def account():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "BuyBest".users ''')
    user = cur.fetchone()
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return render_template("account.html", data = data)

@app.route('/register', methods=["GET", "POST"])
def register():
    conn = db_conn()
    cur = conn.cursor()
    if request.method == 'POST':
        username = request.form.get("username")
        name = request.form.get("name")
        email_address= request.form.get("email_address")
        phone_no = request.form.get("phone_no")
        address = request.form.get("address")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if len(email_address) < 4:
            flash('Email must be greater than 3 characters', category = "error")
        elif len(username)< 4:
            flash('Username must be greater than 2 characters', category='error')
        elif password != confirm_password:
            flash('Passwords do not match!', category='error')
        elif len(password) < 7:
            flash('Passwords must be greater than 7 characters', category= 'error')
        else:
            def hash_password(password):
                password_bytes = password.encode('utf-8')

                sha256 = hashlib.sha256()
                sha256.update(password_bytes)
                password_hash = sha256.hexdigest()
                return password_hash
            password_hash = hash_password(password)
            
            
            cur.execute('INSERT INTO "BuyBest".users(user_id, name, email_address, phone_no, address, password)' 'VALUES(%s, %s,%s,%s,%s, %s)', (username, name, email_address, phone_no, address, password_hash ))
            conn.commit()
            
            flash("Account created!", category="success")
            return redirect("/login")
    
        cur.close()
        conn.close()
        return redirect(url_for("index"))
    return render_template('register.html')
if __name__=="__main__":
    app.run(debug= True)
