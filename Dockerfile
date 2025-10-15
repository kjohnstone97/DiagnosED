FROM python:3.13

ENV HF_HOME=/data/hf_cache

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

COPY . .

EXPOSE 7860

CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]