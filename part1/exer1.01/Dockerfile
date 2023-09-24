FROM ubuntu:22.04

COPY exer1.01.sh /usr/local/bin/exer1.01.sh


# apt is only for terminals, apt is more appropriate for Dockerfiles
# update is necessary in this case for uuid-runtime
RUN adduser appuser && \
    chmod +x /usr/local/bin/exer1.01.sh && \
    apt-get update && \
    apt-get install -y uuid-runtime && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER appuser

ENTRYPOINT ["/usr/local/bin/exer1.01.sh"]
