#! /bin/bash

set -e
set -x

export KVPIO_APIKEY=b5ec28cbb8294663a08261273d53931d

CONFIG_TEMPLATE=`cat <<EOF
# my special app config
user={{ my_user.name }}
sql-server={{ sql.ip }}
EOF`

kvpio bucket list
kvpio bucket get my_user
kvpio bucket set my_user '{"name": "Will", "email": "will@steelhive.com", "store": true}'
kvpio bucket get my_user
kvpio bucket list

kvpio service list
kvpio service get sql ip
kvpio service get sql host
kvpio service set sql ip 10.1.1.100
kvpio service set sql host sql-a.mydomain.com
kvpio service set sql port 1433
kvpio service get sql ip
kvpio service get sql host
kvpio service get sql ip --with-port
kvpio service get sql host --with-port
kvpio service del sql
kvpio service get sql ip
kvpio service get sql host
kvpio service set sql ip 10.1.1.200:1433
kvpio service set sql host sql-b.mydomain.com:1433
kvpio service get sql ip
kvpio service get sql host
kvpio service get sql ip --with-port
kvpio service get sql host --with-port
kvpio service list

kvpio template list
kvpio template get config
kvpio template set config "$CONFIG_TEMPLATE"
kvpio template get config --raw
kvpio template get config
kvpio template list

kvpio bucket del my_user
kvpio service del sql
kvpio template del config
