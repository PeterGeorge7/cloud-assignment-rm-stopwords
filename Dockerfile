FROM python

RUN pip install nltk

COPY . .

CMD ["python", "rm-stopword.py"]