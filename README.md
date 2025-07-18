# xnest

xnest is a lightweight integration script for interacting with the Google Nest API and storing device data locally in a SQLite database.

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `secrets.py`

In the root directory, create a file named `secrets.py` and fill in the following fields:

```python
project_id = "<your_project_id>"
client_id = "<your_client_id>"
client_secret = "<your_client_secret>"
access_token = "<your_access_token>"
refresh_token = "<your_refresh_token>"
device_id = "<your_device_id>"
```

### 4. Set Up SQLite

Create a SQLite database and table to store the data. Then update the `NEST_DB` and `NEST_TABLE` variables in `nest_cron.py` to point to your database and table.

### 5. Run the Script

You can run the script using either:

```bash
./run.sh
```

or

```bash
python3 nest_cron.py
```
