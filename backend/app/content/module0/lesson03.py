"""Module 0, Lesson 3: The Internet Is Computers Talking."""

LESSON = {'id': '0-3',
 'title': 'The Internet Is Computers Talking',
 'summary': 'Follow one request through names, addresses, ports, protocols, Tailscale, Docker, FastAPI, and '
            'PostgreSQL so network problems become traceable conversations instead of mystery.',
 'duration_minutes': 70,
 'xp': 70,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.3: The Internet Is Computers Talking.\n'
                 '\n'
                 'In the previous lesson, you learned to gather evidence before taking action. But evidence '
                 'only helps when you understand where to look. Today, we build the map.\n'
                 '\n'
                 'The internet can seem enormous and mysterious. In practice, it is computers exchanging '
                 'structured messages across connected networks.\n'
                 '\n'
                 'You tap the Ascend icon on your iPhone. The lesson page appears. It feels immediate. But '
                 'many conversations may have succeeded before the first word reached your screen.\n'
                 '\n'
                 'Your phone needed an address for the server. It needed a route to that address. It needed '
                 'to reach the correct port. It needed to speak the expected protocol. The server needed to '
                 'accept the request. The frontend or backend needed to process it. The backend may have '
                 'needed to ask PostgreSQL for data. Then every answer had to travel back.\n'
                 '\n'
                 'A useful mental model is this: every arrow in an architecture diagram is a conversation, '
                 'and every conversation has two sides, an address, a protocol, a request, a response, and a '
                 'possible failure.\n'
                 '\n'
                 'Let us begin with names and addresses.\n'
                 '\n'
                 'Humans prefer names such as ascend dot example dot com, sentinelhome, or forge. Networks '
                 'route traffic using numeric addresses. DNS, the Domain Name System, helps translate a name '
                 'into an IP address.\n'
                 '\n'
                 'You can think of DNS as a distributed directory. Your device asks, “What address belongs '
                 'to this name?” A resolver may answer from cache or ask other DNS servers until it finds '
                 'the authoritative answer.\n'
                 '\n'
                 'If DNS fails, the browser may never attempt to contact the application server. That is '
                 'different from a server refusing a connection. The visible result may still be “the page '
                 'will not load,” but the failed conversation occurs earlier.\n'
                 '\n'
                 'In your Tailscale environment, device names and Tailscale IP addresses create a private '
                 'path between authenticated devices. When your iPhone reaches the home server through a '
                 'one-hundred-dot address, the traffic travels through the Tailscale network rather than '
                 'being exposed directly to the public internet.\n'
                 '\n'
                 'The address identifies a machine or network interface. It does not identify the '
                 'application by itself.\n'
                 '\n'
                 'That is where ports enter the conversation.\n'
                 '\n'
                 'A server can run many services at one address. Ports distinguish them. Ascend’s frontend '
                 'may be published on port three thousand. FastAPI may be published on port eight thousand '
                 'or eight thousand one. PostgreSQL commonly listens on port five four three two inside its '
                 'network.\n'
                 '\n'
                 'An IP address answers, “Which machine?” A port answers, “Which service on that machine?”\n'
                 '\n'
                 'If the iPhone reaches the correct Tailscale IP but the backend port is not published or '
                 'allowed through the firewall, the machine is reachable while the service is not.\n'
                 '\n'
                 'This distinction is extremely important. Ping success does not prove an HTTP service is '
                 'reachable. A working frontend port does not prove the backend port is reachable. Each '
                 'conversation must be tested at the correct boundary.\n'
                 '\n'
                 'Now we need a transport conversation.\n'
                 '\n'
                 'Most web applications use TCP. TCP creates a reliable connection between two endpoints. It '
                 'orders data, detects missing pieces, and retransmits when necessary. Before HTTP messages '
                 'can flow, the client and server establish a TCP connection.\n'
                 '\n'
                 'You do not need to memorize packet flags today. Remember the engineering meaning: a failed '
                 'TCP connection usually points toward address, route, firewall, port exposure, or '
                 'listening-service problems. An established TCP connection means the investigation can move '
                 'higher in the stack.\n'
                 '\n'
                 'On top of that connection, the browser speaks HTTP.\n'
                 '\n'
                 'HTTP is a request-and-response protocol. The client sends a request containing a method, '
                 'path, headers, and sometimes a body. The server returns a response containing a status '
                 'code, headers, and a body.\n'
                 '\n'
                 'For example, Ascend might send GET slash lessons slash zero dash three. The backend may '
                 'return status two hundred and JSON containing the lesson.\n'
                 '\n'
                 'A POST request usually asks the server to create or submit something. A PATCH request '
                 'changes part of something. A DELETE request asks to remove something. These are '
                 'conventions, not magic commands, but they make APIs predictable.\n'
                 '\n'
                 'Status codes summarize the result.\n'
                 '\n'
                 'Two hundred means the request succeeded.\n'
                 '\n'
                 'Four hundred means the client sent something invalid.\n'
                 '\n'
                 'Four oh one means authentication is required or invalid.\n'
                 '\n'
                 'Four oh three means the identity is known but not allowed.\n'
                 '\n'
                 'Four oh four means the requested route or resource was not found.\n'
                 '\n'
                 'Five hundred means the server encountered an unexpected failure.\n'
                 '\n'
                 'Five oh two often means a proxy could not get a valid response from an upstream service.\n'
                 '\n'
                 'Five oh three often means the service is unavailable.\n'
                 '\n'
                 'The status code is evidence, not a complete diagnosis. A five hundred tells you the '
                 'server-side path failed. It does not automatically tell you whether FastAPI code, '
                 'PostgreSQL, configuration, or another dependency caused it.\n'
                 '\n'
                 'HTTPS is HTTP protected by TLS. TLS encrypts the conversation and helps the client verify '
                 'the server’s identity through certificates.\n'
                 '\n'
                 'When TLS fails, the application may be healthy but the secure conversation cannot be '
                 'established. Expired certificates, name mismatches, untrusted certificate authorities, and '
                 'protocol configuration can all prevent the request before the application sees it.\n'
                 '\n'
                 'Next, let us separate frontend and backend conversations.\n'
                 '\n'
                 'When you first open Ascend, the browser or Capacitor web view loads frontend assets: HTML, '
                 'CSS, and JavaScript. That is one conversation.\n'
                 '\n'
                 'After the interface appears, JavaScript sends API requests to FastAPI. Those are '
                 'additional conversations.\n'
                 '\n'
                 'This explains a common symptom: the page shell loads, but data does not. Frontend delivery '
                 'succeeded. The API conversation failed.\n'
                 '\n'
                 'The browser Network panel makes these conversations visible. It shows the requested URL, '
                 'method, status code, timing, request headers, response headers, and response body. The '
                 'Console may show JavaScript errors or blocked requests.\n'
                 '\n'
                 'This is why browser developer tools are so powerful. They let you inspect what the client '
                 'actually asked for.\n'
                 '\n'
                 'Now follow the request into Docker.\n'
                 '\n'
                 'Docker gives containers isolated network environments. A container can listen on a port '
                 'internally, while Docker publishes that port on the host. In Compose, services can usually '
                 'reach one another by service name on the Compose network.\n'
                 '\n'
                 'The frontend container might reach the backend using a service name when communication '
                 'happens server-side. But browser JavaScript runs on the user’s device, not inside the '
                 'Docker network. The iPhone cannot resolve a private Compose service name such as backend '
                 'unless a reachable DNS and routing system exposes it.\n'
                 '\n'
                 'That difference causes many configuration mistakes.\n'
                 '\n'
                 'Inside Docker, backend colon eight thousand may be valid. On your iPhone, localhost means '
                 'the iPhone itself. On the Windows or Mac host, localhost means that host. On another '
                 'machine, the home server’s Tailscale address identifies the server.\n'
                 '\n'
                 'The same word can refer to different places depending on where the code is running.\n'
                 '\n'
                 'Now the request reaches FastAPI.\n'
                 '\n'
                 'FastAPI matches the HTTP method and path to a route handler. The handler may validate '
                 'input, check authentication, run application logic, and query PostgreSQL. If everything '
                 'succeeds, it creates a response. If an unhandled exception occurs, the client may receive '
                 'a five hundred response.\n'
                 '\n'
                 'The backend then begins another conversation with PostgreSQL.\n'
                 '\n'
                 'PostgreSQL listens for database connections. The backend sends SQL queries or uses an '
                 'object-relational mapper to request data. PostgreSQL returns rows, confirms writes, or '
                 'reports an error.\n'
                 '\n'
                 'From the user’s perspective, this entire chain may look like one tap. From the engineer’s '
                 'perspective, it is a sequence of conversations.\n'
                 '\n'
                 'Let us trace a complete example.\n'
                 '\n'
                 'You open Lesson 0.3 in Ascend on your iPhone.\n'
                 '\n'
                 'First, the app knows the frontend location because Capacitor has bundled the web assets or '
                 'because the browser loads them from the server.\n'
                 '\n'
                 'Second, the frontend JavaScript constructs an API request for the lesson.\n'
                 '\n'
                 'Third, the phone routes the request through Wi-Fi or Tailscale to the home server '
                 'address.\n'
                 '\n'
                 'Fourth, the host receives traffic on the published backend port.\n'
                 '\n'
                 'Fifth, Docker forwards the traffic to the FastAPI container.\n'
                 '\n'
                 'Sixth, FastAPI matches the route and asks PostgreSQL or in-memory content for the lesson.\n'
                 '\n'
                 'Seventh, the backend returns JSON with the title, sections, lab, quiz, reflection, and '
                 'audio script.\n'
                 '\n'
                 'Eighth, the response travels back through Docker, the host, Tailscale or Wi-Fi, and the '
                 'phone.\n'
                 '\n'
                 'Ninth, React renders the lesson.\n'
                 '\n'
                 'Now imagine the page displays “Loading lesson” forever.\n'
                 '\n'
                 'Where could the conversation have stopped?\n'
                 '\n'
                 'The request may never have been sent because JavaScript crashed.\n'
                 '\n'
                 'It may have targeted the wrong address.\n'
                 '\n'
                 'The phone may not have had a route.\n'
                 '\n'
                 'The firewall may have blocked the port.\n'
                 '\n'
                 'The backend container may have been restarting.\n'
                 '\n'
                 'FastAPI may have returned an error.\n'
                 '\n'
                 'The response may have been invalid JSON.\n'
                 '\n'
                 'React may have failed while rendering the returned data.\n'
                 '\n'
                 'The same symptom can come from different failed conversations. Your job is to locate the '
                 'last successful boundary and the first failed boundary.\n'
                 '\n'
                 'This is where the tools align with the path.\n'
                 '\n'
                 'Use DNS tools to test name resolution.\n'
                 '\n'
                 'Use ping carefully to test basic reachability, understanding that some systems block it.\n'
                 '\n'
                 'Use curl to send an HTTP request directly.\n'
                 '\n'
                 'Use the browser Network panel to inspect client requests.\n'
                 '\n'
                 'Use Docker ps to check container state.\n'
                 '\n'
                 'Use Docker logs to inspect application output.\n'
                 '\n'
                 'Use ss, netstat, or lsof to confirm which process is listening on a port.\n'
                 '\n'
                 'Use database health checks or a direct connection to test PostgreSQL.\n'
                 '\n'
                 'Every tool answers a specific question. Do not use a tool merely because it is familiar.\n'
                 '\n'
                 'Now consider a TruHearing example. A user opens the internal directory portal and searches '
                 'for an employee. The browser loads the React application. React calls FastAPI. FastAPI may '
                 'call Microsoft Graph. Graph authenticates the application and returns directory data. '
                 'FastAPI transforms the result and returns it to React.\n'
                 '\n'
                 'If the page loads but search returns four oh three, the frontend conversation succeeded '
                 'and the backend reached an authorization boundary. The question becomes whether the token '
                 'has the right audience, scopes, application permissions, consent, or role—not whether the '
                 'user’s monitor needs restarting.\n'
                 '\n'
                 'The conversation model makes escalation clearer because you can say exactly which boundary '
                 'failed.\n'
                 '\n'
                 'There is one more important idea: latency.\n'
                 '\n'
                 'A conversation can succeed but be slow. DNS may take time. A TCP connection may be '
                 'delayed. TLS negotiation adds work. An API may wait on a database. A backend may call '
                 'Microsoft Graph and wait for its response.\n'
                 '\n'
                 'The browser timing waterfall helps show where time was spent. A slow request is not one '
                 'problem category; it may be waiting to connect, waiting for the server, downloading a '
                 'large response, or blocked behind other work.\n'
                 '\n'
                 'Reliability depends on understanding these dependencies. If Ascend requires the frontend, '
                 'backend, database, network, and authentication provider, the user experience is limited by '
                 'the health and coordination of the whole chain.\n'
                 '\n'
                 'This is why DevOps engineers care about health checks, logs, metrics, traces, timeouts, '
                 'retries, and dashboards. They make conversations observable.\n'
                 '\n'
                 'For now, remember the core map.\n'
                 '\n'
                 'Names become addresses through DNS.\n'
                 '\n'
                 'Addresses and routes locate machines.\n'
                 '\n'
                 'Ports locate services.\n'
                 '\n'
                 'TCP creates a reliable connection.\n'
                 '\n'
                 'TLS protects the connection.\n'
                 '\n'
                 'HTTP carries requests and responses.\n'
                 '\n'
                 'Proxies and Docker route traffic to the application.\n'
                 '\n'
                 'FastAPI processes the request.\n'
                 '\n'
                 'PostgreSQL and external APIs answer dependency requests.\n'
                 '\n'
                 'The response travels back to the client.\n'
                 '\n'
                 'When something fails, do not ask only, “Is the internet working?” Ask, “Which conversation '
                 'stopped succeeding?”\n'
                 '\n'
                 'In the next lesson, we will zoom out from the request path and identify the major parts of '
                 'a modern application: frontend, backend, API, database, authentication, infrastructure, '
                 'and deployment. You will learn not only how computers talk, but what each part of the '
                 'system is responsible for.',
 'content': [{'heading': 'Learning objectives',
              'body': 'By the end of this lesson, you should be able to trace a request from client to '
                      'server and back; explain the roles of DNS, IP addresses, ports, TCP, TLS, HTTP, APIs, '
                      'Docker networking, FastAPI, and PostgreSQL; distinguish frontend delivery from API '
                      'communication; select tools that test specific boundaries; and locate the last '
                      'successful and first failing conversation.'},
             {'heading': 'The conversation model',
              'body': 'Every arrow in an architecture diagram represents a conversation. A conversation has '
                      'two endpoints, an address, a port, a protocol, a request, a response, and possible '
                      'failure modes. Troubleshooting becomes easier when you trace those conversations in '
                      'order rather than treating “the internet” as one invisible component.'},
             {'heading': 'Names become addresses through DNS',
              'body': 'Humans remember names; networks route to addresses. DNS translates a hostname into an '
                      'IP address, often using caches and a hierarchy of resolvers. A DNS failure occurs '
                      'before the browser reaches the application server, even though the user may only see '
                      'that the page will not load.'},
             {'heading': 'IP addresses locate machines; ports locate services',
              'body': 'An IP address identifies a network endpoint. A port identifies a service on that '
                      'endpoint. One home server can publish Ascend’s frontend, FastAPI backend, PostgreSQL, '
                      'and other services on different ports. Successful ping or frontend access does not '
                      'prove the backend port is reachable.'},
             {'heading': 'Routes, firewalls, and Tailscale',
              'body': 'A route tells traffic how to reach a destination. Firewalls decide which traffic is '
                      'permitted. Tailscale creates an authenticated private network between devices and '
                      'assigns private addresses, but the target service must still be listening and the '
                      'required port must be reachable. Test the exact path and port used by the '
                      'application.'},
             {'heading': 'TCP creates the connection',
              'body': 'Most web traffic uses TCP for reliable, ordered delivery. If the TCP connection '
                      'cannot be established, investigate address, route, firewall, port publishing, and '
                      'whether a process is listening. If TCP succeeds, the investigation can move to TLS '
                      'and HTTP.'},
             {'heading': 'TLS protects HTTPS',
              'body': 'HTTPS is HTTP carried through TLS encryption. TLS also allows the client to validate '
                      'the server identity using certificates. Expired certificates, hostname mismatches, '
                      'untrusted certificate authorities, or protocol settings can stop the conversation '
                      'before the application receives the request.'},
             {'heading': 'HTTP carries requests and responses',
              'body': 'An HTTP request contains a method, path, headers, and optionally a body. The response '
                      'contains a status code, headers, and body. Status codes narrow the failure class: 2xx '
                      'success, 4xx client or authorization problems, and 5xx server or upstream failures. '
                      'They are evidence, not a complete root cause.'},
             {'heading': 'Frontend delivery and API calls are separate',
              'body': 'The browser first loads HTML, CSS, and JavaScript. React then sends API requests for '
                      'data. If the interface appears but lesson data does not, frontend delivery succeeded '
                      'while a later API conversation failed. The browser Network panel reveals the actual '
                      'URL, method, status, timing, and response.'},
             {'heading': 'Where code runs changes what names mean',
              'body': 'Inside a Compose network, a service may reach another service by its Compose name. '
                      'Browser JavaScript runs on the user device, not inside Docker. On an iPhone, '
                      'localhost is the iPhone. On the home server, localhost is the home server. A private '
                      'Docker hostname is not automatically reachable from another device.'},
             {'heading': 'Docker routes traffic into containers',
              'body': 'A container can listen on an internal port while Docker publishes a host port. '
                      'Host-port reachability, Docker port mapping, Compose networking, and container health '
                      'are distinct boundaries. Verify which address and port the client uses and where '
                      'Docker forwards that traffic.'},
             {'heading': 'FastAPI processes the application request',
              'body': 'FastAPI matches the HTTP method and path to a route handler, validates input, applies '
                      'application logic, and may call databases or external services. An import error can '
                      'prevent the server from starting; an unhandled route exception can produce HTTP 500; '
                      'validation errors can produce HTTP 422.'},
             {'heading': 'PostgreSQL and external APIs are additional conversations',
              'body': 'The backend may query PostgreSQL, contact Microsoft Graph, or call another dependency '
                      'before it can answer the client. The original request can reach FastAPI successfully '
                      'and still fail later. Logs and traces should reveal which dependency conversation '
                      'failed.'},
             {'heading': 'Trace a real Ascend request',
              'body': 'A lesson request may travel from the iPhone through Wi-Fi or Tailscale to the host, '
                      'through a published port into the FastAPI container, into lesson content or '
                      'PostgreSQL, and then back as JSON for React to render. Locate the last confirmed '
                      'successful boundary and the first failed boundary.'},
             {'heading': 'Use the tool that answers the question',
              'body': 'DNS tools test name resolution. ping may test basic reachability. curl tests an HTTP '
                      'endpoint. browser developer tools inspect client behavior. docker ps checks container '
                      'state. docker logs shows application output. ss, netstat, or lsof identifies '
                      'listening ports. Database health checks test the dependency. Choose a tool based on '
                      'the question, not habit.'},
             {'heading': 'TruHearing request path',
              'body': 'A directory search may flow from React to FastAPI, from FastAPI to Microsoft Graph, '
                      'and back. A 403 response points toward identity, scopes, permissions, consent, or '
                      'authorization policy. Mapping the conversation prevents irrelevant device-level '
                      'troubleshooting and produces a stronger escalation.'},
             {'heading': 'Latency is evidence too',
              'body': 'A request can succeed but be slow. Time may be spent resolving DNS, connecting, '
                      'negotiating TLS, waiting for the server, querying a database, calling Microsoft '
                      'Graph, or downloading the response. Browser timing waterfalls, backend duration logs, '
                      'metrics, and traces help identify where the delay occurs.'},
             {'heading': 'Takeaway and bridge',
              'body': 'The internet is computers exchanging structured messages. Names locate addresses, '
                      'ports locate services, protocols define the conversation, and applications call '
                      'dependencies. When a system fails, ask which conversation stopped succeeding. Next, '
                      'you will identify the responsibilities of every major part in a modern application.'}],
 'lab': {'title': 'Trace one request from screen to dependency and back',
         'instructions': ['Choose one real workflow: opening an Ascend lesson, saving a Forge workout, or '
                          'searching the TruHearing directory.',
                          'Draw the complete request path beginning with the user action and ending with the '
                          'rendered response.',
                          'Label every endpoint with the best-known hostname or IP address, port, and '
                          'protocol.',
                          'Mark where DNS or name resolution occurs and identify what evidence would show '
                          'that resolution succeeded or failed.',
                          'Mark where TCP, TLS, and HTTP occur. Write one failure symptom for each layer.',
                          'Identify which code runs on the user device, which runs on the host, which runs '
                          'inside Docker, and which runs in an external service.',
                          'For every arrow, write the request being made and the expected response.',
                          'Add at least eight failure points. For each, choose one tool or observation that '
                          'would test that exact boundary.',
                          'Use browser developer tools or curl against one safe endpoint. Record URL, '
                          'method, status code, response time, and response body summary.',
                          'Write a short explanation of the last successful boundary and first failed '
                          'boundary for a hypothetical failure in your map.']},
 'quiz': [{'question': 'What is the most useful purpose of the conversation model?',
           'choices': ['It proves every issue is network-related',
                       'It lets you trace requests through specific boundaries in order',
                       'It eliminates the need for logs',
                       'It combines every component into one test'],
           'correct': 1},
          {'question': 'What does DNS primarily provide?',
           'choices': ['A port number',
                       'A translation from hostname to IP address',
                       'An HTTP status code',
                       'A Docker image tag'],
           'correct': 1},
          {'question': 'What is the difference between an IP address and a port?',
           'choices': ['An IP identifies a machine or endpoint; a port identifies a service on it',
                       'A port identifies a machine; an IP identifies a file',
                       'They are interchangeable',
                       'Ports are used only by databases'],
           'correct': 0},
          {'question': 'Why does successful ping not prove FastAPI is reachable?',
           'choices': ['Ping checks JavaScript syntax',
                       'Ping does not prove the application port is open and listening',
                       'FastAPI blocks all networks',
                       'Ping always uses HTTP'],
           'correct': 1},
          {'question': 'The Ascend interface loads but lesson data does not. What is the strongest '
                       'conclusion?',
           'choices': ['The entire network is unavailable',
                       'Initial frontend delivery succeeded; investigate the API conversation',
                       'PostgreSQL is definitely corrupted',
                       'DNS cannot resolve the frontend'],
           'correct': 1},
          {'question': 'On an iPhone, what does localhost refer to?',
           'choices': ['The Docker backend service',
                       'The home server',
                       'The iPhone itself',
                       'The Tailscale coordination server'],
           'correct': 2},
          {'question': 'What does HTTP 403 usually indicate?',
           'choices': ['The server cannot be found',
                       'The identity is known but lacks permission',
                       'The request succeeded',
                       'DNS failed'],
           'correct': 1},
          {'question': 'What is Docker port publishing responsible for?',
           'choices': ['Mapping a host port to a container port',
                       'Creating DNS records on the public internet',
                       'Encrypting HTTP with TLS',
                       'Writing rows to PostgreSQL'],
           'correct': 0},
          {'question': 'Which tool best shows the exact API URL, status, and timing used by a browser '
                       'client?',
           'choices': ['Browser Network panel', 'Text editor', 'Docker image list', 'Git log'],
           'correct': 0},
          {'question': 'A request reaches FastAPI, but Microsoft Graph returns 403. Which boundary failed?',
           'choices': ['Frontend file delivery',
                       'The backend-to-Graph authorization conversation',
                       'The user device power supply',
                       'Docker image build'],
           'correct': 1}],
 'diagram': {'title': 'One Ascend lesson request, end to end',
             'description': 'Every arrow is a conversation you can test independently.',
             'nodes': [{'label': 'iPhone or browser',
                        'detail': 'Starts the request and eventually renders the response.'},
                       {'label': 'Wi-Fi or Tailscale',
                        'detail': 'Provides a route from the client to the home server.'},
                       {'label': 'Host address and port',
                        'detail': 'Identifies the machine and the service entry point.'},
                       {'label': 'Frontend container',
                        'detail': 'Serves the Ascend interface and sends API requests.'},
                       {'label': 'FastAPI backend',
                        'detail': 'Matches the route, runs application logic, and prepares a response.'},
                       {'label': 'PostgreSQL or content dependency',
                        'detail': 'Returns the requested lesson, progress, or other data.'},
                       {'label': 'HTTP response',
                        'detail': 'Travels back through the same boundaries to the client.'}],
             'caption': 'When a failure occurs, locate the last successful conversation and the first '
                        'failing one. That boundary is usually more useful than saying “the internet is '
                        'broken.”'},
 'engineer_perspective': {'title': 'Do not troubleshoot “the network” as one invisible object',
                          'body': 'A beginner often asks whether the network works. An engineer asks whether '
                                  'the name resolved, whether a route existed, whether the destination port '
                                  'accepted a connection, whether TLS and HTTP succeeded, and whether the '
                                  'application could reach its dependencies. Precision turns a mystery into '
                                  'testable boundaries.'},
 'try_it_yourself': {'title': 'Trace a real Ascend request',
                     'intro': 'Follow one lesson-loading request through the tools you already use.',
                     'steps': ['Open Ascend in Chrome and select the Network panel in Developer Tools.',
                               'Reload Lesson 0.3 and find the request that returns lesson data.',
                               'Record the hostname or IP address, destination port, HTTP method, status '
                               'code, and total duration.',
                               'Identify which part of the path each value represents: address, service '
                               'entry point, protocol message, and result.',
                               'Compare that browser evidence with docker compose ps and the backend logs.',
                               'Write the last confirmed successful conversation and one hypothetical next '
                               'failure boundary.'],
                     'takeaway': 'The browser, Docker, and backend logs show different parts of the same '
                                 'conversation. Correlating them gives you a system-level view.'},
 'reflection': 'Choose one application workflow you now understand better. Explain the request as a sequence '
               'of conversations using names, addresses, ports, protocols, application services, and '
               'dependencies. Identify the boundary you previously treated as “the internet,” and describe '
               'how you would test it more precisely today.'}
