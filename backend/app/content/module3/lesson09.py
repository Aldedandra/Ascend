"""Module 3, Lesson 3-9: Networking Capstone: Find the Broken Path."""

LESSON = {'id': '3-9',
 'title': 'Networking Capstone: Find the Broken Path',
 'summary': 'Investigate a realistic Ascend outage by tracing the complete request path, correcting the '
            'failed layer, verifying recovery, and documenting the incident.',
 'duration_minutes': 120,
 'xp': 125,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is Networking Capstone: Find the Broken Path.\n'
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
                 'First, Trace an end-to-end application request. Also, Use evidence to isolate a failed '
                 'networking layer. Also, Separate client, proxy, and backend network legs. Also, Make and '
                 'verify a minimal safe correction. Also, Produce a professional incident record.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'Incident brief.\n'
                 '\n'
                 'The Ascend learning API was deployed successfully, but users report that the application '
                 'loads while lesson data fails. Restore service without treating networking as one black '
                 'box.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'Your constraints.\n'
                 '\n'
                 'Preserve evidence before changing configuration. Do not broadly disable security controls. '
                 'Make one justified correction at a time. Record commands, observations, hypotheses, '
                 'changes, and verification.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'The path you must prove.\n'
                 '\n'
                 'Trace the request from hostname resolution through expected address, route, TCP port, TLS '
                 'or HTTP boundary, reverse proxy, and backend listener. Several layers may appear '
                 'plausible; evidence determines where you act.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 'Success criteria.\n'
                 '\n'
                 'The hostname resolves as intended, the endpoint accepts expected traffic, the proxy '
                 'reaches the backend, the API health endpoint succeeds, lesson data loads, unrelated '
                 'services remain unchanged, and your notes explain the failure and correction.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 'Capstone standard.\n'
                 '\n'
                 'Optimize for a defensible investigation, not speed. Another engineer should be able to '
                 'reproduce your reasoning from symptom to root cause to verification.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 'Prevention matters.\n'
                 '\n'
                 'A completed incident includes one improvement that would prevent recurrence or make the '
                 'same failure easier to detect, such as a health check, validation step, alert, or '
                 'configuration test.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'Build a timeline before building a theory.\n'
                 '\n'
                 'Record first observation, affected clients, exact endpoint, recent deployments, '
                 'configuration changes, and relevant timestamps. Correlating client failures with proxy, '
                 'application, and deployment logs can quickly separate coincidence from cause.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'Successful tests are part of the evidence.\n'
                 '\n'
                 'Do not focus only on failures. If DNS resolves, TCP connects, TLS validates, or the proxy '
                 'returns HTTP, each success proves that part of the path works and removes entire '
                 'categories of possible causes.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'Treat every hop as an independent communication leg.\n'
                 '\n'
                 'Client-to-edge, edge-to-backend, and backend-to-dependency paths can fail independently. '
                 'For each leg, identify the source, destination, address, route, port, protocol, policy, '
                 'and available logs.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 'Try to disprove your hypothesis.\n'
                 '\n'
                 'A strong investigation does not merely collect evidence that supports the first theory. '
                 'Before changing configuration, ask what observation would prove the hypothesis wrong. This '
                 'reduces confirmation bias and prevents unnecessary changes.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'One more practical point.\n'
                 '\n'
                 'Verification must reproduce the original user outcome.\n'
                 '\n'
                 'A corrected listener or successful curl command is intermediate evidence. Complete '
                 'verification repeats the failed request and confirms the actual user-facing behavior, '
                 'while checking that unrelated services remain healthy.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now bring these ideas together.\n'
                 '\n'
                 'Finish with prevention and detection.\n'
                 '\n'
                 'The incident is more valuable when it improves the system. Consider deployment validation, '
                 'health checks, configuration tests, better logging, alerts, or a single source of truth '
                 'that would prevent the same mismatch or reveal it sooner.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'Welcome to the Module 3 capstone: Find the Broken Path.\n'
                 '\n'
                 'This is not a command-recitation exercise. You are responding to an incident.\n'
                 '\n'
                 'A new Ascend API release has completed. The front end loads, but lesson data does not.\n'
                 '\n'
                 'Your responsibility is to establish what works, locate where the request path breaks, make '
                 'the smallest safe correction, and prove recovery.\n'
                 '\n'
                 'Capture the hostname, failing endpoint, exact client error, and recent changes. Then trace '
                 'the path.\n'
                 '\n'
                 'Resolve the name.\n'
                 '\n'
                 'Inspect the route.\n'
                 '\n'
                 'Test the expected transport port.\n'
                 '\n'
                 'If you reach a web or TLS endpoint, inspect that response instead of falling back to '
                 'lower-layer guesses.\n'
                 '\n'
                 'Separate client-to-proxy from proxy-to-backend.\n'
                 '\n'
                 'Confirm where the backend listens and whether the proxy targets the correct address and '
                 'port.\n'
                 '\n'
                 'Do not disable the firewall.\n'
                 '\n'
                 'Do not restart everything.\n'
                 '\n'
                 'Do not edit DNS merely because DNS is familiar.\n'
                 '\n'
                 'Every action should follow from evidence.\n'
                 '\n'
                 'When you identify the failure, write your hypothesis before changing it.\n'
                 '\n'
                 'Make one correction.\n'
                 '\n'
                 'Repeat the tests that exposed the failure and continue through the user-facing behavior.\n'
                 '\n'
                 'Finally, create the incident record: symptom, scope, evidence, root cause, correction, '
                 'verification, and one prevention or detection improvement.\n'
                 '\n'
                 'You are finished when the system works and your reasoning can survive review.\n'
                 '\n'
                 'That is the difference between getting lucky and operating like an engineer.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Before you touch the configuration, build a timeline.\n'
                 '\n'
                 'Record when the failure was first observed, which clients are affected, the exact endpoint '
                 'that fails, and the most recent deployment or infrastructure change. A timeline keeps '
                 'correlation grounded in evidence instead of memory.\n'
                 '\n'
                 'Next, establish a known-good baseline wherever possible.\n'
                 '\n'
                 'If the frontend loads, that is evidence. If DNS resolves correctly, that is evidence. If '
                 'TCP connects to the proxy, that is evidence. If TLS succeeds and HTTP returns a 502, that '
                 'is stronger evidence still: the client reached the proxy, and the failure is likely later '
                 'in the path.\n'
                 '\n'
                 'Do not throw away successful tests. Successful layers are how you eliminate '
                 'possibilities.\n'
                 '\n'
                 'Separate the request into legs.\n'
                 '\n'
                 'Client to DNS.\n'
                 '\n'
                 'Client to edge.\n'
                 '\n'
                 'Edge to backend.\n'
                 '\n'
                 'Backend to dependency.\n'
                 '\n'
                 'Each leg can have its own address, route, port, protocol, policy, timeout, and logs.\n'
                 '\n'
                 'Suppose the proxy is configured to forward to port 8001 while the API now listens on 8000. '
                 'The frontend may still load perfectly. DNS may be correct. TLS may be valid. The proxy may '
                 'return an error because its upstream target is wrong.\n'
                 '\n'
                 "That is a much narrower problem than 'networking is broken.'\n"
                 '\n'
                 'Before correcting it, state the hypothesis in writing. For example: the proxy can be '
                 'reached, but its configured upstream port does not match the API listener.\n'
                 '\n'
                 'Then gather one final piece of evidence that could disprove the hypothesis.\n'
                 '\n'
                 "Inspect the listener. Inspect the proxy target. Test the backend directly from the proxy's "
                 'network context if the lab allows it.\n'
                 '\n'
                 'Only then make the smallest safe change.\n'
                 '\n'
                 'Afterward, verification must retrace the path. Confirm the backend listener. Confirm the '
                 'proxy can reach it. Confirm the health endpoint. Confirm the original lesson-data request. '
                 'Confirm the user-facing application.\n'
                 '\n'
                 'Also verify that the correction did not damage an unrelated service.\n'
                 '\n'
                 'Finally, document prevention.\n'
                 '\n'
                 'Could a deployment validation have caught the wrong target port? Could a health check have '
                 'exposed it sooner? Could configuration be generated from one source of truth? Could an '
                 'alert distinguish edge health from backend health?\n'
                 '\n'
                 'The capstone is not about finding one hidden answer. It is about demonstrating a method '
                 'you can reuse when the failure is unfamiliar.\n'
                 '\n'
                 'Observe. Preserve evidence. Narrow the path. State the hypothesis. Make one justified '
                 'correction. Verify end to end. Document what would make the next incident easier.\n'
                 '\n'
                 'That is production thinking.\n'
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
 'objectives': ['Trace an end-to-end application request.',
                'Use evidence to isolate a failed networking layer.',
                'Separate client, proxy, and backend network legs.',
                'Make and verify a minimal safe correction.',
                'Produce a professional incident record.'],
 'content': [{'heading': 'Incident brief',
              'body': 'The Ascend learning API was deployed successfully, but users report that the '
                      'application loads while lesson data fails. Restore service without treating '
                      'networking as one black box.'},
             {'heading': 'Your constraints',
              'body': 'Preserve evidence before changing configuration. Do not broadly disable security '
                      'controls. Make one justified correction at a time. Record commands, observations, '
                      'hypotheses, changes, and verification.'},
             {'heading': 'The path you must prove',
              'body': 'Trace the request from hostname resolution through expected address, route, TCP port, '
                      'TLS or HTTP boundary, reverse proxy, and backend listener. Several layers may appear '
                      'plausible; evidence determines where you act.'},
             {'heading': 'Success criteria',
              'body': 'The hostname resolves as intended, the endpoint accepts expected traffic, the proxy '
                      'reaches the backend, the API health endpoint succeeds, lesson data loads, unrelated '
                      'services remain unchanged, and your notes explain the failure and correction.'},
             {'heading': 'Capstone standard',
              'body': 'Optimize for a defensible investigation, not speed. Another engineer should be able '
                      'to reproduce your reasoning from symptom to root cause to verification.'},
             {'heading': 'Prevention matters',
              'body': 'A completed incident includes one improvement that would prevent recurrence or make '
                      'the same failure easier to detect, such as a health check, validation step, alert, or '
                      'configuration test.'},
             {'heading': 'Build a timeline before building a theory',
              'body': 'Record first observation, affected clients, exact endpoint, recent deployments, '
                      'configuration changes, and relevant timestamps. Correlating client failures with '
                      'proxy, application, and deployment logs can quickly separate coincidence from cause.'},
             {'heading': 'Successful tests are part of the evidence',
              'body': 'Do not focus only on failures. If DNS resolves, TCP connects, TLS validates, or the '
                      'proxy returns HTTP, each success proves that part of the path works and removes '
                      'entire categories of possible causes.'},
             {'heading': 'Treat every hop as an independent communication leg',
              'body': 'Client-to-edge, edge-to-backend, and backend-to-dependency paths can fail '
                      'independently. For each leg, identify the source, destination, address, route, port, '
                      'protocol, policy, and available logs.'},
             {'heading': 'Try to disprove your hypothesis',
              'body': 'A strong investigation does not merely collect evidence that supports the first '
                      'theory. Before changing configuration, ask what observation would prove the '
                      'hypothesis wrong. This reduces confirmation bias and prevents unnecessary changes.'},
             {'heading': 'Verification must reproduce the original user outcome',
              'body': 'A corrected listener or successful curl command is intermediate evidence. Complete '
                      'verification repeats the failed request and confirms the actual user-facing behavior, '
                      'while checking that unrelated services remain healthy.'},
             {'heading': 'Finish with prevention and detection',
              'body': 'The incident is more valuable when it improves the system. Consider deployment '
                      'validation, health checks, configuration tests, better logging, alerts, or a single '
                      'source of truth that would prevent the same mismatch or reveal it sooner.'}],
 'diagram': {'title': 'Find the broken leg',
             'description': 'The outage may be on any one of several independent communication legs.',
             'nodes': [{'label': 'Client', 'detail': 'The user-facing application begins the request.'},
                       {'label': 'DNS', 'detail': 'The API hostname resolves.'},
                       {'label': 'Edge / Proxy',
                        'detail': 'The public or internal entry point accepts traffic.'},
                       {'label': 'Backend target',
                        'detail': 'The proxy forwards to the configured host and port.'},
                       {'label': 'API listener', 'detail': 'The application accepts the request.'},
                       {'label': 'User verification', 'detail': 'Lesson data loads successfully.'}],
             'caption': 'Do not repair a layer until the evidence places the failure there.'},
 'engineer_perspective': {'title': 'A working service is not the only deliverable',
                          'body': 'The capstone is complete when the service is restored and your evidence '
                                  'trail explains why the correction worked. A reproducible investigation is '
                                  'more valuable than a lucky fix.'},
 'try_it_yourself': {'title': 'Build the incident evidence set',
                     'intro': 'Work in a safe lab or local Ascend environment rather than changing '
                              'production infrastructure.',
                     'steps': ['Record symptom, scope, endpoint, and recent changes.',
                               'Verify DNS.',
                               'Verify route and expected TCP port.',
                               'Inspect TLS/HTTP if the endpoint is reachable.',
                               'Separate proxy-to-backend from client-to-proxy.',
                               'Write the hypothesis before making a correction.',
                               'Create a timeline containing the last known-good state, deployment time, '
                               'first failure, and your test timestamps.',
                               'For every successful test, write one or more causes that the result makes '
                               'less likely.',
                               'Before the correction, write one observation that would disprove your '
                               'root-cause hypothesis.',
                               'After recovery, identify one prevention control and one detection control '
                               'that would improve the next incident.'],
                     'takeaway': 'A capstone-quality investigation should be explainable by another engineer '
                                 'from your notes alone.'},
 'lab': {'title': 'Capstone — Restore Ascend Lesson Delivery',
         'instructions': ['Create an incident log with timestamp, symptom, scope, and recent changes.',
                          'Identify the failing Ascend hostname/endpoint and intended destination.',
                          'Verify DNS and record the result.',
                          'Verify route and transport connectivity to the expected port.',
                          'Inspect TLS and HTTP if reachable.',
                          'Separate client-to-proxy and proxy-to-backend legs; verify backend listener and '
                          'target port.',
                          'Write the root-cause hypothesis before changing anything.',
                          'Make one minimal safe correction in the lab.',
                          'Repeat the failed test, verify the API health endpoint, and verify lesson data '
                          'end to end.',
                          'Document symptom, evidence, root cause, correction, verification, and one '
                          'prevention/detection improvement.',
                          'Build a short incident timeline and correlate at least one client observation '
                          'with a server, proxy, or deployment event.',
                          'For each communication leg, record what success would prove and what failure '
                          'would leave possible.',
                          'Write one falsification test for your root-cause hypothesis before making the '
                          'correction.',
                          'After end-to-end recovery, verify one unrelated service or path remained '
                          'unchanged.',
                          'Close the incident with one prevention improvement and one '
                          'detection/observability improvement.']},
 'quiz': [{'question': "What is the capstone's primary objective?",
           'choices': ['Run every command',
                       'Restore service through a defensible evidence-driven investigation',
                       'Disable security',
                       'Replace hostnames'],
           'correct': 1},
          {'question': 'The frontend loads but API data fails. What does that prove?',
           'choices': ['The whole network is down',
                       'Some client-to-frontend communication works',
                       'The database is healthy',
                       'DNS is broken'],
           'correct': 1},
          {'question': 'Before configuration changes, preserve what?',
           'choices': ['Evidence and observations', 'Only UI screenshots', 'Nothing', 'A new image'],
           'correct': 0},
          {'question': 'Why separate client-to-proxy and proxy-to-backend traffic?',
           'choices': ['They are distinct connection legs',
                       'Proxies do not use ports',
                       'DNS cannot cross proxies',
                       'It proves database health'],
           'correct': 0},
          {'question': 'What correction is preferred?',
           'choices': ['Several changes',
                       'The smallest safe change supported by evidence',
                       'Disable filtering',
                       'Rebuild everything'],
           'correct': 1},
          {'question': 'Why repeat tests after correction?',
           'choices': ['Create logs only',
                       'Prove the failure is gone and end-to-end behavior is restored',
                       'First tests are invalid',
                       'Change root cause'],
           'correct': 1},
          {'question': 'Which outcome is NOT enough?',
           'choices': ['Service works but no incident record exists',
                       'Health endpoint succeeds',
                       'Lesson data loads',
                       'Unrelated services remain unchanged'],
           'correct': 0},
          {'question': 'What belongs in the incident record?',
           'choices': ['Symptom, scope, evidence, root cause, correction, verification, improvement',
                       'Only final command',
                       'Only suspected cause',
                       'Unrelated services'],
           'correct': 0},
          {'question': 'Why avoid broadly disabling a firewall?',
           'choices': ['It increases risk and can hide the real policy error',
                       'Firewalls never fail',
                       'It prevents DNS',
                       'It changes HTTP to UDP'],
           'correct': 0},
          {'question': 'What distinguishes engineering from luck here?',
           'choices': ['Longest command',
                       'A reproducible evidence trail from symptom through verification',
                       'Fast restart',
                       'Knowing the answer first'],
           'correct': 1}],
 'reflection': 'What part of your investigation most clearly demonstrated that you were following evidence '
               'rather than guessing?'}
