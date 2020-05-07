from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
  return "root path"

@app.route("/test")
  return "test path"
  
if __name__ == "__main__":
  app.run()
