FROM localhost:80/nd_8.5.0.1_opt_base as builder

# patch wsadmin.sh to avoid error when deploying apps
RUN sed -i 's/-Xms256m/-Xms1024m/g' /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh \
    && sed -i 's/-Xmx256m/-Xmx1024m/g' /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh

LABEL maintainer="wangyt" \
      BuildLabel="$BUILDLABEL" \
      vendor="IBM" \
      name="IBM WebSphere Traditional" \
      version="8.5.0.1" \
      summary="Image for WebSphere Traditional and Centos6.8" \
      description="This image contains the WebSphere Traditional runtime with Centos6.8 as the base OS."

RUN rm -rf /etc/yum.repos.d/*  \
    && curl -o /etc/yum.repos.d/rhel6.8.repo ftp://wasftp:@10.1.98.6/was/rhel6.8.repo 

ARG USER=was

ARG PROFILE_NAME=AppSrv01
ARG CELL_NAME=DefaultCell01
ARG NODE_NAME=DefaultNode01
ARG HOST_NAME=localhost
ARG SERVER_NAME=server1
ARG ADMIN_USER_NAME=wasadmin

COPY scripts/ /work/


RUN useradd $USER -g 0 -m --uid 1001 \
  && chmod -R +x /work/* \
  && mkdir /etc/websphere \
  && mkdir /work/config \
  && chown -R 1001:0 /work /opt/IBM /etc/websphere \
  && chmod -R g+rwx /work


USER $USER

ENV PATH=/opt/IBM/WebSphere/AppServer/bin:$PATH \
    PROFILE_NAME=$PROFILE_NAME \
    SERVER_NAME=$SERVER_NAME \
    ADMIN_USER_NAME=$ADMIN_USER_NAME \
    EXTRACT_PORT_FROM_HOST_HEADER=true


RUN /work/create_profile.sh \
  && find /opt/IBM -user was ! -perm -g=w -print0 | xargs -0 chmod g+w \
  && chmod -R g+rwx /home/was/.java/

# patch server.xml to add -Xnoloa option until JDK is fixed

#RUN sed -i 's/genericJvmArguments=""/genericJvmArguments="-Xnoloa"/' /opt/IBM/WebSphere/AppServer/profiles/$PROFILE_NAME/config/cells/$CELL_NAME/nodes/$NODE_NAME/servers/$SERVER_NAME/server.xml

USER root
RUN ln -s /opt/IBM/WebSphere/AppServer/profiles/${PROFILE_NAME}/logs /logs && chown 1001:0 /logs
USER $USER

CMD ["env", "/work/start_server.sh"]
#CMD ["env", "JVM_EXTRA_CMD_ARGS=-Xnoloa", "/work/start_server.sh"]


#RUN /opt/IBM/WebSphere/AppServer/bin/managesdk.sh -setCommandDefault -sdkname 1.7_64 \
#    && /opt/IBM/WebSphere/AppServer/bin/managesdk.sh -setNewProfileDefault -sdkname 1.7_64 \
#    && /opt/IBM/WebSphere/AppServer/bin/manageprofiles.sh -create  -profileName AppSrv01 \
#    && mkdir -p /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/extJDBCDriver/oracle \
#    && curl -o /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/extJDBCDriver/oracle/ojdbc6.jar \
#    ftp://wasftp:@10.1.98.6/was/ojdbc6.jar


