import zmq
import json
import os
import pandas as pd


# setup context and socket to listen for client
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5985")

print("Microservice A server is listening for client requests...")

# Get data from client
while True:
    data_json = socket.recv_json()

    # Convert back to python dictionary for processing
    movie_data = json.loads(data_json)

    print(f"Microservice A received the following data from the client:\n{movie_data}\n")

    try:
        sort_column = movie_data["sort_column"]

        # Make sure forward slashes are used in file path
        file_path = movie_data["path"].replace("\\", "/")

        # Default sort order is ascending
        if (movie_data["sort_order"].lower() == "desc" or movie_data["sort_order"].lower() == "descending"):
            sort_order = False
        else:
            sort_order = True

        # Read csv file into dataframe for sorting
        movie_dataframe = pd.read_csv(file_path)
        movie_dataframe_sorted = movie_dataframe.sort_values(by=sort_column, ascending=sort_order)

        # Write sorted movie_vault to new csv file in current working directory
        sorted_file_path = os.getcwd().replace("\\", "/") + "/movie_vault_sorted.csv"
        movie_dataframe_sorted.to_csv(sorted_file_path, index=False)

        print(f"Microservice A server is sending sorted csv file path back to the client:\n{sorted_file_path}\n")
        # Send sorted file path back to client
        socket.send_string(sorted_file_path)

    # Error Handling
    except FileNotFoundError as e:
        print(f"Error: Could not open csv file: {e}")
        socket.send_string("Could not open csv file")
    except PermissionError as e:
        print(f"Error: Unable to open file due to denied permission: {e}")
        socket.send_string("Could not open csv file due to denied permission")
    except KeyError as e:
        print(f"Error Column not found in csv file: {e}")
        socket.send_string("Error: Column not found in csv file")
