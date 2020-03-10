FROM python:3.7.0-stretch as base

ENV AUTHOR ady.buxton@fujitsu.com
ENV UPDATED 20200306

# Initialize
WORKDIR /usr/src/app/

# Copy data for production
COPY . /usr/src/app/

ENV LIBRARY_PATH=/lib:/usr/lib

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


CMD ["python3","/usr/src/app/app.py"]
