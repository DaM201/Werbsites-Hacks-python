from http.server import BaseHTTPRequestHandler, HTTPServer
import time, argparse, sys, requests, os
parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str, help="")
parser.add_argument("-e", type=str, help="")
parser.add_argument("--utf", type=str, help="")
args = parser.parse_args()
if args.s:
    if args.e:
      if args.utf:
        utf_code = str(args.utf)

        try:
            log = str(args.s)
            hostName, serverPort = log.split(":")
        except:
            log = str(args.s)
            hostName = log
            serverPort = 9090     
            print("No Port was specified. The port is 9090")
        

        filename = args.e
        if os.path.exists(filename):
            with open(filename,"+r") as f:
                log_text_to_website = str(f.read())
        else:
            print(f"{filename} is not file")
            sys.exit()
        class MyServer(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(f"{log_text_to_website}", ))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, f"{utf_code}"))
        if __name__ == "__main__":        
            webServer = HTTPServer((hostName, serverPort), MyServer)
            print("Server started http://%s:%s" % (hostName, serverPort))

            try:
                webServer.serve_forever()
            except KeyboardInterrupt:
                pass

            webServer.server_close()
            print("Server stopped.")
    else:
        try:
            try:
                
                def check_website_exists(website):
                    try:
                        response = requests.get(website)
                        if response.status_code == 200:
                            return True
                        else:
                            return False
                    except:
                        return False
                if __name__ == "__main__":
                    website = str(args.s)
                    if "https" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "http" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "ssl" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "tls" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "hsts" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "http/2" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "http/3" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "csrf" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    elif "xss" in website:
                        if check_website_exists(website):
                            print("The website exists.")
                        else:
                            print("The website does not exist.")
                    else:
                        sys.exit()
            except:
                sys.exit()
            
        except:
            sys.exit()
else:
    sys.exit()



