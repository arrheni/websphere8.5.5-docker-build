FROM localhost:80/websphere_nd_8.5.0.1 as builder

RUN rm -rf /etc/yum.repos.d/*  \
    && curl -o /etc/yum.repos.d/rhel6.8.repo ftp://wasftp:corenclnew@10.1.98.6/was/rhel6.8.repo \
    && yum clean all && yum install -y util-linux 


RUN /home/ap/was/AppServer/bin/managesdk.sh -setCommandDefault -sdkname 1.7_64 \
    && /home/ap/was/AppServer/bin/managesdk.sh -setNewProfileDefault -sdkname 1.7_64 \
    && curl -o /tmp/imp.car ftp://wasftp:corenclnew@10.1.98.6/was/car/ap2-qry1.car \
    && /home/ap/was/AppServer/bin/manageprofiles.sh -create  -profileName AppSrv01 \
        -nodeName DefaultNode01  -cellName DefaultCell01  -hostName localhost  \
        -serverName server1 -enableAdminSecurity true -adminUserName wasadmin -adminPassword "admin" \
    && mkdir -p /home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle \
    && curl -o /home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle/ojdbc6.jar \
      ftp://wasftp:corenclnew@10.1.98.6/was/ojdbc6.jar  \
    && sed -i 's/-Xms256m/-Xms2048m/g' /home/ap/was/AppServer/bin/wsadmin.sh \
    && sed -i 's/-Xmx256m/-Xmx4096m/g' /home/ap/was/AppServer/bin/wsadmin.sh \
    && /home/ap/was/AppServer/bin/wsadmin.sh -conntype NONE -lang jython -c "AdminTask.importWasprofile(['-archive', '/tmp/imp.car'])" \
    && useradd was -g 0 -m --uid 1000  && chown -R 1000:0 /home/ap/was

from centos:6.8

COPY --chown=1000:0 --from=builder /home/ap/was /home/ap/was

COPY start_server modify_password  updateHostName.py updatePassword.py config_server  create.py /work/

RUN useradd was -g 0 -m --uid 1000   && chown -R was:root /work && chmod +x /work/* 

EXPOSE 2809 9402 9403 9353 9633 9100 11004 11003 9401 7276 7286 5558 5578 5060 5061 8880 9060 9043 9080 9443

ENV PATH /home/ap/was/AppServer/bin:$PATH

USER was

#RUN /work/config_server

CMD ["/work/start_server"]
