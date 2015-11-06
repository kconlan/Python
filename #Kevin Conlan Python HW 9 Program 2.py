Kevin Conlan Python HW 9 Program 2

from wsgiref.simple_server import make_server
import sqlite3

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def hello_world_app(environ, start_response):
    conn = sqlite3.connect("zoo.sqlite")
    cursor = conn.cursor()

    #print("Environ:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)


    if (environ['REQUEST_METHOD'] == 'GET' and len(environ['QUERY_STRING'])):
        message += "<br> Data recieved!:"
        for param in environ['QUERY_STRING'].split("&"):
            message += "<br>"+param
        l = environ['QUERY_STRING'].split("&")
        cursor.execute("insert into animal_count(name, count) values(?, ?)", (l[0].split("=")[1], l[1].split("=")[1]))


    message += "<h1>Welcome to our Zoo!</h1>"
    message += "<form method='GET'><br>Animal:<input type=text name='animal'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"
    return [bytes(message, 'utf-8')]



httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()