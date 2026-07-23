MODULES = [
    {
        "id": "module-0",
        "number": 0,
        "title": "DevOps Foundations and Systems Thinking",
        "subtitle": "Build the mindset before learning the tools.",
        "status": "active",
        "lessons": [
            {
                "id": "0-1",
                "title": "How Engineers Think",
                "summary": "Systems thinking, scope reduction, and building useful hypotheses.",
                "duration_minutes": 20,
                "xp": 25,
                "audio_script": """Welcome to The Journey. Today we are learning how engineers think.

A beginner sees a broken page and asks, “What should I restart?” An experienced engineer asks, “What part of the system is failing, who is affected, and what evidence do I have?”

Your eleven years in IT already gave you an advantage. You know how to ask what a user was doing, what they expected, when it last worked, whether everyone is affected, and whether the issue can be reproduced. DevOps extends that same reasoning into application delivery, infrastructure, networking, automation, and cloud systems.

The goal is not to memorize a longer list of tools. The goal is to understand how the pieces interact. A browser talks to a frontend. The frontend calls an API. The API may talk to Microsoft Graph or a database. Each step is a potential point of delay or failure.

The central principle is simple: understand before you change. Scope the issue, form a hypothesis, gather evidence, and test one change at a time.

Your reflection question is: when a system behaves unexpectedly, what questions help you reduce uncertainty before touching anything?""",
                "content": [
                    {"heading": "Everything is a system", "body": "A production application is not one thing. It is a chain of connected layers: user, browser, frontend, API, authentication, external services, database, server, network, logging, and monitoring."},
                    {"heading": "Reduce the scope", "body": "Ask whether the issue affects one person or everyone, one page or the entire app, one action or every action, and whether the interface loads before the data stalls."},
                    {"heading": "Build hypotheses", "body": "Do not choose a cause immediately. Build a list of plausible causes, then eliminate them using evidence."},
                    {"heading": "Engineer principle", "body": "Understand. Do not memorize."}
                ],
                "lab": {
                    "title": "Map a slow application",
                    "instructions": [
                        "Choose your Directory App or Forge.",
                        "Draw the request path from browser to final response.",
                        "List at least one possible failure at each layer.",
                        "Write the first five questions you would ask a user reporting slowness."
                    ]
                },
                "quiz": [
                    {
                        "question": "What is the best first response to a vague report that an app is slow?",
                        "choices": ["Restart the server", "Redeploy immediately", "Narrow the scope and reproduce the issue", "Clear every cache"],
                        "correct": 2
                    },
                    {
                        "question": "Why do experienced engineers form multiple hypotheses?",
                        "choices": ["To delay fixing the issue", "To avoid assuming the first idea is correct", "Because logs are unnecessary", "Because every issue is caused by the network"],
                        "correct": 1
                    },
                    {
                        "question": "Which statement best represents systems thinking?",
                        "choices": ["Only code can cause application failures", "Each layer can affect the behavior of the entire system", "The user is usually the problem", "Restarting is always the fastest solution"],
                        "correct": 1
                    }
                ],
                "reflection": "Compared with the version of yourself that started this lesson, what can you do now that you could not do before?"
            },
            {
                "id": "0-2",
                "title": "Evidence Before Action",
                "summary": "Use browser tools, logs, metrics, and controlled tests instead of guessing.",
                "duration_minutes": 25,
                "xp": 25,
                "audio_script": """Welcome back to The Journey.

Today we are focusing on evidence before action. In support work, it is tempting to reboot, restart, or clear a cache because those actions sometimes work. But a successful restart does not necessarily reveal the cause. It may also erase evidence.

A stronger troubleshooting loop is: observe, form a hypothesis, gather evidence, test one thing, measure the result, and either keep or reject the hypothesis.

Imagine the Users page takes thirty seconds to show data. The layout appears immediately, every user is affected, and other pages load normally. That tells us the browser can reach the frontend. It also suggests the problem is connected to the Users page data path.

Open browser developer tools and inspect the request. Did it stay pending? What was the status code? Did the server take twenty-nine seconds to respond, or did the response arrive quickly while React froze afterward?

Then compare that evidence with backend logs, server CPU and memory, and external service behavior. The goal is to locate where time is being spent.

The principle for today is: measure the failing layer before changing the system.""",
                "content": [
                    {"heading": "The troubleshooting loop", "body": "Observe → hypothesize → gather evidence → test one change → measure → accept or reject the hypothesis."},
                    {"heading": "Browser evidence", "body": "Use the Network tab to inspect status codes, timing, pending requests, payload size, and duplicate calls."},
                    {"heading": "Backend evidence", "body": "Use application logs to confirm whether the request reached the backend, where it paused, and whether errors occurred."},
                    {"heading": "Infrastructure evidence", "body": "Inspect CPU, RAM, disk, service state, and network behavior. A healthy application can still be slowed by unhealthy infrastructure."}
                ],
                "lab": {
                    "title": "Trace a slow request",
                    "instructions": [
                        "Open browser developer tools on one of your applications.",
                        "Reload a data-heavy page.",
                        "Identify the slowest request.",
                        "Record its status, duration, and response size.",
                        "Write one hypothesis supported by the evidence and one hypothesis the evidence makes less likely."
                    ]
                },
                "quiz": [
                    {
                        "question": "Why can restarting too early be harmful?",
                        "choices": ["It always damages the server", "It can erase useful evidence", "It prevents users from logging in forever", "It disables monitoring"],
                        "correct": 1
                    },
                    {
                        "question": "A request takes 30 seconds, with 29 seconds spent waiting for the server. Which layer should be investigated first?",
                        "choices": ["Frontend color scheme", "Backend or downstream dependency", "Keyboard driver", "Monitor refresh rate"],
                        "correct": 1
                    },
                    {
                        "question": "What makes a troubleshooting test useful?",
                        "choices": ["Changing several variables at once", "Measuring the result of one controlled change", "Avoiding logs", "Assuming the last deployment is always responsible"],
                        "correct": 1
                    }
                ],
                "reflection": "How has your existing end-user troubleshooting experience prepared you to diagnose application and infrastructure problems?"
            },
            {
                "id": "0-3",
                "title": "The Internet Is Computers Talking",
                "summary": "Trace requests as conversations through DNS, networks, servers, applications, and dependencies.",
                "duration_minutes": 30,
                "xp": 30,
                "audio_script": """Welcome back to The Journey.

The internet can feel mysterious, but at its core it is computers having structured conversations.

When you enter a website address, the browser first needs to learn where that name lives. DNS provides an IP address. The browser then establishes a connection, negotiates security, and asks a server for a resource. The server may ask an application, database, authentication provider, or external API for additional information before returning a response.

When an application does not load, ask which conversation failed. Did DNS resolve the name? Could the browser reach the server? Did TLS succeed? Did the reverse proxy route the request? Did the application respond? Did the application reach its database or external dependency?

Thinking in conversations lets you trace a request in order instead of jumping randomly between components.

Your task is to map the login flow for your Directory App from the browser through authentication and finally to the home page.""",
                "content": [
                    {"heading": "Names and addresses", "body": "DNS translates a human-readable name into an IP address that a computer can connect to."},
                    {"heading": "Connections", "body": "The browser connects to a server over a network and may negotiate TLS before sending an HTTP request."},
                    {"heading": "Routing", "body": "A reverse proxy or load balancer can receive the request and route it to the correct application service."},
                    {"heading": "Dependencies", "body": "The application may depend on authentication, databases, caches, or external APIs before it can answer."},
                    {"heading": "Engineer principle", "body": "When a system fails, identify which conversation stopped succeeding."}
                ],
                "lab": {
                    "title": "Map the login conversation",
                    "instructions": [
                        "Start with the user entering the application URL.",
                        "Include DNS, browser, server, frontend, authentication provider, backend, and external APIs.",
                        "Write what each component asks and what it returns.",
                        "Mark at least five possible failure points."
                    ]
                },
                "quiz": [
                    {
                        "question": "What is DNS primarily responsible for?",
                        "choices": ["Rendering React components", "Translating names into IP addresses", "Storing user passwords", "Building Docker images"],
                        "correct": 1
                    },
                    {
                        "question": "Why is the 'conversation' model useful?",
                        "choices": ["It eliminates the need for logs", "It helps trace failures in order through the system", "It proves every problem is DNS", "It replaces networking knowledge"],
                        "correct": 1
                    },
                    {
                        "question": "Which component commonly routes incoming web requests to an application service?",
                        "choices": ["Reverse proxy", "Text editor", "Monitor", "Package manager"],
                        "correct": 0
                    }
                ],
                "reflection": "Which part of a web request path feels most familiar, and which part do you most want to understand better?"
            }
        ]
    },
    {
        "id": "module-1",
        "number": 1,
        "title": "Git and Collaborative Source Control",
        "subtitle": "Repositories, commits, branches, merges, pull requests, tags, and recovery.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-2",
        "number": 2,
        "title": "Linux and the Command Line",
        "subtitle": "Filesystems, users, permissions, processes, services, logs, SSH, and shell fundamentals.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-3",
        "number": 3,
        "title": "Networking and Web Fundamentals",
        "subtitle": "DNS, TCP/IP, HTTP, TLS, ports, routing, proxies, and firewalls.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-4",
        "number": 4,
        "title": "Docker and Containers",
        "subtitle": "Images, containers, Dockerfiles, Compose, volumes, networks, registries, tags, and rollback.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-5",
        "number": 5,
        "title": "CI/CD Pipelines",
        "subtitle": "Automated testing, builds, artifacts, deployment strategies, and pipeline troubleshooting.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-6",
        "number": 6,
        "title": "AWS and Cloud Fundamentals",
        "subtitle": "IAM, billing safety, EC2, S3, VPC, RDS, CloudWatch, ECS, and application deployment.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-7",
        "number": 7,
        "title": "Infrastructure as Code",
        "subtitle": "Terraform fundamentals, state, modules, environments, and safe infrastructure changes.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-8",
        "number": 8,
        "title": "Monitoring, Logging, and Reliability",
        "subtitle": "Metrics, logs, traces, health checks, dashboards, alerts, incidents, and postmortems.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-9",
        "number": 9,
        "title": "Security and Secrets",
        "subtitle": "Least privilege, secret management, patching, vulnerability awareness, HTTPS, and secure delivery.",
        "status": "locked",
        "lessons": []
    },
    {
        "id": "module-10",
        "number": 10,
        "title": "Capstone Deployment",
        "subtitle": "Build, deploy, monitor, document, and recover a complete production-style application.",
        "status": "locked",
        "lessons": []
    }
]

ACHIEVEMENTS = [
    {"id": "first-step", "title": "The First Step", "description": "Complete your first lesson.", "xp": 20},
    {"id": "conversation-mapper", "title": "Conversation Mapper", "description": "Complete Module 0.3.", "xp": 30},
    {"id": "module-zero", "title": "Systems Explorer", "description": "Complete every lesson in Module 0.", "xp": 50},
]
