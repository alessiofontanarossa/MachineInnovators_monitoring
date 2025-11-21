FROM python:3.11-slim

WORKDIR /working_dir

COPY ./requirements.txt /working_dir
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/__init__.py /working_dir/src/
COPY ./src/model.py /working_dir/src/
COPY ./src/main.py /working_dir/src/

COPY ./tests/__init__.py /working_dir/tests/
COPY ./tests/test_model.py /working_dir/tests/
COPY ./tests/test_main.py /working_dir/tests/

# a simpler way would have been 'COPY . .'
EXPOSE 8080
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]