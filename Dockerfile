FROM petronetto/pytorch-alpine

RUN pip install --upgrade pip
RUN pip install --upgrade cython
RUN pip install numpy \
                Image \
                matplotlib \
                lab \
                jupyterlab \
                pytest

WORKDIR /app/app/config
COPY ./app/config/setup.py ./
RUN python setup.py
ADD https://cdn.pixabay.com/photo/2018/10/05/02/26/goldenretriever-3724972_960_720.jpg ./app/data/goldenretriever.jpg

WORKDIR /app

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--port=3100"]
