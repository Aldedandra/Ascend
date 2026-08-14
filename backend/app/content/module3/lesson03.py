"""Module 3, Lesson 3-3: DNS: Names to Addresses."""

LESSON = {'id': '3-3',
 'title': 'DNS: Names to Addresses',
 'summary': 'Learn how DNS resolution works, what recursive and authoritative servers do, how records and '
            'TTLs behave, and how to diagnose name-resolution problems.',
 'duration_minutes': 95,
 'xp': 75,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is DNS: Names to Addresses.\n'
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
                 'First, Explain recursive resolvers, authoritative servers, zones, and caching. Also, '
                 'Recognize A, AAAA, CNAME, MX, TXT, NS, and SOA records. Also, Explain TTL and cache '
                 'behavior. Also, Use dig, nslookup, or host to gather DNS evidence. Also, Distinguish '
                 'NXDOMAIN, SERVFAIL, timeout, and later-layer application failure.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'What DNS contributes to an application request.\n'
                 '\n'
                 'Applications prefer names such as api.example.com because names can remain stable while '
                 'infrastructure changes. DNS supplies information associated with those names. For web '
                 'traffic, that often means finding an IPv4 or IPv6 address, but DNS also publishes aliases, '
                 'mail destinations, ownership and verification data, and information about which servers '
                 'are authoritative for a zone.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'What happens when you type a URL.\n'
                 '\n'
                 'Suppose you request https://api.example.com/health. Before an HTTPS connection can begin, '
                 'the client needs an address for api.example.com unless one is already cached or supplied '
                 'locally. The operating system and resolver configuration determine where that question '
                 'goes. Once an address is available, DNS has completed its immediate job and the request '
                 'moves on to routing, TCP, TLS, and HTTP. DNS success is therefore one step in the path, '
                 'not proof that the application works.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'Recursive resolvers and authoritative servers.\n'
                 '\n'
                 'Your device usually asks a recursive resolver rather than contacting every DNS authority '
                 'itself. The resolver may answer from cache or follow the DNS hierarchy until it reaches '
                 'authoritative information for the requested zone. Authoritative servers publish the '
                 'source-of-truth records for that zone. During troubleshooting, it matters whether you are '
                 'looking at a cached recursive answer or the current authoritative data.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 'A conceptual lookup through the hierarchy.\n'
                 '\n'
                 'For api.example.com, a resolver can begin with knowledge of DNS root servers, learn where '
                 'the .com top-level domain is served, discover the authoritative name servers for '
                 'example.com, and finally ask for api.example.com. In practice, caching means most lookups '
                 'do not repeat the entire chain. The hierarchy is useful because no single DNS server needs '
                 'to contain every record on the Internet.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 'Record types answer different questions.\n'
                 '\n'
                 'An A record maps a name to IPv4. AAAA maps a name to IPv6. CNAME creates an alias to '
                 'another name. MX identifies mail destinations. TXT is commonly used for ownership '
                 'verification and email-security policies. NS identifies authoritative name servers, and '
                 'SOA carries zone authority and timing information. When using dig, explicitly requesting a '
                 'record type makes your question clearer.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 "TTL and the reality behind 'DNS propagation'.\n"
                 '\n'
                 "A DNS record's TTL tells caching resolvers how long they may reuse an answer. Imagine "
                 'api.example.com changed from 192.0.2.10 to 192.0.2.20. A resolver that cached the old '
                 'answer shortly before the change can continue returning it until the remaining TTL '
                 'expires, while another resolver may already return the new address. What people call '
                 'propagation is often a period in which caches expire at different times.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'Your resolver context can change the answer.\n'
                 '\n'
                 'DNS behavior is not determined only by public authoritative records. A hosts file can '
                 'override a name locally. Search domains can expand short names. A corporate VPN can '
                 'install scoped resolvers. Split DNS can intentionally return internal answers to internal '
                 'clients and different answers externally. Tailscale MagicDNS can provide names inside a '
                 'tailnet. Two machines can therefore disagree without either result being random.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'How to read dig as evidence.\n'
                 '\n'
                 'Do not stop after spotting an IP address. Read the status to see whether the query '
                 'succeeded or returned a condition such as NXDOMAIN. Confirm the QUESTION section so you '
                 'know exactly what was asked. Inspect the ANSWER records and TTLs. Finally, note the SERVER '
                 'line because it identifies the resolver that answered your query. These details make DNS '
                 'troubleshooting reproducible.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'NXDOMAIN, SERVFAIL, timeout, and wrong answers are different.\n'
                 '\n'
                 'NXDOMAIN means the resolver is reporting that the requested name does not exist in DNS as '
                 'queried. SERVFAIL means the resolver could not successfully complete the lookup and can '
                 'have causes such as upstream or DNSSEC problems. A DNS timeout means you did not receive '
                 'an answer from the resolver in time. A syntactically successful answer pointing at the '
                 'wrong destination is a different class again. Treating all four as “DNS is broken” throws '
                 'away useful evidence.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 'Compare resolvers deliberately.\n'
                 '\n'
                 'When resolver behavior is suspicious, compare answers in a controlled way. You might query '
                 'your normal resolver and an appropriate public resolver for a public name, or inspect '
                 'authoritative data when you understand the zone. Record the server, answer, TTL, and time. '
                 'A difference can reveal caching or resolver context, but do not assume the public answer '
                 'should match an intentionally private split-DNS answer.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'One more practical point.\n'
                 '\n'
                 'Internal and external DNS are often intentionally different.\n'
                 '\n'
                 'A company may publish app.example.com to a public load balancer for Internet users while '
                 'internal clients resolve the same or a related name to a private endpoint. This design can '
                 'be valid. During an incident, always ask where the failing client is located and which '
                 'resolver it uses. “It works for me” from a different network may be evidence of split '
                 'behavior rather than proof that the reporter is wrong.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now bring these ideas together.\n'
                 '\n'
                 'DNS can be healthy while the application is broken.\n'
                 '\n'
                 'If api.ascend.internal resolves to the expected address but TCP to port 8000 times out, '
                 'the next investigation belongs to routing, filtering, reachability, or the service—not '
                 'repeated DNS flushing. If TCP and TLS succeed but HTTP returns 500, you have moved even '
                 'farther beyond DNS. Good troubleshooting advances when a layer is proven instead of '
                 'returning to it without new evidence.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'A practical DNS troubleshooting sequence.\n'
                 '\n'
                 'Capture the exact hostname first. Check local resolver context and whether the failure '
                 'affects one client or many. Query the relevant record and record status, answer, TTL, and '
                 'resolver. Compare another perspective only when it will answer a specific question. Once '
                 'the expected name resolves correctly, continue forward through route, port, TLS, HTTP, and '
                 'application behavior. DNS is one layer in the evidence chain.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'Welcome to Lesson 3.3: DNS, Names to Addresses.\n'
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
 'objectives': ['Explain recursive resolvers, authoritative servers, zones, and caching.',
                'Recognize A, AAAA, CNAME, MX, TXT, NS, and SOA records.',
                'Explain TTL and cache behavior.',
                'Use dig, nslookup, or host to gather DNS evidence.',
                'Distinguish NXDOMAIN, SERVFAIL, timeout, and later-layer application failure.'],
 'content': [{'heading': 'What DNS contributes to an application request',
              'body': 'Applications prefer names such as api.example.com because names can remain stable '
                      'while infrastructure changes. DNS supplies information associated with those names. '
                      'For web traffic, that often means finding an IPv4 or IPv6 address, but DNS also '
                      'publishes aliases, mail destinations, ownership and verification data, and '
                      'information about which servers are authoritative for a zone.'},
             {'heading': 'What happens when you type a URL',
              'body': 'Suppose you request https://api.example.com/health. Before an HTTPS connection can '
                      'begin, the client needs an address for api.example.com unless one is already cached '
                      'or supplied locally. The operating system and resolver configuration determine where '
                      'that question goes. Once an address is available, DNS has completed its immediate job '
                      'and the request moves on to routing, TCP, TLS, and HTTP. DNS success is therefore one '
                      'step in the path, not proof that the application works.'},
             {'heading': 'Recursive resolvers and authoritative servers',
              'body': 'Your device usually asks a recursive resolver rather than contacting every DNS '
                      'authority itself. The resolver may answer from cache or follow the DNS hierarchy '
                      'until it reaches authoritative information for the requested zone. Authoritative '
                      'servers publish the source-of-truth records for that zone. During troubleshooting, it '
                      'matters whether you are looking at a cached recursive answer or the current '
                      'authoritative data.'},
             {'heading': 'A conceptual lookup through the hierarchy',
              'body': 'For api.example.com, a resolver can begin with knowledge of DNS root servers, learn '
                      'where the .com top-level domain is served, discover the authoritative name servers '
                      'for example.com, and finally ask for api.example.com. In practice, caching means most '
                      'lookups do not repeat the entire chain. The hierarchy is useful because no single DNS '
                      'server needs to contain every record on the Internet.'},
             {'heading': 'Record types answer different questions',
              'body': 'An A record maps a name to IPv4. AAAA maps a name to IPv6. CNAME creates an alias to '
                      'another name. MX identifies mail destinations. TXT is commonly used for ownership '
                      'verification and email-security policies. NS identifies authoritative name servers, '
                      'and SOA carries zone authority and timing information. When using dig, explicitly '
                      'requesting a record type makes your question clearer.'},
             {'heading': "TTL and the reality behind 'DNS propagation'",
              'body': "A DNS record's TTL tells caching resolvers how long they may reuse an answer. Imagine "
                      'api.example.com changed from 192.0.2.10 to 192.0.2.20. A resolver that cached the old '
                      'answer shortly before the change can continue returning it until the remaining TTL '
                      'expires, while another resolver may already return the new address. What people call '
                      'propagation is often a period in which caches expire at different times.'},
             {'heading': 'Your resolver context can change the answer',
              'body': 'DNS behavior is not determined only by public authoritative records. A hosts file can '
                      'override a name locally. Search domains can expand short names. A corporate VPN can '
                      'install scoped resolvers. Split DNS can intentionally return internal answers to '
                      'internal clients and different answers externally. Tailscale MagicDNS can provide '
                      'names inside a tailnet. Two machines can therefore disagree without either result '
                      'being random.'},
             {'heading': 'How to read dig as evidence',
              'body': 'Do not stop after spotting an IP address. Read the status to see whether the query '
                      'succeeded or returned a condition such as NXDOMAIN. Confirm the QUESTION section so '
                      'you know exactly what was asked. Inspect the ANSWER records and TTLs. Finally, note '
                      'the SERVER line because it identifies the resolver that answered your query. These '
                      'details make DNS troubleshooting reproducible.'},
             {'heading': 'NXDOMAIN, SERVFAIL, timeout, and wrong answers are different',
              'body': 'NXDOMAIN means the resolver is reporting that the requested name does not exist in '
                      'DNS as queried. SERVFAIL means the resolver could not successfully complete the '
                      'lookup and can have causes such as upstream or DNSSEC problems. A DNS timeout means '
                      'you did not receive an answer from the resolver in time. A syntactically successful '
                      'answer pointing at the wrong destination is a different class again. Treating all '
                      'four as “DNS is broken” throws away useful evidence.'},
             {'heading': 'Compare resolvers deliberately',
              'body': 'When resolver behavior is suspicious, compare answers in a controlled way. You might '
                      'query your normal resolver and an appropriate public resolver for a public name, or '
                      'inspect authoritative data when you understand the zone. Record the server, answer, '
                      'TTL, and time. A difference can reveal caching or resolver context, but do not assume '
                      'the public answer should match an intentionally private split-DNS answer.'},
             {'heading': 'Internal and external DNS are often intentionally different',
              'body': 'A company may publish app.example.com to a public load balancer for Internet users '
                      'while internal clients resolve the same or a related name to a private endpoint. This '
                      'design can be valid. During an incident, always ask where the failing client is '
                      'located and which resolver it uses. “It works for me” from a different network may be '
                      'evidence of split behavior rather than proof that the reporter is wrong.'},
             {'heading': 'DNS can be healthy while the application is broken',
              'body': 'If api.ascend.internal resolves to the expected address but TCP to port 8000 times '
                      'out, the next investigation belongs to routing, filtering, reachability, or the '
                      'service—not repeated DNS flushing. If TCP and TLS succeed but HTTP returns 500, you '
                      'have moved even farther beyond DNS. Good troubleshooting advances when a layer is '
                      'proven instead of returning to it without new evidence.'},
             {'heading': 'A practical DNS troubleshooting sequence',
              'body': 'Capture the exact hostname first. Check local resolver context and whether the '
                      'failure affects one client or many. Query the relevant record and record status, '
                      'answer, TTL, and resolver. Compare another perspective only when it will answer a '
                      'specific question. Once the expected name resolves correctly, continue forward '
                      'through route, port, TLS, HTTP, and application behavior. DNS is one layer in the '
                      'evidence chain.'}],
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
