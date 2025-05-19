import json
import zmq

# zmq context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5985")

# Data to send to microservice
# sort_column = column name from csv file to sort by
# path = absolute path to csv file
# sort_order = "asc" for ascending order or "desc" for descending order
movie_vault = {
    "sort_column": "column_name",
    "path": "path/to/file.csv",
    "sort_order": "asc"
}

# convert data to json string to send to microservice server
movie_vault_json = json.dumps(movie_vault)
socket.send_json(movie_vault_json)

# Receive file path as string from microservice server
sorted_file_path = socket.recv_string()
