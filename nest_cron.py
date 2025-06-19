import utils
import sqlite3
from datetime import datetime

NEST_DB = 'nest.db'
NEST_TABLE = 'nest_data'

def insert_data():
    con = sqlite3.connect(NEST_DB)
    cur = con.cursor()
    nest = utils.get_traits()

    now = datetime.now().replace(second=0, microsecond=0).strftime("%Y-%m-%d %H:%M")
    cur.execute(f"""
INSERT INTO {NEST_TABLE} (timestamp, temperature, humidity)
VALUES (?, ?, ?)
""", (now, nest['sdm.devices.traits.Temperature']['ambientTemperatureCelsius'], nest['sdm.devices.traits.Humidity']['ambientHumidityPercent']))
    con.commit()
    con.close()

def main():
    insert_data()

if __name__ == "__main__":
    main()
    