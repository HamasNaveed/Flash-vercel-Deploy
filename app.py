from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Auto-Deployed to Vercel with an push 2 try !!"

if __name__ == "__main__":
    app.run()
