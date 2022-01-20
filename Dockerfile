FROM python:3.7-slim-buster
ADD api.py /
ADD linear_model_model.pkl /
ADD linear_reg_model.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install pandas
RUN pip install joblib
RUN pip install scikit-learn
EXPOSE 8888
CMD [ "python", "./api.py"]