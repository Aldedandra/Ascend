"""Module 3, Lesson 3-1: How Computers Talk."""

LESSON = {'id': '3-1',
 'title': 'How Computers Talk',
 'summary': 'Build a practical networking mental model: interfaces, IP addresses, packets, protocols, ports, '
            'sockets, clients, servers, and the path between applications.',
 'duration_minutes': 80,
 'xp': 65,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is How Computers Talk.\n'
                 '\n'
                 'The goal is not to memorize networking vocabulary. The goal is to build a mental model you '
                 'can use when a real system fails. By the end of this lesson, you should be able to explain '
                 'the path in your own words, identify the evidence available at each boundary, and choose a '
                 'next test because of what you observed rather than because a command happens to be '
                 'familiar.\n'
                 '\n'
                 'As you listen, keep one question in mind: how far did the communication actually get?\n'
                 '\n'
                 'Here is what we are building toward.\n'
                 '\n'
                 'First, Explain interfaces, IP addresses, ports, packets, clients, and servers. Also, '
                 'Describe the layered path from DNS through HTTP. Also, Explain localhost and wildcard bind '
                 'addresses. Also, Distinguish DNS, routing, transport, TLS, and application failures. Also, '
                 'Use a layer-by-layer troubleshooting sequence.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 "From 'the network' to a request path.\n"
                 '\n'
                 'When people say an application has a “network problem,” they often compress several '
                 'independent systems into one phrase. A useful DevOps mental model is a path: a client '
                 'chooses a name, DNS may turn that name into an address, the operating system chooses a '
                 'route and interface, a transport connection targets a port, and an application protocol '
                 'such as HTTP carries the request. The server then has its own dependencies and return '
                 'path. Troubleshooting becomes much easier when you ask how far through that path the '
                 'request actually traveled.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'Interfaces give a computer multiple network identities.\n'
                 '\n'
                 'A computer can participate in several networks at the same time. Your Mac may have Wi-Fi, '
                 'loopback, a Tailscale interface, another VPN interface, and Docker-created networking. '
                 'Each interface can have its own addresses and routes. A packet does not simply “use the '
                 'internet”; the operating system selects an interface according to the destination and '
                 'routing table. This is why connecting a VPN can change application behavior even when you '
                 'did not change the application itself.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'IP address, port, and application are three different ideas.\n'
                 '\n'
                 'An IP address answers roughly, “Which network endpoint should receive this traffic?” A TCP '
                 'or UDP port answers, “Which service at that endpoint should receive it?” The application '
                 "is the program actually handling the request. If Ascend's API is expected at "
                 '192.168.1.50:8000, the address and port are both required. Reaching 192.168.1.50 does not '
                 'prove anything is listening on 8000, and reaching 8000 does not prove the API will return '
                 'healthy lesson data.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 'Sockets are where applications meet networking.\n'
                 '\n'
                 "Applications use sockets to communicate through the operating system's network stack. A "
                 'server typically binds a socket to an address and port and then listens for incoming '
                 'connections. A client creates a socket and initiates communication toward a destination. '
                 'Tools such as ss, netstat, and lsof are useful because they let you inspect this boundary '
                 'between the application and the network. Seeing a listener is concrete evidence that a '
                 'process is prepared to accept traffic on that particular address and port.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 'localhost is local to the current network context.\n'
                 '\n'
                 '127.0.0.1 is the IPv4 loopback address. Traffic sent there stays on the local system or, '
                 'with containers, within the current network namespace. This creates a classic failure: an '
                 'API works with curl from the same machine but cannot be reached from another machine '
                 'because it is bound only to loopback. Later, Docker makes this even more important because '
                 'localhost inside one container refers to that container, not to a neighboring backend '
                 'container or automatically to the Docker host.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 'Why 0.0.0.0 matters.\n'
                 '\n'
                 'When a server binds to 0.0.0.0, it commonly means “listen on all IPv4 interfaces available '
                 'in this network context.” It is a bind address, not normally the address a client should '
                 'browse to. Compare a FastAPI process listening on 127.0.0.1:8000 with one listening on '
                 '0.0.0.0:8000: both may work locally, but only the second is prepared to accept traffic '
                 'arriving through other IPv4 interfaces, assuming routing and policy also allow it.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'Follow an Ascend request.\n'
                 '\n'
                 'Imagine the Ascend frontend needs lesson data from the FastAPI backend. The browser or '
                 'frontend must first know the backend name or address. The operating system chooses a '
                 'route. TCP must reach the expected port. The backend must be listening. HTTP must then '
                 'produce a useful response, and the API may still need PostgreSQL to complete the request. '
                 'If the browser receives an HTTP 500, you already know the request traveled much farther '
                 'than if TCP was refused. That difference should change your next troubleshooting step.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'Read failures as boundaries around the problem.\n'
                 '\n'
                 'A DNS failure means you have not yet established the intended destination address. '
                 'Connection refused commonly means the destination was reached but the requested port was '
                 'not accepting the connection, or policy rejected it. A timeout is less specific because '
                 'routing, filtering, reachability, or a silent service can all produce it. A TLS '
                 'certificate error proves you reached a TLS-speaking endpoint. An HTTP 404, 502, or 500 '
                 'proves an HTTP-speaking system returned a response. Each result removes some possible '
                 'explanations.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'Commands should answer questions.\n'
                 '\n'
                 'Do not collect commands as rituals. Use ip addr or ifconfig when you need to understand '
                 'interfaces and addresses. Use ip route or route when you need to understand the selected '
                 'path. Use ss or lsof when you need to know what is listening. Use nc when you need a '
                 'focused transport test. Use curl when you need to inspect HTTP or TLS behavior. Before '
                 'running a command, say the question you expect it to answer.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 'The evidence habit.\n'
                 '\n'
                 'For every observation, practice two statements: “This proves…” and “This does not prove…”. '
                 'A successful ping, where permitted, may prove some IP reachability but does not prove an '
                 'HTTP service is healthy. A listening socket proves a process is accepting connections '
                 'locally on that bind address but does not prove a remote client can reach it. This habit '
                 'prevents one successful test from becoming an unjustified conclusion about the entire '
                 'application.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'Welcome to Module 3: Networking and Web Fundamentals.\n'
                 '\n'
                 'Linux taught you how to operate inside a system. Networking teaches you how systems reach '
                 'one another.\n'
                 '\n'
                 'When an application says connection refused, a browser says a site cannot be reached, or '
                 'an API times out, the problem is not simply “the network.” There are several layers '
                 'between the application making a request and the application expected to answer it.\n'
                 '\n'
                 'Start with endpoints. Your laptop, a server, a container, a load balancer, and a database '
                 'can all participate in network communication. Systems have network interfaces, and those '
                 'interfaces can have IP addresses.\n'
                 '\n'
                 'An IP address identifies a network-layer endpoint. But an IP address alone is not enough '
                 'to identify one application. A host may run SSH, a web server, a database, and monitoring '
                 'software at the same time. Ports distinguish transport-layer services.\n'
                 '\n'
                 'Data moves through protocols. IP handles addressing and routing. TCP provides '
                 'connection-oriented reliable transport. UDP provides datagram transport. DNS maps names to '
                 'address information. TLS protects traffic. HTTP defines web requests and responses.\n'
                 '\n'
                 'Imagine opening an HTTPS site. DNS resolves the hostname. IP routing determines the path. '
                 'TCP establishes a connection to the destination port. TLS creates an encrypted '
                 'authenticated session. HTTP carries the request and response.\n'
                 '\n'
                 'A problem can occur at any layer.\n'
                 '\n'
                 'DNS may return the wrong address. Routing may fail. A firewall may block the port. Nothing '
                 'may be listening. TLS may reject a certificate. The server may accept the request and '
                 'return HTTP 500.\n'
                 '\n'
                 'Each failure produces different evidence.\n'
                 '\n'
                 'Clients and servers are roles. A client initiates communication. A server listens and '
                 'responds. One machine can act as both in different interactions.\n'
                 '\n'
                 'Ascend’s frontend can be a client of the backend API. The backend can then become a client '
                 'of PostgreSQL. PostgreSQL acts as the server for the database connection. A user-facing '
                 'error can therefore originate anywhere along the path.\n'
                 '\n'
                 'Now consider localhost. IPv4 commonly uses 127.0.0.1 for loopback. A service bound only to '
                 'loopback can work on the same machine but remain unreachable from another machine.\n'
                 '\n'
                 'The address 0.0.0.0 has another meaning when used as a listening bind address. It commonly '
                 'means listen on all available IPv4 interfaces. It is not a normal destination you browse '
                 'to remotely.\n'
                 '\n'
                 'Linux and macOS provide tools for different networking questions. Interface tools show '
                 'addresses. Routing tools show path decisions. Socket tools show listening ports. dig '
                 'inspects DNS. curl tests HTTP. ping tests certain reachability conditions.\n'
                 '\n'
                 'Do not run commands randomly. Start by asking what layer needs evidence.\n'
                 '\n'
                 'A useful sequence is name, address, route, port, protocol, application.\n'
                 '\n'
                 'That sequence will return throughout this module.\n'
                 '\n'
                 'The key lesson is simple: computers do not “just connect.” Applications communicate '
                 'through layers. When communication fails, identify the failing layer before changing '
                 'anything.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Before you leave this lesson, try to explain the request path without looking at the '
                 'screen.\n'
                 '\n'
                 'Name the client. Name the destination. Identify the address or name involved. Identify the '
                 'route or network boundary. Identify the transport protocol and port. Then identify the '
                 'application behavior you expect.\n'
                 '\n'
                 'If something fails, do not jump immediately to a fix. Capture the symptom. Run the '
                 'smallest test that separates two plausible explanations. Record the result. Update the '
                 'hypothesis. Then continue.\n'
                 '\n'
                 'That is the pattern we are building throughout Ascend: evidence before action.\n'
                 '\n'
                 'When you are ready, continue into the lab and make the mental model observable with real '
                 'commands and real output.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain interfaces, IP addresses, ports, packets, clients, and servers.',
                'Describe the layered path from DNS through HTTP.',
                'Explain localhost and wildcard bind addresses.',
                'Distinguish DNS, routing, transport, TLS, and application failures.',
                'Use a layer-by-layer troubleshooting sequence.'],
 'content': [{'heading': "From 'the network' to a request path",
              'body': 'When people say an application has a “network problem,” they often compress several '
                      'independent systems into one phrase. A useful DevOps mental model is a path: a client '
                      'chooses a name, DNS may turn that name into an address, the operating system chooses '
                      'a route and interface, a transport connection targets a port, and an application '
                      'protocol such as HTTP carries the request. The server then has its own dependencies '
                      'and return path. Troubleshooting becomes much easier when you ask how far through '
                      'that path the request actually traveled.'},
             {'heading': 'Interfaces give a computer multiple network identities',
              'body': 'A computer can participate in several networks at the same time. Your Mac may have '
                      'Wi-Fi, loopback, a Tailscale interface, another VPN interface, and Docker-created '
                      'networking. Each interface can have its own addresses and routes. A packet does not '
                      'simply “use the internet”; the operating system selects an interface according to the '
                      'destination and routing table. This is why connecting a VPN can change application '
                      'behavior even when you did not change the application itself.'},
             {'heading': 'IP address, port, and application are three different ideas',
              'body': 'An IP address answers roughly, “Which network endpoint should receive this traffic?” '
                      'A TCP or UDP port answers, “Which service at that endpoint should receive it?” The '
                      "application is the program actually handling the request. If Ascend's API is expected "
                      'at 192.168.1.50:8000, the address and port are both required. Reaching 192.168.1.50 '
                      'does not prove anything is listening on 8000, and reaching 8000 does not prove the '
                      'API will return healthy lesson data.'},
             {'heading': 'Sockets are where applications meet networking',
              'body': "Applications use sockets to communicate through the operating system's network stack. "
                      'A server typically binds a socket to an address and port and then listens for '
                      'incoming connections. A client creates a socket and initiates communication toward a '
                      'destination. Tools such as ss, netstat, and lsof are useful because they let you '
                      'inspect this boundary between the application and the network. Seeing a listener is '
                      'concrete evidence that a process is prepared to accept traffic on that particular '
                      'address and port.'},
             {'heading': 'localhost is local to the current network context',
              'body': '127.0.0.1 is the IPv4 loopback address. Traffic sent there stays on the local system '
                      'or, with containers, within the current network namespace. This creates a classic '
                      'failure: an API works with curl from the same machine but cannot be reached from '
                      'another machine because it is bound only to loopback. Later, Docker makes this even '
                      'more important because localhost inside one container refers to that container, not '
                      'to a neighboring backend container or automatically to the Docker host.'},
             {'heading': 'Why 0.0.0.0 matters',
              'body': 'When a server binds to 0.0.0.0, it commonly means “listen on all IPv4 interfaces '
                      'available in this network context.” It is a bind address, not normally the address a '
                      'client should browse to. Compare a FastAPI process listening on 127.0.0.1:8000 with '
                      'one listening on 0.0.0.0:8000: both may work locally, but only the second is prepared '
                      'to accept traffic arriving through other IPv4 interfaces, assuming routing and policy '
                      'also allow it.'},
             {'heading': 'Follow an Ascend request',
              'body': 'Imagine the Ascend frontend needs lesson data from the FastAPI backend. The browser '
                      'or frontend must first know the backend name or address. The operating system chooses '
                      'a route. TCP must reach the expected port. The backend must be listening. HTTP must '
                      'then produce a useful response, and the API may still need PostgreSQL to complete the '
                      'request. If the browser receives an HTTP 500, you already know the request traveled '
                      'much farther than if TCP was refused. That difference should change your next '
                      'troubleshooting step.'},
             {'heading': 'Read failures as boundaries around the problem',
              'body': 'A DNS failure means you have not yet established the intended destination address. '
                      'Connection refused commonly means the destination was reached but the requested port '
                      'was not accepting the connection, or policy rejected it. A timeout is less specific '
                      'because routing, filtering, reachability, or a silent service can all produce it. A '
                      'TLS certificate error proves you reached a TLS-speaking endpoint. An HTTP 404, 502, '
                      'or 500 proves an HTTP-speaking system returned a response. Each result removes some '
                      'possible explanations.'},
             {'heading': 'Commands should answer questions',
              'body': 'Do not collect commands as rituals. Use ip addr or ifconfig when you need to '
                      'understand interfaces and addresses. Use ip route or route when you need to '
                      'understand the selected path. Use ss or lsof when you need to know what is listening. '
                      'Use nc when you need a focused transport test. Use curl when you need to inspect HTTP '
                      'or TLS behavior. Before running a command, say the question you expect it to answer.'},
             {'heading': 'The evidence habit',
              'body': 'For every observation, practice two statements: “This proves…” and “This does not '
                      'prove…”. A successful ping, where permitted, may prove some IP reachability but does '
                      'not prove an HTTP service is healthy. A listening socket proves a process is '
                      'accepting connections locally on that bind address but does not prove a remote client '
                      'can reach it. This habit prevents one successful test from becoming an unjustified '
                      'conclusion about the entire application.'}],
 'diagram': {'title': 'Networking is endpoint communication',
             'description': 'Build a practical networking mental model: interfaces, IP addresses, packets, '
                            'protocols, ports, sockets, clients, servers, and the path between applications.',
             'nodes': [{'label': 'Networking is endpoint communication',
                        'detail': 'Applications use the operating system’s networking stack to communicate '
                                  'between endpoints.'},
                       {'label': 'IP addresses identify network endpoints',
                        'detail': 'A host can have multiple addresses across physical, virtual, loopback, '
                                  'VPN, container, or cloud interfaces.'},
                       {'label': 'Ports distinguish services',
                        'detail': 'Multiple applications can share one IP because TCP and UDP ports identify '
                                  'transport-layer listeners.'},
                       {'label': 'Clients and servers are roles',
                        'detail': 'The client initiates; the server listens and responds. One machine can '
                                  'perform both roles in different interactions.'},
                       {'label': 'localhost is local context',
                        'detail': '127.0.0.1 is the common IPv4 loopback address. A loopback-only service is '
                                  'not remotely reachable.'},
                       {'label': 'Failures belong to layers',
                        'detail': 'DNS errors, timeouts, connection refusal, TLS failures, and HTTP 500 '
                                  'responses point to different parts of the path.'}],
             'caption': 'Follow the path layer by layer and gather evidence before changing anything.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'Use name → address → route → port → protocol → application rather than '
                                  'treating every problem as “the network.”'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and explain what each result proves.',
                     'steps': ['Create a Journal entry titled “Lesson 3.1 — How Computers Talk.”',
                               'Inspect interfaces with ifconfig on macOS or ip addr on Linux.',
                               'Identify loopback and one non-loopback interface.',
                               'List TCP listeners with lsof -iTCP -sTCP:LISTEN on macOS or ss -lnt on '
                               'Linux.',
                               'Run curl -I https://example.com and record the HTTP status.',
                               'Explain which additional layers must have succeeded for curl to receive an '
                               'HTTP response.'],
                     'takeaway': 'Choose commands because they answer specific questions.'},
 'lab': {'title': 'Lesson 3.1 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.1 — How Computers Talk.”',
                          'Inspect interfaces with ifconfig on macOS or ip addr on Linux.',
                          'Identify loopback and one non-loopback interface.',
                          'List TCP listeners with lsof -iTCP -sTCP:LISTEN on macOS or ss -lnt on Linux.',
                          'Run curl -I https://example.com and record the HTTP status.',
                          'Explain which additional layers must have succeeded for curl to receive an HTTP '
                          'response.',
                          'Draw Browser → DNS → IP route → TCP port → TLS → HTTP server.',
                          'For each layer, write one possible failure.',
                          'Write a scenario where a service works on localhost but fails remotely.',
                          'Finish by explaining why “the network is down” is not a diagnosis.']},
 'quiz': [{'question': 'What does an IP address primarily identify?',
           'choices': ['A network-layer endpoint',
                       'A Git repository',
                       'A filesystem permission',
                       'A shell process'],
           'correct': 0},
          {'question': 'Why are ports needed?',
           'choices': ['They distinguish transport-layer services',
                       'They replace IP addresses',
                       'They encrypt traffic',
                       'They provide DNS'],
           'correct': 0},
          {'question': 'What is a client?',
           'choices': ['The side that initiates communication',
                       'Always the browser',
                       'The faster machine',
                       'The side with the public IP'],
           'correct': 0},
          {'question': 'What is 127.0.0.1 commonly used for?',
           'choices': ['Loopback/localhost', 'Public DNS', 'Default route', 'Broadcast only'],
           'correct': 0},
          {'question': 'What does 0.0.0.0 commonly mean as a bind address?',
           'choices': ['Listen on all IPv4 interfaces',
                       'Connect to all internet hosts',
                       'Disable networking',
                       'Use DNS only'],
           'correct': 0},
          {'question': 'Which protocol resolves names?',
           'choices': ['DNS', 'HTTP', 'SSH', 'Git'],
           'correct': 0},
          {'question': 'What does connection refused usually suggest?',
           'choices': ['The host was reached but nothing accepted that port',
                       'The hostname cannot exist',
                       'TLS succeeded',
                       'HTTP returned 500'],
           'correct': 0},
          {'question': 'Which sequence is best for layered troubleshooting?',
           'choices': ['Name → address → route → port → protocol → application',
                       'Restart → reboot → reinstall',
                       'HTTP → Git → filesystem',
                       'Password → CPU → DNS'],
           'correct': 0},
          {'question': 'Why can a local service fail remotely?',
           'choices': ['It may be bound only to loopback',
                       'localhost is always public',
                       'TCP cannot cross hosts',
                       'DNS disables remote traffic'],
           'correct': 0},
          {'question': 'What is the main troubleshooting lesson?',
           'choices': ['Find the failing layer before acting',
                       'All network errors are identical',
                       'Ping proves applications work',
                       'Ports matter only to firewalls'],
           'correct': 0}],
 'reflection': 'When someone says “the network is down,” what questions would you ask to turn that vague '
               'symptom into a layered investigation?'}
