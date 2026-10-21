from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title> device properties </title>
    </head>
    <body bgcolor="lavender">
    <h1 align="center">Prathiksha</h1>
    <h2 align="center">26015225</h2>
    <table border="1" cellspacing="10"
    cellpadding="10">
<captain>device properties</captain>
<tr bgcolor="yellow">
    <th>s.no</th>
    <th>device info</th>
    <th>device properrty</th>
</tr>
<tr>
    <td>1</td>
    <td>device name</td>
    <td>TL15-53M-G2</td>
</tr>
<tr>
    <td>2</td>
    <td>installed ram</td>
    <td>16.0 GB (15.7 GB usable)</td>
</tr>
<tr>
    <td>3</td>
    <td>graphics card</td>
    <td>Intel(R) Graphics (128 MB)</td>
</tr>
<tr>
    <td>4</td>
    <td>storage</td>
    <td>118 GB of 477 GB used</td>
</tr>
<tr>
    <td>5</td>
    <td>device id</td>
    <td>E90BA026-375D-48FC-A494-D915DD5CEA62</td>
</tr>
</tr>
</table>
</body>
</html>
..
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()