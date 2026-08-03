"""Module 0, Lesson 4: Anatomy of a Modern Application."""

LESSON = {'id': '0-4',
 'title': 'Anatomy of a Modern Application',
 'summary': 'Break a modern application into clients, frontends, APIs, backends, databases, identity, '
            'infrastructure, and observability so you can understand what each layer does and where failures '
            'belong.',
 'duration_minutes': 75,
 'xp': 75,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.4: Anatomy of a Modern Application.\n'
                 '\n'
                 'In the previous lesson, you followed a request as a conversation. You saw names become '
                 'addresses, addresses combine with ports, and HTTP requests move through Tailscale, Docker, '
                 'FastAPI, and PostgreSQL.\n'
                 '\n'
                 'Now we are going to slow that journey down and name the major parts.\n'
                 '\n'
                 'When you tap the Ascend icon, it feels like you opened one thing. But Ascend is not one '
                 'thing. It is a collection of components that cooperate to create one experience.\n'
                 '\n'
                 'That distinction matters because every component has a different responsibility, a '
                 'different failure mode, and a different kind of evidence.\n'
                 '\n'
                 'Let us begin with the client.\n'
                 '\n'
                 'The client is the software acting on behalf of the user. A browser can be a client. A '
                 'native iPhone application can be a client. A command-line tool such as curl can be a '
                 'client. Even another backend service can be a client when it calls an API.\n'
                 '\n'
                 'In Ascend, the Capacitor iOS application contains a web view that runs the React frontend. '
                 'In Chrome, the browser runs that same frontend. The client gathers user input, displays '
                 'information, and sends requests to other services.\n'
                 '\n'
                 'The client should not be trusted with secrets or authoritative business rules. Anything '
                 'delivered to a phone or browser can eventually be inspected. The client can improve the '
                 'user experience, validate obvious mistakes, and guide interaction, but the server must '
                 'still verify important decisions.\n'
                 '\n'
                 'Next is the frontend.\n'
                 '\n'
                 'The frontend is the part of the application the user sees and interacts with. In Ascend, '
                 'React builds lesson pages, module cards, quizzes, progress displays, and the workspace '
                 'switcher. Vite bundles the frontend files for development and production.\n'
                 '\n'
                 'A frontend often includes HTML, CSS, JavaScript, images, icons, and local state. It may '
                 'remember which tab is open or whether a menu is expanded. It also calls backend APIs to '
                 'load or save data.\n'
                 '\n'
                 'This gives us an important diagnostic distinction. If the page does not render at all, the '
                 'problem may involve frontend delivery, routing, JavaScript startup, or the client '
                 'environment. If the page renders but data is missing, the frontend may be healthy while an '
                 'API conversation is failing.\n'
                 '\n'
                 'Now consider the API.\n'
                 '\n'
                 'An API is a contract for communication. It defines what requests are accepted, what data '
                 'must be supplied, what responses are returned, and how failures are represented.\n'
                 '\n'
                 'FastAPI routes such as GET slash lessons slash zero dash four are not the entire backend. '
                 'They are entry points into backend behavior.\n'
                 '\n'
                 'A good API separates the user interface from the internal implementation. The frontend '
                 'does not need to know how PostgreSQL stores a lesson. It asks for a lesson using the API '
                 'contract. The backend is free to change its database queries as long as the API continues '
                 'to honor that contract.\n'
                 '\n'
                 'This is one reason APIs are so important in DevOps. They create boundaries that teams can '
                 'test, monitor, version, secure, and automate.\n'
                 '\n'
                 'Behind the API is the backend.\n'
                 '\n'
                 'The backend contains server-side application logic. It receives requests, validates data, '
                 'applies rules, talks to databases or external services, and returns responses.\n'
                 '\n'
                 'In Ascend, FastAPI loads lesson data, records completion, evaluates quizzes, and returns '
                 'module information. In Forge, the backend handles food entries, workout sessions, training '
                 'programs, water, weight, and other fitness data.\n'
                 '\n'
                 'The backend should be authoritative. The frontend may disable a quiz submission button '
                 'when answers are missing, but the backend must still reject invalid submissions. A user '
                 'can bypass frontend controls. The server must enforce the real rules.\n'
                 '\n'
                 'The backend also acts as an orchestrator. One request may require several internal steps. '
                 'A TruHearing directory request might validate the signed-in user, call Microsoft Graph, '
                 'transform the returned data, combine it with Jamf or Intune information, and send a '
                 'simplified response to React.\n'
                 '\n'
                 'Next is the database.\n'
                 '\n'
                 'A database stores durable application state. Durable means the data survives when a '
                 'process restarts or a container is replaced.\n'
                 '\n'
                 'PostgreSQL can store users, progress, workout entries, settings, and relationships between '
                 'records. The database is not simply a large file. It provides structured queries, '
                 'constraints, transactions, indexes, permissions, and concurrency control.\n'
                 '\n'
                 'A database constraint can prevent impossible data even when application code has a bug. A '
                 'transaction can ensure that several related changes succeed together or fail together. An '
                 'index can make a frequent query dramatically faster.\n'
                 '\n'
                 'This is why data design matters. If the frontend is the face of the application and the '
                 'backend is the decision-maker, the database is the long-term memory.\n'
                 '\n'
                 'But not every piece of information belongs in the database.\n'
                 '\n'
                 'Static lesson content may live in Python files today. Images may live in object storage. '
                 'Temporary values may live in memory or a cache. Secrets should live in a secret-management '
                 'system or protected environment configuration, not in source code. Logs belong in a '
                 'logging system. Metrics belong in a time-series monitoring system.\n'
                 '\n'
                 'Modern applications use different storage systems because different kinds of information '
                 'have different needs.\n'
                 '\n'
                 'Now let us add identity and authorization.\n'
                 '\n'
                 'Authentication answers, “Who are you?” Authorization answers, “What are you allowed to '
                 'do?”\n'
                 '\n'
                 'In the TruHearing portal, Microsoft Entra ID authenticates the user. Microsoft Graph '
                 'permissions and application rules determine which directory information the application '
                 'may read. A successful sign-in does not automatically grant access to every resource.\n'
                 '\n'
                 'This distinction appears in HTTP status codes. Four oh one usually means authentication is '
                 'missing or invalid. Four oh three usually means the identity is known but lacks '
                 'permission.\n'
                 '\n'
                 'Identity is not just a login screen. It is a cross-cutting system that affects the client, '
                 'frontend, backend, API, external services, secrets, logs, and audit records.\n'
                 '\n'
                 'Now consider external services.\n'
                 '\n'
                 'Most modern applications depend on systems they do not fully control. The TruHearing '
                 'portal depends on Microsoft Graph, Intune, Jamf, Exchange, and authentication services. '
                 'Forge may later depend on Apple Health or a food database. Ascend may eventually depend on '
                 'an audio-generation service.\n'
                 '\n'
                 'External services introduce network latency, rate limits, permission boundaries, version '
                 'changes, and outages. A backend should handle these dependencies deliberately with '
                 'timeouts, retries where safe, clear error handling, and useful logs.\n'
                 '\n'
                 'A retry is not automatically safe. Reading data can often be retried. Creating a payment '
                 'or duplicating a record may require an idempotency strategy so the same request does not '
                 'produce repeated side effects.\n'
                 '\n'
                 'Next is infrastructure.\n'
                 '\n'
                 'Infrastructure is the environment that allows the application to run. It includes hosts, '
                 'operating systems, containers, networks, volumes, DNS, firewalls, proxies, certificates, '
                 'and cloud resources.\n'
                 '\n'
                 'On your home server, Docker runs the Ascend frontend and backend containers. Ports publish '
                 'services to the host. Tailscale provides private connectivity. Volumes preserve database '
                 'state. The host operating system supplies CPU, memory, storage, and networking.\n'
                 '\n'
                 'The application code and infrastructure are separate concerns, but they are tightly '
                 'connected. Perfect code cannot respond if the port is blocked. A healthy container cannot '
                 'save data if its volume is missing. A correct certificate cannot help if DNS points to the '
                 'wrong address.\n'
                 '\n'
                 'This is where configuration enters the picture.\n'
                 '\n'
                 'Configuration tells the same application how to behave in a particular environment. API '
                 'addresses, database connection strings, feature flags, log levels, and service endpoints '
                 'are configuration.\n'
                 '\n'
                 'Configuration should be separated from code when values differ between development, '
                 'testing, and production. Hard-coding an old Tailscale address into a frontend build is a '
                 'configuration problem that becomes visible as application behavior.\n'
                 '\n'
                 'Environment variables are common, but they are not magic. Frontend environment values may '
                 'be compiled into the JavaScript bundle during the build. Changing the source environment '
                 'file after the build does not change the already-built application. Backend variables are '
                 'often read when the process starts. Understanding when configuration is evaluated is part '
                 'of understanding the application.\n'
                 '\n'
                 'Now let us talk about containers.\n'
                 '\n'
                 'A container packages an application process with its runtime and dependencies. It gives '
                 'the process an isolated filesystem and network environment. It does not automatically make '
                 'the application reliable, secure, or persistent.\n'
                 '\n'
                 'The frontend container may use Nginx to serve built React files. The backend container '
                 'runs Uvicorn and FastAPI. PostgreSQL may run in another container with a persistent '
                 'volume.\n'
                 '\n'
                 'Docker Compose describes how those services fit together: images, ports, networks, '
                 'environment variables, dependencies, and volumes.\n'
                 '\n'
                 'The Compose file is therefore an architecture document as well as an automation file. It '
                 'tells you what services exist and how they are expected to communicate.\n'
                 '\n'
                 'Now add the reverse proxy.\n'
                 '\n'
                 'A reverse proxy receives requests before the application and forwards them to the correct '
                 'internal service. Nginx, Traefik, and cloud load balancers can perform this role.\n'
                 '\n'
                 'A reverse proxy can provide one public entry point, terminate TLS, route paths or '
                 'hostnames, add headers, compress responses, and balance traffic across multiple '
                 'instances.\n'
                 '\n'
                 'A five oh two response often means the proxy is reachable but its upstream application did '
                 'not provide a valid response. Again, the visible page and the actual failing component can '
                 'be different.\n'
                 '\n'
                 'We also need observability.\n'
                 '\n'
                 'Observability is the ability to understand a system from the evidence it produces. Logs '
                 'describe events. Metrics describe measurements over time. Traces follow a request across '
                 'services.\n'
                 '\n'
                 'A container being “up” tells you only that a process exists. It does not prove the '
                 'application is useful. Health checks can test whether the application can respond. '
                 'Readiness checks can test whether it should receive traffic. Metrics can reveal growing '
                 'latency or errors before users report them.\n'
                 '\n'
                 'For Ascend, useful evidence might include frontend errors, API response status and '
                 'duration, backend logs, process restarts, database connection failures, and user-facing '
                 'workflow tests.\n'
                 '\n'
                 'For the TruHearing portal, you may also need Graph request IDs, permission errors, '
                 'throttling details, and timing across several external systems.\n'
                 '\n'
                 'The final layer is delivery.\n'
                 '\n'
                 'Source code on your Mac is not automatically the application running on your server or '
                 'iPhone. It must be built, packaged, transferred, configured, and started.\n'
                 '\n'
                 'A React build becomes static assets. A Docker build becomes an image. Compose creates '
                 'containers from those images. Capacitor copies web assets into the iOS project. Xcode '
                 'builds and installs the native application.\n'
                 '\n'
                 'Each delivery step creates another version boundary. Your source can be correct while the '
                 'server runs an older image. Your dist folder can be current while the iPhone still '
                 'contains an older copied bundle. Git can contain a fix that has never been deployed.\n'
                 '\n'
                 'This explains why engineers ask not only, “Is the code fixed?” but also, “Which version is '
                 'running where?”\n'
                 '\n'
                 'Let us bring the whole anatomy together with Ascend.\n'
                 '\n'
                 'You tap Lesson zero point four in the iPhone app. The client is the Capacitor application '
                 'and web view. React is the frontend. The frontend calls a FastAPI API. The backend finds '
                 'lesson data and progress. PostgreSQL or the content module provides state. Docker runs the '
                 'services. Tailscale provides a private route. Configuration tells the frontend where the '
                 'API lives. Logs and browser network evidence help you observe the flow. Git, Docker '
                 'builds, Capacitor sync, and Xcode deliver versions to their destinations.\n'
                 '\n'
                 'One user experience. Many components. Many boundaries. One system.\n'
                 '\n'
                 'This is the central lesson: an application is not defined only by its code. It is the '
                 'complete system required to deliver a reliable user outcome.\n'
                 '\n'
                 'When something fails, name the layer. Do not say only, “Ascend is broken.” Ask whether the '
                 'client launched, the frontend rendered, the API request left, the route matched, the '
                 'backend logic succeeded, the database responded, the dependency authorized the request, '
                 'the infrastructure carried the traffic, and the correct version was deployed.\n'
                 '\n'
                 'That vocabulary gives you leverage.\n'
                 '\n'
                 'In the next lesson, we will ask a larger question. If developers write code and operations '
                 'teams run systems, what does DevOps actually connect? We will use the application anatomy '
                 'you learned today to understand why delivery, automation, ownership, and feedback must '
                 'cross team boundaries.\n',
 'content': [{'heading': 'Learning objectives',
              'body': 'By the end of this lesson, you should be able to describe the responsibilities of '
                      'clients, frontends, APIs, backends, databases, identity systems, external services, '
                      'infrastructure, configuration, containers, reverse proxies, observability, and '
                      'delivery pipelines; explain why one user experience depends on many components; and '
                      'identify the most likely layer for a reported symptom.'},
             {'heading': 'One product, many cooperating components',
              'body': 'Users experience Ascend or Forge as a single application, but engineering work '
                      'happens across components. Each component owns a responsibility and exposes '
                      'boundaries to other components. Naming those boundaries prevents vague '
                      'troubleshooting and helps teams decide where code, configuration, infrastructure, '
                      'security, or data changes belong.'},
             {'heading': 'The client acts for the user',
              'body': 'A browser, native mobile app, command-line tool, or another service can be a client. '
                      'The client collects input, displays output, and initiates requests. In Ascend, '
                      'Capacitor hosts a React web view on iOS while Chrome can run the same frontend on a '
                      'Mac. Client-side validation improves usability, but authoritative rules must still be '
                      'enforced by the server.'},
             {'heading': 'The frontend creates the experience',
              'body': 'The frontend renders pages, manages interaction state, and calls APIs. Ascend’s React '
                      'frontend builds module cards, lesson tabs, quizzes, and the workspace switcher. If '
                      'the interface renders but data does not load, frontend delivery has succeeded and the '
                      'next investigation should focus on the API request, response, or rendering logic.'},
             {'heading': 'The API is a contract',
              'body': 'An API defines accepted requests and expected responses. It separates a user '
                      'interface from backend implementation details. A route such as GET /lessons/0-4 '
                      'allows the frontend to request lesson data without knowing whether the backend reads '
                      'a Python file, PostgreSQL, or another service. Stable contracts let clients and '
                      'servers evolve independently.'},
             {'heading': 'The backend owns server-side decisions',
              'body': 'The backend validates requests, applies business rules, coordinates dependencies, and '
                      'returns responses. FastAPI powers lesson retrieval, completion, and quiz evaluation '
                      'in Ascend. Forge’s backend handles workouts, food, water, and training programs. '
                      'Important authorization and data-integrity decisions must be enforced here, not only '
                      'in the frontend.'},
             {'heading': 'The database is durable memory',
              'body': 'A database stores state that must survive process and container replacement. '
                      'PostgreSQL adds structured queries, constraints, transactions, indexes, permissions, '
                      'and concurrency controls. Not every asset belongs in a relational database: static '
                      'files, secrets, logs, metrics, and temporary cache data have different storage '
                      'requirements.'},
             {'heading': 'Identity crosses every layer',
              'body': 'Authentication establishes identity; authorization determines allowed actions. In the '
                      'TruHearing portal, Entra ID authenticates the user while Graph permissions and '
                      'application rules control access. Identity affects tokens, API requests, backend '
                      'validation, secrets, external-service permissions, logging, and auditing.'},
             {'heading': 'External services expand the system boundary',
              'body': 'Applications often depend on services outside their direct control. The TruHearing '
                      'portal relies on Graph, Intune, Jamf, Exchange, and Entra ID. These dependencies add '
                      'latency, throttling, permissions, version changes, and outages. Timeouts, safe retry '
                      'behavior, clear errors, and correlation identifiers become part of application '
                      'design.'},
             {'heading': 'Infrastructure makes execution possible',
              'body': 'Hosts, operating systems, networks, ports, firewalls, DNS, certificates, volumes, and '
                      'cloud resources provide the environment in which code runs. Docker on your home '
                      'server packages Ascend services, Tailscale supplies private connectivity, and '
                      'persistent storage protects data. Healthy code cannot overcome an unavailable route '
                      'or missing volume.'},
             {'heading': 'Configuration connects code to an environment',
              'body': 'Configuration includes API addresses, database URLs, feature flags, log levels, and '
                      'external endpoints. Values may be read at build time or runtime. Frontend environment '
                      'variables are often compiled into a bundle, while backend variables are commonly '
                      'loaded at startup. Knowing when configuration becomes fixed helps explain stale '
                      'builds and mismatched deployments.'},
             {'heading': 'Containers package processes, not entire outcomes',
              'body': 'A container bundles an application process with its runtime and dependencies. Docker '
                      'Compose describes multiple services, networks, ports, volumes, and environment '
                      'values. A running container proves that a process exists; it does not prove that the '
                      'user workflow, database connection, or external dependency is healthy.'},
             {'heading': 'Reverse proxies create controlled entry points',
              'body': 'A reverse proxy such as Nginx can terminate TLS, route traffic, add headers, compress '
                      'responses, and forward requests to internal services. A 502 response often means the '
                      'proxy answered but could not obtain a valid upstream response. The component '
                      'displaying the error may not be the component that failed.'},
             {'heading': 'Observability turns behavior into evidence',
              'body': 'Logs describe events, metrics reveal trends, and traces follow requests across '
                      'services. Health checks test availability, while readiness checks determine whether '
                      'an instance should receive traffic. Effective observability lets engineers connect a '
                      'user symptom to the component and version responsible for it.'},
             {'heading': 'Delivery creates version boundaries',
              'body': 'Source code must be built, packaged, copied, configured, and started before users '
                      'experience it. React produces a production bundle, Docker produces images, Compose '
                      'creates containers, Capacitor copies assets, and Xcode installs an iOS build. A fix '
                      'can exist in Git while an older version continues running elsewhere.'},
             {'heading': 'Ascend as a complete system',
              'body': 'An Ascend lesson request crosses the Capacitor client, React frontend, FastAPI API '
                      'and backend, lesson or database storage, Docker infrastructure, Tailscale networking, '
                      'environment configuration, and deployment process. The application is the complete '
                      'system required to deliver the lesson reliably—not merely the React or Python source '
                      'code.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'When someone says an application is broken, translate that statement into layers. Ask '
                      'whether the client launched, frontend rendered, request left, API route matched, '
                      'backend logic completed, data was retrieved, authorization succeeded, infrastructure '
                      'carried the traffic, and the intended version was deployed. Precise vocabulary '
                      'produces precise tests.'},
             {'heading': 'Takeaway',
              'body': 'A modern application is a system of contracts and responsibilities. Understanding its '
                      'anatomy lets you locate failures, design safer changes, communicate clearly, and '
                      'recognize where DevOps must connect work across teams.'}],
 'lab': {'title': 'Create an architecture map for Ascend or Forge',
         'instructions': ['Choose Ascend or Forge and select one user workflow, such as opening a lesson or '
                          'saving a workout.',
                          'List the client, frontend, API, backend, data store, identity system, external '
                          'dependencies, infrastructure, configuration, and delivery mechanism involved.',
                          'Draw the complete workflow from user action to final rendered result. Use arrows '
                          'to represent requests, responses, builds, or data flows.',
                          'For every component, write its primary responsibility in one sentence and one '
                          'responsibility it should not own.',
                          'For every boundary, identify the contract: URL or route, protocol, data format, '
                          'authentication method, port, file, environment variable, or deployment artifact.',
                          'Add at least ten realistic failure modes and place each one at the layer where it '
                          'originates.',
                          'For every failure mode, write one piece of evidence that would support it and one '
                          'tool that could collect that evidence.',
                          'Identify which state is durable, temporary, compiled into a build, stored in a '
                          'volume, or retrieved from an external service.',
                          'Write a version path showing how a source-code change reaches the browser, Docker '
                          'host, and iPhone application.',
                          'Finish by writing a five-sentence incident explanation that identifies the user '
                          'impact, last successful layer, first failing layer, evidence, and next test.']},
 'quiz': [{'question': 'What is the strongest definition of a client?',
           'choices': ['Only a desktop web browser',
                       'Software that acts on behalf of a user or another service to make requests',
                       'The database process',
                       'A Docker volume'],
           'correct': 1},
          {'question': 'The Ascend interface renders, but lesson data does not appear. What is already '
                       'partly verified?',
           'choices': ['Frontend delivery and rendering',
                       'Every backend dependency',
                       'Database writes',
                       'The complete workflow'],
           'correct': 0},
          {'question': 'Why is an API described as a contract?',
           'choices': ['It forces the frontend and database to use the same programming language',
                       'It defines accepted requests and expected responses across a boundary',
                       'It replaces authentication',
                       'It stores container images'],
           'correct': 1},
          {'question': 'Which responsibility belongs most strongly to the backend?',
           'choices': ['Trusting every value sent by the browser',
                       'Enforcing authoritative business and authorization rules',
                       'Displaying CSS animations',
                       'Managing the iPhone home screen'],
           'correct': 1},
          {'question': 'What makes database state durable?',
           'choices': ['It remains available beyond a single application process or container lifecycle',
                       'It is always stored in JavaScript',
                       'It cannot be changed',
                       'It requires no backup'],
           'correct': 0},
          {'question': 'What is the difference between authentication and authorization?',
           'choices': ['Authentication identifies who you are; authorization determines what you may do',
                       'Authentication selects a port; authorization resolves DNS',
                       'They mean exactly the same thing',
                       'Authorization happens only in React'],
           'correct': 0},
          {'question': 'Why can changing a frontend environment file fail to change the running app?',
           'choices': ['Frontend values may have been compiled into an existing production bundle',
                       'Browsers cannot use environment values',
                       'Docker deletes all configuration',
                       'FastAPI controls all React variables'],
           'correct': 0},
          {'question': 'What does a running container prove?',
           'choices': ['The entire user workflow is healthy',
                       'A process exists, but dependencies and outcomes still require verification',
                       'The database is backed up',
                       'The newest Git commit is deployed'],
           'correct': 1},
          {'question': 'What does an HTTP 502 commonly suggest in a proxied architecture?',
           'choices': ['The reverse proxy was reachable but its upstream service did not return a valid '
                       'response',
                       'The browser cannot render CSS',
                       'Authentication definitely succeeded',
                       'PostgreSQL deleted the data'],
           'correct': 0},
          {'question': 'Why are delivery steps part of application anatomy?',
           'choices': ['Because source code and the running version can differ across environments',
                       'Because Git automatically installs iPhone apps',
                       'Because builds eliminate configuration',
                       'Because containers always use the newest code'],
           'correct': 0}],
 'diagram': {'title': 'The layers behind one Ascend lesson',
             'description': 'One user action crosses several components with different responsibilities.',
             'nodes': [{'label': 'Client',
                        'detail': 'The iPhone app, browser, or another caller initiates the workflow.'},
                       {'label': 'React frontend',
                        'detail': 'Renders the experience, manages interaction, and calls the API.'},
                       {'label': 'API contract',
                        'detail': 'Defines the request route, method, data, authentication, and response.'},
                       {'label': 'FastAPI backend',
                        'detail': 'Validates, applies rules, coordinates dependencies, and returns results.'},
                       {'label': 'Data and identity',
                        'detail': 'PostgreSQL, lesson content, Entra ID, or external services supply state '
                                  'and permissions.'},
                       {'label': 'Infrastructure',
                        'detail': 'Docker, host networking, ports, volumes, Tailscale, and proxies keep '
                                  'services reachable.'},
                       {'label': 'Delivery and observability',
                        'detail': 'Git, builds, images, Capacitor, Xcode, logs, metrics, and health checks '
                                  'determine what runs and how it is understood.'}],
             'caption': 'The application is the complete path that delivers a reliable user outcome. Code is '
                        'essential, but it is only one layer.'},
 'engineer_perspective': {'title': 'Name the layer before naming the cause',
                          'body': 'A vague report such as “the app is broken” encourages random changes. An '
                                  'engineer first identifies whether the symptom belongs to the client, '
                                  'frontend, API, backend, data, identity, dependency, infrastructure, '
                                  'configuration, or delivery layer. The layer is not automatically the root '
                                  'cause, but it gives the investigation a precise starting boundary.'},
 'try_it_yourself': {'title': 'Compare source, build, container, and client versions',
                     'intro': 'Use Ascend to see how one codebase becomes several running artifacts.',
                     'steps': ['Open the Ascend repository and identify the React source file, backend '
                               'source file, Dockerfiles, Compose file, Capacitor configuration, and iOS '
                               'project.',
                               'Run git log -1 --oneline and record the current source commit.',
                               'Run docker compose ps and docker image ls to identify the running services '
                               'and images.',
                               'Open the browser Network panel and record the frontend address and one '
                               'backend request address.',
                               'Locate frontend/dist and ios/App/App/public after a Capacitor sync. Explain '
                               'how each relates to the source files.',
                               'Write one scenario where Git is current but Docker is stale, and one where '
                               'Docker is current but the iPhone bundle is stale.'],
                     'takeaway': 'A modern application exists in several forms: source, build artifacts, '
                                 'container images, running processes, persisted data, and installed '
                                 'clients. Version awareness is part of troubleshooting.'},
 'reflection': 'Choose Ascend, Forge, or the TruHearing portal and explain its anatomy in your own words. '
               'Which component did you previously think of as “the application” by itself? Which other '
               'components are required to deliver the complete user outcome? Identify one failure you '
               'experienced and reclassify it by client, frontend, API, backend, data, identity, dependency, '
               'infrastructure, configuration, observability, or delivery layer.'}
