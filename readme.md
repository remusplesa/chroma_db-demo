# REST API to test out chroma_db

* Upload files to the server and encoded into chroma_db with the /pdf endpoint
* Bring the closest documents available to some text query (whole document in the future) with the /search endpoint

Python 3.11 required

```
export HNSWLIB_NO_NATIVE=1
python3 -m venv venv

. /venv/bin/activate

pip install -r requirements.txt

fastapi dev main.py       
```

Swagger:
`http://127.0.0.1:8000/docs`