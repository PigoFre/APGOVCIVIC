from flask import request
from flask import Flask



def index():
  return render_template('index.html')
  



if __name__ == "__main__":
    # Use environment variables for sensitive keys and set debug to True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    index()
