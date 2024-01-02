1.Changing Directory 
cd /opt/security

2.Create topic using user admin properties
kafka-topics --bootstrap-server localhost:9092 --create --topic msg --command-config /opt/security/client-properties/adminclient.properties --partitions 1 --replication-factor 1

3.Grant permission to produce msg to User producer to msg topic
kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:producer --producer --add

4.Grant permission to consume msg to User Consumer from msg topic
kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:consumer --consumer --add --group "test-consumer-group-1"
