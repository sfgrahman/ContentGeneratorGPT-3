from flask import Flask, render_template, request
import config
from aicontent import *

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        query = request.form['productDescription']
        print(query)

        query_s = 'Write a product description about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        query = request.form['jobDescription']
        print(query)

        query_s = 'Write a professional job descriptions about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        query = request.form['tweetIdeas']
        print(query)

        query_s = 'Write a tweet ideas about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        query = request.form['coldEmails']
        #print(query)

        query_s = 'Write a cold email to potential clients about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        query = request.form['socialMedia']
        print(query)

        query_s = 'Write a creative social media advert ideas for online campaigns about {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch():

    if request.method == 'POST':
        query = request.form['businessPitch']
        print(query)

        query_s = 'Write a pitch for your business idea about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        query = request.form['videoIdeas']
        print(query)

        query_s = 'Write some video ideas for YOuTube about: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        query = request.form['videoDescription']
        print(query)

        query_s = 'Write some cool video descriptions based on: {}'.format(query)
        openAIAnswerUnformatted  = openAIQuery(query_s)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('video-description.html', **locals())


if __name__ == '__main__':
    app.run()