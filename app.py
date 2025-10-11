# app.py

import sqlite3
import uuid
import os
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# --- Configuration & Initialisation ---
DATABASE_FILE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            email TEXT,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            poste_id INTEGER NOT NULL,
            access_token TEXT UNIQUE NOT NULL
        );
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def provision_access_on_controller(token, start_time, end_time, poste_id):
    print(f"--> [SIMULATION] Envoi des infos d'accès à l'automate pour le jeton : {token}")
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tarifs')
def tarifs():
    return render_template('tarifs.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        user_name = request.form['userName']
        booking_date = request.form['bookingDate']
        start_t = request.form['startTime']
        end_t = request.form['endTime']
        poste_id = request.form['posteId']
        
        start_iso = f"{booking_date}T{start_t}"
        end_iso = f"{booking_date}T{end_t}"

        access_token = f"tok_{uuid.uuid4().hex}"

        is_provisioned = provision_access_on_controller(access_token, start_iso, end_iso, poste_id)

        if not is_provisioned:
            return "Erreur critique : impossible de générer votre accès.", 500

        try:
            conn = sqlite3.connect(DATABASE_FILE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO bookings (user_name, start_time, end_time, poste_id, access_token) VALUES (?, ?, ?, ?, ?)",
                (user_name, start_iso, end_iso, poste_id, access_token)
            )
            conn.commit()
        finally:
            conn.close()
        
        return redirect(url_for('confirmation'))

    return render_template('reservation.html')

@app.route('/api/bookings')
def get_bookings():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT user_name, start_time, end_time, poste_id FROM bookings")
        rows = cursor.fetchall()
        
        events = [
            {
                "title": f"Réservé - Poste {row['poste_id']}",
                "start": row['start_time'],
                "end": row['end_time'],
                "color": '#a87c7c',
                "display": 'background'
            }
            for row in rows
        ]
        return jsonify(events)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
