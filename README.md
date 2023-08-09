
# Quote API

## Run Locally

From the project directory:

```bash
  docker-compose up -d
```

Setup the database with a 'GET' request to  '/setup_database':

```bash
  curl 'localhost:5000/setup_database'
```

The backend is ready to return quotes!

---

To run tests locally, first install dependencies:

```bash
  pip install -r requitements.txt
```

and initialize the database with: 

```bash
  python init_database.py
```
