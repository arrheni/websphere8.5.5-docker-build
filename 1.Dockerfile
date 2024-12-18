
FROM centos:6.8 as builder

#MAINTAINER wangyt

COPY soft  /tmp

RUN rm -rf /etc/yum.repos.d/* && cp /tmp/rhel6.8.repo /etc/yum.repos.d/ \
    && yum clean all && yum install -y unzip glibc.i686 libgcc.i686 util-linux


###################### IBM Installation Manager ##########################

# Install IBM Installation Manager
RUN unzip -qd /tmp/im /tmp/im/InstalMgr1.5.2_LNX_X86_WAS_8.5.zip \
    && /tmp/im/installc -acceptLicense \
            -installationDirectory /home/ap/was/InstallationManager/eclipse  \
    && rm -fr /tmp/im

################# IBM WebSphere Application Server ######################

# Install IBM WebSphere Application Server ND v850
RUN unzip -qd /tmp/was-nd /tmp/was-nd/WAS_ND_V8.5_1_OF_3.zip \
    && unzip -qd /tmp/was-nd  /tmp/was-nd/WAS_ND_V8.5_2_OF_3.zip \
    && unzip -qd /tmp/was-nd  /tmp/was-nd/WAS_ND_V8.5_3_OF_3.zip \
    && /home/ap/was/InstallationManager/eclipse/tools/imcl \
            install com.ibm.websphere.ND.v85_8.5.0.20120501_1108 \
            -repositories  /tmp/was-nd/repository.config  \
            -installationDirectory /home/ap/was/AppServer \
            -sharedResourcesDirectory /home/ap/was/IMShared \
            -properties cic.selector.nl=zh -acceptLicense  \
#           -showVerboseProgress  \
    && rm -fr /tmp/was-nd

###### IBM WebSphere Application Server Network Deployment Fixpack #######

# Install IBM WebSphere Application Server ND Fixpack v850
RUN unzip  -qd /tmp/was-fp /tmp/was-fp/8.5.0-WS-WAS-FP0000001-part1.zip \
    && unzip  -qd /tmp/was-fp /tmp/was-fp/8.5.0-WS-WAS-FP0000001-part2.zip \
    && /home/ap/was/InstallationManager/eclipse/tools/imcl \
            install com.ibm.websphere.ND.v85_8.5.1.20121017_1724 \
            -repositories /tmp/was-fp/repository.config \
            -installationDirectory /home/ap/was/AppServer \
            -sharedResourcesDirectory /home/ap/was/IMShared \
            -properties cic.selector.nl=zh -acceptLicense \
#           -showVerboseProgress  \
    && rm -fr /tmp/was-fp

########################### Install Java SDK 1.7 ########################

# Install Java SDK 1.7
RUN unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/was.repo.8550.java7_part1.zip \
    && unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/was.repo.8550.java7_part2.zip \
    && unzip -qd /tmp/jdk1.7 /tmp/jdk1.7/was.repo.8550.java7_part3.zip \
    && /home/ap/was/InstallationManager/eclipse/tools/imcl \
         install com.ibm.websphere.IBMJAVA.v70_7.0.4001.20130510_2103 \
             -repositories /tmp/jdk1.7/repository.config \
             -installationDirectory /home/ap/was/AppServer \
             -sharedResourcesDirectory /home/ap/was/IMShared  \
             -properties cic.selector.nl=zh  -acceptLicense  \
#            -showVerboseProgress  \
    && rm -fr /tmp/jdk1.7  


#RUN /home/ap/was/AppServer/bin/managesdk.sh -setCommandDefault -sdkname 1.7_64 \
#    && /home/ap/was/AppServer/bin/managesdk.sh -setNewProfileDefault -sdkname 1.7_64 \
#    && /home/ap/was/AppServer/bin/manageprofiles.sh -create  -profileName AppSrv01 \
#    && mkdir -p /home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle \
#    && mv /tmp/ojdbc6.jar /home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle/


FROM centos:6.8 

COPY --from=builder /home/ap/was/AppServer /home/ap/was/AppServer



#CMD ["tar","cvf","/tmp/was.tar","/home/ap/was/AppServer"]
