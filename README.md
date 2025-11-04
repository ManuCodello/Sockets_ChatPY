<h1>💬 ChatPY - Python Socket Chat</h1>

<p align="center">
  <strong>A simple, multi-client, GUI-based chat application built with Python sockets and Tkinter.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Technology-Sockets_&_Threading-green?style=for-the-badge" alt="Sockets & Threading">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge" alt="MIT License">
</p>

<h2>Project Overview</h2>

<p><strong>ChatPY</strong> is a classic client-server chat room application written entirely in Python. It uses the built-in <code>socket</code> module for networking, <code>threading</code> to handle multiple clients concurrently, and <code>tkinter</code> to provide a simple and functional graphical user interface (GUI) for the client.</p>

<hr>

<h2>Features</h2>

<ul>
  <li><strong>Real-Time Group Chat:</strong> Messages sent by any client are broadcast to all other connected clients instantly.</li>
  <li><strong>GUI Client:</strong> A user-friendly graphical interface built with <code>tkinter</code>, featuring a scrollable message display and a text input field.</li>
  <li><strong>Multi-Threaded Server:</strong> The server uses <code>threading</code> to manage each client connection separately, allowing it to handle multiple users simultaneously without blocking.</li>
  <li><strong>User Nicknames:</strong> Users are prompted for a nickname before joining the chat.</li>
  <li><strong>Join/Leave Notifications:</strong> The chat room is notified when a new user joins or an existing user disconnects.</li>
</ul>

<hr>

<h2>How It Works</h2>

<h3>1. Server (<code>server.py</code>)</h3>
<p>The server script is the central hub of the chat room.</p>
<ol>
  <li>It binds to a host (<code>127.0.0.1</code>) and port (<code>12345</code>).</li>
  <li>It listens for incoming TCP connections.</li>
  <li>When a new client connects, the server accepts the connection and receives the client's chosen nickname.</li>
  <li>It then starts a new <strong>thread</strong> dedicated exclusively to handling that client.</li>
  <li>This client-handling thread continuously listens for messages. When a message is received, the server's <code>broadcast()</code> function sends it to all other connected clients.</li>
  <li>If a client disconnects, their thread terminates, and a "left the chat" message is broadcast to the remaining users.</li>
</ol>

<h3>2. Client (<code>client.py</code>)</h3>
<p>The client script provides the user-facing GUI.</p>
<ol>
  <li>It launches a small <code>tkinter</code> window to ask the user for a nickname.</li>
  <li>After the nickname is submitted, it connects to the server and sends the nickname for registration.</li>
  <li>It then opens the main chat window.</li>
  <li>The client starts a new <strong>thread</strong> (<code>receive_thread</code>) whose only job is to listen for messages from the server and display them in the <code>ScrolledText</code> widget.</li>
  <li>The main GUI thread is responsible for sending messages. When the user types a message and hits "Send" (or presses Enter), the <code>write_message()</code> function sends the formatted text to the server.</li>
</ol>

<hr>

<h2>How to Run</h2>

<h3>Prerequisites</h3>
<ul>
  <li><strong>Python 3.x</strong></li>
  <li><strong>Tkinter:</strong> This is typically included with standard Python installations. If not, you may need to install it (e.g., <code>sudo apt-get install python3-tk</code> on Debian/Ubuntu).</li>
</ul>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/your-username/sockets_chatpy.git
cd sockets_chatpy
</code></pre>

<h3>2. Run the Server</h3>
<p>Open a terminal and run the server script. It will wait for clients to connect.</p>

<pre><code>python server.py
</code></pre>
<blockquote>
  <p>Server is running on 127.0.0.1:12345...</p>
</blockquote>

<h3>3. Run the Client</h3>
<p>Open one or more new terminal windows and run the client script. Each instance will act as a new user.</p>

<pre><code>python client.py
</code></pre>

<p>A small window will pop up asking for your nickname. Once you enter it, the main chat window will appear, and you can start chatting!</p>

<hr>

<h2>File Structure</h2>
<pre><code>sockets_chatpy/
├── server.py       # The multi-threaded chat server
├── client.py       # The Tkinter-based GUI client
└── .gitignore      # Ignores Python cache files
</code></pre>
