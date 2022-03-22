FROM python:3.8-slim-buster
LABEL maintainer="Karthikeyan rathore <karthikeyan@tictactoe:main>"
WORKDIR /home/tictactoe
COPY requirements.txt /home/tictactoe/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /home/tictactoe
EXPOSE 5000
CMD ["chmod +x" , "app.py"]
CMD ["./app.py"] 
