import utils
import sqlite3
from datetime import datetime, timezone

NEST_DB = '/home/wenshan/Documents/sqlite/climate.db'
NEST_TABLE = 'nest_data'

def insert_data():
    con = sqlite3.connect(NEST_DB)
    cur = con.cursor()
    nest = utils.get_traits()

    now_utc = datetime.now(timezone.utc).replace(second=0, microsecond=0).isoformat().replace("+00:00", "Z")
    cur.execute(f"""
INSERT INTO {NEST_TABLE} (timestamp, temperature, humidity)
VALUES (?, ?, ?)
""", (now_utc, nest['sdm.devices.traits.Temperature']['ambientTemperatureCelsius'], nest['sdm.devices.traits.Humidity']['ambientHumidityPercent']))
    con.commit()
    con.close()

def main():
    insert_data()

if __name__ == "__main__":
    main()
