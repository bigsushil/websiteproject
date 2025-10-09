from app import app,render_template 
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