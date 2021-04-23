from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post/', methods = ['POST'])
def post():
    req = request.get_json()

    foldername = req['foldername']
    titles = req['titles']
    dates =  req['dates']
    links = req['links']


    for title, date, link in zip(titles, dates, links):     
        with open('app/accounts/' + foldername + '.json') as f:
            data = json.load(f)
            data['account'].insert(0, {
                'title':title,
                'date':date,
                'link':link
            })

            while len(data['account']) > 25:
                data['account'].pop(-1)
    
        with open('app/accounts/' + foldername + '.json', 'w') as f:
            json.dump(data, f)
        


            
    
    return 'database updated', 201 

@app.route('/streaming/', methods = ['GET'])
def streaming():
    titles = []
    dates = []
    links = []
    with open('app/accounts/streaming.json') as json_file:
        data = json.load(json_file)
    for account in data['account']:
        links.append(account['link'])
        titles.append(account['title'])
        dates.append(account['date'])
        zipped_list = zip(titles, dates, links)
    return render_template('account.html', list = zipped_list)


@app.route('/vpn/')
def vpn():
    titles = []
    dates = []
    links = []
    with open('app/accounts/vpn.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/gaming/')
def gaming():
    titles = []
    dates = []
    links = []
    with open('app/accounts/gaming.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/music/')
def music():
    titles = []
    dates = []
    links = []
    with open('app/accounts/music.json') as json_file:
        data = json.load(json_file)
        for account in data['account']:
            links.append(account['link'])
            titles.append(account['title'])
            dates.append(account['date'])
            zipped_list = zip(titles, dates, links)
            #print(list(zipped_list))
        return render_template('account.html', list = zipped_list)

@app.route('/admin/', methods=['POST', 'GET'])
def admin_login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['pass']
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)