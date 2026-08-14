"""Module 3, Lesson 3-7: Network Troubleshooting & Evidence."""

LESSON = {'id': '3-7',
 'title': 'Network Troubleshooting & Evidence',
 'summary': 'Turn vague connectivity symptoms into a layered, evidence-driven investigation from DNS through '
            'the application.',
 'duration_minutes': 80,
 'xp': 70,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is Network Troubleshooting & Evidence.\n'
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
                 'First, Build a repeatable network troubleshooting workflow. Also, Interpret DNS, timeout, '
                 'refusal, TLS, and HTTP evidence. Also, Compare working and failing network paths. Also, '
                 'Choose the next test based on what prior evidence proved. Also, Verify recovery after a '
                 'minimal correction.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'Troubleshoot the path, not the symptom.\n'
                 '\n'
                 'A report such as “the site is down” does not identify the failed layer. Treat a request as '
                 'a path through name resolution, local networking, routing, transport, TLS, HTTP, proxies, '
                 'and the application. Prove what still works before changing anything.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'Begin with context and preserve evidence.\n'
                 '\n'
                 'Record what is failing, for whom, from where, when it started, and what changed. Capture '
                 'the exact hostname, URL, timeout, certificate message, status code, or connection error '
                 'before a restart or configuration change destroys useful clues.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'Build an evidence ladder.\n'
                 '\n'
                 'A useful sequence is: inspect local interface/address; resolve the hostname; inspect the '
                 'route; test the destination port; validate TLS; inspect the HTTP response; then inspect '
                 'proxy and application logs. Let each result choose the next question.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 'Interpret the result.\n'
                 '\n'
                 'NXDOMAIN points toward DNS or the requested name. Connection refused often means the '
                 'destination was reached but nothing accepted the port, or policy actively rejected it. A '
                 'timeout leaves routing, filtering, reachability, and silent services possible. TLS and '
                 'HTTP errors prove progressively later layers are reachable.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 'Compare perspectives.\n'
                 '\n'
                 'Test from another machine, network, container, or environment. Compare DNS answers, '
                 'routes, certificates, headers, and timing. A working-versus-failing comparison can reduce '
                 'uncertainty faster than repeatedly testing from one host.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 'Verification closes the loop.\n'
                 '\n'
                 'After a justified correction, repeat the same checks that exposed the problem and continue '
                 'all the way through user-facing behavior. Recovery is not proven merely because one '
                 'command returns success.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'Build a symptom matrix before touching configuration.\n'
                 '\n'
                 'Record who fails, from which network, against which hostname or endpoint, and whether a '
                 'known-good comparison exists. If one client works and another fails, the shared server '
                 'path becomes less suspicious. If every client fails at once after a deployment, '
                 'server-side or shared-path changes become more interesting.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'Use branching logic instead of a fixed command ritual.\n'
                 '\n'
                 'If DNS returns NXDOMAIN, investigate the name and resolver context before testing HTTP. If '
                 'DNS succeeds but TCP is refused, inspect listeners and target ports. If TCP succeeds but '
                 'TLS fails, inspect certificate identity, trust, SNI, and time. If HTTP returns 502, '
                 'investigate the proxy-to-upstream leg.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'Correlate client evidence with server evidence.\n'
                 '\n'
                 'A timeout on the client is more useful when paired with server-side listener state, proxy '
                 'logs, firewall counters, or application logs. Evidence from both ends can reveal whether '
                 'the request arrived, whether it was accepted, and whether a response was attempted.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 'Preserve timestamps.\n'
                 '\n'
                 'Time correlation matters during incidents. Record when the client failed and compare that '
                 'moment with proxy, application, deployment, and infrastructure logs. A technically correct '
                 'log entry from the wrong time window can send an investigation in the wrong direction.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'A networking incident often begins with a sentence that sounds useful but is not: the site '
                 'is down.\n'
                 '\n'
                 'Your job is to turn that symptom into evidence.\n'
                 '\n'
                 'Think of every request as a journey through layers. Can the client identify itself on the '
                 'network? Does the name resolve? Is there a route? Can a transport connection reach the '
                 'expected port? If encryption is involved, does TLS negotiate? Does HTTP return a response? '
                 'If those work, what does the application say?\n'
                 '\n'
                 'The important skill is not memorizing a giant command list. It is choosing a test that '
                 'answers a question.\n'
                 '\n'
                 'DNS success is evidence. Connection refused is different from a timeout. Refused often '
                 'tells you the destination was reached but nothing accepted the connection. A timeout '
                 'leaves routing, filtering, and reachability in play.\n'
                 '\n'
                 'Use tools such as ip, dig or nslookup, ss, curl, traceroute, and logs as instruments, not '
                 'rituals. Compare a working client with a failing client. Compare an internal request with '
                 'an external request. Compare where the hostname resolves with where the service actually '
                 'listens.\n'
                 '\n'
                 'Then make the smallest safe correction and run the same checks again.\n'
                 '\n'
                 'Troubleshooting is a loop: observe, hypothesize, test, change, verify.\n'
                 '\n'
                 'The goal is not to look busy. The goal is to reduce uncertainty until the broken layer has '
                 'nowhere left to hide.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'A mature troubleshooting workflow also branches based on evidence. Do not run every '
                 'command in the same order simply because it is on a checklist. NXDOMAIN sends you toward '
                 'the name and resolver context. A refused TCP connection sends you toward the listener and '
                 'target port. A TLS hostname error proves you reached a TLS-speaking endpoint and shifts '
                 'attention toward identity, SNI, and certificate configuration. A 502 proves the client '
                 'reached a proxy that returned HTTP, so the proxy-to-upstream leg becomes more '
                 'interesting.\n'
                 '\n'
                 'Also compare perspectives. A working client is evidence. A failing client is evidence. Put '
                 'them side by side. Record timestamps so you can correlate the exact failure with proxy '
                 'logs, application logs, deployments, and infrastructure events.\n'
                 '\n'
                 'The goal is not to execute more commands. The goal is to make the remaining explanation '
                 'smaller after every test.\n'
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
 'objectives': ['Build a repeatable network troubleshooting workflow.',
                'Interpret DNS, timeout, refusal, TLS, and HTTP evidence.',
                'Compare working and failing network paths.',
                'Choose the next test based on what prior evidence proved.',
                'Verify recovery after a minimal correction.'],
 'content': [{'heading': 'Troubleshoot the path, not the symptom',
              'body': 'A report such as “the site is down” does not identify the failed layer. Treat a '
                      'request as a path through name resolution, local networking, routing, transport, TLS, '
                      'HTTP, proxies, and the application. Prove what still works before changing anything.'},
             {'heading': 'Begin with context and preserve evidence',
              'body': 'Record what is failing, for whom, from where, when it started, and what changed. '
                      'Capture the exact hostname, URL, timeout, certificate message, status code, or '
                      'connection error before a restart or configuration change destroys useful clues.'},
             {'heading': 'Build an evidence ladder',
              'body': 'A useful sequence is: inspect local interface/address; resolve the hostname; inspect '
                      'the route; test the destination port; validate TLS; inspect the HTTP response; then '
                      'inspect proxy and application logs. Let each result choose the next question.'},
             {'heading': 'Interpret the result',
              'body': 'NXDOMAIN points toward DNS or the requested name. Connection refused often means the '
                      'destination was reached but nothing accepted the port, or policy actively rejected '
                      'it. A timeout leaves routing, filtering, reachability, and silent services possible. '
                      'TLS and HTTP errors prove progressively later layers are reachable.'},
             {'heading': 'Compare perspectives',
              'body': 'Test from another machine, network, container, or environment. Compare DNS answers, '
                      'routes, certificates, headers, and timing. A working-versus-failing comparison can '
                      'reduce uncertainty faster than repeatedly testing from one host.'},
             {'heading': 'Verification closes the loop',
              'body': 'After a justified correction, repeat the same checks that exposed the problem and '
                      'continue all the way through user-facing behavior. Recovery is not proven merely '
                      'because one command returns success.'},
             {'heading': 'Build a symptom matrix before touching configuration',
              'body': 'Record who fails, from which network, against which hostname or endpoint, and whether '
                      'a known-good comparison exists. If one client works and another fails, the shared '
                      'server path becomes less suspicious. If every client fails at once after a '
                      'deployment, server-side or shared-path changes become more interesting.'},
             {'heading': 'Use branching logic instead of a fixed command ritual',
              'body': 'If DNS returns NXDOMAIN, investigate the name and resolver context before testing '
                      'HTTP. If DNS succeeds but TCP is refused, inspect listeners and target ports. If TCP '
                      'succeeds but TLS fails, inspect certificate identity, trust, SNI, and time. If HTTP '
                      'returns 502, investigate the proxy-to-upstream leg.'},
             {'heading': 'Correlate client evidence with server evidence',
              'body': 'A timeout on the client is more useful when paired with server-side listener state, '
                      'proxy logs, firewall counters, or application logs. Evidence from both ends can '
                      'reveal whether the request arrived, whether it was accepted, and whether a response '
                      'was attempted.'},
             {'heading': 'Preserve timestamps',
              'body': 'Time correlation matters during incidents. Record when the client failed and compare '
                      'that moment with proxy, application, deployment, and infrastructure logs. A '
                      'technically correct log entry from the wrong time window can send an investigation in '
                      'the wrong direction.'}],
 'diagram': {'title': 'The evidence ladder',
             'description': 'Move from lower layers toward the application only as evidence justifies it.',
             'nodes': [{'label': 'Name', 'detail': 'Does the hostname resolve as intended?'},
                       {'label': 'Route',
                        'detail': 'Where does the operating system intend to send the traffic?'},
                       {'label': 'Port', 'detail': 'Can a transport connection reach the expected listener?'},
                       {'label': 'TLS',
                        'detail': 'Can the encrypted session and certificate validation succeed?'},
                       {'label': 'HTTP', 'detail': 'What status and headers does the web layer return?'},
                       {'label': 'Application', 'detail': 'What do proxy and application logs say?'}],
             'caption': 'Every successful layer removes possibilities. Every failure narrows the next '
                        'question.'},
 'engineer_perspective': {'title': 'Ask what the evidence has already proved',
                          'body': 'Networking incidents reward disciplined elimination. Ask: What have I '
                                  'proven? What remains possible? What single observation would reduce '
                                  'uncertainty most? Evidence before action is the operating model for '
                                  'network troubleshooting.'},
 'try_it_yourself': {'title': 'Trace one request without changing anything',
                     'intro': 'Choose a safe hostname or local service and gather a complete evidence chain.',
                     'steps': ['Record the client, hostname, expected destination, protocol, and port.',
                               'Resolve the hostname with dig, nslookup, or host.',
                               'Inspect the route toward the resolved address.',
                               'Test the expected TCP port.',
                               'Use curl to inspect TLS and HTTP behavior where applicable.',
                               'Write what each result proved and what it ruled out.',
                               'Create a symptom matrix comparing at least two perspectives: working/failing '
                               'client, internal/external path, or host/container.',
                               'For NXDOMAIN, connection refused, timeout, TLS mismatch, HTTP 502, and HTTP '
                               '500, write the most useful next question.',
                               'Add timestamps to your observations so they could be correlated with logs.'],
                     'takeaway': 'The best next command is the one that answers the most important remaining '
                                 'question.'},
 'lab': {'title': 'Trace a Failing Request',
         'instructions': ['Create a Journal entry titled “Lesson 3.7 — Network Troubleshooting.”',
                          'Choose a safe hostname or local service to test.',
                          'Record client, hostname, expected destination, protocol, and port.',
                          'Record DNS resolution.',
                          'Inspect the route to the destination.',
                          'Test the expected TCP port and classify the result as success, refusal, or '
                          'timeout.',
                          'Use curl to inspect TLS/HTTP where applicable.',
                          'Compare one observation from a second host, network, or container if available.',
                          'Write an evidence chain: observation → hypothesis → next test → conclusion.',
                          'Finish with the exact verification you would perform after a correction.',
                          'Build a decision tree whose branches include NXDOMAIN, refused, timeout, TLS '
                          'failure, 502, and 500.',
                          'For each branch, name one test that would be premature or low-value and explain '
                          'why.',
                          'Write a short incident update using only verified facts; keep hypotheses '
                          'explicitly labeled as hypotheses.']},
 'quiz': [{'question': 'A user reports “the site is down.” What is the best first response?',
           'choices': ['Restart the server',
                       'Gather the exact failure, scope, URL, and recent changes',
                       'Flush every DNS cache',
                       'Disable the firewall'],
           'correct': 1},
          {'question': 'A hostname returns NXDOMAIN. Which layer deserves attention first?',
           'choices': ['DNS', 'TLS', 'HTTP', 'Database'],
           'correct': 0},
          {'question': 'A TCP connection is immediately refused. What does that most strongly suggest?',
           'choices': ['DNS failed',
                       'The destination was reached but the port was not accepting the connection',
                       'The certificate expired',
                       'HTTP returned 404'],
           'correct': 1},
          {'question': 'Why test from another machine or network?',
           'choices': ['Generate traffic',
                       'Compare perspectives and narrow scope',
                       'Bypass logs',
                       'Change the hostname'],
           'correct': 1},
          {'question': 'A TLS hostname mismatch proves what?',
           'choices': ['No route exists',
                       'The client reached a TLS-speaking endpoint',
                       'DNS cannot resolve',
                       'The database is healthy'],
           'correct': 1},
          {'question': 'An HTTP 500 proves what?',
           'choices': ['The web stack returned an HTTP response',
                       'The client has no IP',
                       'Port 443 is blocked',
                       'DNS returned NXDOMAIN'],
           'correct': 0},
          {'question': 'Why use a layered troubleshooting sequence?',
           'choices': ['Run every command',
                       'Reduce uncertainty and locate the failed layer',
                       'Avoid documentation',
                       'Blame networking'],
           'correct': 1},
          {'question': 'Which question best reflects evidence-driven troubleshooting?',
           'choices': ['What can I restart?',
                       'What have I proven, and what test reduces uncertainty next?',
                       'Which command looks advanced?',
                       'Can I change several settings?'],
           'correct': 1},
          {'question': 'After a correction, what should you do?',
           'choices': ['Assume success',
                       'Repeat relevant tests and verify end-to-end behavior',
                       'Delete logs',
                       'Make another change'],
           'correct': 1},
          {'question': 'Why is a timeout less specific than connection refused?',
           'choices': ['Timeouts only happen in DNS',
                       'Several routing, filtering, or reachability failures can cause silence',
                       'Refused means TLS succeeded',
                       'Timeout means HTTP 200'],
           'correct': 1}],
 'reflection': 'When a service fails, which observation would you collect first next time, and how would it '
               'reduce uncertainty?'}
