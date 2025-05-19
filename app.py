from flask import Flask, request, jsonify, render_template, url_for, flash, session,redirect,make_response,Blueprint
import mysql.connector
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import blue, black
from io import BytesIO
import os
import io
import base64
import pymysql
import secrets
import uuid
import time
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from admin_auth import admin_bp
from deepface import DeepFace 





app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.register_blueprint(admin_bp, url_prefix='/admin')


saved_image_path=""
# SQLite database file
DATABA = 'logindetails3.db'

# Initialize SQLite database
def initialize_databas():
    conn = sqlite3.connect(DATABA)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS register7 (
            uname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the app starts
initialize_databas()

# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            error = "All fields are required..."
        else:
            # Connect to the SQLite database
            conn = sqlite3.connect(DATABA)
            cursor = conn.cursor()

            # Check user credentials
            query = "SELECT uname, password FROM register7 WHERE email = ?"
            cursor.execute(query, (email,))
            user = cursor.fetchone()

            if user:
                db_uname, db_password = user
                if password == db_password:  # Check if passwords match
                    # Set session variables
                    session["uname"] = db_uname
                    session["email"] = email
                    session["password"] = db_password
                    flash("Login successful!", "success")
                    return redirect(url_for("dashboard"))
                else:
                    error = "Enter the password correctly...."
            else:
                error = "Invalid email or password."
            cursor.close()
            conn.close()

    return render_template("login1.html", error=error)

# Register Route
@app.route('/register', methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        uname = request.form.get("uname")
        email = request.form.get("email")
        password = request.form.get("password")

        if not uname or not email or not password:
            error = "All fields are required."
        else:
            conn = sqlite3.connect(DATABA)
            cursor = conn.cursor()
            query = "SELECT * FROM register7 WHERE email = ?"
            cursor.execute(query, (email,))
            if cursor.fetchone():
                error = "The email already exists."
            else:
                query = "INSERT INTO register7 (uname, email, password) VALUES (?, ?, ?)"
                try:
                    cursor.execute(query, (uname, email, password))
                    conn.commit()
                    flash("Registration successful!", "success")
                    return redirect(url_for("login"))
                except sqlite3.Error as e:
                    error = f"An error occurred: {str(e)}"
            cursor.close()
            conn.close()

    return render_template("register.html", error=error)


# Forgot password route
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        conn = sqlite3.connect(DATABA)
        cursor = conn.cursor()
        
        # Check if email exists
        cursor.execute("SELECT * FROM register7 WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if not user:
            error = "Email not found"
            conn.close()
            return render_template('forgot_password.html', error=error)

        if new_password != confirm_password and new_password =="" or confirm_password =="":
            error = "Passwords do not match"
            return render_template('forgot_password.html', error=error)
        
        
        # Update password
        cursor.execute("UPDATE register7 SET password = ? WHERE email = ?", (new_password, email))
        conn.commit()
        conn.close()
        
        success = "Password updated successfully. You can now login with your new password."
        return render_template('forgot_password.html', success=success)
    
    return render_template('forgot_password.html')


# Dashboard Route
@app.route("/dashboard")
def dashboard():
    if "uname" in session and "email" in session:
        return render_template("instructions.html", uname=session["uname"], email=session["email"])
    else:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))
    
@app.route("/first")
def first():
    return render_template("firstpage.html", uname=session["uname"], email=session["email"])
    

@app.route('/')
def mainpage():
    return render_template("mainpage.html")

@app.route('/admin')
def admin():
    return render_template("adminlogin.html")
   
# Logout Route
@app.route("/")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

@app.route('/image')
def image():
    return render_template("image.html")

@app.route('/firstpage')
def firstpage():
    return render_template("firstpage.html")

@app.route('/registe')
def registe():
    return render_template("register.html")


# SQLite database file
DATABASE = 'webcam7.db'

# Initialize SQLite database
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking02 (
            uname TEXT,
            place1 TEXT,
            place2 TEXT,
            dates TEXT,
            gender TEXT,
            mobile TEXT,
            emailid TEXT,
            amount TEXT,
            image TEXT,
            booking_date TEXT,
            action TEXT
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the app starts
initialize_database()

error=""
emailid = ""
image=""
@app.route("/table", methods=['POST'])
def table():
    global error
    global emailid 
    global saved_image_path # Make the variable accessible globally
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('uname', '')
        place1 = request.form.get('place1', '')
        place2 = request.form.get('place2', '')
        dates = request.form.get('dates', '')
        gender = request.form.get('gender', '')
        phone = request.form.get('phone', '').strip()
        emailid = request.form.get('emailid', '')
        amount = request.form.get('amounts', '')
        image = saved_image_path

        # Get current date
        booking_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD

        empty_fields = []

        # Check each field
        if not image:
            empty_fields.append("image")
        if not dates:
            empty_fields.append("journey date")
        if not place1:
            empty_fields.append("starting place")
        if not place2:
            empty_fields.append("destination place")

        # If there are empty fields, return the error message
        if empty_fields:
            error = f"The following fields are empty: {', '.join(empty_fields)}. Please fill them in."
            return render_template("firstpage.html", uname=name, email=emailid, image=image, phone=phone, error=error)
        else:
            try:
                conn = sqlite3.connect(DATABASE)
                cursor = conn.cursor()
                action="active"
                query = """
                    INSERT INTO booking02 ( uname, place1, place2, dates, gender, mobile, emailid, amount, image, booking_date,action)
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                """
                cursor.execute(query, ( name, place1, place2, dates, gender, phone, emailid, amount, image, booking_date,action))
                conn.commit()
                error = "Booking successful!"
                image=""
                saved_image_path=""
                flash('Booking successful!', 'success')
                return render_template("firstpage.html", uname=name, email=emailid, error=error)
            except sqlite3.Error as e:
                return f"Database Error: {str(e)}"
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()


# SQLite database file
DATABASES = 'session.db'

# Initialize SQLite database
def initialize_database():
    conn = sqlite3.connect(DATABASES)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sesbooking02 (
            uname TEXT,
            place1 TEXT,
            place2 TEXT,
            start_date TEXT,
            end_date TEXT,
            gender TEXT,
            mobile TEXT,
            emailid TEXT,
            amount TEXT,
            image TEXT,
            booking_date TEXT,
            action TEXT
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the app starts
initialize_database()

error=""
emailid = ""
image=""
@app.route("/sespass", methods=['POST'])
def sespass():
    global error
    global emailid 
    global saved_image_path # Make the variable accessible globally
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('uname', '')
        place1 = request.form.get('from_station', '')
        place2 = request.form.get('to_station', '')
        start_date = request.form.get('start-date', '')
        end_date = request.form.get('end-date', '')
        gender = request.form.get('gender', '')
        phone = request.form.get('phone', '').strip()
        emailid = request.form.get('emailid', '')
        amount = request.form.get('amounts1', '')
        image = saved_image_path

        # Get current date
        booking_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD

        empty_fields = []

        # Check each field
        if not image:
            empty_fields.append("image")
        if not start_date:
            empty_fields.append("journey date")
        if not end_date:
            empty_fields.append("end date")
        if not place1:
            empty_fields.append("starting place")
        if not place2:
            empty_fields.append("destination place")

        # If there are empty fields, return the error message
        if empty_fields:
            error = f"The following fields are empty: {', '.join(empty_fields)}. Please fill them in."
            return render_template("firstpage.html", uname=name, email=emailid, image=image, phone=phone, error=error)
        else:
            try:
                conn = sqlite3.connect(DATABASES)
                cursor = conn.cursor()
                action="active"
                query = """
                    INSERT INTO sesbooking02 ( uname, place1, place2, start_date, end_date, gender, mobile, emailid, amount, image, booking_date,action)
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?,?)
                """
                cursor.execute(query, ( name, place1, place2, start_date, end_date, gender, phone, emailid, amount, image, booking_date,action))
                conn.commit()
                error = "Booking successful!"
                print(end_date)
                image=""
                saved_image_path=""
                return render_template("firstpage.html", uname=name, email=emailid, error=error)
            except sqlite3.Error as e:
                return f"Database Error: {str(e)}"
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()


# Ensure the upload directory exists

@app.route("/form")
def form():
    return redirect(url_for("upload"))







saved_image_path = "none"

# Load YOLOv10 model (using the new v10 weights)
model = YOLO('yolov10l.pt')  # Changed from yolov8m.pt to yolov10m.pt
from ultralytics import YOLO
model_v1 = YOLO("/home/saaho/Desktop/Kumerash/trainproject/Models/best (copy 1).pt")


# Create uploads directory if not exists
if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_face():
    global saved_image_path
    try:
        if 'image' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No image uploaded'
            }), 400

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No image selected'
            }), 400
        # Read image
        img_bytes = image_file.read()
        img_np = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({
                'status': 'error',
                'message': 'Failed to decode image'
            }), 400
        
        # Run YOLOv10 detection (same API as v8 but with v10 improvements)
        results = model(img)
        results_2 =  model_v1(img)
        
        # Check for faces and obstructions
        face_detected = False
        obstruction_detected = False
        obstruction_types = []
        person_count = 0
        
        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                
                # Check for person (class 0 in COCO dataset)
                if cls == 0 and conf > 0.5:
                    person_count += 1
                    face_detected = True
                
                # Check for sunglasses (class 1 in custom model)
                if cls == 1 and conf > 0.5:
                    obstruction_detected = True
                    obstruction_types.append("sunglasses")
                
                # Check for masks (class 2 in custom model)
                if cls == 2 and conf > 0.5:
                    obstruction_detected = True
                    obstruction_types.append("mask")
                
                # Check for hats (class 3 in custom model)
                if cls == 3 and conf > 0.5:
                    obstruction_detected = True
                    obstruction_types.append("hat")
        print(results_2)
        for results in results_2:
            if hasattr(result , 'boxes') and results.boxes is not None:
                for box in results.boxes:
                    cls =  int(box.cls[0])
                    if cls == 0:
                        obstruction_detected =  True  
                        obstruction_types.append('glass')
            else:
                print("No Glass found")

            
    
        # Check if exactly one face is detected and no obstructions
        if person_count == 1 and not obstruction_detected:
            # Save the valid image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"valid_face_{timestamp}.jpg"
            save_path = os.path.join('static', 'uploads', filename)
        
            cv2.imwrite(save_path, img)
            saved_image_path = filename
        
            # Convert image to base64 for display
            _, img_encoded = cv2.imencode('.jpg', img)
            img_base64 = base64.b64encode(img_encoded).decode('utf-8')
            
            return jsonify({
                'status': 'success',
                'message': 'Face validated successfully',
                'image': img_base64,
                'redirect': url_for('success_page')
            })
        else:
            error_message = "Validation failed. "
            if person_count == 0:
                error_message += "No face detected. "
            elif person_count > 1:
                error_message += f"Multiple faces detected ({person_count}). "
            if obstruction_detected:
                error_message += f"Obstructions detected: {', '.join(obstruction_types)}. "
            error_message += "Please position your face clearly without glasses, masks, or hats."
            
            return jsonify({
                'status': 'error',
                'message': error_message
            }), 400

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500

