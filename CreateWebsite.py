from flask import Flask, render_template
import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str, help="")
args = parser.parse_args()

if args.s:
    file_html = str(args.s)
    app = Flask(__name__)
    @app.route("/")
    def index():
        return render_template(file_html)
    if __name__ == "__main__":
        app.run()
else:
    sys.exit()