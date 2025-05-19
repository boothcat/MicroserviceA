# Microservice A For Teammate
## CSV File Sorter
- **How to Progmatically Request Data**

A zeroMQ localhost is used to connect the programming requesting data to the localhost server. After a context and socket has been created, a json string containing the name of the column to sort the data by, the csv file path, and the sort order (asc for ascending or desc for descending) is sent to the server.  Please note: the name of the column must match the column name in the csv file and the path must use forward slashes.

![image](https://github.com/user-attachments/assets/dbc8e368-f053-4bd9-86bf-4abba19326f8)

- **How to Progmatically Recieve Data**

  Microservice A server returns a string containing the path to the sorted csv file.  The sorted csv file is created in the current working directory of the microservice program.

   ![image](https://github.com/user-attachments/assets/76e30f89-6b7f-4559-a271-ec2e039c8443)

- **UML Sequence Diagram**

  Notes are provided as orange squares.  

![image](https://github.com/user-attachments/assets/5004591e-5762-43b0-a79d-3a98766ed554)


