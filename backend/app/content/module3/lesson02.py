"""Module 3, Lesson 2: IP Addresses, Subnets & CIDR."""

LESSON = {'id': '3-2',
 'title': 'IP Addresses, Subnets & CIDR',
 'summary': 'Understand IPv4 addressing, private ranges, subnet prefixes, CIDR notation, gateways, and the '
            'practical question: is the destination local or routed?',
 'duration_minutes': 75,
 'xp': 75,
 'audio_script': 'Welcome to Lesson 3.2: IP Addresses, Subnets, and CIDR.\n'
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
                 'Keep climbing.',
 'objectives': ['Explain IPv4 addresses and CIDR prefixes.',
                'Recognize private and special-use IPv4 ranges.',
                'Explain local versus routed destinations.',
                'Explain default gateways and route specificity.',
                'Relate VPNs, containers, and cloud networks to routing tables.'],
 'content': [{'heading': 'IPv4 addresses are 32 bits',
              'body': 'Dotted-decimal notation represents four 8-bit octets.'},
             {'heading': 'CIDR defines the prefix length',
              'body': 'A /24 has 24 network bits. Larger prefix values describe smaller subnets.'},
             {'heading': 'Private ranges are reserved for internal use',
              'body': '10/8, 172.16/12, and 192.168/16 are private, but private addressing is not a security '
                      'control.'},
             {'heading': 'Special ranges have special meaning',
              'body': '127/8 is loopback, 169.254/16 is link-local, and 0.0.0.0 has context-dependent '
                      'meanings.'},
             {'heading': 'Local or remote depends on the prefix',
              'body': 'Hosts use address and prefix information to decide whether a destination is on-link '
                      'or needs routing.'},
             {'heading': 'Default gateways forward toward other networks',
              'body': 'The routing table selects a matching route and next hop.'},
             {'heading': 'The routing table beats intuition',
              'body': 'VPNs, Tailscale, Docker, and cloud networking can add routes that change the actual '
                      'path.'}],
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
