from database import (create_tables, insert_asset, view_all_assets,
                      insert_incident, view_all_incidents, resolve_incident,
                      view_incidents_by_asset)
from models.asset import Asset
from models.incident import Incident
from datetime import date


def add_asset_flow():
    print("\n--- Add Asset ---")
    name = input("Name: ").strip()

    # Validation for asset type
    while True:
        asset_type = input("Type (router/switch/server): ").strip().lower()
        if asset_type in ["router", "switch", "server"]:
            break
        print("❌ Invalid type. Enter router/switch/server")

    ip = input("IP: ").strip()
    location = input("Location: ").strip()

    asset = Asset(name, asset_type, ip, location)
    insert_asset(asset)


def add_incident_flow():
    print("\n--- Add Incident ---")
    view_all_assets()

    try:
        asset_id = int(input("Enter Asset ID: ").strip())
    except ValueError:
        print("❌ Invalid ID")
        return

    description = input("Description: ").strip()

    # Validation for severity
    while True:
        severity = input("Severity (low/medium/high): ").strip().lower()
        if severity in ["low", "medium", "high"]:
            break
        print("❌ Invalid severity")

    today = str(date.today())

    incident = Incident(asset_id, description, severity, today)
    insert_incident(incident)


def resolve_incident_flow():
    print("\n--- Resolve Incident ---")
    view_all_incidents()

    try:
        incident_id = int(input("Enter Incident ID: ").strip())
        resolve_incident(incident_id)
    except ValueError:
        print("❌ Invalid ID")


def view_incidents_by_asset_flow():
    print("\n--- View Incidents by Asset ---")
    view_all_assets()

    try:
        asset_id = int(input("Enter Asset ID: ").strip())
        view_incidents_by_asset(asset_id)
    except ValueError:
        print("❌ Invalid ID")


def main():
    create_tables()

    while True:
        print("\n========================================")
        print("   Network Asset & Incident Manager")
        print("========================================")
        print("1. Add Asset")
        print("2. View Assets")
        print("3. Add Incident")
        print("4. View Incidents")
        print("5. View Incidents by Asset")   # NEW
        print("6. Resolve Incident")
        print("7. Exit")
        print("----------------------------------------")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_asset_flow()
        elif choice == "2":
            view_all_assets()
        elif choice == "3":
            add_incident_flow()
        elif choice == "4":
            view_all_incidents()
        elif choice == "5":
            view_incidents_by_asset_flow()
        elif choice == "6":
            resolve_incident_flow()
        elif choice == "7":
            print("\nExiting program...\n")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()