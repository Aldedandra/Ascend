"""Module 3, Lesson 3-8: Networking in Modern DevOps."""

LESSON = {'id': '3-8',
 'title': 'Networking in Modern DevOps',
 'summary': 'Connect networking fundamentals to containers, service discovery, reverse proxies, load '
            'balancers, cloud networks, and delivery systems.',
 'duration_minutes': 90,
 'xp': 90,
 'audio_script': 'Welcome to Ascend, Module 3.\n'
                 '\n'
                 'This lesson is Networking in Modern DevOps.\n'
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
                 'First, Explain container network namespaces and published ports. Also, Describe service '
                 'discovery in dynamic systems. Also, Separate reverse-proxy/load-balancer connection legs. '
                 'Also, Translate cloud networking concepts into routing and policy fundamentals. Also, '
                 'Trace networking dependencies in a DevOps delivery path.\n'
                 '\n'
                 'Start with this idea.\n'
                 '\n'
                 'The fundamentals do not disappear in the cloud.\n'
                 '\n'
                 'Containers, Kubernetes, load balancers, and cloud networks add abstraction, but packets '
                 'still use addresses, routes, ports, DNS, transport protocols, and application protocols.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now add another layer.\n'
                 '\n'
                 'Container networking creates new boundaries.\n'
                 '\n'
                 'A container normally has its own network namespace and interfaces. Publishing a port '
                 'creates a path from a host address and port toward the container. A service bound only to '
                 'localhost in the wrong namespace can look healthy internally while remaining unreachable '
                 'externally.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Here is where this becomes operational.\n'
                 '\n'
                 'Service discovery handles moving workloads.\n'
                 '\n'
                 'Docker Compose service names, Kubernetes Services, and cloud DNS provide stable identities '
                 'that map to changing workloads. DNS and service discovery therefore become part of '
                 'application reliability.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This distinction matters during troubleshooting.\n'
                 '\n'
                 'Reverse proxies and load balancers add legs.\n'
                 '\n'
                 'A proxy or load balancer accepts one connection and forwards or creates another toward a '
                 'backend. Troubleshoot client-to-edge and edge-to-backend as separate communication legs.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now connect that to a real DevOps environment.\n'
                 '\n'
                 'Cloud networks are routed networks with policy.\n'
                 '\n'
                 'VPCs contain address ranges and subnets. Route tables decide where traffic goes. Gateways '
                 'create paths. Security groups, ACLs, and firewalls enforce policy.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'There is an important evidence rule here.\n'
                 '\n'
                 'DevOps depends on communication paths.\n'
                 '\n'
                 'CI/CD, registries, databases, APIs, monitoring, deployments, DNS, certificates, and health '
                 'checks all depend on networking. Networking is embedded throughout delivery and '
                 'reliability.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Next, think about the request from another perspective.\n'
                 '\n'
                 'Localhost is scoped to a network namespace.\n'
                 '\n'
                 'On a host, localhost points back to that host. Inside a container, localhost points back '
                 'to that container. Two processes can run on the same physical computer and still have '
                 'different loopback contexts. This distinction explains many container connectivity '
                 'failures.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now make the model more concrete.\n'
                 '\n'
                 'Published ports and service ports solve different problems.\n'
                 '\n'
                 'A published Docker port creates a host-to-container path, while an internal service name '
                 'and port can provide container-to-container communication. Always identify which side of '
                 'the boundary the client is on before deciding which address and port it should use.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'This is a good place to slow down and separate what is proven from what is assumed.\n'
                 '\n'
                 'Health checks are real network requests.\n'
                 '\n'
                 'Load balancers and orchestrators often decide whether a workload is usable by sending '
                 'health checks. A healthy process can still be removed from service if the health-check '
                 'path, port, protocol, expected status, or security policy is wrong.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Finally, connect the concept back to the full request path.\n'
                 '\n'
                 '502 and 504 responses narrow the investigation.\n'
                 '\n'
                 "A gateway-generated 502 or 504 is not proof that 'the network is down.' It usually proves "
                 'the client reached an HTTP-speaking intermediary. The next investigation should focus on '
                 "the intermediary's upstream target, connectivity, timeout, and backend behavior.\n"
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'One more practical point.\n'
                 '\n'
                 'Every DevOps dependency is a network dependency.\n'
                 '\n'
                 'Source control, package repositories, container registries, cloud APIs, databases, '
                 'monitoring endpoints, artifact stores, and deployment targets all require communication '
                 'paths. Mapping those dependencies makes pipeline and runtime failures easier to isolate.\n'
                 '\n'
                 'After hearing that, practice the evidence statement. Ask yourself what this observation '
                 'would prove, and what it would still leave possible. That second half is important. DevOps '
                 'troubleshooting gets much safer when a successful test is not allowed to prove more than '
                 'it actually proves.\n'
                 '\n'
                 'Now that the lesson model is in place, here is another pass through the topic in a more '
                 'conversational troubleshooting flow.\n'
                 '\n'
                 'Modern infrastructure can make networking look more complicated than it is.\n'
                 '\n'
                 'Containers may introduce services, ingress controllers, networks, load balancers, and '
                 'cloud security groups. Underneath are the same questions.\n'
                 '\n'
                 'What name did the client use? What address did it resolve to? Where does the route send '
                 'traffic? Which port is expected? What process is listening? Which policy allows the '
                 'traffic? What protocol speaks next?\n'
                 '\n'
                 'Containers add network namespaces. A process inside a container sees a network environment '
                 'different from the host. Publishing a port creates a path into that environment. Localhost '
                 'therefore means this network namespace, not every machine or container.\n'
                 '\n'
                 'Dynamic infrastructure also makes service discovery essential. Workloads move, so stable '
                 'names and service abstractions become part of reliability.\n'
                 '\n'
                 'Reverse proxies and load balancers create additional connection legs. A user may reach a '
                 'load balancer while the load balancer cannot reach the application. Separate those legs '
                 'and test them independently.\n'
                 '\n'
                 'Cloud networking follows the same mental model. VPCs contain address space. Subnets divide '
                 'it. Route tables direct traffic. Gateways create paths. Security controls decide what is '
                 'allowed.\n'
                 '\n'
                 'Learn the product names, but reason from fundamentals.\n'
                 '\n'
                 'Every deployment is also a communication problem. CI/CD runners reach source control and '
                 'artifact stores. Containers pull images. Applications reach databases and APIs. Monitoring '
                 'systems scrape endpoints.\n'
                 '\n'
                 'If you can trace the path, you can debug the system.\n'
                 '\n'
                 'Keep climbing.\n'
                 '\n'
                 'Modern networking also changes how you interpret localhost and service names.\n'
                 '\n'
                 "On the host, localhost refers to the host's own loopback interface. Inside a container, "
                 "localhost refers to that container's network namespace. If an API is listening only on "
                 '127.0.0.1 inside one container, another container cannot reach it merely because both run '
                 'on the same computer.\n'
                 '\n'
                 'Published ports solve a different problem. A mapping such as 8000:8000 creates a path from '
                 'a host port toward a container port. It does not mean every process everywhere can use '
                 'localhost:8000 and reach the same thing.\n'
                 '\n'
                 'Service discovery gives moving workloads a stable identity. In Docker Compose, a service '
                 'name can resolve on the Compose network. In Kubernetes, a Service can provide a stable '
                 'virtual endpoint even while Pods are replaced. In cloud environments, DNS names and '
                 'load-balancer endpoints often play the same role.\n'
                 '\n'
                 'That stability matters because individual workload addresses are often temporary.\n'
                 '\n'
                 'Now consider a reverse proxy or load balancer.\n'
                 '\n'
                 'The client establishes one connection to the edge. The edge may terminate TLS, inspect the '
                 'HTTP request, choose a backend, and establish another connection to that backend. A '
                 'successful client-to-edge connection does not prove the backend is healthy.\n'
                 '\n'
                 'This is why HTTP 502 and 504 responses are valuable evidence. They often tell you the edge '
                 'was reachable but had trouble communicating successfully with an upstream service.\n'
                 '\n'
                 'Health checks add another communication path. A backend can be running while a load '
                 'balancer marks it unhealthy because the health-check port, path, protocol, response code, '
                 'or network policy is wrong.\n'
                 '\n'
                 'Cloud networking uses new product vocabulary, but the questions remain familiar.\n'
                 '\n'
                 'Which address range contains the workload? Which subnet is it in? Which route applies? '
                 'Which gateway provides the next path? Which security control allows or denies the traffic? '
                 'Where does name resolution point?\n'
                 '\n'
                 'The same model applies to delivery systems. A CI runner needs to reach source control. A '
                 'build needs to reach package repositories. A deployment may need to reach a container '
                 'registry. An application needs to reach its database. Monitoring needs to reach health and '
                 'metrics endpoints.\n'
                 '\n'
                 'Treat each dependency as a communication path that can be named, tested, and observed.\n'
                 '\n'
                 'When a platform feels complicated, translate the abstraction back into fundamentals: name, '
                 'address, route, port, protocol, policy, and application behavior.\n'
                 '\n'
                 'That translation is one of the most useful networking habits you can carry into Docker, '
                 'AWS, Kubernetes, CI/CD, and production operations.\n'
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
 'objectives': ['Explain container network namespaces and published ports.',
                'Describe service discovery in dynamic systems.',
                'Separate reverse-proxy/load-balancer connection legs.',
                'Translate cloud networking concepts into routing and policy fundamentals.',
                'Trace networking dependencies in a DevOps delivery path.'],
 'content': [{'heading': 'The fundamentals do not disappear in the cloud',
              'body': 'Containers, Kubernetes, load balancers, and cloud networks add abstraction, but '
                      'packets still use addresses, routes, ports, DNS, transport protocols, and application '
                      'protocols.'},
             {'heading': 'Container networking creates new boundaries',
              'body': 'A container normally has its own network namespace and interfaces. Publishing a port '
                      'creates a path from a host address and port toward the container. A service bound '
                      'only to localhost in the wrong namespace can look healthy internally while remaining '
                      'unreachable externally.'},
             {'heading': 'Service discovery handles moving workloads',
              'body': 'Docker Compose service names, Kubernetes Services, and cloud DNS provide stable '
                      'identities that map to changing workloads. DNS and service discovery therefore become '
                      'part of application reliability.'},
             {'heading': 'Reverse proxies and load balancers add legs',
              'body': 'A proxy or load balancer accepts one connection and forwards or creates another '
                      'toward a backend. Troubleshoot client-to-edge and edge-to-backend as separate '
                      'communication legs.'},
             {'heading': 'Cloud networks are routed networks with policy',
              'body': 'VPCs contain address ranges and subnets. Route tables decide where traffic goes. '
                      'Gateways create paths. Security groups, ACLs, and firewalls enforce policy.'},
             {'heading': 'DevOps depends on communication paths',
              'body': 'CI/CD, registries, databases, APIs, monitoring, deployments, DNS, certificates, and '
                      'health checks all depend on networking. Networking is embedded throughout delivery '
                      'and reliability.'},
             {'heading': 'Localhost is scoped to a network namespace',
              'body': 'On a host, localhost points back to that host. Inside a container, localhost points '
                      'back to that container. Two processes can run on the same physical computer and still '
                      'have different loopback contexts. This distinction explains many container '
                      'connectivity failures.'},
             {'heading': 'Published ports and service ports solve different problems',
              'body': 'A published Docker port creates a host-to-container path, while an internal service '
                      'name and port can provide container-to-container communication. Always identify which '
                      'side of the boundary the client is on before deciding which address and port it '
                      'should use.'},
             {'heading': 'Health checks are real network requests',
              'body': 'Load balancers and orchestrators often decide whether a workload is usable by sending '
                      'health checks. A healthy process can still be removed from service if the '
                      'health-check path, port, protocol, expected status, or security policy is wrong.'},
             {'heading': '502 and 504 responses narrow the investigation',
              'body': "A gateway-generated 502 or 504 is not proof that 'the network is down.' It usually "
                      'proves the client reached an HTTP-speaking intermediary. The next investigation '
                      "should focus on the intermediary's upstream target, connectivity, timeout, and "
                      'backend behavior.'},
             {'heading': 'Every DevOps dependency is a network dependency',
              'body': 'Source control, package repositories, container registries, cloud APIs, databases, '
                      'monitoring endpoints, artifact stores, and deployment targets all require '
                      'communication paths. Mapping those dependencies makes pipeline and runtime failures '
                      'easier to isolate.'}],
 'diagram': {'title': 'A modern application still follows a path',
             'description': 'Abstractions add boundaries, not a replacement for networking fundamentals.',
             'nodes': [{'label': 'Client', 'detail': 'Begins the request.'},
                       {'label': 'DNS / Service discovery', 'detail': 'Finds a stable endpoint.'},
                       {'label': 'Load balancer / Ingress', 'detail': 'Accepts edge traffic.'},
                       {'label': 'Proxy / Service', 'detail': 'Routes traffic toward a workload.'},
                       {'label': 'Container / Pod', 'detail': 'Runs the application listener.'},
                       {'label': 'Database / Dependency', 'detail': 'Receives downstream service traffic.'}],
             'caption': 'Each arrow is a separate network leg with its own addressing, routing, ports, and '
                        'policy.'},
 'engineer_perspective': {'title': 'Translate product vocabulary back to fundamentals',
                          'body': 'When a platform introduces an unfamiliar networking object, ask what it '
                                  'does to names, addresses, routes, ports, state, or policy. That '
                                  'translation keeps the system understandable.'},
 'try_it_yourself': {'title': "Map your application's network legs",
                     'intro': 'Use Ascend or another containerized application as the model.',
                     'steps': ['Draw client → DNS → edge/load balancer → proxy → application → database.',
                               'Identify source, destination, protocol, and port for each leg.',
                               'Mark where routing and security policy apply.',
                               'Mark where TLS begins and ends.',
                               'If using Docker, identify service names and published ports.',
                               'Choose one hypothetical failure and name the exact leg you would test.',
                               'For one containerized service, distinguish host localhost, container '
                               'localhost, the service name, and any published host port.',
                               'Add a health-check leg to your diagram and identify what would make the '
                               'workload appear unhealthy even if its process is running.',
                               'Explain what an HTTP 502 would prove about the client-to-edge leg and what '
                               'it would not prove about the edge-to-backend leg.'],
                     'takeaway': 'Modern infrastructure becomes manageable when every abstraction can be '
                                 'mapped back to a communication path.'},
 'lab': {'title': 'Map a Modern Application Path',
         'instructions': ['Create a Journal entry titled “Lesson 3.8 — Modern DevOps Networking.”',
                          'Map client → DNS → edge/load balancer → proxy → application → database.',
                          'For each leg, identify source, destination, protocol, and port.',
                          'Mark where DNS, routing, security policy, TLS, and health checks apply.',
                          'If using Docker locally, inspect a Compose network and identify service names and '
                          'published ports.',
                          "Explain why localhost inside a container is not the host's localhost.",
                          'Choose one hypothetical failure and identify the exact leg and test that would '
                          'isolate it.',
                          'Write how the same reasoning will transfer later to AWS and Kubernetes.',
                          'Document the difference between a host port, container port, and '
                          'service-discovery name in your example.',
                          'Add one health-check request to the map and identify its source, destination, '
                          'protocol, port, and expected response.',
                          'Create a hypothetical 502 or 504 failure and write the next two '
                          'evidence-gathering steps you would take.']},
 'quiz': [{'question': 'What happens to networking fundamentals in containers?',
           'choices': ['They disappear',
                       'They remain underneath added abstractions',
                       'Only HTTP matters',
                       'IP is eliminated'],
           'correct': 1},
          {'question': 'What does localhost mean inside a container?',
           'choices': ['Every container',
                       'The current network namespace',
                       'The load balancer',
                       'The DNS server'],
           'correct': 1},
          {'question': 'Why are stable service names useful?',
           'choices': ['Workload IPs can change',
                       'TCP has no addresses',
                       'They disable routing',
                       'They replace health checks'],
           'correct': 0},
          {'question': 'A client reaches a load balancer but it cannot reach the backend. What should be '
                       'separated?',
           'choices': ['The connection legs', 'All global DNS', 'Only the browser', 'Git history'],
           'correct': 0},
          {'question': 'What does a load-balancer health check do?',
           'choices': ['Encrypt passwords',
                       'Determine backend eligibility',
                       'Allocate user ports',
                       'Compile code'],
           'correct': 1},
          {'question': 'What does a cloud route table primarily decide?',
           'choices': ['Server ownership',
                       'Where destination traffic should be sent',
                       'Certificate trust',
                       'HTTP method'],
           'correct': 1},
          {'question': 'How should you reason about unfamiliar cloud networking terms?',
           'choices': ['Memorize them alone',
                       'Translate them to destinations, routes, ports, direction, and policy',
                       'Assume cloud fixes networking',
                       'Ignore flow'],
           'correct': 1},
          {'question': 'Why can a containerized app work internally but fail externally?',
           'choices': ['Internal success does not prove binding, publication, or the external path',
                       'Containers cannot use TCP',
                       'DNS only works outside',
                       'HTTP cannot cross namespaces'],
           'correct': 0},
          {'question': 'Which DevOps activity depends on networking?',
           'choices': ['Pulling images',
                       'Reaching databases',
                       'Scraping monitoring endpoints',
                       'All of the above'],
           'correct': 3},
          {'question': 'What is the central troubleshooting idea?',
           'choices': ['Restart every abstraction',
                       'Trace communication through each boundary',
                       'Change firewall first',
                       'Replace DNS with IPs'],
           'correct': 1}],
 'reflection': 'Which modern networking abstraction now feels less mysterious because you can translate it '
               'into fundamentals?'}
