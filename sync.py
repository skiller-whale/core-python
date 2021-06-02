import requests
import os
import json
import hashlib
import threading
import time
from urllib.parse import urljoin

WATCHED_EXTS = [".py", ".ipynb"]
# site-packages is found in a Python environment (which includes LOTS of .py files)
IGNORE_DIRS = [".git", ".ipynb_checkpoints", "site-packages", "bin"]


ASCII_ART = """
  _____ _    _ _ _            __          ___           _
 / ____| |  (_) | |           \\ \\        / / |         | |
| (___ | | ___| | | ___ _ __   \\ \\  /\\  / /| |__   __ _| | ___
 \\___ \\| |/ / | | |/ _ \\ '__|   \\ \\/  \\/ / | '_ \\ / _` | |/ _ \\
 ____) |   <| | | |  __/ |       \\  /\\  /  | | | | (_| | |  __/
|_____/|_|\\_\\_|_|_|\\___|_|        \\/  \\/   |_| |_|\\__,_|_|\\___|

"""


SERVER_URL = os.getenv('SERVER_URL', "https://train.skillerwhale.com")


def create_skiller_whale_url(path):
    return urljoin(SERVER_URL, path)


class Updater:
    def __init__(self, attendance_id):
        self.attendance_id = attendance_id

    @property
    def uri(self):
        return create_skiller_whale_url(self.path)

    @property
    def path(self):
        return f'attendances/{self.attendance_id}/file_snapshots'

    @staticmethod
    def get_file_data(path):
        with open(path, "r") as f:
            data ={"relative_path": path, "contents": f.read()}
            return json.dumps(data)

    @staticmethod
    def get_headers(data):
        return {
            "Content-Type": "application/json",
            "Content-Length": str(len(data))
        }

    def post_file(self, path):
        data = self.get_file_data(path)
        headers = self.get_headers(data)
        try:
            response = requests.post(self.uri, data=data, headers=headers)
        except requests.exceptions.ConnectionError:
            print(f"Failed\nCould not reach {SERVER_URL}")
        else:
            print(f"Status: {response.status_code}")
            if response.text:
                print(response.text)

    def send_file_update(self, path):
        print(f"Uploading: {path}", end='\t')
        if not self.attendance_id:
            print("No attendance id set; file update not sent.")
            return
        self.post_file(path)


class Pinger:
    def __init__(self, attendance_id):
        self.attendance_id = attendance_id

    @property
    def uri(self):
        return create_skiller_whale_url(self.path)

    @property
    def path(self):
        return f'attendances/{self.attendance_id}/pings'

    def ping(self):
        try:
            requests.post(self.uri)
        except requests.exceptions.ConnectionError as err:
            print("Connection error:", err)
            pass  # Tolerate failed pings

    def start(self, wait_time=1):
        while True:
            try:
                self.ping()
            except Exception as err:
                # This should not be reached except in exceptional circumstances
                # We want to continue looping even if we hit an unexpected error
                print("Unexpected error with ping:", err)

            # Send a ping every `wait_time` seconds
            time.sleep(wait_time)


class Watcher:
    def __init__(self, updater, base_path='.'):
        self.updater = updater
        self.base_path = base_path
        self._file_hashes = {}
        # Tracks whether this is the first pass of the directory tree. If not,
        # then any new file encountered will be treated as an update.
        self._first_pass = True

    @staticmethod
    def get_file_hash(path):
        """Return a hash digest of the file located at path"""
        with open(path, "rb") as f:
            contents = f.read()
            return hashlib.md5(contents).hexdigest()

    def _post_file_if_changed(self, path):
        _, extension = os.path.splitext(path)
        if extension not in WATCHED_EXTS:
            return

        hashed = self.get_file_hash(path)
        if not self._first_pass:
            old_hash = self._file_hashes.get(path)
            if old_hash != hashed:
                try:
                    self.updater.send_file_update(path)
                except Exception as err:
                    # This has to be fairly generic to handle any updater
                    print("Unexpected error in updater class:", err)
        self._file_hashes[path] = hashed

    def _check_dir_for_changes(self, dir_path):
        if os.path.basename(dir_path) in IGNORE_DIRS:
            return

        for filename in os.listdir(dir_path):
            new_path = os.path.join(dir_path, filename)
            if os.path.isdir(new_path):
                # Recursively check subdirectories
                self._check_dir_for_changes(new_path)
            else:
                self._post_file_if_changed(new_path)

    def poll_for_changes(self, wait_time=1):
        while True:
            try:
                self._check_dir_for_changes(self.base_path)
            except Exception as err:
                # This should not be reached except in exceptional circumstances
                # We want to continue looping even if we hit an unexpected error
                print("Unexpected error in file watcher:", err)
            else:
                self._first_pass = False

            # Poll for changes every `wait_time` seconds, whether or not the
            # previous call succeeded.
            time.sleep(wait_time)


def skiller_whale_sync():
    print(ASCII_ART)
    attendance_id = input("Please copy and paste your ID from the course "
                          "page here and press enter.\n")
    print("")
    print("Great! We're going to start watching this directory for changes "
          "so that the trainer can see your progress.")
    print("Hit Ctrl+C to stop.")

    updater = Updater(attendance_id=attendance_id)
    pinger = Pinger(attendance_id=attendance_id)
    watcher = Watcher(updater=updater)

    # Start ping service in a separate daemon thread
    threading.Thread(target=pinger.start, daemon=True).start()
    watcher.poll_for_changes()


if __name__ == "__main__":
    skiller_whale_sync()
