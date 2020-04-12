FROM python:3.8.0-alpine

RUN apk update && apk --update add gcc \
                                   g++ \
                                   musl-dev \
                                   python3-dev \
                                   libffi-dev \
                                   openssl-dev \
                                   bash \
                                   curl \
                                   zlib-dev \
                                   freetype-dev \
                                   lcms2-dev \
                                   openjpeg-dev \
                                   tiff-dev \
                                   tk-dev \
                                   tcl-dev \
                                   harfbuzz-dev \
                                   fribidi-dev

RUN pip install --upgrade pip
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /app
# COPY poetry.lock ./
COPY pyproject.toml ./
RUN $HOME/.poetry/bin/poetry install
# torch
RUN pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./ ./

CMD ["/root/.poetry/bin/poetry", "run", "jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--port=3100"]