@app.route('/success')
def success_page():
    return render_template('success.html', image_path=saved_image_path)



   










@app.route('/show')
def show_data():
    email_filter = session["email"]
    try:
        all_records = []
        
        # Connect to webcam7.db (single journey tickets)
        conn1 = sqlite3.connect(DATABASE)
        conn1.row_factory = sqlite3.Row
        cursor1 = conn1.cursor()
        
        # Fetch single journey tickets
        cursor1.execute("""
            SELECT *, 
                   NULL as end_date, 
                   NULL as start_date,
                   'single' as ticket_type 
            FROM booking02 
            WHERE emailid = ?
        """, (email_filter,))
        single_journeys = cursor1.fetchall()
        all_records.extend([dict(row) for row in single_journeys])
        
        # Connect to session.db (season passes)
        conn2 = sqlite3.connect(DATABASES)
        conn2.row_factory = sqlite3.Row
        cursor2 = conn2.cursor()
        
        # Fetch season passes
        cursor2.execute("""
            SELECT *, 
                   'season' as ticket_type 
            FROM sesbooking02 
            WHERE emailid = ?
        """, (email_filter,))
        season_passes = cursor2.fetchall()
        all_records.extend([dict(row) for row in season_passes])
        
        # Sort by booking_date (newest first)
        all_records.sort(key=lambda x: x['booking_date'], reverse=True)
        
        return render_template("bookhis.html", 
                            records=all_records,
                            email=email_filter, 
                            uname=session.get("uname", ""))
    except sqlite3.Error as e:
        return f"Error: {str(e)}"
    finally:
        if 'cursor1' in locals(): cursor1.close()
        if 'conn1' in locals(): conn1.close()
        if 'cursor2' in locals(): cursor2.close()
        if 'conn2' in locals(): conn2.close()


