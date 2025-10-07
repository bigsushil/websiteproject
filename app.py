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
@app.route('/youtube')
def youtube():
    return render_template('https://www.youtube.com/@FliparrowTechnologies')

@app.route('/linkedin')
def linkedin():
    return render_template('https://www.linkedin.com/company/fliparrow-technologies/')
@app.route('/twitter')
def twitter():
    return render_template('https://twitter.com/FliparrowTech')     
@app.route('/facebook') 
def facebook():
    return render_template('https://www.facebook.com/FliparrowTechnologies')    
@app.route('/instagram')
def instagram():
    return render_template('https://www.instagram.com/fliparrow_technologies/') 
#End Social Media and Other Routes
@app.route('/textart')
def textart():    
    return render_template('textart.html')

@app.route('/fliparrow-contactus/')
def fliparrowcontactus():    
    return render_template('fliparrow-contactus.html')

#product Route Section

@app.route('/fliparrow-products/')
def products():
    return render_template('products.html')
@app.route('/fortinet-firewall/')
def productfirewall():    
    return render_template('fortinet-harware-firewall.html')

@app.route('/endpoint-security/')
def endpointsecurity():    
    return render_template('endpoint-security.html')    

if __name__ == '__main__':
    app.run(debug=True , port=8000 , host='0.0.0.0')
