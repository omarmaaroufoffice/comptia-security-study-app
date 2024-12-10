EXAM_TOPICS = {
    "1.0": {
        "name": "General Security Concepts",
        "weight": 12,
        "subtopics": {
            "1.1": {
                "name": "Compare and contrast various types of security controls",
                "topics": {
                    "1.1.1": "Categories of controls",
                    "1.1.1.1": "Technical controls",
                    "1.1.1.2": "Managerial controls",
                    "1.1.1.3": "Operational controls",
                    "1.1.1.4": "Physical controls",
                    "1.1.2": "Control types",
                    "1.1.2.1": "Preventive controls",
                    "1.1.2.2": "Deterrent controls",
                    "1.1.2.3": "Detective controls",
                    "1.1.2.4": "Corrective controls",
                    "1.1.2.5": "Compensating controls",
                    "1.1.2.6": "Directive controls"
                }
            },
            "1.2": {
                "name": "Summarize fundamental security concepts",
                "topics": {
                    "1.2.1": "CIA Triad",
                    "1.2.1.1": "Confidentiality",
                    "1.2.1.2": "Integrity",
                    "1.2.1.3": "Availability",
                    "1.2.2": "Non-repudiation",
                    "1.2.3": "Authentication, Authorization, and Accounting (AAA)",
                    "1.2.3.1": "Authenticating people",
                    "1.2.3.2": "Authenticating systems",
                    "1.2.3.3": "Authorization models",
                    "1.2.4": "Gap analysis",
                    "1.2.5": "Zero Trust concepts",
                    "1.2.5.1": "Control Plane",
                    "1.2.5.1.1": "Adaptive identity",
                    "1.2.5.1.2": "Threat scope reduction",
                    "1.2.5.1.3": "Policy-driven access control",
                    "1.2.5.1.4": "Policy Administrator",
                    "1.2.5.1.5": "Policy Engine",
                    "1.2.5.2": "Data Plane",
                    "1.2.5.2.1": "Implicit trust zones",
                    "1.2.5.2.2": "Subject/System",
                    "1.2.5.2.3": "Policy Enforcement Point",
                    "1.2.6": "Physical security measures",
                    "1.2.6.1": "Bollards",
                    "1.2.6.2": "Access control vestibule",
                    "1.2.6.3": "Fencing",
                    "1.2.6.4": "Video surveillance",
                    "1.2.6.5": "Security guard",
                    "1.2.6.6": "Access badge",
                    "1.2.6.7": "Lighting",
                    "1.2.6.8": "Sensors",
                    "1.2.6.8.1": "Infrared",
                    "1.2.6.8.2": "Pressure",
                    "1.2.6.8.3": "Microwave",
                    "1.2.6.8.4": "Ultrasonic",
                    "1.2.7": "Deception and disruption technology",
                    "1.2.7.1": "Honeypot",
                    "1.2.7.2": "Honeynet",
                    "1.2.7.3": "Honeyfile",
                    "1.2.7.4": "Honeytoken"
                }
            },
            "1.3": {
                "name": "Explain the importance of change management processes",
                "topics": {
                    "1.3.1": "Business processes impacting security operation",
                    "1.3.1.1": "Approval process",
                    "1.3.1.2": "Ownership",
                    "1.3.1.3": "Stakeholders",
                    "1.3.1.4": "Impact analysis",
                    "1.3.1.5": "Test results",
                    "1.3.1.6": "Backout plan",
                    "1.3.1.7": "Maintenance window",
                    "1.3.1.8": "Standard operating procedure",
                    "1.3.2": "Technical implications",
                    "1.3.2.1": "Allow lists/deny lists",
                    "1.3.2.2": "Restricted activities",
                    "1.3.2.3": "Downtime",
                    "1.3.2.4": "Service restart",
                    "1.3.2.5": "Application restart",
                    "1.3.2.6": "Legacy applications",
                    "1.3.2.7": "Dependencies",
                    "1.3.3": "Documentation",
                    "1.3.3.1": "Updating diagrams",
                    "1.3.3.2": "Updating policies/procedures",
                    "1.3.4": "Version control"
                }
            },
            "1.4": {
                "name": "Explain the importance of using appropriate cryptographic solutions",
                "topics": {
                    "1.4.1": "Public key infrastructure (PKI)",
                    "1.4.1.1": "Public key",
                    "1.4.1.2": "Private key",
                    "1.4.1.3": "Key escrow",
                    "1.4.2": "Encryption types and considerations",
                    "1.4.2.1": "Full-disk encryption",
                    "1.4.2.2": "Partition encryption",
                    "1.4.2.3": "File encryption",
                    "1.4.2.4": "Volume encryption",
                    "1.4.2.5": "Database encryption",
                    "1.4.2.6": "Record encryption",
                    "1.4.2.7": "Transport/communication encryption",
                    "1.4.2.8": "Asymmetric encryption",
                    "1.4.2.9": "Symmetric encryption",
                    "1.4.2.10": "Key exchange",
                    "1.4.2.11": "Algorithms",
                    "1.4.2.12": "Key length",
                    "1.4.3": "Cryptographic tools and concepts",
                    "1.4.3.1": "Trusted Platform Module (TPM)",
                    "1.4.3.2": "Hardware security module (HSM)",
                    "1.4.3.3": "Key management system",
                    "1.4.3.4": "Secure enclave",
                    "1.4.3.5": "Obfuscation",
                    "1.4.3.5.1": "Steganography",
                    "1.4.3.5.2": "Tokenization",
                    "1.4.3.5.3": "Data masking",
                    "1.4.3.6": "Hashing",
                    "1.4.3.7": "Salting",
                    "1.4.3.8": "Digital signatures",
                    "1.4.3.9": "Key stretching",
                    "1.4.3.10": "Blockchain",
                    "1.4.3.11": "Open public ledger",
                    "1.4.4": "Certificates and certificate management",
                    "1.4.4.1": "Certificate authorities",
                    "1.4.4.2": "Certificate revocation lists (CRLs)",
                    "1.4.4.3": "Online Certificate Status Protocol (OCSP)",
                    "1.4.4.4": "Self-signed certificates",
                    "1.4.4.5": "Third-party certificates",
                    "1.4.4.6": "Root of trust",
                    "1.4.4.7": "Certificate signing request (CSR) generation",
                    "1.4.4.8": "Wildcard certificates"
                }
            }
        }
    },
    "2.0": {
        "name": "Threats, Vulnerabilities, and Mitigations",
        "weight": 22,
        "subtopics": {
            "2.1": {
                "name": "Compare and contrast common threat actors and motivations",
                "topics": {
                    "2.1.1": "Threat actors",
                    "2.1.1.1": "Nation-state",
                    "2.1.1.2": "Unskilled attacker",
                    "2.1.1.3": "Hacktivist",
                    "2.1.1.4": "Insider threat",
                    "2.1.1.5": "Organized crime",
                    "2.1.1.6": "Shadow IT",
                    "2.1.2": "Attributes of actors",
                    "2.1.2.1": "Internal/external",
                    "2.1.2.2": "Resources/funding",
                    "2.1.2.3": "Level of sophistication/capability",
                    "2.1.3": "Motivations",
                    "2.1.3.1": "Data exfiltration",
                    "2.1.3.2": "Espionage",
                    "2.1.3.3": "Service disruption",
                    "2.1.3.4": "Blackmail",
                    "2.1.3.5": "Financial gain",
                    "2.1.3.6": "Philosophical/political beliefs",
                    "2.1.3.7": "Ethical",
                    "2.1.3.8": "Revenge",
                    "2.1.3.9": "Disruption/chaos",
                    "2.1.3.10": "War"
                }
            },
            "2.2": {
                "name": "Explain common threat vectors and attack surfaces",
                "topics": {
                    "2.2.1": "Message-based threats",
                    "2.2.1.1": "Email",
                    "2.2.1.2": "Short Message Service (SMS)",
                    "2.2.1.3": "Instant messaging (IM)",
                    "2.2.2": "Image-based threats",
                    "2.2.3": "File-based threats",
                    "2.2.4": "Voice call threats",
                    "2.2.5": "Removable device threats",
                    "2.2.6": "Software vulnerabilities",
                    "2.2.6.1": "Client-based vs. agentless",
                    "2.2.7": "Unsupported systems and applications",
                    "2.2.8": "Network vulnerabilities",
                    "2.2.8.1": "Wireless",
                    "2.2.8.2": "Wired",
                    "2.2.8.3": "Bluetooth",
                    "2.2.9": "Open service ports",
                    "2.2.10": "Default credentials",
                    "2.2.11": "Supply chain risks",
                    "2.2.11.1": "Managed service providers (MSPs)",
                    "2.2.11.2": "Vendors",
                    "2.2.11.3": "Suppliers",
                    "2.2.12": "Human vectors/social engineering",
                    "2.2.12.1": "Phishing",
                    "2.2.12.2": "Vishing",
                    "2.2.12.3": "Smishing",
                    "2.2.12.4": "Misinformation/disinformation",
                    "2.2.12.5": "Impersonation",
                    "2.2.12.6": "Business email compromise",
                    "2.2.12.7": "Pretexting",
                    "2.2.12.8": "Watering hole",
                    "2.2.12.9": "Brand impersonation",
                    "2.2.12.10": "Typosquatting"
                }
            },
            "2.3": {
                "name": "Explain various types of vulnerabilities",
                "topics": {
                    "2.3.1": "Application vulnerabilities",
                    "2.3.1.1": "Memory injection",
                    "2.3.1.2": "Buffer overflow",
                    "2.3.1.3": "Race conditions",
                    "2.3.1.3.1": "Time-of-check (TOC)",
                    "2.3.1.3.2": "Time-of-use (TOU)",
                    "2.3.1.4": "Malicious update",
                    "2.3.2": "Operating system (OS)-based",
                    "2.3.3": "Web-based vulnerabilities",
                    "2.3.3.1": "SQL injection (SQLi)",
                    "2.3.3.2": "Cross-site scripting (XSS)",
                    "2.3.4": "Hardware vulnerabilities",
                    "2.3.4.1": "Firmware",
                    "2.3.4.2": "End-of-life",
                    "2.3.4.3": "Legacy",
                    "2.3.5": "Virtualization vulnerabilities",
                    "2.3.5.1": "Virtual machine (VM) escape",
                    "2.3.5.2": "Resource reuse",
                    "2.3.6": "Cloud-specific vulnerabilities",
                    "2.3.7": "Supply chain vulnerabilities",
                    "2.3.7.1": "Service provider",
                    "2.3.7.2": "Hardware provider",
                    "2.3.7.3": "Software provider",
                    "2.3.8": "Cryptographic vulnerabilities",
                    "2.3.9": "Misconfiguration vulnerabilities",
                    "2.3.10": "Mobile device vulnerabilities",
                    "2.3.10.1": "Side loading",
                    "2.3.10.2": "Jailbreaking",
                    "2.3.11": "Zero-day vulnerabilities"
                }
            },
            "2.4": {
                "name": "Given a scenario, analyze indicators of malicious activity",
                "topics": {
                    "2.4.1": "Malware attacks",
                    "2.4.1.1": "Ransomware",
                    "2.4.1.2": "Trojan",
                    "2.4.1.3": "Worm",
                    "2.4.1.4": "Spyware",
                    "2.4.1.5": "Bloatware",
                    "2.4.1.6": "Virus",
                    "2.4.1.7": "Keylogger",
                    "2.4.1.8": "Logic bomb",
                    "2.4.1.9": "Rootkit",
                    "2.4.2": "Physical attacks",
                    "2.4.3": "Brute force attacks",
                    "2.4.4": "RFID cloning",
                    "2.4.5": "Environmental attacks",
                    "2.4.6": "Network attacks",
                    "2.4.6.1": "DDoS attacks",
                    "2.4.6.1.1": "Amplified DDoS",
                    "2.4.6.1.2": "Reflected DDoS",
                    "2.4.6.2": "DNS attacks",
                    "2.4.6.3": "Wireless attacks",
                    "2.4.6.4": "On-path attacks",
                    "2.4.6.5": "Credential replay",
                    "2.4.6.6": "Malicious code injection",
                    "2.4.7": "Application attacks",
                    "2.4.7.1": "Injection attacks",
                    "2.4.7.2": "Buffer overflow",
                    "2.4.7.3": "Replay attacks",
                    "2.4.7.4": "Privilege escalation",
                    "2.4.7.5": "Forgery attacks",
                    "2.4.7.6": "Directory traversal",
                    "2.4.8": "Cryptographic attacks",
                    "2.4.8.1": "Downgrade attacks",
                    "2.4.8.2": "Collision attacks",
                    "2.4.8.3": "Birthday attacks",
                    "2.4.9": "Password attacks",
                    "2.4.9.1": "Password spraying",
                    "2.4.9.2": "Brute force methods",
                    "2.4.10": "Attack indicators",
                    "2.4.10.1": "Account lockout",
                    "2.4.10.2": "Concurrent session usage",
                    "2.4.10.3": "Blocked content",
                    "2.4.10.4": "Impossible travel",
                    "2.4.10.5": "Resource consumption",
                    "2.4.10.6": "Resource inaccessibility",
                    "2.4.10.7": "Out-of-cycle logging",
                    "2.4.10.8": "Published/documented indicators",
                    "2.4.10.9": "Missing logs"
                }
            },
            "2.5": {
                "name": "Explain the purpose of mitigation techniques used to secure the enterprise",
                "topics": {
                    "2.5.1": "Network segmentation",
                    "2.5.1.1": "Physical segmentation",
                    "2.5.1.2": "Logical segmentation",
                    "2.5.1.3": "Virtual segmentation",
                    
                    "2.5.2": "Access control",
                    "2.5.2.1": "Access control lists (ACLs)",
                    "2.5.2.2": "Permissions management",
                    "2.5.2.3": "Role-based access",
                    
                    "2.5.3": "Application control",
                    "2.5.3.1": "Application allow listing",
                    "2.5.3.2": "Application block listing",
                    "2.5.3.3": "Application behavior monitoring",
                    
                    "2.5.4": "Isolation techniques",
                    "2.5.4.1": "Network isolation",
                    "2.5.4.2": "Process isolation",
                    "2.5.4.3": "Physical isolation",
                    
                    "2.5.5": "Patch management",
                    "2.5.5.1": "Operating system patches",
                    "2.5.5.2": "Application patches",
                    "2.5.5.3": "Firmware updates",
                    
                    "2.5.6": "Encryption implementation",
                    "2.5.6.1": "Data at rest",
                    "2.5.6.2": "Data in transit",
                    "2.5.6.3": "Data in use",
                    
                    "2.5.7": "Security monitoring",
                    "2.5.7.1": "Log monitoring",
                    "2.5.7.2": "Network monitoring",
                    "2.5.7.3": "System monitoring",
                    "2.5.7.4": "User activity monitoring",
                    
                    "2.5.8": "Least privilege implementation",
                    "2.5.8.1": "User privileges",
                    "2.5.8.2": "Service accounts",
                    "2.5.8.3": "System permissions",
                    
                    "2.5.9": "Configuration enforcement",
                    "2.5.9.1": "Baseline configurations",
                    "2.5.9.2": "Security templates",
                    "2.5.9.3": "Standard builds",
                    
                    "2.5.10": "Decommissioning procedures",
                    "2.5.10.1": "Data sanitization",
                    "2.5.10.2": "Asset disposal",
                    "2.5.10.3": "Documentation updates",
                    
                    "2.5.11": "System hardening",
                    "2.5.11.1": "Encryption implementation",
                    "2.5.11.2": "Endpoint protection installation",
                    "2.5.11.3": "Host-based firewall configuration",
                    "2.5.11.4": "Host-based IPS implementation",
                    "2.5.11.5": "Port and protocol restrictions",
                    "2.5.11.6": "Default password changes",
                    "2.5.11.7": "Unnecessary software removal"
                }
            }
        }
    },
    "3.0": {
        "name": "Security Architecture",
        "weight": 18,
        "subtopics": {
            "3.1": {
                "name": "Compare and contrast security implications of different architecture models",
                "topics": {
                    "3.1.1": "Architecture and infrastructure concepts",
                    "3.1.1.1": "Cloud",
                    "3.1.1.1.1": "Responsibility matrix",
                    "3.1.1.1.2": "Hybrid considerations",
                    "3.1.1.1.3": "Third-party vendors",
                    "3.1.1.2": "Infrastructure as code (IaC)",
                    "3.1.1.3": "Serverless",
                    "3.1.1.4": "Microservices",
                    "3.1.1.5": "Network infrastructure",
                    "3.1.1.5.1": "Physical isolation",
                    "3.1.1.5.2": "Air-gapped systems",
                    "3.1.1.5.3": "Logical segmentation",
                    "3.1.1.5.4": "Software-defined networking (SDN)",
                    "3.1.1.6": "On-premises",
                    "3.1.1.7": "Centralized vs. decentralized",
                    "3.1.1.8": "Containerization",
                    "3.1.1.9": "Virtualization",
                    "3.1.1.10": "IoT",
                    "3.1.1.11": "Industrial control systems (ICS)/SCADA",
                    "3.1.1.12": "Real-time operating system (RTOS)",
                    "3.1.1.13": "Embedded systems",
                    "3.1.1.14": "High availability",
                    
                    "3.1.2": "Architecture considerations",
                    "3.1.2.1": "Availability",
                    "3.1.2.2": "Resilience",
                    "3.1.2.3": "Cost",
                    "3.1.2.4": "Responsiveness",
                    "3.1.2.5": "Scalability",
                    "3.1.2.6": "Ease of deployment",
                    "3.1.2.7": "Risk transference",
                    "3.1.2.8": "Ease of recovery",
                    "3.1.2.9": "Patch availability",
                    "3.1.2.10": "Inability to patch",
                    "3.1.2.11": "Power considerations",
                    "3.1.2.12": "Compute resources"
                }
            },
            "3.2": {
                "name": "Given a scenario, apply security principles to secure enterprise infrastructure",
                "topics": {
                    "3.2.1": "Infrastructure considerations",
                    "3.2.1.1": "Device placement",
                    "3.2.1.2": "Security zones",
                    "3.2.1.3": "Attack surface",
                    "3.2.1.4": "Connectivity",
                    "3.2.1.5": "Failure modes",
                    "3.2.1.5.1": "Fail-open",
                    "3.2.1.5.2": "Fail-closed",
                    "3.2.1.6": "Device attributes",
                    "3.2.1.6.1": "Active vs. passive",
                    "3.2.1.6.2": "Inline vs. tap/monitor",
                    
                    "3.2.2": "Network appliances",
                    "3.2.2.1": "Jump server",
                    "3.2.2.2": "Proxy server",
                    "3.2.2.3": "IPS/IDS",
                    "3.2.2.4": "Load balancer",
                    "3.2.2.5": "Sensors",
                    
                    "3.2.3": "Port security",
                    "3.2.3.1": "802.1X",
                    "3.2.3.2": "Extensible Authentication Protocol (EAP)",
                    
                    "3.2.4": "Firewall types",
                    "3.2.4.1": "Web application firewall (WAF)",
                    "3.2.4.2": "Unified threat management (UTM)",
                    "3.2.4.3": "Next-generation firewall (NGFW)",
                    "3.2.4.4": "Layer 4/Layer 7 firewalls",
                    
                    "3.2.5": "Secure communication/access",
                    "3.2.5.1": "Virtual private network (VPN)",
                    "3.2.5.2": "Remote access",
                    "3.2.5.3": "Tunneling protocols",
                    "3.2.5.3.1": "Transport Layer Security (TLS)",
                    "3.2.5.3.2": "Internet Protocol Security (IPSec)",
                    "3.2.5.4": "Software-defined WAN (SD-WAN)",
                    "3.2.5.5": "Secure access service edge (SASE)",
                    
                    "3.2.6": "Selection of effective controls"
                }
            },
            "3.3": {
                "name": "Compare and contrast concepts and strategies to protect data",
                "topics": {
                    "3.3.1": "Data types",
                    "3.3.1.1": "Regulated data",
                    "3.3.1.2": "Trade secret",
                    "3.3.1.3": "Intellectual property",
                    "3.3.1.4": "Legal information",
                    "3.3.1.5": "Financial information",
                    "3.3.1.6": "Human- and non-human-readable data",
                    
                    "3.3.2": "Data classifications",
                    "3.3.2.1": "Sensitive",
                    "3.3.2.2": "Confidential",
                    "3.3.2.3": "Public",
                    "3.3.2.4": "Restricted",
                    "3.3.2.5": "Private",
                    "3.3.2.6": "Critical",
                    
                    "3.3.3": "General data considerations",
                    "3.3.3.1": "Data states",
                    "3.3.3.1.1": "Data at rest",
                    "3.3.3.1.2": "Data in transit",
                    "3.3.3.1.3": "Data in use",
                    "3.3.3.2": "Data sovereignty",
                    "3.3.3.3": "Geolocation",
                    
                    "3.3.4": "Methods to secure data",
                    "3.3.4.1": "Geographic restrictions",
                    "3.3.4.2": "Encryption",
                    "3.3.4.3": "Hashing",
                    "3.3.4.4": "Masking",
                    "3.3.4.5": "Tokenization",
                    "3.3.4.6": "Obfuscation",
                    "3.3.4.7": "Segmentation",
                    "3.3.4.8": "Permission restrictions"
                }
            },
            "3.4": {
                "name": "Explain the importance of resilience and recovery in security architecture",
                "topics": {
                    "3.4.1": "High availability",
                    "3.4.1.1": "Load balancing vs. clustering",
                    
                    "3.4.2": "Site considerations",
                    "3.4.2.1": "Hot site",
                    "3.4.2.2": "Cold site",
                    "3.4.2.3": "Warm site",
                    "3.4.2.4": "Geographic dispersion",
                    
                    "3.4.3": "Platform diversity",
                    
                    "3.4.4": "Multi-cloud systems",
                    
                    "3.4.5": "Continuity of operations",
                    
                    "3.4.6": "Capacity planning",
                    "3.4.6.1": "People",
                    "3.4.6.2": "Technology",
                    "3.4.6.3": "Infrastructure",
                    
                    "3.4.7": "Testing",
                    "3.4.7.1": "Tabletop exercises",
                    "3.4.7.2": "Fail over",
                    "3.4.7.3": "Simulation",
                    "3.4.7.4": "Parallel processing",
                    
                    "3.4.8": "Backups",
                    "3.4.8.1": "Onsite/offsite",
                    "3.4.8.2": "Frequency",
                    "3.4.8.3": "Encryption",
                    "3.4.8.4": "Snapshots",
                    "3.4.8.5": "Recovery",
                    "3.4.8.6": "Replication",
                    "3.4.8.7": "Journaling",
                    
                    "3.4.9": "Power considerations",
                    "3.4.9.1": "Generators",
                    "3.4.9.2": "Uninterruptible power supply (UPS)"
                }
            }
        }
    },
    "4.0": {
        "name": "Security Operations",
        "weight": 28,
        "subtopics": {
            "4.1": {
                "name": "Given a scenario, apply common security techniques to computing resources",
                "topics": {
                    "4.1.1": "Secure baselines",
                    "4.1.1.1": "Establish baselines",
                    "4.1.1.2": "Deploy baselines",
                    "4.1.1.3": "Maintain baselines",
                    
                    "4.1.2": "Hardening targets",
                    "4.1.2.1": "Mobile devices",
                    "4.1.2.2": "Workstations",
                    "4.1.2.3": "Switches",
                    "4.1.2.4": "Routers",
                    "4.1.2.5": "Cloud infrastructure",
                    "4.1.2.6": "Servers",
                    "4.1.2.7": "ICS/SCADA systems",
                    "4.1.2.8": "Embedded systems",
                    "4.1.2.9": "RTOS",
                    "4.1.2.10": "IoT devices",
                    
                    "4.1.3": "Wireless devices",
                    "4.1.3.1": "Installation considerations",
                    "4.1.3.1.1": "Site surveys",
                    "4.1.3.1.2": "Heat maps",
                    
                    "4.1.4": "Mobile solutions",
                    "4.1.4.1": "Mobile device management (MDM)",
                    "4.1.4.2": "Deployment models",
                    "4.1.4.2.1": "BYOD",
                    "4.1.4.2.2": "COPE",
                    "4.1.4.2.3": "CYOD",
                    "4.1.4.3": "Connection methods",
                    "4.1.4.3.1": "Cellular",
                    "4.1.4.3.2": "Wi-Fi",
                    "4.1.4.3.3": "Bluetooth",
                    
                    "4.1.5": "Wireless security settings",
                    "4.1.5.1": "WPA3",
                    "4.1.5.2": "AAA/RADIUS",
                    "4.1.5.3": "Cryptographic protocols",
                    "4.1.5.4": "Authentication protocols",
                    
                    "4.1.6": "Application security",
                    "4.1.6.1": "Input validation",
                    "4.1.6.2": "Secure cookies",
                    "4.1.6.3": "Static code analysis",
                    "4.1.6.4": "Code signing",
                    
                    "4.1.7": "Sandboxing",
                    
                    "4.1.8": "Monitoring"
                }
            },
            "4.2": {
                "name": "Explain the security implications of proper hardware, software, and data asset management",
                "topics": {
                    "4.2.1": "Acquisition/procurement process",
                    
                    "4.2.2": "Assignment/accounting",
                    "4.2.2.1": "Ownership",
                    "4.2.2.2": "Classification",
                    
                    "4.2.3": "Monitoring/asset tracking",
                    "4.2.3.1": "Inventory management",
                    "4.2.3.2": "Asset enumeration",
                    
                    "4.2.4": "Disposal/decommissioning",
                    "4.2.4.1": "Data sanitization",
                    "4.2.4.2": "Asset destruction",
                    "4.2.4.3": "Certification of destruction",
                    "4.2.4.4": "Data retention requirements"
                }
            },
            "4.3": {
                "name": "Explain various activities associated with vulnerability management",
                "topics": {
                    "4.3.1": "Identification methods",
                    "4.3.1.1": "Vulnerability scanning",
                    "4.3.1.2": "Application security testing",
                    "4.3.1.2.1": "Static analysis",
                    "4.3.1.2.2": "Dynamic analysis",
                    "4.3.1.2.3": "Package monitoring",
                    "4.3.1.3": "Threat feeds",
                    "4.3.1.3.1": "Open-source intelligence (OSINT)",
                    "4.3.1.3.2": "Proprietary/third-party feeds",
                    "4.3.1.3.3": "Information-sharing organizations",
                    "4.3.1.3.4": "Dark web monitoring",
                    "4.3.1.4": "Penetration testing",
                    "4.3.1.5": "Responsible disclosure programs",
                    "4.3.1.5.1": "Bug bounty programs",
                    "4.3.1.6": "System/process auditing",

                    "4.3.2": "Analysis",
                    "4.3.2.1": "Confirmation",
                    "4.3.2.1.1": "False positive identification",
                    "4.3.2.1.2": "False negative identification",
                    "4.3.2.2": "Prioritization",
                    "4.3.2.3": "CVSS scoring",
                    "4.3.2.4": "CVE identification",
                    "4.3.2.5": "Vulnerability classification",
                    "4.3.2.6": "Exposure factor analysis",
                    "4.3.2.7": "Environmental variables",
                    "4.3.2.8": "Industry/organizational impact",
                    "4.3.2.9": "Risk tolerance assessment",

                    "4.3.3": "Vulnerability response and remediation",
                    "4.3.3.1": "Patching",
                    "4.3.3.2": "Insurance",
                    "4.3.3.3": "Segmentation",
                    "4.3.3.4": "Compensating controls",
                    "4.3.3.5": "Exceptions and exemptions",

                    "4.3.4": "Validation of remediation",
                    "4.3.4.1": "Rescanning",
                    "4.3.4.2": "Audit verification",
                    "4.3.4.3": "Testing confirmation",

                    "4.3.5": "Reporting"
                }
            },
            "4.4": {
                "name": "Explain security alerting and monitoring concepts and tools",
                "topics": {
                    "4.4.1": "Monitoring computing resources",
                    "4.4.1.1": "Systems monitoring",
                    "4.4.1.2": "Applications monitoring",
                    "4.4.1.3": "Infrastructure monitoring",

                    "4.4.2": "Activities",
                    "4.4.2.1": "Log aggregation",
                    "4.4.2.2": "Alerting",
                    "4.4.2.3": "Scanning",
                    "4.4.2.4": "Reporting",
                    "4.4.2.5": "Archiving",
                    "4.4.2.6": "Alert response and remediation",
                    "4.4.2.6.1": "Quarantine",
                    "4.4.2.6.2": "Alert tuning",

                    "4.4.3": "Tools",
                    "4.4.3.1": "Security Content Automation Protocol (SCAP)",
                    "4.4.3.2": "Security benchmarks",
                    "4.4.3.3": "Agent-based vs. agentless monitoring",
                    "4.4.3.4": "Security information and event management (SIEM)",
                    "4.4.3.5": "Antivirus/antimalware",
                    "4.4.3.6": "Data loss prevention (DLP)",
                    "4.4.3.7": "SNMP traps",
                    "4.4.3.8": "NetFlow analysis",
                    "4.4.3.9": "Vulnerability scanners"
                }
            },
            "4.5": {
                "name": "Given a scenario, modify enterprise capabilities to enhance security",
                "topics": {
                    "4.5.1": "Firewall configuration",
                    "4.5.1.1": "Rules",
                    "4.5.1.2": "Access lists",
                    "4.5.1.3": "Ports/protocols",
                    "4.5.1.4": "Screened subnets",
                    
                    "4.5.2": "IDS/IPS configuration",
                    "4.5.2.1": "Trend analysis",
                    "4.5.2.2": "Signature management",
                    
                    "4.5.3": "Web filtering",
                    "4.5.3.1": "Agent-based filtering",
                    "4.5.3.2": "Centralized proxy",
                    "4.5.3.3": "URL scanning",
                    "4.5.3.4": "Content categorization",
                    "4.5.3.5": "Block rules",
                    "4.5.3.6": "Reputation filtering",
                    
                    "4.5.4": "Operating system security",
                    "4.5.4.1": "Group Policy",
                    "4.5.4.2": "SELinux",
                    
                    "4.5.5": "Secure protocol implementation",
                    "4.5.5.1": "Protocol selection",
                    "4.5.5.2": "Port selection",
                    "4.5.5.3": "Transport method",
                    
                    "4.5.6": "DNS filtering",
                    
                    "4.5.7": "Email security",
                    "4.5.7.1": "DMARC",
                    "4.5.7.2": "DKIM",
                    "4.5.7.3": "SPF",
                    "4.5.7.4": "Email gateway configuration",
                    
                    "4.5.8": "File integrity monitoring",
                    
                    "4.5.9": "Data loss prevention",
                    
                    "4.5.10": "Network access control",
                    
                    "4.5.11": "EDR/XDR implementation",
                    
                    "4.5.12": "User behavior analytics"
                }
            },
            "4.6": {
                "name": "Given a scenario, implement and maintain identity and access management",
                "topics": {
                    "4.6.1": "User account provisioning/deprovisioning",
                    
                    "4.6.2": "Permission assignments and implications",
                    
                    "4.6.3": "Identity proofing",
                    
                    "4.6.4": "Federation",
                    
                    "4.6.5": "Single sign-on implementations",
                    "4.6.5.1": "LDAP",
                    "4.6.5.2": "OAuth",
                    "4.6.5.3": "SAML",
                    
                    "4.6.6": "Interoperability",
                    
                    "4.6.7": "Attestation",
                    
                    "4.6.8": "Access controls",
                    "4.6.8.1": "Mandatory access control",
                    "4.6.8.2": "Discretionary access control",
                    "4.6.8.3": "Role-based access control",
                    "4.6.8.4": "Rule-based access control",
                    "4.6.8.5": "Attribute-based access control",
                    "4.6.8.6": "Time-of-day restrictions",
                    "4.6.8.7": "Least privilege principles",
                    
                    "4.6.9": "Multifactor authentication",
                    "4.6.9.1": "Implementation methods",
                    "4.6.9.1.1": "Biometrics",
                    "4.6.9.1.2": "Hard/soft authentication tokens",
                    "4.6.9.1.3": "Security keys",
                    "4.6.9.2": "Authentication factors",
                    "4.6.9.2.1": "Something you know",
                    "4.6.9.2.2": "Something you have",
                    "4.6.9.2.3": "Something you are",
                    "4.6.9.2.4": "Somewhere you are",
                    
                    "4.6.10": "Password concepts",
                    "4.6.10.1": "Password best practices",
                    "4.6.10.1.1": "Length requirements",
                    "4.6.10.1.2": "Complexity requirements",
                    "4.6.10.1.3": "Reuse restrictions",
                    "4.6.10.1.4": "Expiration policies",
                    "4.6.10.1.5": "Age requirements",
                    "4.6.10.2": "Password managers",
                    "4.6.10.3": "Passwordless authentication",
                    
                    "4.6.11": "Privileged access management",
                    "4.6.11.1": "Just-in-time permissions",
                    "4.6.11.2": "Password vaulting",
                    "4.6.11.3": "Ephemeral credentials"
                }
            },
            "4.7": {
                "name": "Explain the importance of automation and orchestration related to secure operations",
                "topics": {
                    "4.7.1": "Use cases of automation and scripting",
                    "4.7.1.1": "User provisioning",
                    "4.7.1.2": "Resource provisioning",
                    "4.7.1.3": "Guard rails implementation",
                    "4.7.1.4": "Security group management",
                    "4.7.1.5": "Ticket creation",
                    "4.7.1.6": "Escalation procedures",
                    "4.7.1.7": "Service enabling/disabling",
                    "4.7.1.8": "Access enabling/disabling",
                    "4.7.1.9": "Continuous integration and testing",
                    "4.7.1.10": "API integrations",
                    
                    "4.7.2": "Benefits of automation",
                    "4.7.2.1": "Efficiency/time saving",
                    "4.7.2.2": "Baseline enforcement",
                    "4.7.2.3": "Standard infrastructure configurations",
                    "4.7.2.4": "Secure scaling capabilities",
                    "4.7.2.5": "Employee retention improvement",
                    "4.7.2.6": "Reaction time optimization",
                    "4.7.2.7": "Workforce multiplication",
                    
                    "4.7.3": "Implementation considerations",
                    "4.7.3.1": "Complexity management",
                    "4.7.3.2": "Cost analysis",
                    "4.7.3.3": "Single point of failure risks",
                    "4.7.3.4": "Technical debt management",
                    "4.7.3.5": "Ongoing supportability"
                }
            },
            "4.8": {
                "name": "Explain appropriate incident response activities",
                "topics": {
                    "4.8.1": "Incident response process",
                    "4.8.1.1": "Preparation",
                    "4.8.1.2": "Detection",
                    "4.8.1.3": "Analysis",
                    "4.8.1.4": "Containment",
                    "4.8.1.5": "Eradication",
                    "4.8.1.6": "Recovery",
                    "4.8.1.7": "Lessons learned",
                    
                    "4.8.2": "Training activities",
                    "4.8.2.1": "Tabletop exercises",
                    "4.8.2.2": "Simulations",
                    
                    "4.8.3": "Testing procedures",
                    
                    "4.8.4": "Root cause analysis",
                    
                    "4.8.5": "Threat hunting",
                    
                    "4.8.6": "Digital forensics",
                    "4.8.6.1": "Legal hold",
                    "4.8.6.2": "Chain of custody",
                    "4.8.6.3": "Data acquisition",
                    "4.8.6.4": "Report documentation",
                    "4.8.6.5": "Evidence preservation",
                    "4.8.6.6": "E-discovery procedures"
                }
            },
            "4.9": {
                "name": "Given a scenario, use data sources to support an investigation",
                "topics": {
                    "4.9.1": "Log data sources",
                    "4.9.1.1": "Firewall logs",
                    "4.9.1.2": "Application logs",
                    "4.9.1.3": "Endpoint logs",
                    "4.9.1.4": "OS-specific security logs",
                    "4.9.1.5": "IPS/IDS logs",
                    "4.9.1.6": "Network logs",
                    "4.9.1.7": "Metadata analysis",
                    
                    "4.9.2": "Investigation data sources",
                    "4.9.2.1": "Vulnerability scan results",
                    "4.9.2.2": "Automated reports",
                    "4.9.2.3": "Security dashboards",
                    "4.9.2.4": "Network packet captures"
                }
            }
        }
    },
    "5.0": {
        "name": "Security Program Management and Oversight",
        "weight": 20,
        "subtopics": {
            "5.1": {
                "name": "Summarize elements of effective security governance",
                "topics": {
                    "5.1.1": "Security guidelines",
                    
                    "5.1.2": "Security policies",
                    "5.1.2.1": "Acceptable use policy (AUP)",
                    "5.1.2.2": "Information security policies",
                    "5.1.2.3": "Business continuity policy",
                    "5.1.2.4": "Disaster recovery policy",
                    "5.1.2.5": "Incident response policy",
                    "5.1.2.6": "SDLC policy",
                    "5.1.2.7": "Change management policy",
                    
                    "5.1.3": "Security standards",
                    "5.1.3.1": "Password standards",
                    "5.1.3.2": "Access control standards",
                    "5.1.3.3": "Physical security standards",
                    "5.1.3.4": "Encryption standards",
                    
                    "5.1.4": "Security procedures",
                    "5.1.4.1": "Change management procedures",
                    "5.1.4.2": "Onboarding/offboarding procedures",
                    "5.1.4.3": "Security playbooks",
                    
                    "5.1.5": "External considerations",
                    "5.1.5.1": "Regulatory requirements",
                    "5.1.5.2": "Legal requirements",
                    "5.1.5.3": "Industry requirements",
                    "5.1.5.4": "Local/regional requirements",
                    "5.1.5.5": "National requirements",
                    "5.1.5.6": "Global requirements",
                    
                    "5.1.6": "Monitoring and revision processes",
                    
                    "5.1.7": "Governance structures",
                    "5.1.7.1": "Security boards",
                    "5.1.7.2": "Security committees",
                    "5.1.7.3": "Government entities",
                    "5.1.7.4": "Centralized/decentralized models",
                    
                    "5.1.8": "Roles and responsibilities",
                    "5.1.8.1": "Data owners",
                    "5.1.8.2": "Data controllers",
                    "5.1.8.3": "Data processors",
                    "5.1.8.4": "Data custodians/stewards"
                }
            },
            "5.2": {
                "name": "Explain elements of the risk management process",
                "topics": {
                    "5.2.1": "Risk identification",
                    
                    "5.2.2": "Risk assessment types",
                    "5.2.2.1": "Ad hoc assessment",
                    "5.2.2.2": "Recurring assessment",
                    "5.2.2.3": "One-time assessment",
                    "5.2.2.4": "Continuous assessment",
                    
                    "5.2.3": "Risk analysis methods",
                    "5.2.3.1": "Qualitative analysis",
                    "5.2.3.2": "Quantitative analysis",
                    "5.2.3.3": "Single loss expectancy (SLE)",
                    "5.2.3.4": "Annualized loss expectancy (ALE)",
                    "5.2.3.5": "Annualized rate of occurrence (ARO)",
                    "5.2.3.6": "Probability assessment",
                    "5.2.3.7": "Likelihood assessment",
                    "5.2.3.8": "Exposure factor analysis",
                    "5.2.3.9": "Impact assessment",
                    
                    "5.2.4": "Risk register components",
                    "5.2.4.1": "Key risk indicators",
                    "5.2.4.2": "Risk owners",
                    "5.2.4.3": "Risk thresholds",
                    
                    "5.2.5": "Risk tolerance levels",
                    
                    "5.2.6": "Risk appetite types",
                    "5.2.6.1": "Expansionary",
                    "5.2.6.2": "Conservative",
                    "5.2.6.3": "Neutral",
                    
                    "5.2.7": "Risk management strategies",
                    "5.2.7.1": "Transfer",
                    "5.2.7.2": "Accept",
                    "5.2.7.2.1": "Exemption",
                    "5.2.7.2.2": "Exception",
                    "5.2.7.3": "Avoid",
                    "5.2.7.4": "Mitigate",
                    
                    "5.2.8": "Risk reporting",
                    
                    "5.2.9": "Business impact analysis",
                    "5.2.9.1": "Recovery time objective (RTO)",
                    "5.2.9.2": "Recovery point objective (RPO)",
                    "5.2.9.3": "Mean time to repair (MTTR)",
                    "5.2.9.4": "Mean time between failures (MTBF)"
                }
            },
            "5.3": {
                "name": "Explain the processes associated with third-party risk assessment and management",
                "topics": {
                    "5.3.1": "Vendor assessment",
                    "5.3.1.1": "Penetration testing",
                    "5.3.1.2": "Right-to-audit clause",
                    "5.3.1.3": "Internal audit evidence",
                    "5.3.1.4": "Independent assessments",
                    "5.3.1.5": "Supply chain analysis",
                    
                    "5.3.2": "Vendor selection",
                    "5.3.2.1": "Due diligence",
                    "5.3.2.2": "Conflict of interest",
                    
                    "5.3.3": "Agreement types",
                    "5.3.3.1": "Service-level agreement (SLA)",
                    "5.3.3.2": "Memorandum of agreement (MOA)",
                    "5.3.3.3": "Memorandum of understanding (MOU)",
                    "5.3.3.4": "Master service agreement (MSA)",
                    "5.3.3.5": "Work order (WO)/Statement of work (SOW)",
                    "5.3.3.6": "Non-disclosure agreement (NDA)",
                    "5.3.3.7": "Business partners agreement (BPA)",
                    
                    "5.3.4": "Vendor monitoring",
                    
                    "5.3.5": "Questionnaires",
                    
                    "5.3.6": "Rules of engagement"
                }
            },
            "5.4": {
                "name": "Summarize elements of effective security compliance",
                "topics": {
                    "5.4.1": "Compliance reporting",
                    "5.4.1.1": "Internal reporting",
                    "5.4.1.2": "External reporting",
                    
                    "5.4.2": "Non-compliance consequences",
                    "5.4.2.1": "Fines",
                    "5.4.2.2": "Sanctions",
                    "5.4.2.3": "Reputational damage",
                    "5.4.2.4": "License loss",
                    "5.4.2.5": "Contractual impacts",
                    
                    "5.4.3": "Compliance monitoring",
                    "5.4.3.1": "Due diligence/care",
                    "5.4.3.2": "Attestation and acknowledgement",
                    "5.4.3.3": "Internal monitoring",
                    "5.4.3.4": "External monitoring",
                    "5.4.3.5": "Automated monitoring",
                    
                    "5.4.4": "Privacy considerations",
                    "5.4.4.1": "Legal implications",
                    "5.4.4.1.1": "Local/regional requirements",
                    "5.4.4.1.2": "National requirements",
                    "5.4.4.1.3": "Global requirements",
                    "5.4.4.2": "Data subject rights",
                    "5.4.4.3": "Controller vs. processor roles",
                    "5.4.4.4": "Data ownership",
                    "5.4.4.5": "Data inventory and retention",
                    "5.4.4.6": "Right to be forgotten"
                }
            },
            "5.5": {
                "name": "Explain types and purposes of audits and assessments",
                "topics": {
                    "5.5.1": "Attestation",
                    
                    "5.5.2": "Internal audits",
                    "5.5.2.1": "Compliance audits",
                    "5.5.2.2": "Audit committee",
                    "5.5.2.3": "Self-assessments",
                    
                    "5.5.3": "External audits",
                    "5.5.3.1": "Regulatory audits",
                    "5.5.3.2": "Examinations",
                    "5.5.3.3": "Assessments",
                    "5.5.3.4": "Independent third-party audits",
                    
                    "5.5.4": "Penetration testing",
                    "5.5.4.1": "Physical penetration testing",
                    "5.5.4.2": "Offensive security testing",
                    "5.5.4.3": "Defensive security testing",
                    "5.5.4.4": "Integrated security testing",
                    "5.5.4.5": "Known environment testing",
                    "5.5.4.6": "Partially known environment testing",
                    "5.5.4.7": "Unknown environment testing",
                    "5.5.4.8": "Reconnaissance",
                    "5.5.4.8.1": "Passive reconnaissance",
                    "5.5.4.8.2": "Active reconnaissance"
                }
            },
            "5.6": {
                "name": "Given a scenario, implement security awareness practices",
                "topics": {
                    "5.6.1": "Phishing awareness",
                    "5.6.1.1": "Phishing campaigns",
                    "5.6.1.2": "Phishing identification",
                    "5.6.1.3": "Suspicious message response",
                    
                    "5.6.2": "Behavior recognition",
                    "5.6.2.1": "Risky behavior",
                    "5.6.2.2": "Unexpected behavior",
                    "5.6.2.3": "Unintentional behavior",
                    
                    "5.6.3": "User guidance and training",
                    "5.6.3.1": "Policy and handbook training",
                    "5.6.3.2": "Situational awareness",
                    "5.6.3.3": "Insider threat awareness",
                    "5.6.3.4": "Password management",
                    "5.6.3.5": "Removable media handling",
                    "5.6.3.6": "Social engineering awareness",
                    "5.6.3.7": "Operational security practices",
                    "5.6.3.8": "Remote work security",
                    
                    "5.6.4": "Reporting and monitoring",
                    "5.6.4.1": "Initial reporting",
                    "5.6.4.2": "Recurring reporting",
                    
                    "5.6.5": "Development",
                    
                    "5.6.6": "Execution"
                }
            }
        }
    }
} 