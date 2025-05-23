import json
import zmq


def sort_csv(sort_column, path, sort_order="asc"):
    """ Set up data to send to microservice server:
    sort_column: string name of column to sort by ("Title"/"Format"/"Year"),
    path: string path to the csv file, must use forward slashes /,
    sort_order: "asc" or "desc", sorts in ascending or descending order.
                Defaults to asc.
    returns: string path to sorted csv file
    """

    # zmq context and socket setup
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5985")

    movie_vault = {
        "sort_column": sort_column,
        "path": path,
        "sort_order": sort_order
    }

    # convert to json format to send to microservice server
    movie_vault_json = json.dumps(movie_vault)
    socket.send_json(movie_vault_json)

    # Get sorted file path back from microservice server
    return socket.recv_string()


# Example UI that makes call to Microservice A
file_path = input("Enter csv file path (use forward /): ")
sort_column = input("Enter column name to sort csv file by: ")
sort_order = input("Enter a for ascending order or d for descending order: ")

if sort_order.lower() == "d":
    sort_order = "desc"
else:
    sort_order = "asc"

print("Let's get this sorted! Calling Microservice A...\n")
sorted_file_path = sort_csv(sort_column, file_path, sort_order)
print(f"The sorted csv file is located at : {sorted_file_path}\n")
