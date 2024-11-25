FROM localhost:8080/websphere_nd_8.5.0.1 as builder

ARG CAR CELL

RUN curl -o /tmp/imp.car ftp://wasftp:corenclnew@10.1.98.6/was/car/${CAR}  \
    && /home/ap/was/AppServer/bin/wsadmin.sh -conntype NONE -lang jython -c "AdminTask.importWasprofile(['-archive', '/tmp/imp.car'])" \
    && rm -rf /home/ap/was/AppServer/profiles/AppSrv01/installedApps/${CELL}/*
    


from centos:6.8

COPY --chown=1000:0 --from=builder /home/ap/was /home/ap/was

COPY start_server modify_password  updateHostName.py updatePassword.py  /work/

RUN useradd was -g 0 -m --uid 1000   && chown -R was:root /work && chmod +x /work/* 

#EXPOSE 2809 9402 9403 9353 9633 9100 11004 11003 9401 7276 7286 5558 5578 5060 5061 8880 9060 9043 9080 9443

ENV PATH /home/ap/was/AppServer/bin:$PATH

USER was

#RUN /work/config_server

CMD ["/work/start_server"]
