"""Module 3, Lesson 3-5: HTTP, HTTPS & TLS."""

LESSON = {'id': '3-5',
 'title': 'HTTP, HTTPS & TLS',
 'summary': 'Understand URLs, HTTP requests and responses, methods, headers, status codes, HTTPS, TLS '
            'certificates, and how curl exposes whether a failure belongs to HTTP, TLS, or an earlier '
            'networking layer.',
 'duration_minutes': 75,
 'xp': 80,
 'audio_script': 'Welcome to Lesson 3.5: HTTP, HTTPS, and TLS.\n'
                 '\n'
                 'HTTP is one of the most important application protocols in DevOps because modern systems '
                 'are full of APIs, web applications, health checks, reverse proxies, load balancers, '
                 'package registries, and cloud services that communicate over HTTP.\n'
                 '\n'
                 'HTTP stands for Hypertext Transfer Protocol.\n'
                 '\n'
                 'At its core, HTTP is a request-response protocol.\n'
                 '\n'
                 'A client sends a request.\n'
                 '\n'
                 'A server sends a response.\n'
                 '\n'
                 'The request includes a method, target, headers, and sometimes a body.\n'
                 '\n'
                 'The response includes a status code, headers, and sometimes a body.\n'
                 '\n'
                 'Start with methods.\n'
                 '\n'
                 'GET retrieves a representation of a resource.\n'
                 '\n'
                 'POST commonly creates or submits data.\n'
                 '\n'
                 'PUT commonly replaces or updates a resource.\n'
                 '\n'
                 'PATCH commonly performs a partial update.\n'
                 '\n'
                 'DELETE requests deletion.\n'
                 '\n'
                 'HEAD asks for headers similar to GET without a normal response body.\n'
                 '\n'
                 'OPTIONS can describe communication options and is important in browser CORS behavior.\n'
                 '\n'
                 'These are conventions defined by HTTP semantics, but application APIs decide exactly how '
                 'each endpoint behaves.\n'
                 '\n'
                 'Now status codes.\n'
                 '\n'
                 'One hundred range codes are informational.\n'
                 '\n'
                 'Two hundred range codes represent successful handling.\n'
                 '\n'
                 'Three hundred range codes involve redirection.\n'
                 '\n'
                 'Four hundred range codes indicate client-side request problems.\n'
                 '\n'
                 'Five hundred range codes indicate server-side failures.\n'
                 '\n'
                 'Common examples matter.\n'
                 '\n'
                 '200 OK means the request succeeded.\n'
                 '\n'
                 '201 Created means a resource was created.\n'
                 '\n'
                 '204 No Content means success without a response body.\n'
                 '\n'
                 '301 and 302 are redirects.\n'
                 '\n'
                 '304 Not Modified is commonly associated with cache validation.\n'
                 '\n'
                 '400 Bad Request means the server considers the request invalid.\n'
                 '\n'
                 '401 Unauthorized usually means authentication is required or failed.\n'
                 '\n'
                 '403 Forbidden means the server understood the request but refuses authorization.\n'
                 '\n'
                 '404 Not Found means the target resource was not found.\n'
                 '\n'
                 '429 Too Many Requests indicates rate limiting.\n'
                 '\n'
                 '500 Internal Server Error is a general server failure.\n'
                 '\n'
                 '502 Bad Gateway often means a proxy or gateway could not get a valid response from an '
                 'upstream.\n'
                 '\n'
                 '503 Service Unavailable often means the service is temporarily unable to handle the '
                 'request.\n'
                 '\n'
                 '504 Gateway Timeout often means a gateway timed out waiting for an upstream.\n'
                 '\n'
                 'These codes are evidence.\n'
                 '\n'
                 'A 502 from nginx proves much more than, quote, the network is down.\n'
                 '\n'
                 'It means the client reached nginx and received an HTTP response. The failure is likely '
                 'between the proxy and its upstream or in the upstream response path.\n'
                 '\n'
                 'Now URLs.\n'
                 '\n'
                 'A URL such as https colon slash slash api dot example dot com colon 8443 slash health '
                 'question-mark full equals true contains several pieces.\n'
                 '\n'
                 'Scheme: HTTPS.\n'
                 '\n'
                 'Hostname: api.example.com.\n'
                 '\n'
                 'Port: explicitly 8443.\n'
                 '\n'
                 'Path: slash health.\n'
                 '\n'
                 'Query string: full equals true.\n'
                 '\n'
                 'If the port is omitted, the scheme implies a default convention such as 80 for HTTP or 443 '
                 'for HTTPS.\n'
                 '\n'
                 'Now headers.\n'
                 '\n'
                 'Headers carry metadata.\n'
                 '\n'
                 'Host identifies the requested hostname in HTTP.\n'
                 '\n'
                 'Content-Type describes body format.\n'
                 '\n'
                 'Authorization carries credentials in many APIs.\n'
                 '\n'
                 'Accept describes response formats the client prefers.\n'
                 '\n'
                 'User-Agent identifies client software.\n'
                 '\n'
                 'Cache-Control influences caching.\n'
                 '\n'
                 'Location commonly appears in redirect responses.\n'
                 '\n'
                 'Headers often explain behavior that the status code alone cannot.\n'
                 '\n'
                 'curl is one of your most valuable DevOps tools.\n'
                 '\n'
                 'curl https colon slash slash example dot com makes an HTTP request.\n'
                 '\n'
                 'curl dash I requests headers.\n'
                 '\n'
                 'curl dash v enables verbose output and can expose DNS resolution, TCP connection, TLS '
                 'handshake details, request headers, and response headers.\n'
                 '\n'
                 'curl dash s controls progress output.\n'
                 '\n'
                 'curl dash o can write output to a file.\n'
                 '\n'
                 'curl dash H adds a header.\n'
                 '\n'
                 'curl dash X can specify a method, although many operations automatically choose the '
                 'appropriate method.\n'
                 '\n'
                 'When troubleshooting, start simple and add verbosity deliberately.\n'
                 '\n'
                 'Now HTTPS.\n'
                 '\n'
                 'HTTPS is HTTP carried over TLS.\n'
                 '\n'
                 'TLS stands for Transport Layer Security.\n'
                 '\n'
                 'TLS provides encryption, integrity protection, and server identity verification through '
                 'certificates.\n'
                 '\n'
                 'During a TLS handshake, the client and server negotiate cryptographic parameters.\n'
                 '\n'
                 'The server presents a certificate.\n'
                 '\n'
                 'The client verifies that the certificate chains to a trusted certificate authority, is '
                 'valid for the hostname, is within its validity period, and meets other policy '
                 'requirements.\n'
                 '\n'
                 'If that verification fails, the client should not quietly ignore it.\n'
                 '\n'
                 'A certificate error is evidence.\n'
                 '\n'
                 'Common causes include expired certificates, wrong hostname, incomplete certificate chains, '
                 'untrusted issuers, incorrect system time, or interception by a proxy that the client does '
                 'not trust.\n'
                 '\n'
                 'The curl dash k option disables certificate verification.\n'
                 '\n'
                 'It is useful only in controlled diagnostics when you understand the risk.\n'
                 '\n'
                 'Do not make insecure verification the permanent fix.\n'
                 '\n'
                 'If curl fails verification but curl dash k succeeds, that strongly points to trust or '
                 'certificate validation rather than basic TCP reachability.\n'
                 '\n'
                 'Now SNI.\n'
                 '\n'
                 'Server Name Indication lets a TLS client indicate the hostname it is trying to reach '
                 'during the handshake.\n'
                 '\n'
                 'This allows one server IP to host multiple TLS certificates and virtual hosts.\n'
                 '\n'
                 'Modern HTTPS infrastructure relies heavily on this.\n'
                 '\n'
                 'The hostname matters even when several services share the same IP.\n'
                 '\n'
                 'Now reverse proxies.\n'
                 '\n'
                 'A reverse proxy such as nginx, HAProxy, Traefik, or a cloud load balancer accepts client '
                 'requests and forwards them to upstream applications.\n'
                 '\n'
                 'The proxy can terminate TLS.\n'
                 '\n'
                 'That means the client may establish HTTPS to the proxy while the proxy speaks HTTP or '
                 'HTTPS to the backend.\n'
                 '\n'
                 'This creates separate network legs.\n'
                 '\n'
                 'Client to proxy.\n'
                 '\n'
                 'Proxy to upstream.\n'
                 '\n'
                 'A 502 often indicates the first leg succeeded but the second leg failed.\n'
                 '\n'
                 'This is why architecture matters during troubleshooting.\n'
                 '\n'
                 'Now health checks.\n'
                 '\n'
                 'Applications often expose endpoints such as slash health or slash ready.\n'
                 '\n'
                 'A basic health endpoint may prove that the process responds.\n'
                 '\n'
                 'A readiness endpoint may prove that required dependencies are available.\n'
                 '\n'
                 'A load balancer might remove a target from rotation when checks fail.\n'
                 '\n'
                 'But health checks must be designed carefully.\n'
                 '\n'
                 'A health endpoint that always returns 200 even when the database is unavailable can create '
                 'misleading evidence.\n'
                 '\n'
                 'Now cookies and sessions.\n'
                 '\n'
                 'HTTP is stateless by design, but applications create state using cookies, tokens, and '
                 'server-side session stores.\n'
                 '\n'
                 'If only authenticated users fail while public endpoints work, basic networking may be fine '
                 'and the failure may involve identity or session state.\n'
                 '\n'
                 'Again, scope the symptom.\n'
                 '\n'
                 'Now browser versus curl.\n'
                 '\n'
                 'A browser introduces additional behavior such as caching, cookies, JavaScript, CORS, '
                 'service workers, proxy configuration, and certificate stores.\n'
                 '\n'
                 'curl is often useful because it provides a simpler client.\n'
                 '\n'
                 'If curl succeeds but the browser fails, that narrows the investigation.\n'
                 '\n'
                 'If both fail identically, the shared network or service path becomes more interesting.\n'
                 '\n'
                 'For the lab, you will inspect HTTP responses, redirects, headers, verbose TLS output, and '
                 'the distinction between transport success and application success.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'HTTP is request-response.\n'
                 '\n'
                 'Methods describe intended operations.\n'
                 '\n'
                 'Status codes are evidence.\n'
                 '\n'
                 'Headers carry important metadata.\n'
                 '\n'
                 'HTTPS is HTTP over TLS.\n'
                 '\n'
                 'TLS protects confidentiality, integrity, and server identity.\n'
                 '\n'
                 'Certificates prove identity only when clients verify them correctly.\n'
                 '\n'
                 'Reverse proxies create multiple network legs.\n'
                 '\n'
                 'And curl can show you exactly how far a request gets.\n'
                 '\n'
                 'In the next lesson, we will step down and outward into routing, gateways, NAT, and '
                 'firewalls.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Before we finish, remember that H T T P status codes are evidence about how far the '
                 'request traveled.\n'
                 '\n'
                 'A four-oh-four is very different from a connection timeout. A five-hundred is very '
                 'different from a T L S certificate error. A five-oh-two from a reverse proxy is different '
                 'again. If you receive an H T T P response, you have already proven that the request '
                 'reached an H T T P-speaking system.\n'
                 '\n'
                 'Use curl deliberately. First inspect the status and headers. Add verbosity when you need '
                 'connection or T L S detail. Separate transport success, T L S success, and H T T P '
                 'behavior instead of compressing them into one statement like, “the website is broken.”\n'
                 '\n'
                 'That separation is what makes H T T P troubleshooting predictable.',
 'objectives': ['Explain HTTP request/response structure, methods, headers, and status codes.',
                'Interpret common 2xx, 3xx, 4xx, and 5xx responses as evidence.',
                'Explain HTTPS as HTTP over TLS and describe certificate validation.',
                'Use curl to separate DNS, TCP, TLS, and HTTP evidence.',
                'Explain reverse proxies and why 502/503/504 often point to upstream problems.'],
 'content': [{'heading': 'HTTP is a request-response application protocol',
              'body': 'Clients send methods, targets, headers, and optional bodies. Servers answer with '
                      'status codes, headers, and optional bodies.'},
             {'heading': 'Status-code families indicate broad outcomes',
              'body': '2xx success, 3xx redirection, 4xx client/request problems, and 5xx server-side or '
                      'gateway failures.'},
             {'heading': 'Headers often explain behavior',
              'body': 'Content-Type, Authorization, Host, Location, Cache-Control, and other headers carry '
                      'metadata that can change how a request is processed.'},
             {'heading': 'HTTPS is HTTP over TLS',
              'body': 'TLS provides encryption, integrity, and server identity verification through '
                      'certificate validation.'},
             {'heading': 'Certificate failures are security evidence',
              'body': 'Expired, wrong-host, untrusted, or incomplete certificates should be investigated '
                      'rather than permanently bypassed.'},
             {'heading': 'Reverse proxies create multiple network legs',
              'body': 'A client may reach the proxy successfully while the proxy cannot reach or obtain a '
                      'valid response from the upstream application.'},
             {'heading': 'curl exposes layers',
              'body': 'Verbose curl output can show name resolution, TCP connection, TLS negotiation, '
                      'request headers, and final HTTP response.'},
             {'heading': 'HTTP sits above successful transport',
              'body': 'HTTP troubleshooting starts after lower layers have worked far enough. If you receive '
                      'an HTTP status code, you already have evidence that DNS, routing, transport, and '
                      'enough application handling succeeded to produce a response.'},
             {'heading': 'Read status codes as evidence',
              'body': 'A 404, 502, and 500 are not interchangeable failures. They indicate different '
                      'boundaries in the request path. A strong operator uses the code to decide where to '
                      'investigate next instead of treating every browser error as the same problem.'},
             {'heading': 'TLS is part of the application journey',
              'body': "HTTPS is not simply 'HTTP with a lock icon.' TLS establishes encryption and identity "
                      'before normal HTTP communication continues. Certificate names, trust chains, and '
                      'expiration dates are operational dependencies that can break otherwise healthy '
                      'applications.'}],
 'diagram': {'title': 'HTTP is a request-response application protocol',
             'description': 'Understand URLs, HTTP requests and responses, methods, headers, status codes, '
                            'HTTPS, TLS certificates, and how curl exposes whether a failure belongs to '
                            'HTTP, TLS, or an earlier networking layer.',
             'nodes': [{'label': 'HTTP is a request-response application protocol',
                        'detail': 'Clients send methods, targets, headers, and optional bodies. Servers '
                                  'answer with status codes, headers, and optional bodies.'},
                       {'label': 'Status-code families indicate broad outcomes',
                        'detail': '2xx success, 3xx redirection, 4xx client/request problems, and 5xx '
                                  'server-side or gateway failures.'},
                       {'label': 'Headers often explain behavior',
                        'detail': 'Content-Type, Authorization, Host, Location, Cache-Control, and other '
                                  'headers carry metadata that can change how a request is processed.'},
                       {'label': 'HTTPS is HTTP over TLS',
                        'detail': 'TLS provides encryption, integrity, and server identity verification '
                                  'through certificate validation.'},
                       {'label': 'Certificate failures are security evidence',
                        'detail': 'Expired, wrong-host, untrusted, or incomplete certificates should be '
                                  'investigated rather than permanently bypassed.'},
                       {'label': 'Reverse proxies create multiple network legs',
                        'detail': 'A client may reach the proxy successfully while the proxy cannot reach or '
                                  'obtain a valid response from the upstream application.'}],
             'caption': 'Follow the network path layer by layer and use evidence to locate the failing '
                        'boundary.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'Verbose curl output can show name resolution, TCP connection, TLS '
                                  'negotiation, request headers, and final HTTP response.'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and safe local tests. Explain what each result proves '
                              'before moving to the next layer.',
                     'steps': ['Create a Journal entry titled “Lesson 3.5 — HTTP and TLS.”',
                               'Run curl -I https://example.com and record the status line plus two response '
                               'headers.',
                               'Run curl -v https://example.com -o /dev/null and identify the points where '
                               'DNS, TCP, TLS, and HTTP each appear.',
                               'Write one example each of a 2xx, 3xx, 4xx, and 5xx status and explain what '
                               'it generally means.',
                               'Explain the difference between 401 and 403.',
                               'Explain what a 502 from a reverse proxy proves about the client-to-proxy '
                               'leg.'],
                     'takeaway': 'A networking command is useful only when it answers a specific question.'},
 'lab': {'title': 'Lesson 3.5 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.5 — HTTP and TLS.”',
                          'Run curl -I https://example.com and record the status line plus two response '
                          'headers.',
                          'Run curl -v https://example.com -o /dev/null and identify the points where DNS, '
                          'TCP, TLS, and HTTP each appear.',
                          'Write one example each of a 2xx, 3xx, 4xx, and 5xx status and explain what it '
                          'generally means.',
                          'Explain the difference between 401 and 403.',
                          'Explain what a 502 from a reverse proxy proves about the client-to-proxy leg.',
                          'Identify the hostname being verified by TLS in your curl request.',
                          'Write why using curl -k permanently would be a bad certificate fix.',
                          'Describe a client → reverse proxy → API architecture with separate network legs.',
                          'Explain how a health endpoint can mislead operators if it does not test important '
                          'dependencies.',
                          'Finish by describing why an HTTP 500 is evidence that DNS and transport succeeded '
                          'far enough to reach an application endpoint.']},
 'quiz': [{'question': 'What is HTTP?',
           'choices': ['A request-response application protocol',
                       'A routing protocol',
                       'A filesystem format',
                       'A Git transport only'],
           'correct': 0},
          {'question': 'Which method commonly retrieves data?',
           'choices': ['GET', 'DELETE', 'PATCH only', 'TLS'],
           'correct': 0},
          {'question': 'What do 2xx status codes broadly indicate?',
           'choices': ['Success', 'Redirection', 'Client errors', 'Server errors'],
           'correct': 0},
          {'question': 'What does 404 mean?',
           'choices': ['Resource not found', 'TLS certificate expired', 'TCP timeout', 'DNS NXDOMAIN'],
           'correct': 0},
          {'question': 'What does 502 commonly indicate?',
           'choices': ['A gateway/proxy could not get a valid upstream response',
                       'The client definitely has bad DNS',
                       'The certificate is always expired',
                       'The browser cache is full'],
           'correct': 0},
          {'question': 'What is HTTPS?',
           'choices': ['HTTP over TLS', 'HTTP over DNS', 'TCP without encryption', 'A different filesystem'],
           'correct': 0},
          {'question': 'What does TLS primarily provide?',
           'choices': ['Encryption, integrity, and identity verification',
                       'IP routing only',
                       'Git history',
                       'Process scheduling'],
           'correct': 0},
          {'question': 'Why is curl -k risky as a permanent fix?',
           'choices': ['It disables certificate verification',
                       'It disables TCP',
                       'It deletes cookies',
                       'It changes DNS TTL'],
           'correct': 0},
          {'question': 'What can curl -v help reveal?',
           'choices': ['DNS, TCP, TLS, and HTTP stages',
                       'Only file permissions',
                       'Only CPU load',
                       'Only Git remotes'],
           'correct': 0},
          {'question': 'If a server returns HTTP 500, what has probably already succeeded?',
           'choices': ['Enough DNS/routing/transport to reach the application endpoint',
                       'Nothing at all',
                       'Only local filesystem access',
                       'Only SSH'],
           'correct': 0}],
 'reflection': 'How would you use an HTTP status code and verbose curl output together to decide whether an '
               'outage belongs to the client, proxy, network path, TLS layer, or application?'}
