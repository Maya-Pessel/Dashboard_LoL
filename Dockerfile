FROM python:3.9

COPY test.py .

COPY style.css .

COPY match_full_time.csv .

RUN  pip3 install streamlit && pip3 install matplotlib && pip3 install pandas && pip3 install plotly express

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "test.py" ]