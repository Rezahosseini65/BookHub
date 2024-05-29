FROM hemanhp/djbase:5.0

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR /src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/development.txt

RUN mkdir -p /vol/web/static && mkdir -p /vol/web/media && \
    chmod -R +x /scripts && \
    adduser --disabled-password --no-create-home bookhub && \
    chown -R bookhub:bookhub /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER bookhub

CMD ["run.sh"]