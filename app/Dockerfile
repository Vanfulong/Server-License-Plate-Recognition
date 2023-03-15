FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx libzbar0
ENTRYPOINT ["python"]
CMD ["rest.py"]