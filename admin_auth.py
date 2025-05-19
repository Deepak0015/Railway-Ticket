from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename


admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

DATABASE = 'webcam7.db'
DATABASES = 'session.db'
USER_DB = 'logindetails3.db'

VALID_ADMINS = {
    "mariselvam": "mari"
}

@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('adminlogin.html')
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in VALID_ADMINS and VALID_ADMINS[username] == password:
        return jsonify({"success": True, "redirect": "/admin/dashboard"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

@admin_bp.route('/dashboard')
def admin_dashboard():
    return render_template('admin.html')

@admin_bp.route('/get_users')
def get_users():
    try:
        conn = sqlite3.connect(USER_DB)
        c = conn.cursor()
        c.execute("SELECT rowid, uname, email, password FROM register7")
        rows = c.fetchall()
        users = [{'id': r[0], 'username': r[1], 'email': r[2], 'password': r[3]} for r in rows]
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        conn.close()

@admin_bp.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    conn = sqlite3.connect(USER_DB)
    c = conn.cursor()
    c.execute("DELETE FROM register7 WHERE rowid=?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})




@admin_bp.route('/get_tickets')
def get_tickets():
    try:
        all_tickets = []
        
        # Get single journey tickets
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT rowid as id, *FROM booking02")
        
        for row in cursor.fetchall():
            all_tickets.append({
                'id': row[0],
                'type': 'single',
                'username': row[1],
                'from_station': row[2],
                'to_station': row[3],
                'date': row[4],
                'end_date': '',
                'gender': row[5],
                'mobile': row[6],
                'email': row[7],
                'amount': row[8],
                'image_path': row[9],
                'booking_date': row[10],
                'status': row[11]
            })
        conn.close()

        # Get season pass tickets
        conns = sqlite3.connect(DATABASES)
        cursor = conns.cursor()
        cursor.execute("SELECT rowid as id, * FROM sesbooking02 ")
        
        for row in cursor.fetchall():
            all_tickets.append({
                'id': row[0],
                'type': 'season',
                'username': row[1],
                'from_station': row[2],
                'to_station': row[3],
                'date': row[4],
                'end_date': row[5],
                'gender': row[6],
                'mobile': row[7],
                'email': row[8],
                'amount': row[9],
                'image_path': row[10],
                'booking_date': row[11],
                'status': row[12]
            })
        conn.close()

        return jsonify(all_tickets)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/cancel_ticket/<int:ticket_id>', methods=['POST'])
def cancel_ticket(ticket_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # First try to update single journey ticket
        cursor.execute("""
            UPDATE booking02 
            SET action='cancelled' 
            WHERE rowid=? AND action='active'
        """, (ticket_id,))
        affected = cursor.rowcount
        conn.commit()
        
        # If no rows affected, try season pass
        if affected == 0:
            conns = sqlite3.connect(DATABASES)
            cursors = conns.cursor()
            cursors.execute("""
                UPDATE sesbooking02 
                SET action='cancelled' 
                WHERE rowid=? AND action='active'
            """, (ticket_id,))
            affected = cursors.rowcount
            conns.commit()
            conns.close()
        
        conn.close()
        
        if affected == 0:
            return jsonify({'error': 'Ticket not found or already cancelled'}), 404
            
        return jsonify({'success': True, 'message': 'Ticket cancelled successfully'})
        
    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/delete_ticket/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        # Try to delete from single journey tickets first
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM booking02 WHERE rowid=?", (ticket_id,))
        affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        # If not found in single journey, try season pass
        if affected == 0:
            conn = sqlite3.connect(DATABASES)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sesbooking02 WHERE rowid=?", (ticket_id,))
            conn.commit()
            conn.close()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
from deepface import DeepFace 
    
@admin_bp.route('/verify_face', methods=['POST'])
def verify_face():
    try:
        image_file = request.files['image']
        if not image_file:
            return jsonify({'success': False, 'message': 'No image uploaded'})

        filename = secure_filename(image_file.filename)
        path = os.path.join("temp_images", filename)
        os.makedirs("temp_images", exist_ok=True)
        image_file.save(path)
        #+++++++++++++++++++++
       

    #     for rowid , uname , image_path in rows:
    #         try:
    #             filename =  os.path.join(register_folder , image_path)
    #             print(filename)
    #             result = DeepFace.verify(img1_path=temp_image , img2_path=filename , enforce_detection= False)
    #             if result['verified']:
    #                 print(f"✅ Match found: {image_path}")
    #                 matched_users.append({
    #                     'booking_id': rowid,
    #                     'username': uname,
    #                     'image_path': image_path
    #                 })
            

    #         except Exception as e:
    #             print(f"❌ Error verifying {image_path}: {e}")
    #     print(matched_users[1]['username'])
    #     if matched_users:
    #         return jsonify({
    #         'success': True,
    #         'match': True,
    #         # 'matches': matched_users  ,# ✅ return full list
    #         'username':matched_users[0]['username'], 
    #         'booking_id':matched_users[0]['booking_id']
    #     })
    #     else:
    #         return jsonify({'success': True, 'match': False})

    
    # except Exception as e:
    #     print(e)
    #     return jsonify({'success': False, 'message': str(e)})

        # matched_file = None
        # register_folder = '/home/saaho/Desktop/Kumerash/trainproject/static/uploads'
        # temp_image  = '/home/saaho/Desktop/Kumerash/trainproject/temp_images/capture.jpg'

        # matched = False
        # conn = sqlite3.connect(DATABASE)
        # c = conn.cursor()
        # c.execute("SELECT rowid, uname, image FROM booking02" )
        # rows = c.fetchall()
        # conn.close()
        # conn_s = sqlite3.connect(DATABASE)
        # c_s = conn_s.cursor()
        # c_s.execute("SELECT rowid, uname, image FROM sesbooking02" )
        # rows_s = c_s.fetchall()
        # conn_s.close()
      
        
        # for rowid , username , filname in rows:
        #     if filname.lower().endswith('.jpg'):
        #         file_path = os.path.join(register_folder, filname)

        #         try:
        #             result = DeepFace.verify(img1_path=temp_image, img2_path=file_path, enforce_detection=False)
                    
        #             if result['verified']:
        #                 matched = True
        #                 matched_file  =  filname
        #                 print(f" Match found: {file_path}")
        #                 break  # Optional: stop at first match

        #         except Exception as e:
        #             print(f"Error comparing {file_path}: {e}")

      

        # if not matched_file:
        #                     return jsonify({'success': True, 'match': False, 'message': 'No matching face found'})
        


        
        # print(matched_file)
        # conn = sqlite3.connect(DATABASE)
        # c = conn.cursor()
        # c.execute("SELECT rowid, uname, image FROM booking02 WHERE image = ?", (matched_file,))
        # rows = c.fetchall()
        # conn.close()

        # # Simulated matching logic
        # match_found = bool(rows)
        # if match_found:
        #     return jsonify({
        #         'success': True,
        #         'match': True,
        #         'username': rows[0][1],
        #         'booking_id': rows[0][0]
        #     })
        # else:
        #     return jsonify({'success': True, 'match': False})
        matched = False 
        matched_results = []

        register_folder = 'static/uploads'
        temp_image = 'temp_images/capture.jpg'

        databases = [DATABASE, DATABASES]  # Ensure these are defined paths like 'webcam7.db', etc.

        for db_path in databases:
            if db_path == 'webcam7.db':
                query = "SELECT rowid, uname, image FROM booking02" 
            else:
                query = "SELECT rowid, uname, image FROM sesbooking02"

            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute(query)
                rows = c.fetchall()
                conn.close()
            except Exception as e:
                print(f"Error reading {db_path}: {e}")
                continue

            for rowid, username, filename in rows:
                if not filename or not filename.lower().endswith('.jpg'):
                    continue

                filepath = os.path.join(register_folder, filename)
                try:
                    result = DeepFace.verify(img1_path=temp_image, img2_path=filepath, enforce_detection=False)
                    if result.get('verified'):
                        matched = True
                        matched_results.append({
                            'username': username,
                            'booking_id': rowid,
                            'matched_image': filename,
                        
                        })
                except Exception as e:
                    print(f" Error comparing {filepath}: {e}")
        print('matched results ' ,matched_results)
        if matched:
            return jsonify({
                'success': True,
                'match': True,
                'matched_faces': matched_results
            })
        else:
            return jsonify({'success': True, 'match': False})


    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@admin_bp.route('/logout')
def logout():
    return render_template('mainpage.html')



        




