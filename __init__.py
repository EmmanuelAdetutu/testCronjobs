import datetime
import logging

def main() -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f"Timer trigger function ran at {utc_timestamp}")
    print("This is a scheduled job running from GitHub deployment!")
