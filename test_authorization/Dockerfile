FROM python:3.6
ENV LOG=1
WORKDIR /app
ADD requirements.txt /app/
ADD test_authorization.py /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
CMD python3 ./test_authorization.py