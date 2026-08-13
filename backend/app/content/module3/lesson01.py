"""Module 3, Lesson 1: How Computers Talk."""

LESSON = {'id': '3-1',
 'title': 'How Computers Talk',
 'summary': 'Build a practical networking mental model: interfaces, IP addresses, packets, protocols, ports, '
            'sockets, clients, servers, and the path between applications.',
 'duration_minutes': 60,
 'xp': 65,
 'audio_script': 'Welcome to Module 3: Networking and Web Fundamentals.\n'
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
                 'Keep climbing.',
 'objectives': ['Explain interfaces, IP addresses, ports, packets, clients, and servers.',
                'Describe the layered path from DNS through HTTP.',
                'Explain localhost and wildcard bind addresses.',
                'Distinguish DNS, routing, transport, TLS, and application failures.',
                'Use a layer-by-layer troubleshooting sequence.'],
 'content': [{'heading': 'Networking is endpoint communication',
              'body': 'Applications use the operating system’s networking stack to communicate between '
                      'endpoints.'},
             {'heading': 'IP addresses identify network endpoints',
              'body': 'A host can have multiple addresses across physical, virtual, loopback, VPN, '
                      'container, or cloud interfaces.'},
             {'heading': 'Ports distinguish services',
              'body': 'Multiple applications can share one IP because TCP and UDP ports identify '
                      'transport-layer listeners.'},
             {'heading': 'Clients and servers are roles',
              'body': 'The client initiates; the server listens and responds. One machine can perform both '
                      'roles in different interactions.'},
             {'heading': 'localhost is local context',
              'body': '127.0.0.1 is the common IPv4 loopback address. A loopback-only service is not '
                      'remotely reachable.'},
             {'heading': 'Failures belong to layers',
              'body': 'DNS errors, timeouts, connection refusal, TLS failures, and HTTP 500 responses point '
                      'to different parts of the path.'},
             {'heading': 'Troubleshoot by asking how far the request got',
              'body': 'Use name → address → route → port → protocol → application rather than treating every '
                      'problem as “the network.”'}],
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
