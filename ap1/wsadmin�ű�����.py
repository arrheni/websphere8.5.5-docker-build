#####################################################################################
#                                                                                   #
#  Script to create                                                                 #
#                                                                                   #
#  Usage : wsadmin -lang jython -f create.py                                        #
#                                                                                   #
#####################################################################################
import sys
import socket


def cf_uninstallapp(appname):

    funcname='卸载应用'

    if(AdminApp.list().find(appname) == -1):

        print appname+'-应用未安装'

        return

    AdminApp.uninstall(appname)

    AdminConfig.save()

    print funcname + '-完毕'

    return


def cf_createjdbcprovider():

    funcname='创建oracleJDBC提供程序'
    
    AdminConfig.create('VariableSubstitutionEntry', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|variables.xml#VariableMap_1)', '[[symbolicName "ORACLE_JDBC_DRIVER_PATH"] [description ""] [value "/home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle"]]')

    #AdminTask.createJDBCProvider('[-scope Cell=' + AdminControl.getCell() +' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${WAS_INSTALL_ROOT}/lib/ojdbc6.jar ] -nativePath "" ]')
    AdminTask.createJDBCProvider('[-scope Cell=' + AdminControl.getCell() +' -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')
    #AdminTask.createJDBCProvider('[-scope Node=DefaultNode01,Server=server1 -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')

    AdminConfig.save()

    print funcname + '-完毕'

    return




def cf_createJ2Cdata(name, user, pwd):

    funcname='创建J2C认证数据'

    arg='[-alias ' + name + ' -user ' + user + ' -password ' + pwd + ' -description  ]'

    AdminTask.createAuthDataEntry(arg)

    AdminConfig.save()

    print funcname + name + '-完毕'

    return

#2.2.5  创建数据源
#参数 datasourcename 数据源名称 示例 'kb'

#参数 jndiname jndi名字 示例 'jdbc/kb'

#参数 authalias 使用的J2C认证数据名 示例 'newcc'

#参数 jdbcurl JDBC连接数据库的url 示例 'jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=sz-qzgbkdb1)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=sz-qzgbkdb2)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=szgbkqz)))'

cf_createdatasource(PAJndiDataSource, jdbc/PAJndiDataSource, APP___PAS__DBUSER, jdbc:oracle:thin:@10.1.96.16:1521/):

def cf_createdatasource(datasourcename, jndiname, authalias, jdbcurl):

    funcname='创建数据源'

    jdbcCFname=datasourcename + '_CF'

    authalias_use=AdminControl.getNode() + '/' + authalias



    #获取oracle jdbc提供程序ID

    oracle_jdbc='"Oracle JDBC Driver('

    jdbc_list_1=AdminConfig.list('JDBCProvider', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    jdbc_list_2=jdbc_list_1.split(getlinesep())

    jdbc_index=0

    jdbcproviderid=''



    for i in range(len(jdbc_list_2)):

        if jdbc_list_2[i].find(oracle_jdbc) == 0:

            jdbc_index=i

            break



    jdbcproviderid=jdbc_list_2[jdbc_index].split('|resources.xml#')[1].split(')')[0]

    print jdbcproviderid





    #创建数据源

    AdminTask.createDatasource('"Oracle JDBC Driver(cells/' + AdminControl.getCell() + '|resources.xml#' + jdbcproviderid + ')"', '[-name ' + datasourcename + ' -jndiName ' + jndiname + ' -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias ' + authalias_use + ' -configureResourceProperties [[URL java.lang.String ' + jdbcurl + ']]]')
    #AdminTask.createDatasource( p1 , '[-name PAJndiDataSource -jndiName jdbc/PAJndiDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/APP___PAS__DBUSER -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@10.1.96.16:1521/pasdb]]]')


    #获取数据源ID

    datasource_list_1=AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:' + AdminControl.getCell()+ '/'))

    datasource_list_2=datasource_list_1.split(getlinesep())

    datasource_index=0

    datasourceid=''



    for i in range(len(datasource_list_2)):

        if datasource_list_2[i].find(datasourcename+ '(') == 0:

            datasource_index=i

            break



    datasourceid=datasource_list_2[datasource_index].split('|resources.xml#')[1].split(')')[0]

    print datasourceid





    #获取CMPConnectorFactoryID

    jdbcCF_list_1=AdminConfig.list('CMPConnectorFactory', AdminConfig.getid( '/Cell:' + AdminControl.getCell()+ '/'))

    jdbcCF_list_2=jdbcCF_list_1.split(getlinesep())

    jdbcCF_index=0

    jdbcCFid=''



    for i in range(len(jdbcCF_list_2)):

        if jdbcCF_list_2[i].find(jdbcCFname + '(') == 0:

            jdbcCF_index=i

            break



    jdbcCFid=jdbcCF_list_2[jdbcCF_index].split('|resources.xml#')[1].split(')')[0]

    print jdbcCFid



    #设置认证别名

    arg1='(cells/' + AdminControl.getCell() + '|resources.xml#' + datasourceid + ')'

    arg2='[[authDataAlias ' + authalias_use + '] [mappingConfigAlias ""]]'

    AdminConfig.create('MappingModule', arg1 , arg2)



    arg1='(cells/' + AdminControl.getCell() + '|resources.xml#' + jdbcCFid + ')'

    arg2='[[name "' + jdbcCFname + '"] [authDataAlias "' + authalias_use + '"] [xaRecoveryAuthAlias ""]]'

    AdminConfig.modify(arg1, arg2)



    arg2='[[authDataAlias ' + authalias_use + '] [mappingConfigAlias ""]]'

    AdminConfig.create('MappingModule', arg1, arg2)



    AdminConfig.save()

    print funcname + '-完毕'

    return


def cf_createvirtualhost(hostname):

    funcname='创建虚拟主机'



    AdminConfig.create('VirtualHost', AdminConfig.getid('/Cell:' + AdminControl.getCell()+ '/'), '[[name "' + hostname + '"]]')

    AdminConfig.save()



    print funcname + '-完毕'

    return


def cf_setvirtualhostport(hostname, portnum):

    funcname='设置虚拟主机端口'



    AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/VirtualHost:' + hostname + '/'), '[[hostname "*"] [port "' + portnum + '"]]')



    AdminConfig.save()

    print funcname + '-完毕'

    return


def cf_createserverport(portname, portnum, servername='server1'):

    funcname='设置服务端口'



    #获取ServerEntryID

    serverentry_list_1=AdminConfig.list('ServerEntry', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    serverentry_list_2=serverentry_list_1.split(getlinesep())

    serverentry_index=0

    serverentryid=''



    for i in range(len(serverentry_list_2)):

        if serverentry_list_2[i].find(servername+ '(') == 0:

            serverentry_index=i

            break



    serverentryid=serverentry_list_2[serverentry_index].split('|serverindex.xml#')[1].split(')')[0]

    print serverentryid





    AdminConfig.create('NamedEndPoint', '(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '|serverindex.xml#' + serverentryid +')', '[[endPointName "' + portname + '"]]')





    #获取NamedEndPointID

    nameendpoint_list_1=AdminConfig.list('NamedEndPoint', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    nameendpoint_list_2=nameendpoint_list_1.split(getlinesep())



    for i in range(len(nameendpoint_list_2)):

        if AdminConfig.show(nameendpoint_list_2[i]).find('[endPointName ' + portname + ']') != -1:

            nameendpoint_index=i

    nameendpointid=nameendpoint_list_2[nameendpoint_index].split('|serverindex.xml#')[1].split(')')[0]



    print nameendpointid



    AdminConfig.create('EndPoint', '(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '|serverindex.xml#' + nameendpointid + ')', '[[port "' + portnum + '"] [host "*"]]')



    AdminConfig.save()

    print funcname + '-完毕'

    return



def cf_createchain(chainname, portname, type='HTTP', servername='server1'):

    funcname='设置Web容器传输链设置'



    #获取TransportChannelServiceID

    tcs_list_1=AdminConfig.list('TransportChannelService', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    tcs_list_2=tcs_list_1.split(getlinesep())



    tcs_index=0

    tcsid=''



    for i in range(len(tcs_list_2)):

        if tcs_list_2[i].find('/' + servername + '|') != -1:

            tcs_index=i

            break



    tcsid=tcs_list_2[tcs_index].split('|server.xml#')[1].split(')')[0]

    print tcsid



    #获取NamedEndPointID

    nameendpoint_list_1=AdminConfig.list('NamedEndPoint', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    nameendpoint_list_2=nameendpoint_list_1.split(getlinesep())



    for i in range(len(nameendpoint_list_2)):

        if AdminConfig.show(nameendpoint_list_2[i]).find('[endPointName ' + portname + ']') != -1:

            nameendpoint_index=i

    nameendpointid=nameendpoint_list_2[nameendpoint_index].split('|serverindex.xml#')[1].split(')')[0]



    print nameendpointid



    #判断创建HTTP/HTTPS传输链

    if(type == 'HTTPS'):

        chaintemplate='WebContainer-Secure(templates/chains|webcontainer-chains.xml#Chain_2'

    else:

        chaintemplate='WebContainer(templates/chains|webcontainer-chains.xml#Chain_1'



    AdminTask.createChain('(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '/servers/' + servername + '|server.xml#' + tcsid + ')', '[-template ' + chaintemplate + ') -name ' + chainname + ' -endPoint (cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '|serverindex.xml#' + nameendpointid + ')]')



    AdminConfig.save()

    print funcname + '-完毕'

    return

#   设置JAVA虚拟机堆大小
#参数 initialsize 初始堆大小 示例 '1024'

#参数 maxsize 最大堆大小 示例 '2048'

#参数 servername 默认'server1' 示例 'server1'



def cf_setjavaheapsize(initialsize, maxsize, servername='server1'):

    funcname='设置JAVA虚拟机堆大小'

     jvm=AdminConfig.list("JavaVirtualMachine")
      #AdminConfig.modify(jvm, '[[initialHeapSize 51200]]')
      #AdminConfig.modify(jvm, '[[maximumHeapSize 51200]]')
     AdminConfig.modify(jvm,[['genericJvmArguments',"-Dcom.ibm.websphere.webservices.DisableIBMJAXWSEngine=true -Xdisableexplicitgc -Dfile.encoding=UTF-8  -Ddefault.client.encoding=UTF-8  -Dclient.encoding.override=UTF-8  -Duser.language=zh  -Duser.region=CN  -Duser.country=CN"]])

    AdminTask.setJVMProperties('[-nodeName ' + AdminControl.getNode() + ' -serverName ' + servername + ' -initialHeapSize ' + initialsize + ' -maximumHeapSize ' + maxsize + ']')



    AdminConfig.save()

    print funcname + '-完毕'

    return





def cf_setwebcontainerthread(minsize, maxsize, threadname='WebContainer', servername='server1'):

    funcname='设置Web容器线程池'

      #pools=AdminConfig.list('ThreadPool', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')).split()
      ##print pools
      #AdminConfig.modify( pools[10] , '[[maximumSize "350"] [name "WebContainer"] [minimumSize "50"] [inactivityTimeout "60000"] [description ""] [isGrowable "false"]]')

    #获取WebContainerID

    thread_list_1=AdminConfig.list('ThreadPool', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    thread_list_2=thread_list_1.split(getlinesep())



    thread_index=0

    threadid=''



    for i in range(len(thread_list_2)):

        if thread_list_2[i].find(threadname + '(') != -1:

            thread_index=i

            break



    threadid=thread_list_2[thread_index].split('|server.xml#')[1].split(')')[0]

    print threadid



    AdminConfig.modify('(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '/servers/' + servername + '|server.xml#' + threadid + ')', '[[maximumSize "' + maxsize + '"] [name "' + threadname + '"] [minimumSize "' + minsize + '"]]')



    AdminConfig.save()

    print funcname + '-完毕'

    return


def cf_setconnectionpool(datasourcename, mincon, maxcon):

    funcname='设置数据源连接池'



    #获取数据源信息

    datasource_list_1=AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:' + AdminControl.getCell()+ '/'))

    datasource_list_2=datasource_list_1.split(getlinesep())

    datasource_index=0



    for i in range(len(datasource_list_2)):

        if datasource_list_2[i].find(datasourcename+ '(') == 0:

            datasource_index=i

            break



    datasourceinfo=AdminConfig.show(datasource_list_2[datasource_index])



    #获取连接池ID

    connectionpoolid=datasourceinfo.split('[connectionPool')[1].split('|resources.xml#')[1].split(')')[0]

    print connectionpoolid





    AdminConfig.modify('(cells/' + AdminControl.getCell() + '|resources.xml#' + connectionpoolid + ')', '[[maxConnections "' + maxcon + '"] [minConnections "' + mincon + '"]]')

    AdminConfig.save()



    print funcname + '-完毕'

    return

#   设置JVM日志参数
#参数 streamredirectname 需要设置的输出名称 示例 'SystemErr.log'或'SystemOut.log'

#参数 logsize 日志文件大小，单位M 示例 '20'

#参数 lognum 日志文件数量 示例 '10'

#参数 servername 默认'server1' 示例 'server1'



def cf_setJVMlog(streamredirectname, logsize, lognum, servername='server1'):

    funcname='设置JVM日志'



    streamredirect_list_1=AdminConfig.list('StreamRedirect', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    streamredirect_list_2=streamredirect_list_1.split(getlinesep())



    #遍历StreamRedirect

    for i in range(len(streamredirect_list_2)):

        streamredirectinfo=AdminConfig.show(streamredirect_list_2[i])

        if streamredirectinfo.find(streamredirectname) != -1:

            streamredirectid=streamredirect_list_2[i].split('server.xml#')[1].split(')')[0]

            AdminConfig.modify('(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '/servers/' + servername + '|server.xml#' + streamredirectid + ')', '[[rolloverType "SIZE"] [maxNumberOfBackupFiles "' + lognum + '"] [rolloverSize "' + logsize + '"] [baseHour "24"] [rolloverPeriod "24"] [formatWrites "true"]  [messageFormatKind "BASIC"] [suppressWrites "false"] [suppressStackTrace "false"]]')



    AdminConfig.save()

    print funcname + '-完毕'

    return



def cf_createsslkey(keyname, keypath, pwd, keytype='JKS'):

    funcname='创建SSL证书库和密钥'



    AdminTask.createKeyStore('[-keyStoreName ' + keyname + ' -scopeName (cell):' + AdminControl.getCell() + ':(node):' + AdminControl.getNode() + ' -keyStoreDescription  -keyStoreLocation ' + keypath + ' -keyStorePassword ' + pwd + ' -keyStorePasswordVerify ' + pwd + ' -keyStoreType ' + keytype + ' -keyStoreInitAtStartup false -keyStoreReadOnly false -keyStoreStashFile false -keyStoreUsage SSLKeys ]')

    AdminConfig.save()

    print funcname + '-完毕'

    return





def cf_createsslconfig(sslname, keyname, keyalias):

    funcname='创建SSL配置'



    AdminTask.createSSLConfig('[-alias ' + sslname + ' -type JSSE -scopeName (cell):' + AdminControl.getCell() + ':(node):' + AdminControl.getNode() + ' -keyStoreName ' + keyname + ' -keyStoreScopeName (cell):' + AdminControl.getCell() + ':(node):' + AdminControl.getNode() + ' -trustStoreName ' + keyname + ' -trustStoreScopeName (cell):' + AdminControl.getCell() + ':(node):' + AdminControl.getNode() + ' -serverKeyAlias ' + keyalias + ' -clientKeyAlias ' + keyalias + ' ]')

    AdminConfig.save()

    print funcname + '-完毕'

    return




def cf_sethttpschain(chainname, sslname, servername='server1'):

    funcname='设置HTTPS传输链SSL配置'



    #获取传输链信息

    transportchannel_list1=AdminConfig.list('TransportChannelService', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    transportchannel_list2=transportchannel_list1.split(getlinesep())



    chaininfo=''



    #遍历传输链信息

    for i in range(len(transportchannel_list2)):

        #获取全部传输链信息

        transportchannel_all=AdminConfig.show(transportchannel_list2[i])

        #判断待修改的传输链是否在当前的信息中

        if(transportchannel_all.find(chainname + '(') != -1):

            chaininfo=transportchannel_all.split(chainname)[1].split(']')[0]

            break





    #获得待修改HTTPS传输链信息

    chaininfo_list1=AdminConfig.show(chaininfo)

    chaininfo_list2=chaininfo_list1.split(getlinesep())



    sslinboundchannelid=''

    #查找对应的SSLInboundChannelID

    for i in range(len(chaininfo_list2)):

        if(chaininfo_list2[i].find('[transportChannels') == 0):

            chaininfo_list3=chaininfo_list2[i].split(' ')

            for i in range(len(chaininfo_list3)):

                if(chaininfo_list3[i].find('SSL_') == 0):

                    sslinboundchannelid=chaininfo_list3[i].split('|server.xml#')[1].split(')')[0]

                    break



    AdminConfig.modify('(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '/servers/' + servername + '|server.xml#' + sslinboundchannelid + ')', '[[sslConfigAlias "' + sslname + '"]]')

    AdminConfig.save()





    print funcname + '-完毕'

    return

#   获取主机名信息(前三个字节与最后一个字节)
import socket



def cf_gethostname_short():

    hostname=socket.gethostname()

    len_hostname=len(hostname)

    hn=hostname[0:3]+hostname[len_hostname-1:len_hostname]

    return hn

#2.2.18     修改访问was时返回的HTTP头中的Server字段为主机名信息
#参数 chainname Web容器传输链名字 示例 'csr_chain_ssl'

#参数 servername 默认'server1' 示例 'server1'



def cf_setservervalue(chainname, servername='server1'):

    funcname='修改访问was时返回的HTTP头中的Server字段为主机名信息'



    #获取传输链信息

    transportchannel_list1=AdminConfig.list('TransportChannelService', AdminConfig.getid( '/Cell:' + AdminControl.getCell() + '/'))

    transportchannel_list2=transportchannel_list1.split(getlinesep())



    chaininfo=''



    #遍历传输链信息

    for i in range(len(transportchannel_list2)):

        #获取全部传输链信息

        transportchannel_all=AdminConfig.show(transportchannel_list2[i])

        #判断待修改的传输链是否在当前的信息中

        if(transportchannel_all.find(chainname + '(') != -1):

            chaininfo=transportchannel_all.split(chainname)[1].split(']')[0]

            break





    #获得待修改HTTPS传输链信息

    chaininfo_list1=AdminConfig.show(chaininfo)

    chaininfo_list2=chaininfo_list1.split(getlinesep())



    httpinboundchannelid=''

    #查找对应的httpinboundchannelid

    for i in range(len(chaininfo_list2)):

        if(chaininfo_list2[i].find('[transportChannels') == 0):

            chaininfo_list3=chaininfo_list2[i].split(' ')

            for i in range(len(chaininfo_list3)):

                if(chaininfo_list3[i].find('HTTP_') == 0):

                    httpinboundchannelid=chaininfo_list3[i].split('|server.xml#')[1].split(')')[0]

                    break



    AdminConfig.create('Property', '(cells/' + AdminControl.getCell() + '/nodes/' + AdminControl.getNode() + '/servers/' + servername + '|server.xml#' + httpinboundchannelid + ')', '[[validationExpression ""] [name "ServerHeaderValue"] [description ""] [value "' + cf_gethostname_short() + '"] [required "false"]]')

    AdminConfig.save()





    print funcname + '-完毕'

    return
    
    
    

cf_uninstallapp('DefaultApplication')
cf_uninstallapp('ivtApp')
cf_uninstallapp('query')

cf_createjdbcprovider()

cf_createJ2Cdata('APP___PAS__DBUSER', 'APP___PAS__DBUSER', '#')
cf_createJ2Cdata('global1', 'global1', '#')
cf_createJ2Cdata('common', 'common', '#')
cf_createJ2Cdata('APP___CSS__DBUSER', 'APP___CSS__DBUSER', '#')

cf_createdatasource('PAJndiDataSource', 'jdbc/PAJndiDataSource', 'APP___PAS__DBUSER', 'jdbc:oracle:thin:@10.1.96.16:1521/')
cf_createdatasource('GLOBALJndiDataSource', 'jdbc/GLOBALJndiDataSource', 'GLOBALJndiDataSource', 'jdbc:oracle:thin:@10.1.96.16:1521/')
cf_createdatasource('UdmpCommonDataSource', 'jdbc/UdmpCommonDataSource', 'UdmpCommonDataSource', 'jdbc:oracle:thin:@10.1.96.16:1521/')
cf_createdatasource('CSSJndiDataSource', 'jdbc/CSSJndiDataSource', 'CSSJndiDataSource', 'jdbc:oracle:thin:@10.1.96.16:1521/')

cf_setjavaheapsize('51200', '51200')

cf_setwebcontainerthread('50', '350')

cf_setconnectionpool('PAJndiDataSource', '10', '200')
cf_setconnectionpool('GLOBALJndiDataSource', '10', '200')
cf_setconnectionpool('UdmpCommonDataSource', '10', '200')
cf_setconnectionpool('CSSJndiDataSource', '10', '200')

cf_setJVMlog('SystemOut.log', '100', '10')
cf_setJVMlog('SystemErr.log', '100', '10')






