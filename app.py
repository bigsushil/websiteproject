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

@app.route('/Fliparrow-Products/')
def products():
    return render_template('products.html')

@app.route('/Fliparrow-aboutus/')
def aboutus():
    return render_template('aboutus.html')

@app.route('/Fliparrow-contactus/')
def contactus():
    return render_template('contactus.html')
@app.route('/service-details/')
def services():
    return render_template('service-details.html') 
@app.route('/Fliparrow-careers/')
def careers():
    return render_template('careers.html')  

@app.route('/Privacy-Policy/')
def privacy():
    return render_template('Privacy_Policy.html')
@app.route('/Terms-of-Service/')
def terms():
    return render_template('Terms_of_Service.html') 
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
@app.route('/blog')
def blog():
    return render_template('https://fliparrow.medium.com/') 
@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')   
@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')    
@app.route('/admin')
def admin():    
    return render_template('admin.html')    
@app.route('/dashboard')
def dashboard():    
    return render_template('dashboard.html')
@app.route('/profile')
def profile():    
    return render_template('profile.html')  
@app.route('/textart')
def textart():    
    return render_template('textart.html')
   
if __name__ == '__main__':
    app.run(debug=True , port=8000 , host='0.0.0.0')
