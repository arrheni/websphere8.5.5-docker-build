#####################################################################################
#                                                                                   #
#  Script to create                                                                 #
#                                                                                   #
#  Usage : wsadmin -lang jython -f create.py                                        # 
#                                                                                   #
#####################################################################################
import sys


def create():
        
        	
        AdminApp.list()
        AdminApp.uninstall('DefaultApplication')
        AdminApp.uninstall('ivtApp')
        AdminApp.uninstall('query')
        AdminApp.list()
        
        AdminConfig.create('VariableSubstitutionEntry', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|variables.xml#VariableMap_1)', '[[symbolicName "ORACLE_JDBC_DRIVER_PATH"] [description ""] [value "/home/ap/was/AppServer/profiles/AppSrv01/extJDBCDriver/oracle"]]')
        
        AdminTask.createAuthDataEntry('[-alias APP___PAS__DBUSER -user APP___PAS__DBUSER -password # -description ]')
        AdminTask.createAuthDataEntry('[-alias global1 -user global1 -password # -description ]')
        AdminTask.createAuthDataEntry('[-alias common -user common -password # -description ]')
        AdminTask.createAuthDataEntry('[-alias APP___CSS__DBUSER -user APP___CSS__DBUSER -password #  -description ]')
       
 
        p1=AdminTask.createJDBCProvider('[-scope Node=DefaultNode01,Server=server1 -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')
#        print p1
        d1=AdminTask.createDatasource( p1 , '[-name PAJndiDataSource -jndiName jdbc/PAJndiDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/APP___PAS__DBUSER -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@10.1.96.16:1521/pasdb]]]')
#        print d1
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#DataSource_1630391002984)', '[[authDataAlias DefaultNode01/APP___PAS__DBUSER] [mappingConfigAlias ""]]')
       # AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630391002995)', '[[name "PAJndiDataSource_CF"] [authDataAlias "DefaultNode01/APP___PAS__DBUSER"] [xaRecoveryAuthAlias ""]]')
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630391002995)', '[[authDataAlias DefaultNode01/APP___PAS__DBUSER] [mappingConfigAlias ""]]')
        # Note that scripting list commands may generate more information than is displayed by the administrative console because the console generally filters with respect to scope, templates, and built-in entries.
        
       # AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#ConnectionPool_1630391002987)', '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        
        
        
        p2= AdminTask.createJDBCProvider('[-scope Node=DefaultNode01,Server=server1 -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')
        d2=AdminTask.createDatasource( p2 , '[-name GLOBALJndiDataSource -jndiName jdbc/GLOBALJndiDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/global1 -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@10.1.96.16:1521/pasdb]]]')
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#DataSource_1630392062677)', '[[authDataAlias DefaultNode01/global1] [mappingConfigAlias ""]]')
       # AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630392062689)', '[[name "GLOBALJndiDataSource_CF"] [authDataAlias "DefaultNode01/global1"] [xaRecoveryAuthAlias ""]]')
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630392062689)', '[[authDataAlias DefaultNode01/global1] [mappingConfigAlias ""]]')
        # Note that scripting list commands may generate more information than is displayed by the administrative console because the console generally filters with respect to scope, templates, and built-in entries.
        
       # AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#ConnectionPool_1630392062680)', '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        
        
        p3=AdminTask.createJDBCProvider('[-scope Node=DefaultNode01,Server=server1 -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')
        d3=AdminTask.createDatasource( p3 , '[-name UdmpCommonDataSource -jndiName jdbc/UdmpCommonDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/common -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@10.1.96.16:1521/pasdb]]]')
        #AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#DataSource_1630392167754)', '[[authDataAlias DefaultNode01/common] [mappingConfigAlias ""]]')
        #AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630392167765)', '[[name "UdmpCommonDataSource_CF"] [authDataAlias "DefaultNode01/common"] [xaRecoveryAuthAlias ""]]')
        #AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630392167765)', '[[authDataAlias DefaultNode01/common] [mappingConfigAlias ""]]')
        # Note that scripting list commands may generate more information than is displayed by the administrative console because the console generally filters with respect to scope, templates, and built-in entries.
        #ds=AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')).split()
        #print ds
        p4=AdminTask.createJDBCProvider('[-scope Node=DefaultNode01,Server=server1 -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "Connection pool data source" -name "Oracle JDBC Driver" -description "Oracle JDBC Driver" -classpath [${ORACLE_JDBC_DRIVER_PATH}/ojdbc6.jar ] -nativePath "" ]')
        d4=AdminTask.createDatasource( p4 , '[-name CSSJndiDataSource -jndiName jdbc/CSSJndiDataSource -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias DefaultNode01/APP___CSS__DBUSER -configureResourceProperties [[URL java.lang.String jdbc:oracle:thin:@10.1.96.16:1521/pasdb]]]')
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#DataSource_1630459639087)', '[[authDataAlias DefaultNode01/APP___CSS__DBUSER] [mappingConfigAlias ""]]')
       # AdminConfig.modify('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630459639109)', '[[name "CSSJndiDataSource_CF"] [authDataAlias "DefaultNode01/APP___CSS__DBUSER"] [xaRecoveryAuthAlias ""]]')
       # AdminConfig.create('MappingModule', '(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#CMPConnectorFactory_1630459639109)', '[[authDataAlias DefaultNode01/APP___CSS__DBUSER] [mappingConfigAlias ""]]')
       # Note that scripting list commands may generate more information than is displayed by the administrative console because the console generally filters with respect to scope, templates, and built-in entries.
        ds=AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')).split()
        print ds

        AdminTask.deleteDatasource('(cells/DefaultCell01/nodes/DefaultNode01/servers/server1|resources.xml#DataSource_1183122153625)')
        #AdminTask.deleteDatasource(ds[1])


        cp=AdminConfig.list('ConnectionPool', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')).split()
        
        AdminConfig.modify(cp[0], '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        AdminConfig.modify(cp[1], '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        AdminConfig.modify(cp[2], '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        AdminConfig.modify(cp[3], '[[connectionTimeout "180"] [maxConnections "200"] [unusedTimeout "1800"] [minConnections "10"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]')
        
        #w=AdminConfig.list('WebContainer', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')) 
        pools=AdminConfig.list('ThreadPool', AdminConfig.getid( '/Cell:DefaultCell01/Node:DefaultNode01/Server:server1/')).split()
        #print pools
        AdminConfig.modify( pools[10] , '[[maximumSize "350"] [name "WebContainer"] [minimumSize "50"] [inactivityTimeout "60000"] [description ""] [isGrowable "false"]]')


        jvm=AdminConfig.list("JavaVirtualMachine")

        AdminConfig.modify(jvm, '[[initialHeapSize 51200]]')
        AdminConfig.modify(jvm, '[[maximumHeapSize 51200]]')
        AdminConfig.modify(jvm,[['genericJvmArguments',"-Dcom.ibm.websphere.webservices.DisableIBMJAXWSEngine=true -Xdisableexplicitgc -Dfile.encoding=UTF-8  -Ddefault.client.encoding=UTF-8  -Dclient.encoding.override=UTF-8  -Duser.language=zh  -Duser.region=CN  -Duser.country=CN"]])

        
      	AdminConfig.save()

def installApp (war_path, appName, croot):
	# declare global variable
#	global AdminApp
	# install ear file
	#server_attr = [-appname  appName -contextroot croot]
	#AdminApp.install(war_path, server_attr)
        #AdminApp.install('/demo/pbw-ear8.ear', '[ -appname PlantsByWebSphere8 -contextroot /PlantsByWebSphere8]')

     
        AdminApp.install(war_path, '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname local-webapp -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig  -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -novalidateSchema -contextroot /ls -MapResRefToEJB [[ local-webapp-0.5.5.5.war "" local-webapp-0.5.5.5.war,WEB-INF/web.xml jdbc/UdmpJndiDataSource javax.sql.DataSource jdbc/GLOBALJndiDataSource "" "" "" ][ local-webapp-0.5.5.5.war "" local-webapp-0.5.5.5.war,WEB-INF/web.xml jdbc/UdmpCommonDataSource javax.sql.DataSource jdbc/UdmpCommonDataSource "" "" "" ][ local-webapp-0.5.5.5.war "" local-webapp-0.5.5.5.war,WEB-INF/web.xml jdbc/UdmpDataSource javax.sql.DataSource jdbc/PAJndiDataSource "" "" "" ][ local-webapp-0.5.5.5.war "" local-webapp-0.5.5.5.war,WEB-INF/web.xml jdbc/NBSJndiDataSource javax.sql.DataSource jdbc/NBSJndiDataSource "" "" "" ][ local-webapp-0.5.5.5.war "" local-webapp-0.5.5.5.war,WEB-INF/web.xml jdbc/BankDataSource javax.sql.DataSource jdbc/BankDataSource "" "" "" ]] -MapModulesToServers [[ local-webapp-0.5.5.5.war local-webapp-0.5.5.5.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]] -MapWebModToVH [[ local-webapp-0.5.5.5.war local-webapp-0.5.5.5.war,WEB-INF/web.xml default_host ]] -CtxRootForWebMod [[ local-webapp-0.5.5.5.war local-webapp-0.5.5.5.war,WEB-INF/web.xml /ls ]]]' )
        #AdminApp.install(war_path/appwar, '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname appName -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -contextroot /ls -MapResRefToEJB [[ appwar "" appwar,WEB-INF/web.xml jdbc/UdmpJndiDataSource javax.sql.DataSource jdbc/GLOBALJndiDataSource "" "" "" ][ appwar "" appwar,WEB-INF/web.xml jdbc/UdmpCommonDataSource javax.sql.DataSource jdbc/UdmpCommonDataSource "" "" "" ][ appwar "" appwar,WEB-INF/web.xml jdbc/UdmpDataSource javax.sql.DataSource jdbc/PAJndiDataSource "" "" "" ]] -MapModulesToServers [ appwar appwar,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ] -MapWebModToVH [ appwar appwar,WEB-INF/web.xml default_host ] -CtxRootForWebMod [ appwar appwar,WEB-INF/web.xml /ls ]]' )
      	AdminConfig.save()
#endDef


def updateEar(appName, earFile):
	# declare global variable
	global AdminApp
	# update the existing application
	AdminApp.update(appName, "app", "-operation update -contents "+earFile )
#end update()

def changeModuleClassloaderMode(appName, moduleName, classloaderMode):
    # declare global variable
    global AdminConfig
    if len(classloaderMode) > 0:
        appid = AdminConfig.getid("/Deployment:"+appName+"/" )
        deployedApp = AdminConfig.showAttribute(appid, "deployedObject")
        modules = AdminConfig.showAttribute(deployedApp, "modules")
        moduleList = modules[1:len(modules)-1].split(" ")
        for module in moduleList:
            uri = AdminConfig.showAttribute(module, "uri")
            if cmp(moduleName, uri) == 0:
                cmode = AdminConfig.showAttribute(module, "classloaderMode")
                if(cmp(cmode, classloaderMode) != 0):
                    print "Modifying classloader for module: " + uri
                    AdminConfig.modify(module, [["classloaderMode", classloaderMode]])
                #end if
            #end if
        #end for
      	AdminConfig.save()
    #end if
#end def        

def changeClassLoader(appName, classloaderMode, classloaderPolicy):
	# declare global variable
    # changeClassLoader('local_webapp', 'PARENT_LAST', 'Application')
    #global AdminConfig
	appid = AdminConfig.getid("/Deployment:"+appName+"/" )
	deployedApp = AdminConfig.showAttribute(appid, "deployedObject")
        print deployedApp
	# update classloader policy
	if(len(classloaderPolicy) > 0):
		policy = AdminConfig.showAttribute(deployedApp, "warClassLoaderPolicy")
		if(cmp(classloaderPolicy.strip(), "Module") == 0):
			policy = "MULTIPLE"
		elif(cmp(classloaderPolicy.strip(), "Application") == 0):
			policy = "SINGLE"
		#end if
		AdminConfig.modify(deployedApp, [["warClassLoaderPolicy", policy]])
	#end if
	# update classloader mode
	if(len(classloaderMode) > 0):
		classLoader = AdminConfig.showAttribute(deployedApp, "classloader")
		modeAttr = ["mode", classloaderMode]
		AdminConfig.modify(classLoader, [modeAttr])
	#end if
#end changeClassLoader()


create()	


installApp('/tmp/local-webapp-0.5.5.5.war', 'local-webapp', 'local-webapp-0.5.5.5.war')
changeClassLoader('local-webapp', 'PARENT_LAST', 'Application')
