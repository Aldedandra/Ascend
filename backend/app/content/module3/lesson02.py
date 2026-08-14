"""Module 3, Lesson 3-2: IP Addresses, Subnets & CIDR."""

LESSON = {'id': '3-2',
 'title': 'IP Addresses, Subnets & CIDR',
 'summary': 'Understand IPv4 addressing, private ranges, subnet prefixes, CIDR notation, gateways, and the '
            'practical question: is the destination local or routed?',
 'duration_minutes': 95,
 'xp': 75,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is IP Addresses, Subnets & CIDR.\n'
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
                 'First, Explain IPv4 addresses and CIDR prefixes. Also, Recognize private and special-use '
                 'IPv4 ranges. Also, Explain local versus routed destinations. Also, Explain default '
                 'gateways and route specificity. Also, Relate VPNs, containers, and cloud networks to '
                 'routing tables.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'Why addressing needs a boundary.\n'
                 '\n'
                 'An IPv4 address identifies an endpoint, but a host also needs to know which destinations '
                 'are directly reachable on its local network and which require routing. The CIDR prefix '
                 'supplies that boundary. In 192.168.10.25/24, the /24 says that the first 24 bits describe '
                 'the network portion. The remaining bits vary within that subnet.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'CIDR without turning into a subnet calculator.\n'
                 '\n'
                 'The most important early rule is counterintuitive: a larger prefix number means a smaller '
                 'subnet because fewer bits remain for addresses inside it. A /24 has 8 host bits and 256 '
                 'total IPv4 addresses. A /28 has 4 host bits and 16 total addresses. In real DevOps work '
                 'you can use calculators and tools for unusual prefixes; the goal is to understand what the '
                 'prefix means well enough to predict network boundaries and catch obviously wrong designs.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'Worked example: 192.168.10.25/24.\n'
                 '\n'
                 'With 192.168.10.25/24, the subnet is 192.168.10.0/24. A destination such as 192.168.10.80 '
                 'falls inside the same /24. A destination such as 192.168.11.80 does not. For the second '
                 'destination, the host needs a route that tells it where to send the packet next. This '
                 'simple local-versus-routed decision is the foundation beneath much larger cloud networks.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 "Private does not mean 'on my subnet'.\n"
                 '\n'
                 'The private IPv4 ranges are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. They are '
                 'intended for private networks rather than direct public Internet addressing. But two '
                 'private addresses are not automatically local to each other. 10.10.1.20/24 and '
                 '10.10.2.20/24 are both private while belonging to different /24 subnets. Communication '
                 'between them still needs routing.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 "The routing table is the operating system's decision.\n"
                 '\n'
                 'When an application sends traffic, the operating system compares the destination with '
                 'routes it knows. A more-specific matching route normally wins over a broader one. If '
                 'nothing more specific matches, the default route—often represented as 0.0.0.0/0—can '
                 'provide the next hop. This is why looking at the routing table is stronger evidence than '
                 "saying, “I'm connected to Wi-Fi, so it must be using Wi-Fi.”\n"
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 'What a gateway actually does.\n'
                 '\n'
                 'A gateway is a next-hop router used when the destination is not directly reachable on the '
                 'current local network. Your computer sends the frame to the gateway while keeping the '
                 'ultimate IP destination in the packet. The router then makes its own forwarding decision. '
                 'A packet can therefore cross many routed networks even though the application thinks only '
                 'in terms of its final destination.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'VPNs and Tailscale make route selection visible.\n'
                 '\n'
                 'VPN software can create a virtual interface and install routes for particular networks. '
                 'Tailscale does something similar for its overlay network. A specific VPN route can win '
                 'over your ordinary default route, causing only selected destinations to travel through the '
                 'tunnel. When an application works with the VPN disconnected but fails when it is '
                 'connected, compare routes before blaming the application or DNS.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'Containers introduce additional subnets.\n'
                 '\n'
                 'Docker commonly creates private bridge networks for containers. Containers receive '
                 'addresses from those networks, and Docker provides routing, name resolution, and sometimes '
                 'NAT or port publishing between network contexts. You usually should not hard-code a '
                 "container's temporary IP; service discovery gives you a stable name while networking "
                 'handles the changing endpoint underneath.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'This becomes AWS VPC networking later.\n'
                 '\n'
                 'An AWS VPC is not a completely new kind of networking. You will still choose CIDR ranges, '
                 'divide them into subnets, attach interfaces, inspect route tables, and decide where '
                 'traffic can go. Public and private subnets, Internet gateways, NAT gateways, peering, and '
                 'transit routing add architecture, but the local-or-routed mental model remains useful.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 'Predict the path before inspecting it.\n'
                 '\n'
                 'Choose a destination and make a prediction: Is it on-link or routed? Which interface '
                 'should be used? Is a VPN-specific route likely to win? Then inspect the actual route. On '
                 'Linux, ip route get DESTINATION is especially useful. On macOS, route -n get DESTINATION '
                 "exposes similar information. When your prediction differs from the operating system's "
                 'decision, you have found something worth investigating.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'One more practical point.\n'
                 '\n'
                 'A routing failure can look like an application failure.\n'
                 '\n'
                 'Suppose DNS correctly resolves api.ascend.internal, but curl simply times out. The '
                 'hostname may be perfect and the API may be healthy. If the client has no valid route to '
                 'the destination network—or a VPN installed the wrong route—the request may never reach the '
                 'server. This is why troubleshooting should move layer by layer rather than repeatedly '
                 'changing the first technology you recognize.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'Welcome to Lesson 3.2: IP Addresses, Subnets, and CIDR.\n'
                 '\n'
                 'The operational purpose of subnetting is not to turn you into a human subnet calculator. '
                 'It is to help you understand where an address belongs and how a host intends to reach it.\n'
                 '\n'
                 'IPv4 addresses are 32 bits, normally written as four decimal octets such as '
                 '192.168.10.25.\n'
                 '\n'
                 'An IPv4 address is interpreted together with a subnet mask or CIDR prefix. CIDR stands for '
                 'Classless Inter-Domain Routing.\n'
                 '\n'
                 'A prefix such as slash twenty-four means the first twenty-four bits identify the network '
                 'portion, leaving eight host bits.\n'
                 '\n'
                 'A larger prefix number means a smaller subnet. A smaller prefix number means a larger '
                 'subnet.\n'
                 '\n'
                 'Three major IPv4 ranges are reserved for private use: 10.0.0.0 slash eight, 172.16.0.0 '
                 'slash twelve, and 192.168.0.0 slash sixteen.\n'
                 '\n'
                 'Private does not mean secure. It means those addresses are reserved for internal use '
                 'rather than normal global internet routing. Security still depends on firewalls, routing, '
                 'identity, and application controls.\n'
                 '\n'
                 'Some addresses have special purposes. 127.0.0.0 slash eight is loopback. 169.254.0.0 slash '
                 'sixteen is link-local. 0.0.0.0 has context-dependent meanings, including wildcard bind '
                 'and, with slash zero, the default IPv4 route prefix.\n'
                 '\n'
                 'The most important operational question is local or remote.\n'
                 '\n'
                 'If your host is 192.168.1.50 slash twenty-four and the destination is 192.168.1.80, the '
                 'destination is in the same local subnet.\n'
                 '\n'
                 'If the destination is 10.20.30.40, the host needs a route toward another network, commonly '
                 'through a default gateway.\n'
                 '\n'
                 'The routing table is the source of truth for where the operating system intends to send '
                 'traffic. More-specific routes normally win over broader routes.\n'
                 '\n'
                 'VPNs can add routes. Tailscale creates interfaces and routes. Docker creates virtual '
                 'networks. Cloud platforms create virtual interfaces, subnets, and route tables.\n'
                 '\n'
                 'This is why private versus public is not the same question as local versus remote. Two '
                 'private addresses can be in different subnets and require routing.\n'
                 '\n'
                 'Subnets are also not automatically security boundaries. They organize addressing and '
                 'routing. Firewalls, security groups, ACLs, and application controls determine what is '
                 'permitted.\n'
                 '\n'
                 'IPv6 uses 128-bit addresses and different notation, but the same concepts transfer: '
                 'interfaces, prefixes, routes, DNS, and transport protocols.\n'
                 '\n'
                 'On Linux, ip addr and ip route provide direct evidence. On macOS, ifconfig and route -n '
                 'get can answer similar questions.\n'
                 '\n'
                 'Predict the path. Then ask the operating system to confirm it.\n'
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
 'objectives': ['Explain IPv4 addresses and CIDR prefixes.',
                'Recognize private and special-use IPv4 ranges.',
                'Explain local versus routed destinations.',
                'Explain default gateways and route specificity.',
                'Relate VPNs, containers, and cloud networks to routing tables.'],
 'content': [{'heading': 'Why addressing needs a boundary',
              'body': 'An IPv4 address identifies an endpoint, but a host also needs to know which '
                      'destinations are directly reachable on its local network and which require routing. '
                      'The CIDR prefix supplies that boundary. In 192.168.10.25/24, the /24 says that the '
                      'first 24 bits describe the network portion. The remaining bits vary within that '
                      'subnet.'},
             {'heading': 'CIDR without turning into a subnet calculator',
              'body': 'The most important early rule is counterintuitive: a larger prefix number means a '
                      'smaller subnet because fewer bits remain for addresses inside it. A /24 has 8 host '
                      'bits and 256 total IPv4 addresses. A /28 has 4 host bits and 16 total addresses. In '
                      'real DevOps work you can use calculators and tools for unusual prefixes; the goal is '
                      'to understand what the prefix means well enough to predict network boundaries and '
                      'catch obviously wrong designs.'},
             {'heading': 'Worked example: 192.168.10.25/24',
              'body': 'With 192.168.10.25/24, the subnet is 192.168.10.0/24. A destination such as '
                      '192.168.10.80 falls inside the same /24. A destination such as 192.168.11.80 does '
                      'not. For the second destination, the host needs a route that tells it where to send '
                      'the packet next. This simple local-versus-routed decision is the foundation beneath '
                      'much larger cloud networks.'},
             {'heading': "Private does not mean 'on my subnet'",
              'body': 'The private IPv4 ranges are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. They are '
                      'intended for private networks rather than direct public Internet addressing. But two '
                      'private addresses are not automatically local to each other. 10.10.1.20/24 and '
                      '10.10.2.20/24 are both private while belonging to different /24 subnets. '
                      'Communication between them still needs routing.'},
             {'heading': "The routing table is the operating system's decision",
              'body': 'When an application sends traffic, the operating system compares the destination with '
                      'routes it knows. A more-specific matching route normally wins over a broader one. If '
                      'nothing more specific matches, the default route—often represented as 0.0.0.0/0—can '
                      'provide the next hop. This is why looking at the routing table is stronger evidence '
                      "than saying, “I'm connected to Wi-Fi, so it must be using Wi-Fi.”"},
             {'heading': 'What a gateway actually does',
              'body': 'A gateway is a next-hop router used when the destination is not directly reachable on '
                      'the current local network. Your computer sends the frame to the gateway while keeping '
                      'the ultimate IP destination in the packet. The router then makes its own forwarding '
                      'decision. A packet can therefore cross many routed networks even though the '
                      'application thinks only in terms of its final destination.'},
             {'heading': 'VPNs and Tailscale make route selection visible',
              'body': 'VPN software can create a virtual interface and install routes for particular '
                      'networks. Tailscale does something similar for its overlay network. A specific VPN '
                      'route can win over your ordinary default route, causing only selected destinations to '
                      'travel through the tunnel. When an application works with the VPN disconnected but '
                      'fails when it is connected, compare routes before blaming the application or DNS.'},
             {'heading': 'Containers introduce additional subnets',
              'body': 'Docker commonly creates private bridge networks for containers. Containers receive '
                      'addresses from those networks, and Docker provides routing, name resolution, and '
                      'sometimes NAT or port publishing between network contexts. You usually should not '
                      "hard-code a container's temporary IP; service discovery gives you a stable name while "
                      'networking handles the changing endpoint underneath.'},
             {'heading': 'This becomes AWS VPC networking later',
              'body': 'An AWS VPC is not a completely new kind of networking. You will still choose CIDR '
                      'ranges, divide them into subnets, attach interfaces, inspect route tables, and decide '
                      'where traffic can go. Public and private subnets, Internet gateways, NAT gateways, '
                      'peering, and transit routing add architecture, but the local-or-routed mental model '
                      'remains useful.'},
             {'heading': 'Predict the path before inspecting it',
              'body': 'Choose a destination and make a prediction: Is it on-link or routed? Which interface '
                      'should be used? Is a VPN-specific route likely to win? Then inspect the actual route. '
                      'On Linux, ip route get DESTINATION is especially useful. On macOS, route -n get '
                      'DESTINATION exposes similar information. When your prediction differs from the '
                      "operating system's decision, you have found something worth investigating."},
             {'heading': 'A routing failure can look like an application failure',
              'body': 'Suppose DNS correctly resolves api.ascend.internal, but curl simply times out. The '
                      'hostname may be perfect and the API may be healthy. If the client has no valid route '
                      'to the destination network—or a VPN installed the wrong route—the request may never '
                      'reach the server. This is why troubleshooting should move layer by layer rather than '
                      'repeatedly changing the first technology you recognize.'}],
 'diagram': {'title': 'IPv4 addresses are 32 bits',
             'description': 'Understand IPv4 addressing, private ranges, subnet prefixes, CIDR notation, '
                            'gateways, and the practical question: is the destination local or routed?',
             'nodes': [{'label': 'IPv4 addresses are 32 bits',
                        'detail': 'Dotted-decimal notation represents four 8-bit octets.'},
                       {'label': 'CIDR defines the prefix length',
                        'detail': 'A /24 has 24 network bits. Larger prefix values describe smaller '
                                  'subnets.'},
                       {'label': 'Private ranges are reserved for internal use',
                        'detail': '10/8, 172.16/12, and 192.168/16 are private, but private addressing is '
                                  'not a security control.'},
                       {'label': 'Special ranges have special meaning',
                        'detail': '127/8 is loopback, 169.254/16 is link-local, and 0.0.0.0 has '
                                  'context-dependent meanings.'},
                       {'label': 'Local or remote depends on the prefix',
                        'detail': 'Hosts use address and prefix information to decide whether a destination '
                                  'is on-link or needs routing.'},
                       {'label': 'Default gateways forward toward other networks',
                        'detail': 'The routing table selects a matching route and next hop.'}],
             'caption': 'Follow the path layer by layer and gather evidence before changing anything.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'VPNs, Tailscale, Docker, and cloud networking can add routes that change '
                                  'the actual path.'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and explain what each result proves.',
                     'steps': ['Create a Journal entry titled “Lesson 3.2 — IP and Routing.”',
                               'Inspect your active interface addresses with ifconfig or ip addr.',
                               'Record one IPv4 address and its subnet/prefix.',
                               'Classify it as loopback, private, public, or another special range.',
                               'Find your default route with netstat -rn/route on macOS or ip route on '
                               'Linux.',
                               'Inspect the route to 8.8.8.8.'],
                     'takeaway': 'Choose commands because they answer specific questions.'},
 'lab': {'title': 'Lesson 3.2 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.2 — IP and Routing.”',
                          'Inspect your active interface addresses with ifconfig or ip addr.',
                          'Record one IPv4 address and its subnet/prefix.',
                          'Classify it as loopback, private, public, or another special range.',
                          'Find your default route with netstat -rn/route on macOS or ip route on Linux.',
                          'Inspect the route to 8.8.8.8.',
                          'Inspect the route to 127.0.0.1.',
                          'Explain what /24 means.',
                          'Explain why /28 is a smaller subnet than /24.',
                          'List the three private IPv4 ranges.',
                          'If a VPN or Tailscale route is present, explain how it can alter destination '
                          'routing.']},
 'quiz': [{'question': 'How many bits are in IPv4?', 'choices': ['32', '8', '64', '128'], 'correct': 0},
          {'question': 'What does /24 mean?',
           'choices': ['24 network-prefix bits', '24 ports', '24 routes', '24 DNS records'],
           'correct': 0},
          {'question': 'Which is private IPv4?',
           'choices': ['10.0.0.0/8', '8.8.8.0/24', '1.1.1.0/24', '224.0.0.0/4'],
           'correct': 0},
          {'question': 'What is 127.0.0.1?',
           'choices': ['Loopback', 'Public DNS', 'Default gateway everywhere', 'Broadcast only'],
           'correct': 0},
          {'question': 'What does a larger CIDR prefix mean?',
           'choices': ['Smaller subnet', 'Larger subnet', 'Faster network', 'Different protocol'],
           'correct': 0},
          {'question': 'What does a default gateway do?',
           'choices': ['Forward traffic toward non-local networks',
                       'Resolve DNS',
                       'Change permissions',
                       'Encrypt HTTP'],
           'correct': 0},
          {'question': 'Why can VPN software change connectivity?',
           'choices': ['It can add interfaces and routes',
                       'It changes UIDs',
                       'It removes ports',
                       'It disables DNS by definition'],
           'correct': 0},
          {'question': 'Are private addresses automatically secure?',
           'choices': ['No', 'Yes', 'Only on Linux', 'Only in AWS'],
           'correct': 0},
          {'question': 'Can two private addresses require routing between them?',
           'choices': ['Yes', 'No', 'Only with IPv6', 'Only with HTTP'],
           'correct': 0},
          {'question': 'What shows how the OS intends to reach a destination?',
           'choices': ['Routing table', 'Git history', 'File ownership', 'Shell aliases'],
           'correct': 0}],
 'reflection': 'How would you explain the difference between private addressing, local-subnet addressing, '
               'and remotely routed addressing?'}