@app.route('/cancel_ticket', methods=['POST'])
def cancel_ticket():
    try:
        uname = request.form['uname']
        ticket_type = request.form['ticket_type']
        
        if ticket_type == 'season':
            # Cancel season pass
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            
            conn = sqlite3.connect(DATABASES)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE sesbooking02 
                SET action = 'cancelled' 
                WHERE uname = ? AND start_date = ? AND end_date = ?
            """, (uname, start_date, end_date))
            
        else:
            # Cancel single journey ticket
            dates = request.form['dates']
            
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE booking02 
                SET action = 'cancelled' 
                WHERE uname = ? AND dates = ?
            """, (uname, dates))
            
        conn.commit()
        flash('Ticket cancelled successfully!', 'success')
        return redirect(url_for('show_data'))
        
    except Exception as e:
        flash(f'Error cancelling ticket: {str(e)}', 'error')
        return redirect(url_for('show_data'))
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
    # Redirect back to the booking records page
    return redirect(url_for('show_data'))



@app.route('/download_ticket', methods=['POST'])
def download_ticket():
    
    
    # Get form data
    uname = request.form.get('uname')
    place1 = request.form.get('place1')
    place2 = request.form.get('place2')
    amount = request.form.get('amount')
    ticket_type = request.form.get('ticket_type')
    
    if ticket_type == 'season':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        dates = f"{start_date} to {end_date}"
    else:
        dates = request.form.get('dates')
    
    # Create PDF in memory
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=18,
        alignment=1,  # Center aligned
        spaceAfter=20
    )
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=14,
        alignment=1,
        spaceAfter=10
    )
    normal_style = styles['Normal']
    bold_style = ParagraphStyle(
        'Bold',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        spaceAfter=5
    )
    
    # Content
    elements = []
    
    # Title
    elements.append(Paragraph("Metro Railway Ticket", title_style))
    elements.append(Spacer(1, 10))
    
    # Ticket type
    ticket_title = "Season Pass" if ticket_type == 'season' else "Single Journey Ticket"
    elements.append(Paragraph(ticket_title, subtitle_style))
    elements.append(Spacer(1, 20))
    
    # Ticket details
    data = [
        ["Passenger Name:", uname],
        ["From:", place1],
        ["To:", place2],
        ["Date(s):", dates],
        ["Amount:", f"₹{amount}"],
        ["Status:", "Confirmed"]
    ]
    
    # Create table
    table = Table(data, colWidths=[2*inch, 3*inch])
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 30))
    
    # Add QR code placeholder (replace with actual QR code generation if needed)
    elements.append(Paragraph("Scan this QR code at the station:", bold_style))
    # In a real app, you would generate or use an actual QR code image here
    # elements.append(Image("path/to/qr_code.png", width=2*inch, height=2*inch))
    elements.append(Paragraph("[QR Code Placeholder]", normal_style))
    
    # Terms and conditions
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Terms & Conditions:", bold_style))
    terms = [
        "1. This ticket is non-transferable.",
        "2. Please carry valid ID proof when traveling.",
        "3. Ticket must be presented for inspection when requested.",
        "4. No refunds for lost or stolen tickets."
    ]
    for term in terms:
        elements.append(Paragraph(term, normal_style))
    
    # Build PDF
    doc.build(elements)
    
    # Get PDF content
    pdf = buffer.getvalue()
    buffer.close()
    
    # Create response
    response = make_response(pdf)
    filename = f"Metro_Ticket_{uname}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'

    return response
    
    
@app.route('/delete_ticket', methods=['POST'])
def delete_ticket():
    try:
        # Get form data
        uname = request.form['uname']
        ticket_type = request.form['ticket_type']
        
        if ticket_type == 'season':
            # Delete season pass ticket
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            
            conn = sqlite3.connect(DATABASES)  # Use session.db for season passes
            cursor = conn.cursor()
            
            # Delete the record
            cursor.execute("""
                DELETE FROM sesbooking02 
                WHERE uname = ? AND start_date = ? AND end_date = ?
            """, (uname, start_date, end_date))
            
        else:
            # Delete single journey ticket
            dates = request.form['dates']
            
            conn = sqlite3.connect(DATABASE)  # Use webcam7.db for single tickets
            cursor = conn.cursor()
            
            # Delete the record
            cursor.execute("""
                DELETE FROM booking02 
                WHERE uname = ? AND dates = ?
            """, (uname, dates))
        
        conn.commit()
        flash('Ticket deleted successfully!', 'success')
        
    except sqlite3.Error as e:
        conn.rollback()
        flash(f'Error deleting ticket: {str(e)}', 'error')
        
    except Exception as e:
        flash(f'Unexpected error: {str(e)}', 'error')
        
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()
    
    return redirect(url_for('show_data'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)


