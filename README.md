# Kafka-ACL-Authentication

1.Start the docker environment compose file

<code>docker-compose up
</code>


2.Changing Directory 

<code> cd /opt/security</code>

3.Create topic using user admin properties

<code> kafka-topics --bootstrap-server localhost:9092 --create --topic msg --command-config /opt/security/client-properties/adminclient.properties --partitions 1 --replication-factor 1</code>

![Screenshot from 2023-12-31 17-48-19](https://github.com/rokesh-rokesh/Kafka-ACL-Authentication-security/assets/84179582/ffab879d-95a5-44c7-a6f5-48b08e410276)


4.Grant permission to produce msg to User producer to msg topic

<code> kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:producer --producer --add</code>

![Screenshot from 2023-12-31 17-48-48](https://github.com/rokesh-rokesh/Kafka-ACL-Authentication-security/assets/84179582/cf4df9a4-f0db-46b9-b9c6-17a6ae0cee73)


5.Grant permission to consume msg to User Consumer from msg topic

<code>kafka-acls --bootstrap-server localhost:9092 --command-config /opt/security/client-properties/adminclient.properties --topic msg --allow-principal User:consumer --consumer --add --group "test-consumer-group-1"</code>

![Screenshot from 2023-12-31 17-49-47](https://github.com/rokesh-rokesh/Kafka-ACL-Authentication-security/assets/84179582/a8bfbdcd-b9c6-4e85-a8e2-4482d1b83622)

6.Executing Sample producer.py program
![Screenshot from 2023-12-31 17-50-55](https://github.com/rokesh-rokesh/Kafka-ACL-Authentication-security/assets/84179582/86df4be1-d441-45ae-b87f-f20ba9c71037)

7.Executing Sample Consumer.py program
![Screenshot from 2023-12-31 17-52-23](https://github.com/rokesh-rokesh/Kafka-ACL-Authentication-security/assets/84179582/37a2447d-3abe-428e-8815-a66e79b9fc51)




