# Notes-Api

The API should have the following capabilities:

* **Create a new note containing a note title and content**  
```bash
curl -d '{"title":"<your title here>", "content":"<your content here>"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/POST/note/
```
* **Edit the title or content of an existing note**  
```bash
curl -X PUT -d '{"title":"<your updated title here>", "content":"<your updated content here>"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/PUT/note/<int:pk>/
```
* **Get a list of titles of all the notes in the system**  
```bash
curl -X GET http://127.0.0.1:8000/GET/notes/
```
* **Get the title and content of a particular note**  
```bash
curl -X GET http://127.0.0.1:8000/GET/note/<int:pk>/
```
* **Delete a note from the system**  
```bash
curl -X DELETE http://127.0.0.1:8000/DELETE/note/<int:pk>/
```

## How to run this Project
1. Clone the Repo
2. Use Pip and run `pip3 install -r requirements.txt`
3. Run `python3 manage.py runserver`
4. Have fun
