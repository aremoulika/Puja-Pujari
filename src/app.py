import datetime
from gc import get_count
from bson import ObjectId
from flask import Flask, abort, render_template, request, redirect, session,jsonify, url_for
from pymongo import MongoClient
from flask import jsonify
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = "qwerty" 

client = MongoClient('mongodb://localhost:27017/')
db = client['puja'] 
users= db["users"]
puja_items=db['pujaSamagri']
puja_services=db['pujaServices']
cart_item=db['cart']
s_cart=db['servicesCart']
p_list=db['panditlist']
t_puja=db['Temples']
t_services=db['Tservices']
contactUs=db['contactus']
prasadam1=db['prasadam']
prasad1=db['prasad']
chat=db['chatBot']

@app.route('/register')
def register():
    return render_template('login.html')

@app.route('/main')
def main():
    p_info=puja_items.find()
    p_info1=puja_services.find()
    info1=s_cart.find()       
    l=[]
    l1=[]
    l2=[]
    for i in p_info:
        dummy=[]
        dummy.append(i.get('_id'))
        dummy.append(i.get('name'))
        dummy.append(i.get('description'))
        dummy.append(i.get('price'))
        l.append(dummy)
    for i in p_info1:
        dummy1=[]
        id=i.get('_id')
        dummy1.append(i.get('_id'))
        dummy1.append(i.get('p_name'))
        dummy1.append(i.get('description'))
        dummy1.append(i.get('price'))
        l1.append(dummy1)
    for i in info1:
         if(session['email']==i.get('email')):
              dummy=[]
              dummy.append(i.get('_id'))
              dummy.append(i.get('name'))
              dummy.append(i.get('price'))
              dummy.append(i.get('date'))
              dummy.append(i.get('time'))
              dummy.append(i.get('location'))
              dummy.append(i.get('reg_date'))
              l2.append(dummy)
    pandit=p_list.find()
    pList=[]
    for i in pandit:
        dummy2=[]
        dummy2.append(i.get('name'))
        dummy2.append(i.get('location'))
        pList.append(dummy2)
    info2=t_services.find()
    pujaList=[]
    for i in info2:
            if(session['email']==i.get('email')):
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('p_name'))
                dummy.append(i.get('t_name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('date'))
                dummy.append(i.get('time'))
                dummy.append(i.get('status'))
                pujaList.append(dummy)
    info=cart_item.find()
    info1=s_cart.find()
    l3=[]
    l4=[]
    for i in info:
          if(session['email']==i.get('email')):
               dummy=[]
               dummy.append(i.get('_id'))
               dummy.append(i.get('name'))
               dummy.append(i.get('qty'))
               dummy.append(i.get('price'))
               dummy.append(i.get('total'))
               dummy.append(i.get('reg_date'))
               l3.append(dummy)
    for i in info1:
              if(session['email']==i.get('email')):
                dummy1=[]
                dummy1.append(i.get('_id'))
                dummy1.append(i.get('name'))
                dummy1.append(i.get('price'))
                dummy1.append(i.get('date'))
                dummy1.append(i.get('time'))
                dummy1.append(i.get('location'))
                dummy1.append(i.get('status'))
                dummy1.append(i.get('reg_date'))
                l4.append(dummy1)
    pra1=[]
    info3=prasad1.find()
    for i in info3:
          if session['email']==i.get('email'):
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('prasadam_name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('total'))
                dummy.append(i.get('qty'))
                dummy.append(i.get('date'))
                pra1.append(dummy)
    n=len(l3)+len(l4)+len(pujaList)+len(pra1)   
    return render_template('main.html',l=l,l1=l1,l2=l2,pList=pList,n=n)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgot')
def forg():
    return render_template("forgot.html")

@app.route('/plogin')
def plogin():
    return render_template("plogin.html")
   
@app.route('/pandit')
def pandit():
     info1=s_cart.find()
     p=[]
     for i in info1:
                            
                             if session['email1']==i.get('pmail'):
                                print(i.get('pmail'),"Hii")
                                print(i.get('status'))
                                if i.get('status')=='Accepted' or i.get('status')=='Rejected' :
                                        
                                        dummy=[]
                                        dummy.append(i.get('_id'))
                                        dummy.append(i.get('email'))
                                        dummy.append(i.get('name'))
                                        dummy.append(i.get('price'))
                                        dummy.append(i.get('date'))
                                        dummy.append(i.get('time'))
                                        dummy.append(i.get('location'))
                                        dummy.append(i.get('status'))
                                        p.append(dummy)
                                        print(p,"  List")
     info = p_list.find_one({'email':session['email1']})
     name=info['name']
     email=info['email']
     phno=info['phno']
     location=info['location']                       
     return render_template('pandit.html',p=p,name=name,location=location,phno=phno,email=email)

     

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/404')
def error_404():
    return render_template('404.html')

@app.route('/tlogin')
def tlogin():
     return render_template('tlogin.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/')
def index1():
    p_info=puja_items.find()
    print(p_info)
    p_info1=puja_services.find()
    l=[]
    l1=[]
    for i in p_info:
        dummy=[]
        dummy.append(i.get('_id'))
        dummy.append(i.get('name'))
        dummy.append(i.get('description'))
        dummy.append(i.get('price'))
        l.append(dummy)
    for i in p_info1:
        dummy1=[]
        dummy.append(i.get('_id'))
        dummy1.append(i.get('p_name'))
        dummy1.append(i.get('description'))
        dummy1.append(i.get('price'))
        l1.append(dummy1)
    return render_template('index.html',l=l,l1=l1)

def is_valid_password(psw):
    if len(psw) < 8:
        return False
    if not any(char.isdigit() for char in psw):
        return False
    if not any(char.isupper() for char in psw):
        return False
    if not any(char.islower() for char in psw):
        return False
    if not any(char in '!@#$%^&*()_-+=[]{}|;:,.<>?/' for char in psw):
        return False
    return True

@app.route('/reg', methods=['POST', 'GET'])
def reg():
    name = request.form['name']
    email = request.form['email']
    pwd = request.form['pwd']
    phno = request.form['phno']
    if not isinstance(name, str) or not any(c.isalpha() for c in name):
            msg1 = 'Invalid name format. Please enter a valid name.'
            return render_template('login.html', msg1=msg1)
    existing_user = users.find_one({'email': email})
    existing_num = users.find_one({'phno': phno})
    if existing_user:
            msg1='Email already exists'
            return render_template('login.html',msg1=msg1)
    if existing_num:
            msg1='Phone Number Already Exists'
            return render_template('login.html',msg1=msg1)
    if not is_valid_password(pwd):
            msg1 = 'Password must be Valid.'

            return render_template('login.html', msg1=msg1)
    reg_date = datetime.datetime.now()
    user_data = {
            'name': name,
            'email': email,
            'psw': pwd,
            'phno':phno,
            'reg_date': reg_date  
        }
    users.insert_one(user_data)
    msg1='Registration successful'
    account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
    auth_token = '7d4264c8df08ac640d854db91d08f2bd'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Your Registration for Puja Pujari is Successful',
        from_='+12513135289',
        to='+91 9392419102'
    )
    print(f'Message SID: {message.sid}')
    return render_template('login.html',msg1=msg1)

@app.route('/log', methods=['POST'])
def login_post():
        global e_mail
        global type1
        email = request.form['email']
        pwd = request.form['pwd']
        user = users.find_one({'email': email})
        if user:
            if user.get('email')==email:
                if user.get('psw')==pwd:
                    session['email'] = email
                    msg1='Login Successful'
                    account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
                    auth_token = '7d4264c8df08ac640d854db91d08f2bd'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                    body='Login to Puja Pujari is Successful',
                    from_='+12513135289',
                    to='+91 9392419102'
                )
                    print(f'Message SID: {message.sid}')
                    p_info=puja_items.find()
                    p_info1=puja_services.find()
                    l=[]
                    l1=[]
                    for i in p_info:
                        dummy=[]
                        dummy.append(i.get('_id'))
                        dummy.append(i.get('name'))
                        dummy.append(i.get('description')) 
                        dummy.append(i.get('price'))
                        l.append(dummy)
                    for j in p_info1:
                        dummy1=[]
                        dummy1.append(j.get('_id'))
                        dummy1.append(j.get('p_name'))
                        dummy1.append(j.get('description'))
                        dummy1.append(j.get('price'))
                        l1.append(dummy1)
                    pandit=p_list.find()
                    pList=[]
                    for k in pandit:
                        dummy2=[]
                        dummy2.append(k.get('name'))
                        dummy2.append(k.get('location'))
                        pList.append(dummy2)
                    info=cart_item.find()
                    info1=s_cart.find()
                    l3=[]
                    l4=[]
                    for i in info:
                        if(session['email']==i.get('email')):
                            dummy=[]
                            dummy.append(i.get('_id'))
                            dummy.append(i.get('name'))
                            dummy.append(i.get('qty'))
                            dummy.append(i.get('price'))
                            dummy.append(i.get('total'))
                            dummy.append(i.get('reg_date'))
                            l3.append(dummy)
                    for i in info1:
                        if(session['email']==i.get('email')):
                            dummy1=[]
                            dummy1.append(i.get('_id'))
                            dummy1.append(i.get('name'))
                            dummy1.append(i.get('price'))
                            dummy1.append(i.get('date'))
                            dummy1.append(i.get('time'))
                            dummy1.append(i.get('location'))
                            dummy1.append(i.get('status'))
                            dummy1.append(i.get('reg_date'))
                            l4.append(dummy1)
                    pList=[]
                    pandit=p_list.find()
                    for i in pandit:
                        dummy2=[]
                        dummy2.append(i.get('name'))
                        dummy2.append(i.get('location'))
                        pList.append(dummy2)
                        info2=t_services.find()
                        pujaList=[]
                        for i in info2:
                            if(session['email']==i.get('email')):
                                dummy=[]
                                dummy.append(i.get('_id'))
                                dummy.append(i.get('p_name'))
                                dummy.append(i.get('t_name'))
                                dummy.append(i.get('price'))
                                dummy.append(i.get('date'))
                                dummy.append(i.get('time'))
                                dummy.append(i.get('status'))
                                pujaList.append(dummy)
                    n=len(l3)+len(l4)+len(pujaList)                              
                    print("Login Successful")
                    return render_template('main.html', user=user,msg1=msg1,l=l,l1=l1,pList=pList,n=n)
                else:
                    return render_template("login.html",msg="Password Wrong")
            else:
                msg = 'Invalid email or password. Please try again.'
                return render_template('login.html', msg=msg)
        else:      
            return render_template("login.html",msg="Please Register")

@app.route('/forgotpassword',methods=['POST','GET'])
def forgot():
    email=request.form['email']
    npwd=request.form['pwd']
    info=users.find_one({'email':email})
    if info:
            users.update_one({'email': email}, {'$set': {'psw': npwd}})
            return render_template('login.html') 
    return render_template("forgot.html",msg="Mail Not Found")

@app.route('/logout')
def logout():
    session.pop('email', None)
    p_info=puja_items.find()
    p_info1=puja_services.find()
    l=[]
    l1=[]
    for i in p_info:
        dummy=[]
        dummy.append(i.get('_id'))
        dummy.append(i.get('name'))
        dummy.append(i.get('description'))
        dummy.append(i.get('price'))
        l.append(dummy)
    for i in p_info1:
        dummy1=[]
        dummy.append(i.get('_id'))
        dummy1.append(i.get('p_name'))
        dummy1.append(i.get('description'))
        dummy1.append(i.get('price'))
        l1.append(dummy1)
    return render_template('index.html',l=l,l1=l1)

@app.route('/preg', methods=['POST', 'GET'])
def preg():
    name = request.form['name']
    email = request.form['email']
    pwd = request.form['pwd']
    phno = request.form['phno']
    age = request.form['age']
    location = request.form['location']
    if not isinstance(name, str) or not any(c.isalpha() for c in name):
        msg1 = 'Invalid name format. Please enter a valid name.'
        return render_template('login.html', msg1=msg1)
    existing_user = p_list.find_one({'email': email})
    existing_num =p_list.find_one({'phno': phno})
    if existing_user:
        msg1='Email already exists'
        return render_template('plogin.html',msg1=msg1)
    if existing_num:
        msg1='Phone Number Already Exists'
        return render_template('plogin.html',msg1=msg1)
    if not is_valid_password(pwd):
        msg1 = 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'
        return render_template('plogin.html', msg1=msg1)
    reg_date = datetime.datetime.now()
    user_data = {
            'name': name,
            'email': email,
            'pwd': pwd,
            'phno':phno,
            'age':age,
            'location':location,
            'reg_date': reg_date  
        }
    p_list.insert_one(user_data)
    account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
    auth_token = '7d4264c8df08ac640d854db91d08f2bd'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Your registration for pandit was Successful!',
        from_='+12513135289',
        to='+91 9392419102'
    )
    print(f'Message SID: {message.sid}')
    msg1='Registration successful'
    return render_template('plogin.html',msg1=msg1)


