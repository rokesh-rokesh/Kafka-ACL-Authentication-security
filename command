1.cd /opt/security

2.kafka-topics --bootstrap-server localhost:9092 --create --topic msg --command-config /opt/security/client-properties/adminclient.properties --partitions 1 --replication-factor 1

3.kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:producer --producer --add

4.kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:consumer --consumer --add --group "test-consumer-group-1"

5.
