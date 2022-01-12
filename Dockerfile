FROM ubuntu
RUN apt-get update && apt-get install -y python
ADD helloworld.py /home/helloworld.py
CMD ["python", "./home/helloworkld.py"]