@app.route('/plog', methods=['POST','GET'])
def plogin_post():
        email1 = request.form['email']
        pwd = request.form['pwd']
        user = p_list.find_one({'email': email1})
        l=[]
        if user:
            if user.get('email')==email1:
                if user.get('pwd')==pwd:
                    session['email1']=email1
                    msg1='Login Successful'
                    account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
                    auth_token = '7d4264c8df08ac640d854db91d08f2bd'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body='Pandit LoginWas Successful',
                        from_='+12513135289',
                        to='+91 93924 19102'
                    )
                    print(f'Message SID: {message.sid}')
                    info=s_cart.find()
                    for i in info:
                        if i.get('status')=="pending":
                            dummy=[]
                            dummy.append(i.get('_id'))
                            dummy.append(i.get('email'))
                            dummy.append(i.get('name'))
                            dummy.append(i.get('price'))
                            dummy.append(i.get('date'))
                            dummy.append(i.get('time'))
                            dummy.append(i.get('location'))
                            dummy.append(i.get('status'))
                            l.append(dummy)
                    p=[]
                    info1=s_cart.find()
                    for i in info1:     
                        if session['email1']==i.get('pmail'):
                            if i.get('status')=='Accepted' or i.get('status')=='Rejected' :            
                                dummy=[]
                                dummy.append(i.get('_id'))
                                dummy.append(i.get('email'))
                                dummy.append(i.get('name'))
                                dummy.append(i.get('price'))
                                dummy.append(i.get('date'))
                                dummy.append(i.get('time'))
                                dummy.append(i.get('location'))
                                dummy.append(i.get('status'))
                                p.append(dummy)
                    info = p_list.find_one({'email':session['email1']})
                    name=info['name']
                    email=info['email']
                    phno=info['phno']
                    location=info['location']
                    return render_template('pandit.html', user=user,msg1=msg1,l=l,p=p,name=name,location=location,phno=phno,email=email)
                else:
                    return render_template("plogin.html",msg="Password Wrong")
            else:
                msg = 'Invalid email or password. Please try again.'
                return render_template('plogin.html', msg=msg)
        else:      
            return render_template("plogin.html",msg="Please Register")
        
