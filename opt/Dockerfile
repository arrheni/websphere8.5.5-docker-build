FROM centos:6.8 as builder

#MAINTAINER wangyt

RUN rm -rf /etc/yum.repos.d/*  \
    && curl -o /etc/yum.repos.d/rhel6.8.repo ftp://wasftp:corenclnew@10.1.98.6/was/rhel6.8.repo \
    && yum clean all && yum install -y unzip glibc.i686 libgcc.i686 util-linux \
    && mkdir /tmp/{im,jdk1.7,was-fp,was-nd}


###################### IBM Installation Manager ##########################

# Install IBM Installation Manager
RUN curl ftp://wasftp:corenclnew@10.1.98.6/was/im/InstalMgr1.5.2_LNX_X86_WAS_8.5.zip >/tmp/im/im.zip \
    && unzip -qd /tmp/im /tmp/im/im.zip\
    && /tmp/im/installc -acceptLicense \
	    -installationDirectory /opt/IBM/WebSphere/InstallationManager/eclipse  \
    && rm -fr /tmp/im

################# IBM WebSphere Application Server ######################

# Install IBM WebSphere Application Server ND v85
RUN curl ftp://wasftp:corenclnew@10.1.98.6/was/was-nd/WAS_ND_V8.5_1_OF_3.zip >/tmp/was-nd/nd1.zip  \
    && curl ftp://wasftp:corenclnew@10.1.98.6/was/was-nd/WAS_ND_V8.5_2_OF_3.zip >/tmp/was-nd/nd2.zip  \
    && curl ftp://wasftp:corenclnew@10.1.98.6/was/was-nd/WAS_ND_V8.5_3_OF_3.zip >/tmp/was-nd/nd3.zip  \
    && unzip -qd /tmp/was-nd /tmp/was-nd/nd1.zip \
    && unzip -qd /tmp/was-nd  /tmp/was-nd/nd2.zip \
    && unzip -qd /tmp/was-nd  /tmp/was-nd/nd3.zip \
    && /opt/IBM/WebSphere/InstallationManager/eclipse/tools/imcl \
	    install com.ibm.websphere.ND.v85_8.5.0.20120501_1108 \
	    -repositories  /tmp/was-nd/repository.config  \
	    -installationDirectory /opt/IBM/WebSphere/AppServer \
	    -sharedResourcesDirectory /opt/IBM/WebSphere/IMShared \
	    -properties cic.selector.nl=zh -acceptLicense  \
#	    -showVerboseProgress  \
    && rm -fr /tmp/was-nd

###### IBM WebSphere Application Server Network Deployment Fixpack #######

# Install IBM WebSphere Application Server ND Fixpack v85
RUN curl ftp://wasftp:corenclnew@10.1.98.6/was/was-fp/8.5.0-WS-WAS-FP0000001-part1.zip >/tmp/was-fp/fp1.zip  \
    && curl ftp://wasftp:corenclnew@10.1.98.6/was/was-fp/8.5.0-WS-WAS-FP0000001-part2.zip >/tmp/was-fp/fp2.zip  \
    && unzip  -qd /tmp/was-fp /tmp/was-fp/fp1.zip \
    && unzip  -qd /tmp/was-fp /tmp/was-fp/fp2.zip \
    && /opt/IBM/WebSphere/InstallationManager/eclipse/tools/imcl \
	    install com.ibm.websphere.ND.v85_8.5.1.20121017_1724 \
	    -repositories /tmp/was-fp/repository.config \
	    -installationDirectory /opt/IBM/WebSphere/AppServer \
	    -sharedResourcesDirectory /opt/IBM/WebSphere/IMShared \
	    -properties cic.selector.nl=zh -acceptLicense \
#	    -showVerboseProgress  \
    && rm -fr /tmp/was-fp

########################### Install Java SDK 1.7 ########################

# Install Java SDK 1.7
RUN curl ftp://wasftp:corenclnew@10.1.98.6/was/jdk1.7/was.repo.8550.java7_part1.zip  >/tmp/jdk1.7/jdk1.zip  \
    && curl ftp://wasftp:corenclnew@10.1.98.6/was/jdk1.7/was.repo.8550.java7_part2.zip  >/tmp/jdk1.7/jdk2.zip  \
    && curl ftp://wasftp:corenclnew@10.1.98.6/was/jdk1.7/was.repo.8550.java7_part3.zip  >/tmp/jdk1.7/jdk3.zip  \
    && unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/jdk1.zip \
    && unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/jdk2.zip \
    && unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/jdk3.zip \
    && /opt/IBM/WebSphere/InstallationManager/eclipse/tools/imcl \
         install com.ibm.websphere.IBMJAVA.v70_7.0.4001.20130510_2103 \
	     -repositories /tmp/jdk1.7/repository.config \
	     -installationDirectory /opt/IBM/WebSphere/AppServer \
	     -sharedResourcesDirectory /opt/IBM/WebSphere/IMShared  \
	     -properties cic.selector.nl=zh  -acceptLicense  \
#	     -showVerboseProgress  \
    && rm -fr /tmp/jdk1.7  


#RUN /opt/IBM/WebSphere/AppServer/bin/managesdk.sh -setCommandDefault -sdkname 1.7_64 \
#    && /opt/IBM/WebSphere/AppServer/bin/managesdk.sh -setNewProfileDefault -sdkname 1.7_64 \
#    && /opt/IBM/WebSphere/AppServer/bin/manageprofiles.sh -create  -profileName AppSrv01 \
#    && mkdir -p /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/extJDBCDriver/oracle \
#    && curl -o /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/extJDBCDriver/oracle/ojdbc6.jar \
#    ftp://wasftp:corenclnew@10.1.98.6/was/ojdbc6.jar


FROM centos:6.8

COPY --from=builder /opt/IBM/WebSphere/AppServer /opt/IBM/WebSphere/AppServer



#CMD ["tar","cvf","/tmp/was.tar","/opt/IBM/WebSphere/AppServer"]
