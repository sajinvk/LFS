FROM python:3
ADD fixed_width_file.py /
WORKDIR /app
COPY . /app
RUN python -m pip install  argparse  \
 pandas 
ENTRYPOINT [ "python",  "./fixed_width_file.py"]
