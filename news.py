import tkinter as tk
import nltk
from textblob import TextBlob, sentiments
from newspaper import Article

#nltk.download('punkt')


def summarize():
  url = url_link.get("1.0", "end").strip()
  article = Article(url)

  article.download()
  article.parse()

  article.nlp()

  title.config(state='normal')
  author.config(state='normal')
  publication.config(state='normal')
  summary.config(state='normal')
  sentiment.config(state='normal')

  title.delete('1.0', 'end')
  title.insert('1.0', article.title)

  author.delete('1.0', 'end')
  author.insert('1.0', ', '.join(article.authors))

  publication.delete('1.0', 'end')
  publication.insert(
      '1.0',
      str(article.publish_date) if article.publish_date else 'N/A')

  summary.delete('1.0', 'end')
  summary.insert('1.0', article.summary)

  analysis = TextBlob(article.text)
  sentiment.delete('1.0', 'end')
  sentiment.insert(
      '1.0',
      f'Polarity : {analysis.polarity} ,  Sentiment : {"positive" if analysis.polarity > 0 else "negative"}'
  )

  title.config(state='disabled')
  author.config(state='disabled')
  publication.config(state='disabled')
  summary.config(state='disabled')
  sentiment.config(state='disabled')


root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analyis')
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

url_link = tk.Text(root, height=1, width=140)
url_link.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
