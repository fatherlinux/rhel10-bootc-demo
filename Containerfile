FROM registry.redhat.io/rhel10/rhel-bootc

# Create necessary directories
RUN mkdir -p /var/roothome

RUN dnf groupinstall -y \
	 "Minimal Install" \
	; dnf -y clean all

RUN dnf -y install python3-pip && pip install flask

ADD app /root
COPY app.service /etc/systemd/system/app.service

# Prevent this version of Python from loading
RUN echo "exit(2)" > /usr/lib64/python3.12/site-packages/sitecustomize.py

#clean up after rpms using legacy paths:
RUN rm -rf /var/run

# Final lint step to prevent easy-to-catch issues at build time
RUN bootc container lint
