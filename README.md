# Skiller Whale, Exercises for Core Python

This repo includes exercises to accompany Skiller Whale sessions on the core features of Python 3

During each session you'll be asked to write and edit code in some of the files. 

## Using `docker` (recommended):

1. Clone the repository at `https://github.com/skiller-whale/core-python.git` onto your computer.

2. If this isn't your first Core Python session, then navigate to the exercises you cloned last time, and ensure you have the latest code by running `git pull`.

3. Open the repository directory in a code editor, and replace the contents of the `attendance_id` file, so that it just contains your unique id for the session.

4. In a terminal, navigate to the directory of the repository you just cloned, then run the following two commands:

```
docker compose up --build -d
docker compose run exercises
```

The very first time you run this it might take a while to download and build some docker images, but the future times you run it should be quicker.

Python is installed inside the Docker container you downloaded, so you won't need to separately install it, and running the exercises won't affect any other local Python installations.

The `docker compose up` process will continue running in the background, and watch for any file changes in the repo.

## Legacy instructions:

Make sure your Python version is `>= 3.10`. You can check the version you have installed by running:

```sh
python3 --version
```

2. Clone the repository at `https://github.com/skiller-whale/core-python.git` onto your computer.

3. In a terminal, navigate to the `core-python` directory you cloned.

4. Make sure you have the `requests` package installed in a Python 3 environment.
You could do that by running these two commands:

```sh
python3 -m ensurepip
python3 -m pip install requests
```

5. To check this is all set up, run `python3 sync.py` and enter your unique user id when prompted. You shouldn't see any errors.

7. When you need to stop the sync script, you can terminate it with `Ctrl + C`.