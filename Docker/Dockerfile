FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app

RUN apt-get update \
  && apt-get -y install tesseract-ocr \ # required for pytesseract \
  && apt-get -y install ffmpeg libsm6 libxext6

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-m", "src"]