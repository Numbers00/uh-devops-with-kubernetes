FROM alpine:3.18

COPY exer1.01.sh /usr/local/bin/exer1.01.sh
RUN adduser -S appuser && \
    chmod +x /usr/local/bin/exer1.01.sh && \
    apk add util-linux && \
    apk cache clean --purge && \
    rm -rf /etc/apk/repositories /var/cache/apk/*

USER appuser

ENTRYPOINT ["/usr/local/bin/exer1.01.sh"]
