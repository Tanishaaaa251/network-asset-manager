import sqlite3

DB_NAME = "assets.db"

def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            ip_address TEXT UNIQUE,
            location TEXT,
            status TEXT DEFAULT 'active'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER NOT NULL,
            description TEXT,
            severity TEXT,
            date_reported TEXT,
            resolved TEXT DEFAULT 'no',
            FOREIGN KEY (asset_id) REFERENCES Assets(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Tables created successfully.")


def insert_asset(asset):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Assets (name, type, ip_address, location, status)
            VALUES (?, ?, ?, ?, ?)
        ''', asset.to_tuple())

        conn.commit()
        print(f"✅ Asset '{asset.name}' added successfully.")

    except sqlite3.IntegrityError:
        print(f"❌ Error: IP {asset.ip_address} already exists.")

    finally:
        conn.close()


def view_all_assets():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Assets")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No assets found.")
    else:
        print("\n========== ALL ASSETS ==========")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Type: {row[2]} | IP: {row[3]} | Location: {row[4]} | Status: {row[5]}")
        print("=================================\n")

def insert_incident(incident):
    conn = connect()
    cursor = conn.cursor()

    try:
        # check if asset exists
        cursor.execute("SELECT id FROM Assets WHERE id = ?", (incident.asset_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"❌ No asset found with ID {incident.asset_id}")
            return

        cursor.execute('''
            INSERT INTO Incidents (asset_id, description, severity, date_reported, resolved)
            VALUES (?, ?, ?, ?, ?)
        ''', incident.to_tuple())

        conn.commit()
        print("✅ Incident added successfully")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        conn.close()

def view_all_incidents():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Incidents.id, Assets.name, Incidents.description,
               Incidents.severity, Incidents.date_reported, Incidents.resolved
        FROM Incidents
        JOIN Assets ON Incidents.asset_id = Assets.id
    ''')

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No incidents found.")
    else:
        print("\n========== ALL INCIDENTS ==========")
        for row in rows:
            print(f"ID: {row[0]} | Asset: {row[1]} | Issue: {row[2]} | Severity: {row[3]} | Date: {row[4]} | Resolved: {row[5]}")
        print("====================================\n")

def resolve_incident(incident_id):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id FROM Incidents WHERE id = ?", (incident_id,))
        result = cursor.fetchone()

        if result is None:
            print("❌ Incident not found")
            return

        cursor.execute("UPDATE Incidents SET resolved = 'yes' WHERE id = ?", (incident_id,))
        conn.commit()
        print("✅ Incident marked as resolved")

    finally:
        conn.close()

def view_incidents_by_asset(asset_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM Assets WHERE id = ?", (asset_id,))
    asset = cursor.fetchone()

    if asset is None:
        print("❌ No asset found")
        conn.close()
        return

    cursor.execute('''
        SELECT id, description, severity, date_reported, resolved
        FROM Incidents
        WHERE asset_id = ?
    ''', (asset_id,))

    rows = cursor.fetchall()
    conn.close()

    print(f"\nIncidents for {asset[0]}:")

    for row in rows:
        print(row)