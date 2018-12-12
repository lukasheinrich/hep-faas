FROM pyhf/pyhf
RUN apk add g++ python-dev libc-dev musl-dev
RUN pip install jupyter https://github.com/diana-hep/excursion/archive/master.zip
RUN pip install requests
ADD . /notebook
WORKDIR /notebook
CMD ["jupyter","notebook","--ip=0.0.0.0","--allow-root","BlackBox.ipynb"]
