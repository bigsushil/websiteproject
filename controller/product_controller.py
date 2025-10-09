from app import app,render_template
@app.route('/fliparrow-products/')
def products():
    return render_template('products.html')
@app.route('/fortinet-firewall/')
def productfirewall():    
    return render_template('fortinet-harware-firewall.html')

@app.route('/endpoint-security/')
def endpointsecurity():    
    return render_template('endpoint-security.html')

@app.route('/tally-services/')
def tallyservices():
    return render_template('tally-accounting-software.html')
@app.route('/tally-whatsapp-integration/')
def tallywhatsappintegration():
    return render_template('tally-whatsapp-integration.html')