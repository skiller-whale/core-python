# Skiller Whale, Exercises for Core Python

This repo includes exercises to accompany Skiller Whale sessions on the core features of Python 3.

During each session you'll be asked to write and edit code in some of the files.

## Using `sync.py` With a Local Python Installation

1. Make sure your Python version is `>= 3.10`. You can check the version you have installed by running:
    ```sh
    python3 --version
    ```

2. Clone this repository onto your computer. You can do this in a terminal by using:
    ```sh
    git clone https://github.com/skiller-whale/core-python.git
    ```

3. In a terminal, navigate to the `core-python` directory you cloned.

4. Make sure you have the `requests` package installed in a Python 3 environment. You can do that by running these two commands:
    ```sh
    python3 -m ensurepip
    python3 -m pip install requests
    ```

5. To check this is all set up, run `python3 sync.py` and enter your attendance ID when prompted. You shouldn't see any errors.

6. At the end of the session termimnate the sync script with `Ctrl + C`.

## Using `docker`

1. Clone this repository onto your computer. You can do this in a terminal by using:
    ```sh
    git clone https://github.com/skiller-whale/core-python.git
    ```

2. Open the repository directory in a code editor, and replace the contents of the `attendance_id` file, so that it contains only your unique attendance ID for the session (and nothing else).

3. In a terminal, navigate to the `core-python` directory you cloned.

4. Run the following two commands to start the sync script:
    ```sh
    docker compose up --build -d
    docker compose run exercises
    ```

    The very first time you run this it might take a while to download and build some docker images, but the future times you run it should be quicker.

    Python is installed inside the Docker container you downloaded, so you won't need to separately install it, and running the exercises won't affect any other local Python installations.

    The `docker compose up` process will continue running in the background, and watch for any file changes in the repo.

5. At the end of the session, exit the `exercises` container (e.g. by running `exit`), then run the following to shutdown the sync container:
    ```sh
    docker compose down
    ```
