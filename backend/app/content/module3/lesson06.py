"""Module 3, Lesson 3-6: Routes, Gateways, NAT & Firewalls."""

LESSON = {'id': '3-6',
 'title': 'Routes, Gateways, NAT & Firewalls',
 'summary': 'Follow traffic across network boundaries using routing tables, gateways, NAT, ingress and '
            'egress policy, stateful firewalls, and the practical question: where is the packet being '
            'allowed, translated, or dropped?',
 'duration_minutes': 80,
 'xp': 85,
 'audio_script': 'Welcome to Lesson 3.6: Routes, Gateways, NAT, and Firewalls.\n'
                 '\n'
                 'You now understand addresses, ports, transport connections, HTTP, and TLS.\n'
                 '\n'
                 'The next question is how traffic moves between networks and where policy can allow or '
                 'block it.\n'
                 '\n'
                 'Start with routing.\n'
                 '\n'
                 'A host uses a routing table to decide where packets should go.\n'
                 '\n'
                 'Routes match destination prefixes.\n'
                 '\n'
                 'More-specific routes normally take precedence over broader ones.\n'
                 '\n'
                 'If no specific route matches, a default route such as 0.0.0.0 slash zero can catch the '
                 'destination.\n'
                 '\n'
                 'The route usually identifies an output interface and, when needed, a next-hop gateway.\n'
                 '\n'
                 'A gateway is a router that forwards traffic toward another network.\n'
                 '\n'
                 'Your laptop commonly sends internet-bound traffic to a local router.\n'
                 '\n'
                 'A cloud instance may send traffic to a virtual router in its subnet.\n'
                 '\n'
                 'A container may send traffic to a bridge gateway created by the container runtime.\n'
                 '\n'
                 'The details change. The model does not.\n'
                 '\n'
                 'Now forwarding.\n'
                 '\n'
                 'Routers receive packets on one interface and forward them out another according to routing '
                 'policy.\n'
                 '\n'
                 'A host can have a valid route and still fail if the next hop has no route onward.\n'
                 '\n'
                 'Routing is end-to-end.\n'
                 '\n'
                 'The source host’s route is only the first decision.\n'
                 '\n'
                 'Now NAT.\n'
                 '\n'
                 'NAT stands for Network Address Translation.\n'
                 '\n'
                 'NAT modifies network address information as traffic crosses a boundary.\n'
                 '\n'
                 'The most familiar home example is source NAT.\n'
                 '\n'
                 'Many private devices share one public IPv4 address.\n'
                 '\n'
                 'Outbound connections have their private source addresses translated to the router’s public '
                 'address, along with port mapping information so return traffic can be associated with the '
                 'correct internal flow.\n'
                 '\n'
                 'This behavior is often called PAT or port address translation in addition to NAT '
                 'terminology.\n'
                 '\n'
                 'Cloud environments use NAT gateways and similar services so private instances can initiate '
                 'internet connections without being directly reachable from the public internet.\n'
                 '\n'
                 'Destination NAT works in the other direction.\n'
                 '\n'
                 'A public address and port can be translated to an internal address and port.\n'
                 '\n'
                 'Docker port publishing is conceptually similar from the operator’s perspective: host port '
                 '8080 can direct traffic to container port 8000.\n'
                 '\n'
                 'NAT changes addressing.\n'
                 '\n'
                 'It does not automatically equal security.\n'
                 '\n'
                 'A NAT device may be combined with firewall behavior, but keep the concepts distinct.\n'
                 '\n'
                 'Now firewalls.\n'
                 '\n'
                 'A firewall evaluates traffic against rules and decides whether to allow, reject, or drop '
                 'it.\n'
                 '\n'
                 'Rules can consider source address, destination address, protocol, source port, destination '
                 'port, interface, connection state, and other metadata.\n'
                 '\n'
                 'Ingress means traffic entering a system or boundary.\n'
                 '\n'
                 'Egress means traffic leaving.\n'
                 '\n'
                 'Cloud security groups, network ACLs, host firewalls, load balancers, and corporate '
                 'firewalls can all apply policy at different boundaries.\n'
                 '\n'
                 'This means one end-to-end connection may cross several policy layers.\n'
                 '\n'
                 'Your laptop firewall.\n'
                 '\n'
                 'Your home or corporate gateway.\n'
                 '\n'
                 'A VPN policy.\n'
                 '\n'
                 'A cloud security group.\n'
                 '\n'
                 'A subnet ACL.\n'
                 '\n'
                 'The destination host firewall.\n'
                 '\n'
                 'A reverse proxy policy.\n'
                 '\n'
                 'When troubleshooting, do not ask, quote, is the firewall open?\n'
                 '\n'
                 'Ask which firewall, on which boundary, in which direction, for which protocol and port, '
                 'from which source to which destination.\n'
                 '\n'
                 'Now stateful firewalls.\n'
                 '\n'
                 'A stateful firewall tracks connection state.\n'
                 '\n'
                 'If an outbound TCP connection is allowed, return traffic associated with that established '
                 'connection can normally be permitted automatically.\n'
                 '\n'
                 'You do not necessarily need a separate inbound rule for the ephemeral client port.\n'
                 '\n'
                 'This is a critical distinction from purely stateless filtering.\n'
                 '\n'
                 'Many host firewalls and cloud security groups are stateful.\n'
                 '\n'
                 'Network ACLs in some cloud platforms may be stateless and require explicit consideration '
                 'of both directions.\n'
                 '\n'
                 'You will learn AWS-specific behavior in Module 6.\n'
                 '\n'
                 'Now allow versus reject versus drop.\n'
                 '\n'
                 'An allow rule permits traffic.\n'
                 '\n'
                 'A reject rule actively tells the sender the traffic is not accepted.\n'
                 '\n'
                 'A drop rule silently discards it.\n'
                 '\n'
                 'From the client perspective, reject may produce a fast failure, while drop often looks '
                 'like a timeout.\n'
                 '\n'
                 'Again, error behavior is evidence.\n'
                 '\n'
                 'Now routing versus firewall.\n'
                 '\n'
                 'A timeout can be caused by either.\n'
                 '\n'
                 'If the source has no route, the local host may report network unreachable.\n'
                 '\n'
                 'If a router drops traffic, the client may time out.\n'
                 '\n'
                 'If a firewall silently drops traffic, the result can look similar.\n'
                 '\n'
                 'You need multiple pieces of evidence.\n'
                 '\n'
                 'Route lookup.\n'
                 '\n'
                 'Traceroute.\n'
                 '\n'
                 'Firewall rules.\n'
                 '\n'
                 'Packet capture when appropriate.\n'
                 '\n'
                 'Server-side logs.\n'
                 '\n'
                 'Listener state.\n'
                 '\n'
                 'Now traceroute.\n'
                 '\n'
                 'Traceroute attempts to reveal hops along a network path by manipulating packet TTL or '
                 'hop-limit behavior and observing responses.\n'
                 '\n'
                 'It can be useful, but it is not perfect.\n'
                 '\n'
                 'Some routers do not respond.\n'
                 '\n'
                 'Firewalls may block traceroute probes.\n'
                 '\n'
                 'Different traffic types can take different paths.\n'
                 '\n'
                 'A missing hop does not automatically mean the network breaks there.\n'
                 '\n'
                 'Use traceroute as evidence, not absolute truth.\n'
                 '\n'
                 'On macOS, traceroute is commonly available.\n'
                 '\n'
                 'On Linux, traceroute or tracepath may be available.\n'
                 '\n'
                 'Now ping.\n'
                 '\n'
                 'Ping uses ICMP echo messages.\n'
                 '\n'
                 'A successful ping proves something about ICMP reachability.\n'
                 '\n'
                 'A failed ping does not prove the host is down because ICMP may be filtered.\n'
                 '\n'
                 'A server can block ping while HTTPS works perfectly.\n'
                 '\n'
                 'Do not use ping as your only network test.\n'
                 '\n'
                 'Now imagine a cloud-style scenario.\n'
                 '\n'
                 'The Ascend API runs on a private VM.\n'
                 '\n'
                 'The load balancer is public.\n'
                 '\n'
                 'Users connect to the load balancer on TCP 443.\n'
                 '\n'
                 'The load balancer forwards to the API on TCP 8000.\n'
                 '\n'
                 'The API must allow traffic from the load balancer’s network or security identity.\n'
                 '\n'
                 'The API may initiate outbound connections to PostgreSQL on 5432.\n'
                 '\n'
                 'The database may accept only traffic from the API layer.\n'
                 '\n'
                 'Each leg has its own routing and policy.\n'
                 '\n'
                 'If users receive 502, you ask whether the load balancer can reach the API.\n'
                 '\n'
                 'If the API logs database timeout errors, you ask about the API-to-database route and '
                 'firewall.\n'
                 '\n'
                 'This is how layered architecture turns into layered network policy.\n'
                 '\n'
                 'Now local tools.\n'
                 '\n'
                 'On Linux, ip route shows routing.\n'
                 '\n'
                 'ip route get asks for the effective route to one destination.\n'
                 '\n'
                 'Host firewalls may use nftables, iptables, firewalld, or ufw depending on the system.\n'
                 '\n'
                 'On macOS, pf is the native packet filter, and the system firewall provides '
                 'application-level controls.\n'
                 '\n'
                 'Do not modify firewall rules casually in this lesson.\n'
                 '\n'
                 'Inspection and reasoning are enough.\n'
                 '\n'
                 'Now security principle.\n'
                 '\n'
                 'Default deny is a common network-security approach.\n'
                 '\n'
                 'Instead of allowing everything and blocking known bad traffic, allow only the flows that '
                 'are required.\n'
                 '\n'
                 'That is networking’s version of least privilege.\n'
                 '\n'
                 'If an API only needs database access on TCP 5432, it does not need unrestricted access to '
                 'every port.\n'
                 '\n'
                 'If a public load balancer is the only intended entry point to a private API, the API does '
                 'not need direct public exposure.\n'
                 '\n'
                 'This reduces blast radius.\n'
                 '\n'
                 'For the lab, you will map a hypothetical Ascend architecture and inspect your current '
                 'routes without changing firewall or NAT configuration.\n'
                 '\n'
                 'The goal is to learn to ask:\n'
                 '\n'
                 'What is the source?\n'
                 '\n'
                 'What is the destination?\n'
                 '\n'
                 'What protocol and port?\n'
                 '\n'
                 'What route is used?\n'
                 '\n'
                 'What gateway or translation occurs?\n'
                 '\n'
                 'Which policy boundaries are crossed?\n'
                 '\n'
                 'What evidence proves where the flow stops?\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'Routes decide where traffic should go.\n'
                 '\n'
                 'Gateways forward traffic between networks.\n'
                 '\n'
                 'NAT translates addressing.\n'
                 '\n'
                 'Firewalls enforce policy.\n'
                 '\n'
                 'Ingress and egress describe direction.\n'
                 '\n'
                 'Stateful filtering tracks connections.\n'
                 '\n'
                 'Drop and reject produce different client behavior.\n'
                 '\n'
                 'Ping and traceroute are useful but limited.\n'
                 '\n'
                 'And end-to-end networking means every leg of the path must have valid routing and '
                 'permitted policy.\n'
                 '\n'
                 'In the next lesson, we will combine these tools into a structured network troubleshooting '
                 'workflow.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Before we finish, turn every network-policy question into a precise flow.\n'
                 '\n'
                 'State the source. State the destination. State the protocol and port. Then identify the '
                 'route and the policy boundaries that evaluate that traffic.\n'
                 '\n'
                 'For example, instead of saying, “the database firewall might be blocking it,” say, “the A '
                 'P I workload needs to initiate T C P traffic to the database on port fifty-four '
                 'thirty-two, and I need to identify which route and security rule govern that leg.”\n'
                 '\n'
                 'Precision makes troubleshooting faster and security safer. It also prepares you for cloud '
                 'networking, where route tables, security groups, network A C Ls, gateways, and load '
                 'balancers are still expressions of the same underlying path.',
 'objectives': ['Explain routing tables, gateways, and route specificity.',
                'Explain source NAT, destination NAT, and port translation conceptually.',
                'Distinguish routing from firewall policy.',
                'Explain ingress, egress, stateful filtering, allow/reject/drop, and default deny.',
                'Map an end-to-end application flow across multiple routing and policy boundaries.'],
 'content': [{'heading': 'Routing decides where packets should go',
              'body': 'Hosts and routers match destination prefixes and select interfaces or next-hop '
                      'gateways.'},
             {'heading': 'Gateways connect networks',
              'body': 'A gateway forwards traffic beyond the local subnet toward other destinations.'},
             {'heading': 'NAT rewrites addressing information',
              'body': 'Source NAT commonly lets private clients share public connectivity; destination NAT '
                      'can direct public endpoints toward internal services.'},
             {'heading': 'Firewalls enforce communication policy',
              'body': 'Rules can match addresses, ports, protocols, interfaces, and connection state.'},
             {'heading': 'Stateful firewalls understand established flows',
              'body': 'Return traffic for an allowed outbound connection can be recognized as part of the '
                      'same stateful session.'},
             {'heading': 'Drop and reject behave differently',
              'body': 'A reject produces an explicit failure; a silent drop commonly appears as timeout.'},
             {'heading': 'End-to-end paths cross multiple boundaries',
              'body': 'A working application path may require routing, NAT, and firewall permission at '
                      'several different network layers.'},
             {'heading': 'Every network boundary is a decision point',
              'body': 'As traffic moves from a laptop to a cloud service or from a load balancer to an '
                      'application server, it crosses boundaries. Each boundary can route, translate, allow, '
                      'deny, or drop traffic.'},
             {'heading': 'Security controls should be specific questions',
              'body': "Instead of asking 'is the firewall open?', ask: what source is connecting, what "
                      'destination is required, what protocol and port are involved, and which security '
                      'boundary evaluates that traffic? Precision leads to faster troubleshooting.'},
             {'heading': 'Follow the packet, not assumptions',
              'body': 'A working route on the client does not guarantee end-to-end success. The next hop, '
                      'NAT behavior, firewall rules, and destination service all participate in the final '
                      'outcome.'}],
 'diagram': {'title': 'Routing decides where packets should go',
             'description': 'Follow traffic across network boundaries using routing tables, gateways, NAT, '
                            'ingress and egress policy, stateful firewalls, and the practical question: '
                            'where is the packet being allowed, translated, or dropped?',
             'nodes': [{'label': 'Routing decides where packets should go',
                        'detail': 'Hosts and routers match destination prefixes and select interfaces or '
                                  'next-hop gateways.'},
                       {'label': 'Gateways connect networks',
                        'detail': 'A gateway forwards traffic beyond the local subnet toward other '
                                  'destinations.'},
                       {'label': 'NAT rewrites addressing information',
                        'detail': 'Source NAT commonly lets private clients share public connectivity; '
                                  'destination NAT can direct public endpoints toward internal services.'},
                       {'label': 'Firewalls enforce communication policy',
                        'detail': 'Rules can match addresses, ports, protocols, interfaces, and connection '
                                  'state.'},
                       {'label': 'Stateful firewalls understand established flows',
                        'detail': 'Return traffic for an allowed outbound connection can be recognized as '
                                  'part of the same stateful session.'},
                       {'label': 'Drop and reject behave differently',
                        'detail': 'A reject produces an explicit failure; a silent drop commonly appears as '
                                  'timeout.'}],
             'caption': 'Follow the network path layer by layer and use evidence to locate the failing '
                        'boundary.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'A working application path may require routing, NAT, and firewall '
                                  'permission at several different network layers.'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and safe local tests. Explain what each result proves '
                              'before moving to the next layer.',
                     'steps': ['Create a Journal entry titled “Lesson 3.6 — Routes, NAT and Firewalls.”',
                               'Inspect your default route using a platform-appropriate command.',
                               'Inspect the route to 8.8.8.8 and record the selected interface and gateway '
                               'if shown.',
                               'Run traceroute example.com or another safe destination and record several '
                               'hops. Note that missing responses are not automatically failures.',
                               'Run ping against a safe host and explain what success or failure does and '
                               'does not prove.',
                               'Draw a hypothetical path: Browser → public load balancer:443 → private '
                               'API:8000 → PostgreSQL:5432.'],
                     'takeaway': 'A networking command is useful only when it answers a specific question.'},
 'lab': {'title': 'Lesson 3.6 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.6 — Routes, NAT and Firewalls.”',
                          'Inspect your default route using a platform-appropriate command.',
                          'Inspect the route to 8.8.8.8 and record the selected interface and gateway if '
                          'shown.',
                          'Run traceroute example.com or another safe destination and record several hops. '
                          'Note that missing responses are not automatically failures.',
                          'Run ping against a safe host and explain what success or failure does and does '
                          'not prove.',
                          'Draw a hypothetical path: Browser → public load balancer:443 → private API:8000 → '
                          'PostgreSQL:5432.',
                          'For each leg, write source, destination, protocol, and destination port.',
                          'Mark where routing decisions occur.',
                          'Mark one place NAT could occur.',
                          'Mark one firewall/security-policy boundary on each leg.',
                          'Explain how a silent drop could look different from an active reject.',
                          'Finish by describing why default-deny network policy is analogous to least '
                          'privilege.']},
 'quiz': [{'question': 'What does a routing table do?',
           'choices': ['Select how packets should reach destination prefixes',
                       'Resolve DNS only',
                       'Assign file permissions',
                       'Encrypt HTTP'],
           'correct': 0},
          {'question': 'What is a gateway?',
           'choices': ['A router that forwards traffic between networks',
                       'A DNS record type',
                       'A shell process',
                       'A Git server'],
           'correct': 0},
          {'question': 'What does NAT do?',
           'choices': ['Translate network address information',
                       'Encrypt TLS certificates',
                       'Create UIDs',
                       'Resolve hostnames'],
           'correct': 0},
          {'question': 'What is source NAT commonly used for?',
           'choices': ['Letting private clients share translated outbound connectivity',
                       'Creating DNS zones',
                       'Listening on ports',
                       'Serving HTTP bodies'],
           'correct': 0},
          {'question': 'What does ingress mean?',
           'choices': ['Traffic entering a system or boundary',
                       'Traffic leaving only',
                       'DNS cache expiration',
                       'Process startup'],
           'correct': 0},
          {'question': 'What does egress mean?',
           'choices': ['Traffic leaving a system or boundary',
                       'Traffic entering only',
                       'TCP handshake',
                       'TLS identity'],
           'correct': 0},
          {'question': 'What is a stateful firewall?',
           'choices': ['A firewall that tracks connection state',
                       'A firewall that cannot see ports',
                       'A DNS resolver',
                       'A route table'],
           'correct': 0},
          {'question': 'How does silent drop often appear to a client?',
           'choices': ['Timeout', 'HTTP 200', 'Immediate success', 'DNS CNAME'],
           'correct': 0},
          {'question': 'Does failed ping prove a host is down?',
           'choices': ['No, ICMP may be filtered', 'Yes, always', 'Only on IPv6', 'Only in Docker'],
           'correct': 0},
          {'question': 'What principle does default deny resemble?',
           'choices': ['Least privilege', 'Eventual consistency', 'Load balancing', 'Git rebasing'],
           'correct': 0}],
 'reflection': 'How would you trace one failed application request across routing, NAT, firewall, transport, '
               'and application boundaries without changing anything first?'}
