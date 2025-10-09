from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('index.html')
@app.route('/login/')
def login():
    return "Welcome to the login page!"

@app.route('/logout-now/')
def logout():
    return render_template('logout.html')


@app.route('/Fliparrow-aboutus/')
def aboutus():
    return render_template('aboutus.html')
@app.route('/service-details/')
def services():
    return render_template('service-details.html') 

# Social Media and Other Routes

@app.route('/textart')
def textart():    
    return render_template('textart.html')

@app.route('/fliparrow-contactus/')
def fliparrowcontactus():    
    return render_template('fliparrow-contactus.html')



if __name__ == '__main__':
    app.run(debug=True , port=8000 , host='0.0.0.0')
    
import controller.product_controller as  product_controller
import controller.social_media as social_media