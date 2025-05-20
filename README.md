# Microservice A For Teammate - CSV File Sorter
## **How to Programmatically Request Data**

A zeroMQ localhost is used to connect the programming requesting data to the localhost server. After a context and socket has been created, a json string containing the name of the column to sort the data by, the csv file path, and the sort order (asc for ascending or desc for descending) is sent to the server.  Please note: the name of the column must match the column name in the csv file and the path must use forward slashes.  The default sort order is set to ascending if a sort order is not provided.

![image](https://github.com/user-attachments/assets/1e8854b6-5985-445a-9e95-222fa1202646)


## **How to Programmatically Recieve Data**

  Microservice A server returns a string containing the path to the sorted csv file.  The sorted csv file is created in the current working directory of the microservice program. The original csv file is unchanged by the microservice.

   ![image](https://github.com/user-attachments/assets/76e30f89-6b7f-4559-a271-ec2e039c8443)

## **UML Sequence Diagram**

  The orange boxes in the UML Sequence Diagram below represent notes.

![image](https://github.com/user-attachments/assets/0400b0a7-4ada-49e7-8d6d-4b09d4ea2d99)



