from flask import Flask, render_template, url_for, flash, request
from forms import inputform
app = Flask(__name__)
def fin(ind,s,lis):
    num=0.0
    while ord(s[ind])<=57 and ord(s[ind])>=48:
        lis[2]+=1
        x=ord(s[ind])-48
        num=num*10 + x
        ind+=1

    if s[ind]=='.':
        lis[2]=lis[2]+1
        ind+=1
        div=10.000
        while ord(s[ind])<=57 and ord(s[ind])>=48:
            lis[2]+=1
            x=ord(s[ind])-48
            num=num+x/div
            div=div*10
            ind=ind+1
    return num

def sol(s,lis):
    n=len(s)
    for i in range(n):
        if s[i]=='(':
            lis[1]=i
        elif s[i]==')':
            lis[0]=i
            break
# lis[0]=next lis[1]=prev
# s = input()
def getans(s):
    lis =[-1,-1,0]
    sol(s,lis)

    # print("Initial Circuit: " + s)
    anss=[s];
    cnt=1;
    while lis[1]!=-1:
        ss=""
        j=lis[1]
        k=lis[0]
        if j!=0:
            ss=ss+s[:j]
        # print(ss)
        num=0
        a='*'
        j+=1
        i=j
        while i<k:
            if ord(s[i])<=57 and ord(s[i])>=48 and a=='*':
                store=fin(i,s,lis)
                num=store
                i+=lis[2]
                lis[2]=0
            elif ord(s[i])<=57 and ord(s[i])>=48 and a=='|':
                store=fin(i,s,lis)
                num+=store
                i= i+lis[2]
                lis[2]=0
            elif ord(s[i])<=57 and ord(s[i])>=48 and a=='+':
                store=fin(i,s,lis)
                num=(num*store)/(num+store)
                i+=lis[2]
                lis[2]=0
            else:
                a=s[i]
                i+=1
        ss+=str(num)
        ss+=s[k+1:]
        anss.append(ss)
        s=ss
        cnt+=1
        lis=[-1,-1,0]
        a='*'
        sol(s,lis)
    return anss

app.config['SECRET_KEY']= 'qw8791w7e1d17d891d798d1798df17we9fwv1g8'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/report', methods=['GET','POST'])
def Report():
    return render_template('report.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/solve', methods=['GET','POST'])
def solve():
    if request.method == 'POST':
      user = request.form['name']
      result = getans(user)
      return render_template('result.html' , input=user,output=result, len=len(result))

@app.route('/answer', methods=['GET','POST'])
def answer():
    form =inputform()
    return render_template('answer.html', title='Find Answer', form=form)

if __name__ =="__main__":
    app.run(debug=True)
