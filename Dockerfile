#base image
FROM python
COPY . / Docker_Assingment
WORKDIR /Docker_Assingment
RUN pip install requests
RUN pip install bs4
CMD python submit.py