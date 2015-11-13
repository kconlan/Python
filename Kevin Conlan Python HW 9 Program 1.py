#Kevin Conlan Python HW 9 Program 1

import psutil, datetime
from wsgiref.simple_server import make_server


def my_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    cpu_utilization = psutil.cpu_percent(interval=1, percpu=True)

    message = "<h1>My System information</h1>"
    message += "<table>"
    message += "<tr><th bgcolor = 'lightblue' > Boot time </th><th bgcolor='lightgreen' >" \
               + str(boot_time) + "</th></tr>"
    message += "<tr><th bgcolor = 'lightblue' > CPU Utilization </th></tr>"
    i = 1
    for cpu in cpu_utilization:
        message += "<tr><th bgcolor = 'lightblue' > CPU " + str(i) + "</th><th bgcolor='lightpink'>" \
                   + str(cpu) + "</th><tr>"
        i += 1
    mem = psutil.virtual_memory()
    Threshold = 100 * 1024 * 1024  # 100MB
    message += "<tr><th bgcolor = 'lightblue' > Available memory </th><th bgcolor='lightgreen'>" \
               + str(mem.available) + "</th></tr>"
    message += "<tr><th bgcolor = 'lightblue' > Used memory </th><th bgcolor = 'lightgreen' >" \
               + str(mem.used) + "</th></tr>"
    message += "<tr><th bgcolor = 'lightblue' > Used percentage </th><th bgcolor= 'lightgreen' >" \
               + str(mem.percent) + "</th></tr>"
    message += "</table>"
    return [bytes(message, 'utf-8')]

httpd = make_server('', 8000, my_app)
print("Serving on port 8000...")
httpd.serve_forever()