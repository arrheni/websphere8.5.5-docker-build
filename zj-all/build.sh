


cat > bak << EOF
10.1.94.14  8880 server1 was admi     ap2-pa1.car     SITap2pa      SITap2paNode01Cell
10.1.94.14  8881 server1 was admi     ap2-pa2.car     SITap2pa      SITap2paNode02Cell
10.1.115.3  8880 server1 was admi     ap2-nb1.car     SITap2nb      SITap2nbNode01Cell
10.1.115.3  8881 server1 was admi     ap2-nb2.car     SITap2nb      SITap2nbNode02Cell
10.1.115.4  8880 server1 was admi     ap2-qry1.car    SITap2qry     SITap2qryNode01Cell
10.1.115.4  8881 server1 was admi     ap2-qry2.car    SITap2qry     SITap2qryNode02Cell
10.1.160.5  8880 server1 was M\!H\-g  ap2-jqrd.car    CloudKVM01    CloudKVM01Node01Cell
10.1.90.131 8880 server1 was admi     zj-cip.car      SITapcip      SITapcipNode01Cell
10.1.90.130 8880 server1 was admi     zj-batch.car    SITapbatch    SITapbatchNode01Cell
10.1.94.22  8880 server1 was admi     ap1-pa1.car     SITap1pa      SITap1paNode01Cell
10.1.94.22  8881 server1 was admi     ap1-pa2.car     SITap1pa      SITap1paNode02Cell
10.1.115.6  8880 server1 was admi     ap1-nb1.car     SITap1nb      SITap1nbNode01Cell
10.1.115.6  8881 server1 was admi     ap1-nb2.car     SITap1nb      SITap1nbNode02Cell
10.1.115.9  8880 server1 was admi     ap1-qry1.car    SITap1qry     SITap1qryNode01Cell
10.1.115.9  8881 server1 was admi     ap1-qry2.car    SITap1qry     SITap1qryNode02Cell
10.1.98.1   8880 server1 was admi     ap1-jqrd.car    CloudKVM02    CloudKVM02Node01Cell
EOF


cat > zj << EOF
10.1.90.130 8880 server1 was admi     zj-batch.car    SITapbatch    SITapbatchNode01Cell
10.1.90.131 8880 server1 was admi     zj-cip.car      SITapcip      SITapcipNode01Cell
10.1.94.14  8880 server1 was admi     ap2-pa1.car     SITap2pa      SITap2paNode01Cell
10.1.94.14  8881 server1 was admi     ap2-pa2.car     SITap2pa      SITap2paNode02Cell
10.1.115.3  8880 server1 was admi     ap2-nb1.car     SITap2nb      SITap2nbNode01Cell
10.1.115.3  8881 server1 was admi     ap2-nb2.car     SITap2nb      SITap2nbNode02Cell
10.1.115.4  8880 server1 was admi     ap2-qry1.car    SITap2qry     SITap2qryNode01Cell
10.1.115.4  8881 server1 was admi     ap2-qry2.car    SITap2qry     SITap2qryNode02Cell
10.1.94.22  8880 server1 was admi     ap1-pa1.car     SITap1pa      SITap1paNode01Cell
10.1.94.22  8881 server1 was admi     ap1-pa2.car     SITap1pa      SITap1paNode02Cell
10.1.115.6  8880 server1 was admi     ap1-nb1.car     SITap1nb      SITap1nbNode01Cell
10.1.115.6  8881 server1 was admi     ap1-nb2.car     SITap1nb      SITap1nbNode02Cell
10.1.115.9  8880 server1 was admi     ap1-qry1.car    SITap1qry     SITap1qryNode01Cell
10.1.115.9  8881 server1 was admi     ap1-qry2.car    SITap1qry     SITap1qryNode02Cell
EOF

# 目标镜像版本号
VERSION=`date +%F_%H`

cat zj | while read line ; do 

	a=(${line})

	# 目标镜像
    TARGET_IMAGE=localhost:8080/webshphere_nd_8.5.0.1/${a[5]}:${VERSION}
    # 构建目标镜像
    time docker build --build-arg CAR=${a[5]} --build-arg  CELL=${a[7]}  -t ${TARGET_IMAGE} .
	
done

