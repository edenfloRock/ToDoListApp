# To-Do List App with SQL Lite

This project is simple ToDo List App using SQL Lite.

To-Do App created with Flet.
Some notes:
- This is a full app => UI + Database function
- Slighlty longer video but with more explanations.
- Database is local with sqlite3


- Download project
```sh
git clone
```
- Create virtual environment and install dependencies:
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# if Error libmpv.so.1
s udo apt install libmpv-dev
#find files libmpv
sudo find / -name "libmpv.so*"
# create link
sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1

```

- Run application
```sh
flet -r app.py
```
