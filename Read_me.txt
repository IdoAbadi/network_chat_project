hello user!

PART 1:

the answers and all explanations are inside the jupyter notebook
in addition there are screenshots of the packet exchange in wireshark
and the csv file we used

PART 2:

Initial Configuration (Mandatory)
Before running the application, you must update the IP addresses so clients can locate the server:

Identify Server IP: On the server machine, run ipconfig in the terminal and find the IPv4 Address (e.g., 192.168.31.229).

Update Standard Client (client.py): Go to line 17 and update the SERVER_IP variable with the identified server IP.

Update GUI Client (client_gui.py): Go to line 62 and update the IP parameter in the ChatClient initialization.

Server Configuration (server.py): Ensure that on line 4, the IP variable is set to '0.0.0.0' to allow external connections.

Execution Instructions
Step 1: Start the Server
On the host machine, run server.py in VS Code. The terminal will display: server is running and listeninng on port 5555.

Step 2: Start the Clients
You can choose either client type (or mix both):

A. Standard Terminal Client
Run client.py.

Enter your username when prompted in the terminal.

To send a message, use the format: Recipient:Message (e.g., Ronnie:Hello).

B. Graphical User Interface (GUI) Client
Run client_gui.py.

In the popup window, enter your username and click OK.

Type your message in the format: Recipient:Message (e.g., Ronnie:Hello) inside the input field and click Send or press Enter.