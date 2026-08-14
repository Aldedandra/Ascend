"""Module 3, Lesson 3-4: TCP, UDP & Ports."""

LESSON = {'id': '3-4',
 'title': 'TCP, UDP & Ports',
 'summary': 'Understand transport-layer communication: TCP connections, the three-way handshake, UDP '
            'datagrams, source and destination ports, listening sockets, ephemeral ports, and the evidence '
            'behind timeout versus connection refused.',
 'duration_minutes': 70,
 'xp': 75,
 'audio_script': 'Welcome to Lesson 3.4: TCP, UDP, and Ports.\n'
                 '\n'
                 'You already know that an IP address identifies a network endpoint. But applications need a '
                 'way to share that address.\n'
                 '\n'
                 'That is where transport protocols and ports come in.\n'
                 '\n'
                 'The two transport protocols you will encounter constantly are TCP and UDP.\n'
                 '\n'
                 'TCP stands for Transmission Control Protocol.\n'
                 '\n'
                 'TCP is connection-oriented. Before application data is exchanged, the two endpoints '
                 'establish a connection.\n'
                 '\n'
                 'The familiar model is the three-way handshake.\n'
                 '\n'
                 'The client sends SYN.\n'
                 '\n'
                 'The server replies with SYN-ACK.\n'
                 '\n'
                 'The client replies with ACK.\n'
                 '\n'
                 'At that point, the connection is established and application data can flow.\n'
                 '\n'
                 'The exact packet mechanics become deeper than we need today, but the troubleshooting value '
                 'is immediate.\n'
                 '\n'
                 'If the client never receives a response to the initial SYN, you may see a timeout.\n'
                 '\n'
                 'If the destination host responds that nothing is listening on the requested TCP port, the '
                 'client may receive connection refused.\n'
                 '\n'
                 'Those two outcomes point to different next questions.\n'
                 '\n'
                 'Timeout often means the connection attempt is being silently dropped, misrouted, filtered, '
                 'or never reaching a responsive endpoint.\n'
                 '\n'
                 'Connection refused usually means the destination is reachable enough to reject the '
                 'request, but no process is listening on that port, or a firewall is actively rejecting '
                 'it.\n'
                 '\n'
                 'Neither message alone proves the complete root cause, but each narrows the search.\n'
                 '\n'
                 'TCP also provides ordered delivery, retransmission, flow control, and congestion-control '
                 'behavior.\n'
                 '\n'
                 'Applications such as HTTPS, SSH, PostgreSQL, and many APIs commonly use TCP because they '
                 'need a reliable byte stream.\n'
                 '\n'
                 'UDP is different.\n'
                 '\n'
                 'UDP is connectionless at the transport layer.\n'
                 '\n'
                 'Applications send datagrams without performing a TCP-style connection handshake.\n'
                 '\n'
                 'UDP does not provide the same built-in guarantees for ordered delivery or retransmission.\n'
                 '\n'
                 'That makes it lightweight and useful for protocols where speed, simplicity, multicast, or '
                 'application-controlled reliability matter.\n'
                 '\n'
                 'DNS commonly uses UDP for many ordinary queries, although TCP is also used when needed.\n'
                 '\n'
                 'Other examples include streaming, telemetry, gaming, DHCP, and time synchronization, '
                 'depending on the protocol.\n'
                 '\n'
                 'Now ports.\n'
                 '\n'
                 'A port is a 16-bit transport-layer number.\n'
                 '\n'
                 'Ports range from zero through sixty-five thousand five hundred thirty-five.\n'
                 '\n'
                 'Well-known service ports occupy the lower ranges by convention.\n'
                 '\n'
                 'SSH commonly uses TCP 22.\n'
                 '\n'
                 'HTTP commonly uses TCP 80.\n'
                 '\n'
                 'HTTPS commonly uses TCP 443.\n'
                 '\n'
                 'DNS commonly uses UDP and TCP 53.\n'
                 '\n'
                 'PostgreSQL commonly uses TCP 5432.\n'
                 '\n'
                 'But remember: a port number is a convention, not a law.\n'
                 '\n'
                 'An application can listen on a different port if configured to do so.\n'
                 '\n'
                 'This matters constantly in development. A Vite frontend may run on 3000. A FastAPI backend '
                 'may run on 8000. Docker can publish one host port to a different container port.\n'
                 '\n'
                 'Now distinguish destination ports from source ports.\n'
                 '\n'
                 'When your browser connects to HTTPS on port 443, the destination port is 443.\n'
                 '\n'
                 'Your client also uses a temporary source port, usually selected from an ephemeral range.\n'
                 '\n'
                 'That source port helps the operating system distinguish simultaneous connections.\n'
                 '\n'
                 'A TCP connection is commonly identified by a tuple including source address, source port, '
                 'destination address, destination port, and protocol.\n'
                 '\n'
                 'This explains how your machine can open many connections to the same web server at the '
                 'same time.\n'
                 '\n'
                 'Now listening sockets.\n'
                 '\n'
                 'A server process creates a socket and binds it to an address and port.\n'
                 '\n'
                 'It then listens for incoming TCP connections.\n'
                 '\n'
                 'The bind address matters.\n'
                 '\n'
                 'A server listening on 127.0.0.1 colon 8000 accepts only local loopback connections.\n'
                 '\n'
                 'A server listening on 0.0.0.0 colon 8000 can normally accept connections arriving on any '
                 'IPv4 interface, subject to routing and firewall policy.\n'
                 '\n'
                 'A server listening on one specific interface address accepts traffic targeted to that '
                 'address.\n'
                 '\n'
                 'This is why, quote, the process is running, end quote, does not prove remote '
                 'reachability.\n'
                 '\n'
                 'The process may be bound to the wrong address.\n'
                 '\n'
                 'Now tools.\n'
                 '\n'
                 'On Linux, ss is an excellent socket inspection tool.\n'
                 '\n'
                 'ss dash lnt shows listening TCP sockets numerically.\n'
                 '\n'
                 'ss dash lun shows listening UDP sockets.\n'
                 '\n'
                 'ss dash ant can show TCP sockets including established connections.\n'
                 '\n'
                 'On macOS, lsof dash iTCP dash sTCP colon LISTEN can show TCP listeners.\n'
                 '\n'
                 'lsof dash i can show broader network socket information.\n'
                 '\n'
                 'netstat may also exist, although modern Linux commonly favors ss.\n'
                 '\n'
                 'The important thing is not memorizing every option.\n'
                 '\n'
                 'Ask the question.\n'
                 '\n'
                 'What address and port is listening?\n'
                 '\n'
                 'Which process owns the listener?\n'
                 '\n'
                 'Is the connection established?\n'
                 '\n'
                 'Which local and remote ports are involved?\n'
                 '\n'
                 'Now netcat, commonly invoked as nc.\n'
                 '\n'
                 'Netcat can test whether a TCP connection can be established to a host and port.\n'
                 '\n'
                 'For example, nc dash vz host 443 is often used as a quick TCP connectivity test.\n'
                 '\n'
                 'It does not prove that HTTPS itself works.\n'
                 '\n'
                 'It proves something narrower: a TCP connection to that destination and port could be '
                 'established.\n'
                 '\n'
                 'That distinction matters.\n'
                 '\n'
                 'curl tests at the application layer.\n'
                 '\n'
                 'nc tests transport connectivity.\n'
                 '\n'
                 'dig tests DNS.\n'
                 '\n'
                 'Each tool gives evidence at a different layer.\n'
                 '\n'
                 'Now imagine Ascend.\n'
                 '\n'
                 'The frontend loads, but API calls fail.\n'
                 '\n'
                 'DNS is correct.\n'
                 '\n'
                 'The route is correct.\n'
                 '\n'
                 'You run nc against the API host on port 8000 and get connection refused.\n'
                 '\n'
                 'That points you toward the server side.\n'
                 '\n'
                 'Is the backend process running?\n'
                 '\n'
                 'Is it listening on 8000?\n'
                 '\n'
                 'Is it bound only to localhost?\n'
                 '\n'
                 'Did the service start on a different port?\n'
                 '\n'
                 'If instead the connection times out, you investigate routing, firewall policy, security '
                 'groups, host reachability, and whether traffic reaches the destination at all.\n'
                 '\n'
                 'Now consider Docker.\n'
                 '\n'
                 'A container may listen on port 8000 internally.\n'
                 '\n'
                 'Docker may publish host port 8080 to container port 8000.\n'
                 '\n'
                 'From outside the container, the client connects to host port 8080.\n'
                 '\n'
                 'Inside the container, the application still listens on 8000.\n'
                 '\n'
                 'Port mapping introduces another translation boundary.\n'
                 '\n'
                 'You will explore this more deeply in Module 4.\n'
                 '\n'
                 'Now graceful connection closure.\n'
                 '\n'
                 'TCP connections can be closed through a coordinated exchange.\n'
                 '\n'
                 'You may also encounter states such as LISTEN, ESTABLISHED, TIME-WAIT, and CLOSE-WAIT.\n'
                 '\n'
                 'You do not need to memorize every state today.\n'
                 '\n'
                 'Recognize LISTEN as a server waiting for connections and ESTABLISHED as an active '
                 'connection.\n'
                 '\n'
                 'TIME-WAIT is commonly normal after connection closure.\n'
                 '\n'
                 'CLOSE-WAIT can become interesting when applications fail to close sockets properly.\n'
                 '\n'
                 'Again, state is evidence, not a verdict.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'TCP is connection-oriented and reliable.\n'
                 '\n'
                 'UDP is datagram-oriented and does not provide the same built-in delivery guarantees.\n'
                 '\n'
                 'Ports identify transport-layer endpoints.\n'
                 '\n'
                 'Clients normally use ephemeral source ports.\n'
                 '\n'
                 'Servers bind and listen on destination ports.\n'
                 '\n'
                 'Bind addresses control where a service accepts traffic.\n'
                 '\n'
                 'Connection refused and timeout are different evidence.\n'
                 '\n'
                 'And tools such as ss, lsof, nc, and curl answer different transport and application '
                 'questions.\n'
                 '\n'
                 'In the next lesson, we will move up one layer into HTTP, HTTPS, and TLS.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Before we finish, connect transport troubleshooting back to the evidence ladder.\n'
                 '\n'
                 'An I P address gets you toward a network endpoint. A T C P or U D P port identifies the '
                 'service endpoint you intend to use. With T C P, a successful connection tells you '
                 'something specific: the destination was reachable far enough for the transport handshake '
                 'to complete. It does not tell you that the application is healthy.\n'
                 '\n'
                 'If the connection is refused, ask whether the process is listening on the expected address '
                 'and port. If it times out, widen the investigation to routing, filtering, reachability, '
                 'and silent drops. If T C P succeeds but the application still fails, move upward instead '
                 'of repeating the same port test.\n'
                 '\n'
                 'That is the habit to keep: use each result to decide which layer deserves the next '
                 'question.',
 'objectives': ['Explain the difference between TCP and UDP.',
                'Describe the TCP three-way handshake at a practical troubleshooting level.',
                'Explain source ports, destination ports, ephemeral ports, and listening sockets.',
                'Interpret timeout and connection refused as different transport evidence.',
                'Use ss, lsof, nc, and curl for layer-specific investigation.'],
 'content': [{'heading': 'TCP establishes a connection before application data',
              'body': 'The SYN → SYN-ACK → ACK handshake creates a connection-oriented session before normal '
                      'TCP application traffic flows.'},
             {'heading': 'UDP sends datagrams without a TCP-style handshake',
              'body': 'UDP is useful where lightweight transport or application-controlled behavior matters, '
                      'but it does not provide TCP’s built-in ordered reliable byte stream.'},
             {'heading': 'Ports identify transport endpoints',
              'body': 'One IP can host many services because TCP and UDP ports distinguish listeners.'},
             {'heading': 'Clients use source ports too',
              'body': 'A client normally uses an ephemeral source port while connecting to a server’s known '
                      'destination port.'},
             {'heading': 'A listener is address plus port plus protocol',
              'body': 'A process can be running but still unreachable if it is bound to the wrong interface '
                      'or port.'},
             {'heading': 'Timeout and refusal are different evidence',
              'body': 'Timeout suggests no usable response arrived; refusal often means the destination '
                      'could reject the connection because nothing was accepting it.'},
             {'heading': 'Inspect transport before blaming the application',
              'body': 'Use ss or lsof to inspect listeners and nc to test a port. Use curl only when you '
                      'want application-layer HTTP evidence.'},
             {'heading': 'The transport layer answers a different question',
              'body': 'IP helps a packet reach the correct machine, but the transport layer helps deliver '
                      'that traffic to the correct application. Ports are the bridge between the network '
                      'identity of a computer and the services running on it.'},
             {'heading': 'A successful connection is evidence, not a complete diagnosis',
              'body': 'A successful TCP connection proves that a path existed far enough for a connection to '
                      'be established. It does not prove that the application is healthy, that '
                      'authentication will succeed, or that the response will be correct. Continue moving '
                      'upward through the stack.'},
             {'heading': 'A DevOps troubleshooting decision path',
              'body': 'When an API is unavailable, ask questions in order: did the name resolve, did traffic '
                      'reach the host, did TCP connect to the expected port, is a process listening, and did '
                      'the application return a useful response? Each answer narrows the possible causes.'}],
 'diagram': {'title': 'TCP establishes a connection before application data',
             'description': 'Understand transport-layer communication: TCP connections, the three-way '
                            'handshake, UDP datagrams, source and destination ports, listening sockets, '
                            'ephemeral ports, and the evidence behind timeout versus connection refused.',
             'nodes': [{'label': 'TCP establishes a connection before application data',
                        'detail': 'The SYN → SYN-ACK → ACK handshake creates a connection-oriented session '
                                  'before normal TCP application traffic flows.'},
                       {'label': 'UDP sends datagrams without a TCP-style handshake',
                        'detail': 'UDP is useful where lightweight transport or application-controlled '
                                  'behavior matters, but it does not provide TCP’s built-in ordered reliable '
                                  'byte stream.'},
                       {'label': 'Ports identify transport endpoints',
                        'detail': 'One IP can host many services because TCP and UDP ports distinguish '
                                  'listeners.'},
                       {'label': 'Clients use source ports too',
                        'detail': 'A client normally uses an ephemeral source port while connecting to a '
                                  'server’s known destination port.'},
                       {'label': 'A listener is address plus port plus protocol',
                        'detail': 'A process can be running but still unreachable if it is bound to the '
                                  'wrong interface or port.'},
                       {'label': 'Timeout and refusal are different evidence',
                        'detail': 'Timeout suggests no usable response arrived; refusal often means the '
                                  'destination could reject the connection because nothing was accepting '
                                  'it.'}],
             'caption': 'Follow the network path layer by layer and use evidence to locate the failing '
                        'boundary.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'Use ss or lsof to inspect listeners and nc to test a port. Use curl only '
                                  'when you want application-layer HTTP evidence.'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and safe local tests. Explain what each result proves '
                              'before moving to the next layer.',
                     'steps': ['Create a Journal entry titled “Lesson 3.4 — TCP and Ports.”',
                               'List current TCP listeners using ss -lnt on Linux or lsof -iTCP -sTCP:LISTEN '
                               'on macOS.',
                               'Choose one listener you recognize and record its local address and port.',
                               'Explain whether the listener is bound to loopback, all interfaces, or a '
                               'specific address.',
                               'Run nc -vz example.com 443 if netcat is available and record whether TCP '
                               'connection establishment succeeds.',
                               'Run curl -I https://example.com and explain what curl proves beyond the '
                               'netcat test.'],
                     'takeaway': 'A networking command is useful only when it answers a specific question.'},
 'lab': {'title': 'Lesson 3.4 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.4 — TCP and Ports.”',
                          'List current TCP listeners using ss -lnt on Linux or lsof -iTCP -sTCP:LISTEN on '
                          'macOS.',
                          'Choose one listener you recognize and record its local address and port.',
                          'Explain whether the listener is bound to loopback, all interfaces, or a specific '
                          'address.',
                          'Run nc -vz example.com 443 if netcat is available and record whether TCP '
                          'connection establishment succeeds.',
                          'Run curl -I https://example.com and explain what curl proves beyond the netcat '
                          'test.',
                          'Write the TCP three-way handshake in order.',
                          'Explain the difference between destination port 443 and the client’s ephemeral '
                          'source port.',
                          'Write one scenario that would likely produce connection refused.',
                          'Write one scenario that could produce a timeout.',
                          'Explain why a process being present in ps output does not prove its network '
                          'service is reachable.']},
 'quiz': [{'question': 'What does TCP establish before normal application data?',
           'choices': ['A connection', 'A DNS zone', 'A filesystem mount', 'A Git branch'],
           'correct': 0},
          {'question': 'What is the TCP handshake order?',
           'choices': ['SYN → SYN-ACK → ACK', 'ACK → SYN → FIN', 'DNS → TCP → HTTP', 'GET → POST → ACK'],
           'correct': 0},
          {'question': 'What does UDP lack compared with TCP?',
           'choices': ['The same built-in connection and ordered reliable delivery behavior',
                       'IP addressing',
                       'Ports',
                       'Packets'],
           'correct': 0},
          {'question': 'What is a destination port used for?',
           'choices': ['Identifying the target transport service',
                       'Selecting a Git commit',
                       'Choosing a DNS server only',
                       'Assigning a UID'],
           'correct': 0},
          {'question': 'What is an ephemeral port?',
           'choices': ['A temporary client-side source port',
                       'A permanent DNS port',
                       'A firewall only',
                       'A port that cannot be reused'],
           'correct': 0},
          {'question': 'What does LISTEN mean for a TCP socket?',
           'choices': ['The process is waiting for incoming connections',
                       'The connection is encrypted',
                       'DNS failed',
                       'The process is stopped'],
           'correct': 0},
          {'question': 'What does connection refused commonly suggest?',
           'choices': ['The destination rejected the connection because nothing accepted that port or it was '
                       'actively rejected',
                       'DNS always failed',
                       'TLS already succeeded',
                       'The route cannot exist'],
           'correct': 0},
          {'question': 'What does timeout suggest more strongly?',
           'choices': ['No usable response arrived in time',
                       'The service definitely returned HTTP 500',
                       'The client authenticated successfully',
                       'The server is listening'],
           'correct': 0},
          {'question': 'What does nc -vz HOST PORT primarily test?',
           'choices': ['TCP connectivity to that host and port',
                       'HTTP status codes',
                       'DNS TTL only',
                       'TLS certificate validity'],
           'correct': 0},
          {'question': 'Why can a service work locally but not remotely?',
           'choices': ['It may be bound only to loopback',
                       'TCP never works across hosts',
                       'UDP disables routing',
                       'Ports are local-only'],
           'correct': 0}],
 'reflection': 'How would you distinguish a transport-layer failure from an application-layer failure when a '
               'user says an API is unavailable?'}
