import pyodbc
import psutil
import argparse

parser = argparse.ArgumentParser(description="Clears saved crews from local PCREditor.")
parser.add_argument('--username', required=True, help='Local SQL Username')
parser.add_argument('--password', required=True, help='Local SQL Password')
args = parser.parse_args()

# Close TabletPCR if running
for process in psutil.process_iter():
    if process.name().lower() == 'tabletpcr.exe':
        process.kill()

try:
    # Use pyodbc to connect to SQL Server using Native CLient 11.0 (SQL EXPRESS 2016)
    connection_string = (
        "DRIVER={SQL Server Native Client 11.0};"
        "SERVER=(local)\\SQLEXPRESS;"
        "UID=" + args.username + ";"
        "PWD=" + args.password + ";"
        "DATABASE=PCREditor;"
    )
    conn = pyodbc.connect(connection_string)
    print("Connection to SQL Server established successfully.")

    try:
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE SHIFTS")
            cursor.execute("TRUNCATE TABLE SHIFT_CREW")
            conn.commit()
        print('Successfully purged saved crews.')
    except Exception as e:
        print(f'Operation Failed. {e}')
    finally:
        conn.close()
except pyodbc.Error as e:
    print(f"ODBC Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
