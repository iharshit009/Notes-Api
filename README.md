# Notes-Api

The API should have the following capabilities:

* Create a new note containing a note title and content.  
`curl -d '{"title":"<your title here>", "content":"<your contest here>"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/postNote/`
* Edit the title or content of an existing note.  
`curl -X PUT -d '{"title":"<your updated title here>", "content":"<your updated content here>"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/update/<pk>/`
* Get a list of titles of all the notes in the system.  
` curl -X GET http://127.0.0.1:8000/`
* Get the title and content of a particular note.  
`curl -X GET http://127.0.0.1:8000/<pk>/`
* Delete a note from the system.  
` curl -X DELETE http://127.0.0.1:8000/delete/<pk>/`


## How to run this Project
1. Clone the Repo
2. Use Pip and run `pip3 install -r requirements.txt`
3. Run `python3 manage.py runserver`
4. Have fun
