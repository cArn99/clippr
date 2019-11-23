from datetime import datetime
from flask import Flask, render_template, flash, request,redirect,url_for,session
from clippr import app
import pytube
import os
import errno
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
def on_progress(stream,chunk,file_handle,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage_of_completion=int((bytes_downloaded/total_size)*100)
    print(percentage_of_completion)

@app.route('/')
@app.route('/home.html',methods=['GET','POST'])
def download():
    if request.method=='POST':
        link12=request.form['fname']
        session["link12"]=link12
        return redirect(url_for('options'))
    return render_template("home.html");
    
@app.route('/options.html',methods=['GET','POST'])
def options():
    p="D:\Ahad\Videos\pytube"
    vid1080=[]
    vid720=[]
    vid480=[]
    vid360=[]
    vid240=[]
    vid144=[]
    link1=session.get('link12',None)
    yt=pytube.YouTube(link1)
    vid1080=yt.streams.filter(res="1080p").all()
    vid720=yt.streams.filter(res="720p").all()
    vid480=yt.streams.filter(res="480p").all()
    vid360=yt.streams.filter(res="360p").all()
    vid240=yt.streams.filter(res="240p").all()
    vid144=yt.streams.filter(res="144p").all()
    title=yt.title
    session["title"]=title
    imgurl=yt.thumbnail_url
    session["imgurl"]=imgurl
    if request.method=='POST':

        if request.form['res']=="1080":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid1080[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                yt.register_on_progress_callback(on_progress)
                vid1080[0].download(p)
                return redirect(url_for('thanks'))

        if request.form['res']=="720":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid720[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                yt.register_on_progress_callback(on_progress)
                vid720[0].download(p)
                return redirect(url_for('thanks'))

        if request.form['res']=="480":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid480[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                 yt.register_on_progress_callback(on_progress)
                 vid480[0].download(p)
                 return redirect(url_for('thanks'))

        if request.form['res']=="360":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid360[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                yt.register_on_progress_callback(on_progress)
                vid360[0].download(p)
                return redirect(url_for('thanks'))

        if request.form['res']=="240":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid240[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                yt.register_on_progress_callback(on_progress)
                vid240[0].download(p)
                return redirect(url_for('thanks'))

        if request.form['res']=="144":
            if request.form['path']!="":
                yt.register_on_progress_callback(on_progress)
                vid144[0].download(request.form['path'])
                return redirect(url_for('thanks'))
            else:
                yt.register_on_progress_callback(on_progress)
                vid144[0].download(p)
                return redirect(url_for('thanks'))

    return render_template("options.html",p=p,vid1080=vid1080,vid720=vid720,vid480=vid480,vid360=vid360,vid240=vid240,vid144=vid144,title=title,imgurl=imgurl);

@app.route('/thanks.html')
def thanks():
    title1=session.get('title',None)
    imgurl1=session.get('imgurl',None)
    return render_template("thanks.html",title1=title1,imgurl1=imgurl1);


