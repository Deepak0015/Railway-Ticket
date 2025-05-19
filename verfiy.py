from deepface import DeepFace 
import os 

# temp_image  = '/home/saaho/Desktop/Kumerash/trainproject/temp_images/capture.jpg'
# register_folder = '/home/saaho/Desktop/Kumerash/trainproject/static/uploads'

# matched = False

# for filname in os.listdir(register_folder):
#     if filname.lower().endswith('.jpg'):
#         file_path = os.path.join(register_folder, filname)

#         try:
#             result = DeepFace.verify(img1_path=temp_image, img2_path=file_path, enforce_detection=False)
            
#             if result['verified']:
#                 matched = True
#                 print(f"✅ Match found: {file_path}")
#                 break  # Optional: stop at first match

#         except Exception as e:
#             print(f"❌ Error comparing {file_path}: {e}")

# if not matched:
#     print('❌ No match found')
from admin_auth import DATABASE ,DATABASES
import sqlite3
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

def check_database():
    import os
    import sqlite3
    from deepface import DeepFace
    from flask import jsonify

    matched = False 
    matched_results = []

    register_folder = '/home/saaho/Desktop/Kumerash/trainproject/static/uploads'
    temp_image = '/home/saaho/Desktop/Kumerash/trainproject/temp_images/capture.jpg'

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

    if matched:
        return jsonify({
            'success': True,
            'match': True,
            'matched_faces': matched_results
        })
    else:
        return jsonify({'success': True, 'match': False})
