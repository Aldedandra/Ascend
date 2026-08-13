"""Module 3, Lesson 3: DNS: Names to Addresses."""

LESSON = {'id': '3-3',
 'title': 'DNS: Names to Addresses',
 'summary': 'Learn how DNS resolution works, what recursive and authoritative servers do, how records and '
            'TTLs behave, and how to diagnose name-resolution problems.',
 'duration_minutes': 70,
 'xp': 75,
 'audio_script': 'Welcome to Lesson 3.3: DNS, Names to Addresses.\n'
                 '\n'
                 'Humans prefer names. Networks route using addresses. DNS connects those worlds.\n'
                 '\n'
                 'DNS stands for Domain Name System. It is distributed and hierarchical, not one global '
                 'server.\n'
                 '\n'
                 'Applications normally ask a resolver for answers. The resolver may answer from cache or '
                 'locate authoritative information for the requested name.\n'
                 '\n'
                 'Authoritative DNS servers publish source-of-truth records for a zone. Recursive resolvers '
                 'answer clients and often cache results.\n'
                 '\n'
                 'DNS record types answer different questions.\n'
                 '\n'
                 'A records map names to IPv4 addresses.\n'
                 '\n'
                 'AAAA records map names to IPv6 addresses.\n'
                 '\n'
                 'CNAME records alias one name to another.\n'
                 '\n'
                 'MX records identify mail targets.\n'
                 '\n'
                 'TXT records store text and are used for verification and email-security purposes.\n'
                 '\n'
                 'NS records identify authoritative name servers.\n'
                 '\n'
                 'SOA records contain zone authority metadata.\n'
                 '\n'
                 'TTL means Time To Live. TTL influences how long a resolver may reuse a cached answer '
                 'before refreshing it.\n'
                 '\n'
                 'This explains why DNS changes can appear inconsistent temporarily. Authoritative data may '
                 'already be updated while clients still use previously cached answers.\n'
                 '\n'
                 'Applications can also be affected by local hosts files, search domains, VPN-scoped '
                 'resolvers, and platform resolver behavior.\n'
                 '\n'
                 'Corporate VPNs may provide internal DNS. Tailscale can provide MagicDNS. Other VPNs can '
                 'alter resolver choices. A hostname may intentionally resolve differently depending on '
                 'network context.\n'
                 '\n'
                 'dig is one of the best DNS diagnostic tools.\n'
                 '\n'
                 'dig example.com asks for DNS information.\n'
                 '\n'
                 'dig A example.com requests IPv4 address records.\n'
                 '\n'
                 'dig AAAA example.com requests IPv6 address records.\n'
                 '\n'
                 'dig +short example.com shows concise answer values.\n'
                 '\n'
                 'dig at a specific server lets you compare resolvers.\n'
                 '\n'
                 'DNS failures are not all the same.\n'
                 '\n'
                 'NXDOMAIN means the requested name is reported as nonexistent.\n'
                 '\n'
                 'SERVFAIL means the resolver could not successfully complete the query.\n'
                 '\n'
                 'Timeout means no usable DNS response arrived in time.\n'
                 '\n'
                 'A CNAME also adds another dependency. The alias may exist while its target is wrong or '
                 'unavailable.\n'
                 '\n'
                 'Most importantly, successful DNS does not prove application health.\n'
                 '\n'
                 'A hostname can resolve correctly while routing fails, a firewall blocks the port, TLS '
                 'fails, or the application returns HTTP 500.\n'
                 '\n'
                 'If dig succeeds but curl fails, move forward in the path instead of repeatedly changing '
                 'DNS.\n'
                 '\n'
                 'Ask which resolver answered. Ask what record type was requested. Ask what TTL applies. Ask '
                 'whether the application failure is actually later than DNS.\n'
                 '\n'
                 'That is DNS troubleshooting.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain recursive resolvers, authoritative servers, zones, and caching.',
                'Recognize A, AAAA, CNAME, MX, TXT, NS, and SOA records.',
                'Explain TTL and cache behavior.',
                'Use dig, nslookup, or host to gather DNS evidence.',
                'Distinguish NXDOMAIN, SERVFAIL, timeout, and later-layer application failure.'],
 'content': [{'heading': 'DNS is distributed',
              'body': 'Clients commonly ask recursive resolvers, while authoritative servers publish zone '
                      'data.'},
             {'heading': 'Record types answer different questions',
              'body': 'A and AAAA map to addresses; CNAME aliases; MX, TXT, NS, and SOA serve other '
                      'purposes.'},
             {'heading': 'TTL controls cache lifetime',
              'body': 'Different caches may retain old answers until their stored TTL expires.'},
             {'heading': 'Resolver context matters',
              'body': 'Hosts files, search domains, VPNs, and scoped resolvers can change which answer an '
                      'application receives.'},
             {'heading': 'dig asks focused DNS questions',
              'body': 'Query record types, use +short for concise output, or ask a specific resolver '
                      'directly.'},
             {'heading': 'DNS errors are distinct evidence',
              'body': 'NXDOMAIN, SERVFAIL, and timeout are different conditions with different next '
                      'questions.'},
             {'heading': 'DNS success is only one layer',
              'body': 'If DNS resolves but curl fails, investigate routing, transport, TLS, or application '
                      'behavior next.'}],
 'diagram': {'title': 'DNS is distributed',
             'description': 'Learn how DNS resolution works, what recursive and authoritative servers do, '
                            'how records and TTLs behave, and how to diagnose name-resolution problems.',
             'nodes': [{'label': 'DNS is distributed',
                        'detail': 'Clients commonly ask recursive resolvers, while authoritative servers '
                                  'publish zone data.'},
                       {'label': 'Record types answer different questions',
                        'detail': 'A and AAAA map to addresses; CNAME aliases; MX, TXT, NS, and SOA serve '
                                  'other purposes.'},
                       {'label': 'TTL controls cache lifetime',
                        'detail': 'Different caches may retain old answers until their stored TTL expires.'},
                       {'label': 'Resolver context matters',
                        'detail': 'Hosts files, search domains, VPNs, and scoped resolvers can change which '
                                  'answer an application receives.'},
                       {'label': 'dig asks focused DNS questions',
                        'detail': 'Query record types, use +short for concise output, or ask a specific '
                                  'resolver directly.'},
                       {'label': 'DNS errors are distinct evidence',
                        'detail': 'NXDOMAIN, SERVFAIL, and timeout are different conditions with different '
                                  'next questions.'}],
             'caption': 'Follow the path layer by layer and gather evidence before changing anything.'},
 'engineer_perspective': {'title': 'Engineer’s Perspective',
                          'body': 'If DNS resolves but curl fails, investigate routing, transport, TLS, or '
                                  'application behavior next.'},
 'try_it_yourself': {'title': 'Try It Yourself',
                     'intro': 'Use read-only commands and explain what each result proves.',
                     'steps': ['Create a Journal entry titled “Lesson 3.3 — DNS Evidence.”',
                               'Run dig example.com or nslookup example.com.',
                               'Query A records explicitly.',
                               'Query AAAA records explicitly.',
                               'Record at least one TTL if your tool shows it.',
                               'Use dig +short and compare it with the full response.'],
                     'takeaway': 'Choose commands because they answer specific questions.'},
 'lab': {'title': 'Lesson 3.3 Lab',
         'instructions': ['Create a Journal entry titled “Lesson 3.3 — DNS Evidence.”',
                          'Run dig example.com or nslookup example.com.',
                          'Query A records explicitly.',
                          'Query AAAA records explicitly.',
                          'Record at least one TTL if your tool shows it.',
                          'Use dig +short and compare it with the full response.',
                          'Identify your current resolver configuration using a platform-appropriate tool.',
                          'Run curl -I https://example.com.',
                          'Explain why the HTTP response proves more than DNS success.',
                          'Write the difference between NXDOMAIN, SERVFAIL, and timeout.',
                          'Create a hypothetical CNAME chain and explain how a broken target can break the '
                          'original name.']},
 'quiz': [{'question': 'What does DNS do?',
           'choices': ['Maps names to information such as addresses',
                       'Changes file ownership',
                       'Schedules CPU',
                       'Creates Git branches'],
           'correct': 0},
          {'question': 'Which record maps to IPv4?', 'choices': ['A', 'AAAA', 'MX', 'TXT'], 'correct': 0},
          {'question': 'Which record maps to IPv6?', 'choices': ['AAAA', 'A', 'NS', 'SOA'], 'correct': 0},
          {'question': 'What does CNAME do?',
           'choices': ['Aliases one name to another',
                       'Stores a TCP port',
                       'Creates a route',
                       'Encrypts HTTP'],
           'correct': 0},
          {'question': 'What does TTL affect?',
           'choices': ['DNS cache lifetime',
                       'TCP retransmission only',
                       'File permissions',
                       'SSH key lifetime'],
           'correct': 0},
          {'question': 'What does NXDOMAIN mean?',
           'choices': ['The requested name is reported nonexistent',
                       'The TCP port is closed',
                       'TLS succeeded',
                       'HTTP returned 500'],
           'correct': 0},
          {'question': 'What does SERVFAIL mean?',
           'choices': ['The resolver failed to complete the query',
                       'The name definitely exists',
                       'The app is healthy',
                       'The route is local'],
           'correct': 0},
          {'question': 'Why can clients see different answers after a DNS change?',
           'choices': ['Caches may expire at different times',
                       'DNS has no caching',
                       'All clients use one global cache',
                       'TCP rewrites DNS'],
           'correct': 0},
          {'question': 'Does DNS success prove the web service is healthy?',
           'choices': ['No', 'Yes', 'Only on IPv6', 'Only with CNAME'],
           'correct': 0},
          {'question': 'Why query a specific resolver?',
           'choices': ['To compare DNS answers between servers',
                       'To change filesystem routes',
                       'To restart DNS globally',
                       'To bypass IP'],
           'correct': 0}],
 'reflection': 'If a hostname resolves correctly for you but not for a coworker on VPN, what evidence would '
               'you gather before deciding where the failure is?'}
