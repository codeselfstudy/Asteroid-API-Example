Sample App
==========

I put together this quick Flask site to demo some things that people asked about at the past couple of meetups.

To run this site on your computer:

1. Clone this repo.
1. Make a Python 3 virtualenv. See below for details.
1. Install the requirements with `pip install -r requirements.txt`.
1. Run the server: `python app.py`.
1. Visit [http://localhost:5002/](http://localhost:5002/)

## Python 3 Virtualenvs

On Ubuntu, I use this command, which I've aliased to `mkve3`:

    alias mkve3='mkvirtualenv --python=\`which python3\`'

You can probably also use Python 3's [venv feature](https://docs.python.org/3/library/venv.html).