@app.route('/p_update/<id>',methods=['POST','GET'])
def p_update(id):
     info = s_cart.find_one({'_id': ObjectId(id)})
     id=info['_id']
     if info:
          s_cart.update_one(
            {'_id': id},
            {'$set': {'status': "Accepted"}}
        )
          account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
          auth_token = '7d4264c8df08ac640d854db91d08f2bd'
          client = Client(account_sid, auth_token)
          message = client.messages.create(
            body='Pandit Accepted Your request!!',
            from_='+12513135289',
            to='+91 9392419102'
        )
          print(f'Message SID: {message.sid}')
     p=[]
     info=s_cart.find()
     for i in info:
        if session['email1']==i.get('pmail'):
            if i.get('status')=='Accepted' or i.get('status')=='Rejected' :
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('email'))
                dummy.append(i.get('name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('date'))
                dummy.append(i.get('time'))
                dummy.append(i.get('location'))
                dummy.append(i.get('status'))
                p.append(dummy)
     return redirect(url_for('pandit',p=p))

@app.route('/p_deny/<id>',methods=['POST','GET'])
def p_deny(id):
     info = s_cart.find_one({'_id': ObjectId(id)})
     id=info['_id']
     print(info," hello")
     if info:
          s_cart.update_one(
            {'_id': id},
            {'$set': {'status': "Rejected"}}
        )
          account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
          auth_token = '7d4264c8df08ac640d854db91d08f2bd'
          client = Client(account_sid, auth_token)
          message = client.messages.create(
            body='Pandit Denied your Request',
            from_='+12513135289',
            to='+91 9392419102'
        )
          print(f'Message SID: {message.sid}')
     p=[]
     info=s_cart.find()
     for i in info:
        if session['email1']==i.get('pmail'):
            if i.get('status')=='Accepted' or i.get('status')=='Rejected' :
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('email'))
                dummy.append(i.get('name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('date'))
                dummy.append(i.get('time'))
                dummy.append(i.get('location'))
                dummy.append(i.get('status'))
                p.append(dummy)
     return redirect(url_for('pandit',p=p))

@app.route('/add_to_cart/<id>', methods=['POST', 'GET'])
def add_to_cart(id):
    info = puja_items.find_one({'_id': ObjectId(id)})
    if info:
        qty = 1
        name = info.get('name')
        price = info.get('price')
        total = price * qty 
        existing_item = cart_item.find_one({'email': session['email'], 'name': name})
        if existing_item:
            msg = "Item Already present in the Cart"
            new_qty = existing_item.get('qty') + qty
            new_total = new_qty * price
            cart_item.update_one(
                {'_id': existing_item['_id']},
                {'$set': {'qty': new_qty, 'total': new_total}}
            )
        else:
            date = str(datetime.datetime.today()).split()[0]
            msg = "Item Added to cart"
            items = {
                'email': session['email'],
                'name': name,
                'price': price,
                'qty': qty,
                'total': total,
                'reg_date': date,
                'status': "pending"
            }
            cart_item.insert_one(items)
            account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
            auth_token = '7d4264c8df08ac640d854db91d08f2bd'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body='Item Added to Cart Successfully!!!',
            from_='+12513135289',
            to='+91 9392419102'
            )
            print(f'Message SID: {message.sid}')
    else:
        msg = "Item not found"
    return redirect(url_for('main', msg=msg))

@app.route('/cart')
def cart():
    samagriTotal=0
    overallTotalS=0
    overallTotal=0
    serviceTotal=0
    prasadamTotal=0
    pujaTotal=0
    info=cart_item.find()
    info1=s_cart.find()
    shipping=int(25)
    l=[]
    l1=[]
    for i in info:
        if(session['email']==i.get('email')):
            dummy=[]
            dummy.append(i.get('_id'))
            dummy.append(i.get('name'))
            dummy.append(i.get('qty'))
            dummy.append(int(i.get('price')))
            samagriTotal=samagriTotal+int(i.get('total'))
            dummy.append(i.get('total'))
            dummy.append(i.get('reg_date'))
            l.append(dummy)
    for i in info1:
        if(session['email']==i.get('email')):
            dummy1=[]
            dummy1.append(i.get('_id'))
            dummy1.append(i.get('name'))
            dummy1.append(i.get('price'))
            serviceTotal=int(i.get('price'))
            dummy1.append(i.get('date'))
            dummy1.append(i.get('time'))
            dummy1.append(i.get('location'))
            dummy1.append(i.get('status'))
            dummy1.append(i.get('reg_date'))
            l1.append(dummy1)
    pList=[]
    pandit=p_list.find()
    for i in pandit:
        dummy2=[]
        dummy2.append(i.get('name'))
        dummy2.append(i.get('location'))
        pList.append(dummy2)
    info2=t_services.find()
    pujaList=[]
    for i in info2:
         if(session['email']==i.get('email')):
              dummy=[]
              dummy.append(i.get('_id'))
              dummy.append(i.get('p_name'))
              dummy.append(i.get('t_name'))
              dummy.append(i.get('price'))
              pujaTotal=int(i.get('price'))
              print(i.get('price'))
              dummy.append(i.get('date'))
              dummy.append(i.get('time'))
              dummy.append(i.get('status'))
              pujaList.append(dummy)
    pra1=[]
    info3=prasad1.find()
    for i in info3:
          if session['email']==i.get('email'):
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('prasadam_name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('total'))
                prasadamTotal=prasadamTotal+i.get('total')
                dummy.append(i.get('qty'))
                dummy.append(i.get('date'))
                pra1.append(dummy)
    n=len(l)+len(l1)+len(pujaList) + len(pra1)
    overallTotal=samagriTotal+serviceTotal+pujaTotal+prasadamTotal
    overallTotalS=overallTotal+shipping   
    return render_template("cart.html",l=l,l1=l1,pList=pList,pujaList=pujaList,n=n,overallTotal=overallTotal,overallTotalS=overallTotalS,shipping=shipping,pra1=pra1)

@app.route('/increase_quantity/<id>', methods=['POST'])
def increase_quantity(id):
    item = cart_item.find_one({'_id': ObjectId(id)})
    if item and item['qty'] >= 1:
        cart_item.update_one({'_id': ObjectId(id)}, {'$inc': {'qty': 1}})
        price = int(float(item['price']))
        n_total = (item['qty'] + 1) * price
        cart_item.update_one({'_id': ObjectId(id)}, {'$set': {'total': n_total}})
    else:
        abort(400, 'Quantity must be greater than or equal to one')
    return redirect(url_for('cart'))

@app.route('/decrease_quantity/<item_id>', methods=['POST'])
def decrease_quantity(item_id):
    item = cart_item.find_one({'_id': ObjectId(item_id)})
    if item:
        if item['qty'] > 1:
            cart_item.update_one({'_id': ObjectId(item_id)}, {'$inc': {'qty': -1}}, upsert=False)
            n_total = item['qty'] * float(item['price']) - float(item['price'])  # Convert price to float
            cart_item.update_one({'_id': ObjectId(item_id)}, {'$set': {'total': n_total}})
        else:
            cart_item.delete_one({'_id': ObjectId(item_id)})
    else:
        msg = "Quantity must be greater than or equal to one"  
    return redirect(url_for('cart'))

@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    uid = cart_item.find_one({'_id': ObjectId(id)})
    if uid:
        cart_item.delete_one({'_id': uid['_id']})     
    return redirect(url_for('cart'))

@app.route('/addservices/<id>', methods=['POST', 'GET'])
def addservice(id):
    pandit_email = None 
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        name, loc = location.split('-')
        print(name," ",loc)
        pandit_data = p_list.find_one({'name': name, 'location': loc})
        print(pandit_data)
        if pandit_data:
            pandit_email = pandit_data.get('email')
        uid = puja_services.find_one({'_id': ObjectId(id)})
        if uid:
            services = {
                'email':session['email'],
                'name': uid.get('p_name'),
                'price': uid.get('price'),
                'date': date,
                'time': time,
                'location': loc,
                'pmail':pandit_email,
                'status':"pending"
            }
            s_cart.insert_one(services)     
    return redirect(url_for('cart'))

@app.route('/deleteservice/<id>',methods=['POST','GET'])
def deleteService(id):
     uid1=s_cart.find_one({'_id':ObjectId(id)})
     if uid1:
          s_cart.delete_one({'_id':uid1['_id']})
     return redirect(url_for('cart'))

@app.route('/admin')
def admin():
    info=puja_items.find()
    l=[]
    for i in info:
          dummy=[]
          dummy.append(i.get('_id'))
          dummy.append(i.get('name'))
          dummy.append(i.get('price'))
          dummy.append(i.get('description'))
          l.append(dummy)
          print(l)
    user_details =users.find()
    user=[]
    for j in user_details:
          dummy=[]
          dummy.append(j.get('name'))
          dummy.append(j.get('email'))
          dummy.append(j.get('phno'))
          user.append(dummy)
    p_details=p_list.find()
    pandit=[]
    for k in p_details:
         dummy=[]
         dummy.append(k.get('_id'))
         dummy.append(k.get('name'))
         dummy.append(k.get('location'))
         pandit.append(dummy)
    k=[]
    puja_service=puja_services.find()
    for r in puja_service:
         dummy=[]
         dummy.append(r.get('_id'))
         dummy.append(r.get('p_name'))
         dummy.append(r.get('description'))
         dummy.append(r.get('price'))
         
         
         k.append(dummy)  
    info1=t_puja.find()
    t=[]
    for i in info1:
          dummy=[]
          dummy.append(i.get('_id'))
          dummy.append(i.get('t_name'))
          dummy.append(i.get('p_name'))
          dummy.append(i.get('location'))
          dummy.append(i.get('price'))
          dummy.append(i.get('description'))
          t.append(dummy) 
    prasad1=prasadam1.find()
    prasad=[]
    for i in prasad1:
          dummy=[]
          dummy.append(i.get('_id'))
          dummy.append(i.get('name'))
          dummy.append(i.get('price'))
          prasad.append(dummy)  
          print(prasad)     
    return render_template('admin.html',l=l,user=user,pandit=pandit,k=k,t=t,prasad=prasad)

@app.route('/display',methods=['POST','GET'])
def display():
     info=puja_items.find()
     l=[]
     for i in info:
          dummy=[]
          dummy.append(i.get('_id'))
          dummy.append(i.get('name'))
          dummy.append(i.get('price'))
          dummy.append(i.get('description'))
          l.append(dummy)
     return redirect(url_for('admin'))

@app.route('/p_delete/<id>',methods=['POST','GET'])
def p_delete(id):
     uid1=puja_items.find_one({'_id':ObjectId(id)})
     id1=uid1['_id']
     if id1:
          puja_items.delete_one({'_id':id1})
     return redirect(url_for('admin'))

@app.route('/updateSamagri/<id>', methods=['POST', 'GET'])
def updateSamagri(id):
    if request.method == 'POST':
        info = puja_items.find_one({'_id': ObjectId(id)})
        info1=puja_items.find()
        if info:
            update_fields = {}
            if 'name' in request.form and request.form['name'].strip() != "":
                update_fields['name'] = request.form['name']
            else:
                update_fields['name'] = info['name']
            if 'description' in request.form and request.form['description'].strip() != "":
                update_fields['description'] = request.form['description']
            else:
                update_fields['description'] = info['description']
            if 'price' in request.form and request.form['price'].strip() != "":
                update_fields['price'] = request.form['price']
            else:
                update_fields['price'] = info['price']
            if update_fields:
                puja_items.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
        return redirect(url_for('admin'))

@app.route('/add',methods=['POST','GET'])
def add():
     name=request.form['name']
     description=request.form['description']
     price=request.form['price']
     items={
          'name':name,
          'description':description,
          'price':price
     }
     puja_items.insert_one(items)
     return redirect(url_for('admin'))

@app.route('/pandit_delete/<id>',methods=['POST','GET'])
def delete_pandit(id):
     uid=p_list.find_one({'_id':ObjectId(id)})
     id=uid['_id']
     info=p_list.find()
     pandit=[]
     if id:
          p_list.delete_one({'_id':id})
     return redirect(url_for('admin'))

@app.route('/updatePandit/<id>',methods=['POST','GET'])
def updatePandit(id):
     info=p_list.find_one({'_id':ObjectId(id)})
     id=info['_id']
     if info:
            update_fields = {}
            if 'name' in request.form and request.form['name'].strip() != "":
                update_fields['name'] = request.form['name']
            else:
                update_fields['name'] = info['name']
            if 'location' in request.form and request.form['location'].strip() != "":
                update_fields['location'] = request.form['location']
            else:
                update_fields['location'] = info['location']
            if update_fields:
                p_list.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
            return redirect(url_for('admin'))
     return redirect(url_for('admin'))

@app.route('/contact')
def contact():
     info=cart_item.find()
     info1=s_cart.find()
     l3=[]
     l4=[]
     for i in info:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('name'))
                                    dummy.append(i.get('qty'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('total'))
                                    dummy.append(i.get('reg_date'))
                                    l3.append(dummy)
                                    #    print(l)
     for i in info1:
                                    if(session['email']==i.get('email')):
                                        dummy1=[]
                                        dummy1.append(i.get('_id'))
                                        dummy1.append(i.get('name'))
                                        dummy1.append(i.get('price'))
                                        dummy1.append(i.get('date'))
                                        dummy1.append(i.get('time'))
                                        dummy1.append(i.get('location'))
                                        dummy1.append(i.get('status'))
                                        dummy1.append(i.get('reg_date'))
                                        l4.append(dummy1)
                                        # print(l1)
     pList=[]
     info2=t_services.find()
     pujaList=[]
     for i in info2:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('p_name'))
                                    dummy.append(i.get('t_name'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('date'))
                                    dummy.append(i.get('time'))
                                    dummy.append(i.get('status'))
                                    pujaList.append(dummy)
     pra1=[]
     info3=prasad1.find()
     for i in info3:
          if session['email']==i.get('email'):
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('prasadam_name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('total'))
                # prasadamTotal=prasadamTotal+i.get('total')
                dummy.append(i.get('qty'))
                dummy.append(i.get('date'))
                pra1.append(dummy)
     n=len(l3)+len(l4)+len(pujaList)+len(pra1)
     print(n)  
     return render_template('contactus.html',n=n)

@app.route('/contactus',methods=['POST','GET'])
def contactus():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    contact={
         'name':name,
         'email':email,
         'message':message
    }
    contactUs.insert_one(contact)
    
    return redirect(url_for('contact'))

@app.route('/addprasadam/<id>', methods=['POST', 'GET'])
def addprasadam(id):
    pri=0
    name = request.form['name']
    qty = request.form['qty']
    info = prasadam1.find()
    for i in info:
        if i.get('name') == name:
            pri = i.get('price')
            break
    
    uid = t_puja.find_one({'_id': ObjectId(id)})
    existing_item = cart_item.find_one({'email': session['email'], 'name': name})
    total = int(pri) * int(qty) 
    if existing_item:
            msg = "Item Already present in the Cart"
            new_qty = existing_item.get('qty') + qty
            new_total = new_qty * pri
            prasad1.update_one(
                {'_id': existing_item['_id']},
                {'$set': {'qty': new_qty, 'total': new_total}}
            )

    else:
        date = str(datetime.datetime.today()).split()[0]
        prasadam = {
            'email':session['email'],
            't_name': uid['t_name'],
            'p_name': uid['p_name'],
            'prasadam_name': name,
            'qty': int(qty),
            'date':date,
            'total':total,
            'price': pri,
            'status': "pending"
        }
        prasad1.insert_one(prasadam)
        pra = []
        info3 = prasadam1.find()
        for i in info3:
            dummy = []
            dummy.append(i.get('name'))
            pra.append(dummy)
        info=t_puja.find({'t_name':uid['t_name']})
        l=[]
        if info:
            for i in info:
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('p_name'))
                dummy.append(i.get('description'))
                dummy.append(i.get('price'))
                l.append(dummy)
        l3=[]
        l4=[]
        info=cart_item.find()
        info1=s_cart.find()
        for i in info:
                                #   print(e_mail)
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('name'))
                                    dummy.append(i.get('qty'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('total'))
                                    dummy.append(i.get('reg_date'))
                                    l3.append(dummy)
                                    #    print(l)
        for i in info1:
                                    if(session['email']==i.get('email')):
                                        dummy1=[]
                                        dummy1.append(i.get('_id'))
                                        dummy1.append(i.get('name'))
                                        dummy1.append(i.get('price'))
                                        dummy1.append(i.get('date'))
                                        dummy1.append(i.get('time'))
                                        dummy1.append(i.get('location'))
                                        dummy1.append(i.get('status'))
                                        dummy1.append(i.get('reg_date'))
                                        l4.append(dummy1)
                                        # print(l1)
        pList=[]
        pandit=p_list.find()
        for i in pandit:
                                                        dummy2=[]
                                                        dummy2.append(i.get('name'))
                                                        dummy2.append(i.get('location'))
                                                        pList.append(dummy2)
        info2=t_services.find()
        pujaList=[]
        for i in info2:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('p_name'))
                                    dummy.append(i.get('t_name'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('date'))
                                    dummy.append(i.get('time'))
                                    dummy.append(i.get('status'))
                                    pujaList.append(dummy)
        pra1=[]
        info3=prasad1.find()
        for i in info3:
                if session['email']==i.get('email'):
                    dummy=[]
                    dummy.append(i.get('_id'))
                    dummy.append(i.get('prasadam_name'))
                    dummy.append(i.get('price'))
                    dummy.append(i.get('total'))
                    # prasadamTotal=prasadamTotal+i.get('total')
                    dummy.append(i.get('qty'))
                    dummy.append(i.get('date'))
                    pra1.append(dummy)
        n=len(l3)+len(l4)+len(pujaList)+len(pra1)
    return render_template('templepuja.html',pra=pra,l=l,n=n)

@app.route('/increase_qty/<id>', methods=['POST'])
def increase_qty(id):
    item = prasad1.find_one({'_id': ObjectId(id)})
    if item and int(item.get('qty', 0)) >= 1:
        prasad1.update_one({'_id': ObjectId(id)}, {'$inc': {'qty': 1}})
        
        # Convert the price from string to float and then to int
        price = int(float(item.get('price', '0')))
        
        n_total = (item.get('qty', 0) + 1) * price
        prasad1.update_one({'_id': ObjectId(id)}, {'$set': {'total': n_total}})
    else:
        abort(400, 'Quantity must be greater than or equal to one')
    return redirect(url_for('cart'))

@app.route('/decrease_qty/<item_id>', methods=['POST'])
def decrease_qty(item_id):
    item = prasad1.find_one({'_id': ObjectId(item_id)})
    if item:
        qty = int(item.get('qty', '0'))  # Convert qty to an integer
        if qty > 1:
            prasad1.update_one({'_id': ObjectId(item_id)}, {'$inc': {'qty': -1}}, upsert=False)
            price = float(item.get('price', '0'))  # Convert price to a float
            n_total = qty * price - price
            prasad1.update_one({'_id': ObjectId(item_id)}, {'$set': {'total': n_total}})
        else:
            prasad1.delete_one({'_id': ObjectId(item_id)})
    else:
        msg = "Quantity must be greater than or equal to one"
    return redirect(url_for('cart'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    info = users.find()
    
    l = []
    l1 = []
    
    name = ''  # Initialize with default value
    email = ''  # Initialize with default value
    phno = ''  # Initialize with default value
    
    for i in info:
        if session['email'] == i.get('email'):
            print(session['email'])
            name = i.get('name')
            email = i.get('email')
            phno = i.get('phno')
            
            info1 = cart_item.find()
            for j in info1:
                if session['email'] == j.get('email'):
                    dummy = []
                    dummy.append(j.get('name'))
                    dummy.append(j.get('qty'))
                    dummy.append(j.get('reg_date'))
                    dummy.append(j.get('price'))
                    l.append(dummy)
                
            info2 = s_cart.find()
            for k in info2:
                if session['email'] == k.get('email'):
                    dummy = [] 
                    dummy.append(k.get('name'))
                    dummy.append(k.get('location'))
                    dummy.append(k.get('date'))
                    dummy.append(k.get('time'))
                    dummy.append(k.get('price')) 
                    l1.append(dummy)  
    
    return render_template('profile.html', name=name, email=email, phno=phno, l=l, l1=l1)

@app.route('/temple')
def temple():
    info=t_puja.find()
    l=[]
    for i in info:
         name=i.get('t_name')
         dummy=[]
         if name not in [i[0] for i in l]:
              dummy.append(name)
              dummy.append(i.get('location'))
              l.append(dummy)   
              l3=[]
              l4=[]
              info=cart_item.find()
              info1=s_cart.find()
              for i in info:
                                #   print(e_mail)
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('name'))
                                    dummy.append(i.get('qty'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('total'))
                                    dummy.append(i.get('reg_date'))
                                    l3.append(dummy)
                                    #    print(l)
              for i in info1:
                                    if(session['email']==i.get('email')):
                                        dummy1=[]
                                        dummy1.append(i.get('_id'))
                                        dummy1.append(i.get('name'))
                                        dummy1.append(i.get('price'))
                                        dummy1.append(i.get('date'))
                                        dummy1.append(i.get('time'))
                                        dummy1.append(i.get('location'))
                                        dummy1.append(i.get('status'))
                                        dummy1.append(i.get('reg_date'))
                                        l4.append(dummy1)
                                        # print(l1)
              pList=[]
              pandit=p_list.find()
              for i in pandit:
                                                        dummy2=[]
                                                        dummy2.append(i.get('name'))
                                                        dummy2.append(i.get('location'))
                                                        pList.append(dummy2)
              info2=t_services.find()
              pujaList=[]
              for i in info2:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('p_name'))
                                    dummy.append(i.get('t_name'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('date'))
                                    dummy.append(i.get('time'))
                                    dummy.append(i.get('status'))
                                    pujaList.append(dummy)
              pra1=[]
              info3=prasad1.find()
              for i in info3:
                if session['email']==i.get('email'):
                    dummy=[]
                    dummy.append(i.get('_id'))
                    dummy.append(i.get('prasadam_name'))
                    dummy.append(i.get('price'))
                    dummy.append(i.get('total'))
                    # prasadamTotal=prasadamTotal+i.get('total')
                    dummy.append(i.get('qty'))
                    dummy.append(i.get('date'))
                    pra1.append(dummy)
    n=len(l3)+len(l4)+len(pujaList)+len(pra1)  
    print(n)  
    return render_template('temple.html',l=l,n=n)

@app.route('/templepuja/<name>')
def templepuj(name):
    x=name
    info=t_puja.find({'t_name':x})
    l=[]
    if info:
         for i in info:
              dummy=[]
              dummy.append(i.get('_id'))
              dummy.append(i.get('p_name'))
              dummy.append(i.get('description'))
              dummy.append(i.get('price'))
              l.append(dummy)
         l3=[]
         l4=[]
         info=cart_item.find()
         info1=s_cart.find()
         for i in info:
                                #   print(e_mail)
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('name'))
                                    dummy.append(i.get('qty'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('total'))
                                    dummy.append(i.get('reg_date'))
                                    l3.append(dummy)
                                    #    print(l)
         for i in info1:
                                    if(session['email']==i.get('email')):
                                        dummy1=[]
                                        dummy1.append(i.get('_id'))
                                        dummy1.append(i.get('name'))
                                        dummy1.append(i.get('price'))
                                        dummy1.append(i.get('date'))
                                        dummy1.append(i.get('time'))
                                        dummy1.append(i.get('location'))
                                        dummy1.append(i.get('status'))
                                        dummy1.append(i.get('reg_date'))
                                        l4.append(dummy1)
                                        # print(l1)
         pList=[]
         pandit=p_list.find()
         for i in pandit:
                                                        dummy2=[]
                                                        dummy2.append(i.get('name'))
                                                        dummy2.append(i.get('location'))
                                                        pList.append(dummy2)
         info2=t_services.find()
         pujaList=[]
         for i in info2:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('p_name'))
                                    dummy.append(i.get('t_name'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('date'))
                                    dummy.append(i.get('time'))
                                    dummy.append(i.get('status'))
                                    pujaList.append(dummy)
         pra1=[]
         info3=prasad1.find()
         for i in info3:
          if session['email']==i.get('email'):
                dummy=[]
                dummy.append(i.get('_id'))
                dummy.append(i.get('prasadam_name'))
                dummy.append(i.get('price'))
                dummy.append(i.get('total'))
                # prasadamTotal=prasadamTotal+i.get('total')
                dummy.append(i.get('qty'))
                dummy.append(i.get('date'))
                pra1.append(dummy)
    n=len(l4)+len(l3)+len(pujaList)+len(pra1)
    print(n)
    pra=[]
    info3=prasadam1.find()
    for i in info3:
                dummy=[]
                dummy.append(i.get('name'))
                pra.append(dummy)
    return render_template('templepuja.html',l=l,n=n,pra=pra)

@app.route('/addTService/<id>',methods=['POST','GET'])
def addtService(id):
     if request.method == 'POST':
        date=request.form['date']
        time=request.form['time']
        uid = t_puja.find_one({'_id': ObjectId(id)})
        print(uid)
        if uid:
            tServices={
                'email':session['email'],
                't_name':uid.get('t_name'),
                'p_name':uid.get('p_name'),
                'location':uid.get('location'),
                'price':uid.get('price'),
                'date':date,
                'time':time,
                'status':"pending"
            }
            t_services.insert_one(tServices)
            info=t_puja.find()
            l=[]
            for i in info:
                    if i.get('t_name')==uid.get('t_name'):
                        dummy=[]
                        dummy.append(i.get('_id'))
                        dummy.append(i.get('p_name'))
                        dummy.append(i.get('description'))
                        dummy.append(i.get('price'))
                        l.append(dummy)
            l3=[]
            l4=[]
            info=cart_item.find()
            info1=s_cart.find()
            for i in info:
                                #   print(e_mail)
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('name'))
                                    dummy.append(i.get('qty'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('total'))
                                    dummy.append(i.get('reg_date'))
                                    l3.append(dummy)
                                    #    print(l)
            for i in info1:
                                    if(session['email']==i.get('email')):
                                        dummy1=[]
                                        dummy1.append(i.get('_id'))
                                        dummy1.append(i.get('name'))
                                        dummy1.append(i.get('price'))
                                        dummy1.append(i.get('date'))
                                        dummy1.append(i.get('time'))
                                        dummy1.append(i.get('location'))
                                        dummy1.append(i.get('status'))
                                        dummy1.append(i.get('reg_date'))
                                        l4.append(dummy1)
                                        # print(l1)
            pList=[]
            pandit=p_list.find()
            for i in pandit:
                                                        dummy2=[]
                                                        dummy2.append(i.get('name'))
                                                        dummy2.append(i.get('location'))
                                                        pList.append(dummy2)
            info2=t_services.find()
            pujaList=[]
            for i in info2:
                                if(session['email']==i.get('email')):
                                    dummy=[]
                                    dummy.append(i.get('_id'))
                                    dummy.append(i.get('p_name'))
                                    dummy.append(i.get('t_name'))
                                    dummy.append(i.get('price'))
                                    dummy.append(i.get('date'))
                                    dummy.append(i.get('time'))
                                    dummy.append(i.get('status'))
                                    pujaList.append(dummy)
            pra1=[]
            info3=prasad1.find()
            for i in info3:
                if session['email']==i.get('email'):
                    dummy=[]
                    dummy.append(i.get('_id'))
                    dummy.append(i.get('prasadam_name'))
                    dummy.append(i.get('price'))
                    dummy.append(i.get('total'))
                    # prasadamTotal=prasadamTotal+i.get('total')
                    dummy.append(i.get('qty'))
                    dummy.append(i.get('date'))
                    pra1.append(dummy)
            n=len(l3)+len(l4)+len(pujaList)+len(pra1)
            pra=[]
            info3=prasadam1.find()
            for i in info3:
                dummy=[]
                dummy.append(i.get('name'))
                pra.append(dummy)  
            print(n)
            
        return render_template('templepuja.html',l=l,n=n,pra=pra)
     
@app.route('/deleteTemplePuja/<id>',methods=['POST','GET'])
def deleteTemplePuja(id):
     uid=t_services.find_one({'_id':ObjectId(id)})
     if uid:
          t_services.delete_one({'_id':uid['_id']})
     return redirect(url_for('cart'))

@app.route('/addService',methods=['POST','GET'])
def addService():
     p_name=request.form['name']
     description=request.form['description']
     price=request.form['price']

     services={
          'p_name':p_name,
          'description':description,
          'price':price
     }
     puja_services.insert_one(services)
     return redirect(url_for('admin'))

@app.route('/deleteService/<id>',methods=['POST','GET'])
def deleteServices(id):
     uid1=puja_services.find_one({'_id':ObjectId(id)})
     if uid1:
          puja_services.delete_one({'_id':uid1['_id']})
     return redirect(url_for('admin'))

@app.route('/UpdateService/<id>',methods=['POST','GET'])
def UpdateService(id):
     if request.method == 'POST':
        info0 = puja_services.find_one({'_id': ObjectId(id)})
        if info0:
            update_fields = {}
            if 'name' in request.form and request.form['name'].strip() != "":
                update_fields['p_name'] = request.form['name']
            else:
                update_fields['name'] = info0['p_name']
            if 'price' in request.form and request.form['price'].strip() != "":
                update_fields['price'] = request.form['price']
            else:
                update_fields['price'] = info0['price']
            if 'description' in request.form and request.form['description'].strip() != "":
                update_fields['description'] = request.form['description']
            else:
                update_fields['description'] = info0['description']
           
            if update_fields:
                puja_services.update_one({'_id': ObjectId(id)}, {'$set': update_fields})        
     return redirect(url_for('admin'))

@app.route('/addTemples',methods=['POST','GET'])
def addTemples():
     t_name=request.form['t_name']
     location=request.form['location']
     p_name=request.form['p_name']
     price=request.form['price']
     description=request.form['description']
     temple={
          't_name':t_name,
           'location':location,
          'p_name':p_name,
         
          'price':price,
          'description':description
     }
     t_puja.insert_one(temple)
     return redirect(url_for('admin'))

@app.route('/deleteTemple/<id>',methods=['POST','GET'])
def deleteTemple(id):
     print(id)
     uid = t_puja.find_one({'_id': ObjectId(id)})
     if uid:
          t_puja.delete_one({'_id':uid['_id']})
     return redirect(url_for('admin'))

@app.route('/updateTemple/<id>',methods=['POST','GET'])
def updateTemple(id):
     info=t_puja.find_one({'_id':ObjectId(id)})
     t=[]
     if info:
            update_fields = {}
            if 't_name' in request.form and request.form['t_name'].strip() != "":
                update_fields['t_name'] = request.form['t_name']
            else:
                update_fields['t_name'] = info['t_name']
            if 'p_name' in request.form and request.form['p_name'].strip() != "":
                update_fields['p_name'] = request.form['p_name']
            else:
                update_fields['p_name'] = info['p_name']
            if 'location' in request.form and request.form['location'].strip() != "":
                update_fields['location'] = request.form['location']
            else:
                update_fields['location'] = info['location']
            if 'price' in request.form and request.form['price'].strip() != "":
                update_fields['price'] = request.form['price']
            else:
                update_fields['price'] = info['price']
            
            if 'description' in request.form and request.form['description'].strip() != "":
                update_fields['description'] = request.form['description']
            else:
                update_fields['description'] = info['description']
            if update_fields:
                t_puja.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
     return redirect(url_for('admin'))

@app.route('/addPrasadam',methods=['POST','GET'])
def addPrasadam():
     name=request.form['name']
     price=request.form['price']
     pra={
          'name':name,
          'price':price
     }
     prasadam1.insert_one(pra)
     return redirect(url_for('admin'))

@app.route('/prasadamUpdate/<id>',methods=['POST','GET'])
def prasadamUpdate(id):
     info=prasadam1.find_one({'_id':ObjectId(id)})
     if info:
          update_fields = {}
          if 'name' in request.form and request.form['name'].strip() != "":
                update_fields['name'] = request.form['name']
          else:
            update_fields['name'] = info['name']
          if 'price' in request.form and request.form['price'].strip() != "":
                update_fields['price'] = request.form['price']
          else:
                update_fields['price'] = info['price']
     if update_fields:
                prasadam1.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
     return redirect(url_for('admin'))

@app.route('/deletePrasadam/<id>',methods=['POST','GET'])
def deletePrasadam(id):
     uid=prasadam1.find_one({'_id':ObjectId(id)})
     if uid:
          prasadam1.delete_one({'_id': uid['_id']})
     return redirect(url_for('admin'))

@app.route('/editPandit', methods=['POST', 'GET'])
def editPandit():
    info = p_list.find_one({'email': session['email1']})
    if info:
        update_fields = {}
        if 'name' in request.form and request.form['name'].strip() != "":
            update_fields['name'] = request.form['name']
        else:
            update_fields['name'] = info['name']
        if 'email' in request.form and request.form['email'].strip() != "":
            update_fields['email'] = request.form['email']
            session['email1']=update_fields['email']
        else:
            update_fields['email'] = info['email']
        if 'phno' in request.form and request.form['phno'].strip() != "":
            update_fields['phno'] = request.form['phno']
        else:
            update_fields['phno'] = info['phno']
        if 'location' in request.form and request.form['location'].strip() != "":
            update_fields['location'] = request.form['location']
        else:
            update_fields['location'] = info['location']
        
        if update_fields:
            p_list.update_one({'email': session['email1']}, {'$set': update_fields})  
    return redirect(url_for('pandit'))

@app.route('/deleteP/<id>', methods=['POST', 'GET'])
def deleteP(id):
    uid = prasad1.find_one({'_id': ObjectId(id)})
    if uid:
        prasad1.delete_one({'_id': uid['_id']})
    return redirect(url_for('cart'))

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            # Store the message in the MongoDB collection
            # chat.insert_one({'message': message})

            # Your chatbot logic to generate a response
            account_sid = 'AC4da61e8f74035eabee3b23f2d68dc2d3'
            auth_token = '7d4264c8df08ac640d854db91d08f2bd'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message,
                from_='+12513135289',
                to='+91 9392419102'
            )
            print(f'Message SID: {message.sid}')
            return 'Message sent and processed'
        else:
            return 'No message provided', 400  # Bad request if message is missing
    else:
        return 'Method Not Allowed', 405  # Method not allowed for other HTTP methods

if __name__ == '__main__':
    app.run(debug=True)