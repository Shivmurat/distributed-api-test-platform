# Distributed API Test Platform

A scalable and resilient PyTest-based API automation framework designed for distributed systems and cloud-native platform testing.

This framework focuses on:

* reusable architecture
* resiliency validation
* distributed-system testing patterns
* CI/CD readiness
* maintainability
* extensibility

---

# Tech Stack

* Python 3
* PyTest
* Requests
* Allure Reporting
* Jenkins
* Docker (planned integration)
* YAML Configuration Management

---

# Key Features

## Framework Architecture

* Layered client-based API abstraction
* Reusable BaseClient architecture
* Environment-driven configuration
* Modular utilities and helpers
* Scalable test organization

---

## Resiliency Testing

* Automatic retry handling
* Timeout validation
* Polling support for eventual consistency
* Distributed-system failure simulation
* Transient error validation

---

## Authentication Strategy

* Centralized authentication architecture
* Token lifecycle management design
* Auto token regeneration strategy
* Reusable auth abstraction

---

## Reporting & Observability

* Allure reporting integration
* Structured centralized logging
* Request/response logging
* Timestamped log generation

---

## CI/CD Readiness

* Jenkins pipeline integration
* Marker-based execution strategy
* Parallel execution ready structure
* Environment-aware execution

---

# Project Structure

```text
distributed-api-test-platform/
│
├── clients/
│   ├── base_client.py
│   ├── auth_client.py
│   └── httpbin_client.py
│
├── config/
│   ├── qa.yaml
│   ├── staging.yaml
│   ├── prod.yaml
│   └── config_loader.py
│
├── tests/
│   ├── smoke/
│   ├── resiliency/
│   ├── regression/
│   ├── integration/
│   └── contract/
│
├── utils/
│   ├── logger.py
│   ├── assertions.py
│   ├── retry_handler.py
│   ├── polling_helper.py
│   ├── file_reader.py
│   └── data_generator.py
│
├── reports/
├── logs/
├── jenkins/
│   └── Jenkinsfile
│
├── requirements.txt
├── pytest.ini
├── conftest.py
└── README.md
```

---

# Framework Design Principles

## Separation of Concerns

Tests focus only on business validation while transport, retries, logging, and authentication are centralized in reusable layers.

---

## Client-Based API Architecture

Dedicated API clients encapsulate endpoint interactions and abstract raw request handling from tests.

Example:

```python
response = httpbin_client.get_headers()
```

instead of:

```python
requests.get(...)
```

---

## Distributed-System Testing Mindset

Framework includes support for:

* eventual consistency validation
* retry resiliency
* timeout handling
* async workflow validation
* transient infrastructure failure testing

---

# Supported Test Categories

| Marker      | Purpose                             |
| ----------- | ----------------------------------- |
| smoke       | Basic validation suite              |
| resiliency  | Distributed-system resiliency tests |
| regression  | Regression validation               |
| contract    | API schema/contract validation      |
| integration | End-to-end workflow validation      |

---

# Installation

## Clone Repository

```bash
git clone <repo-url>
cd distributed-api-test-platform
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Smoke Tests

```bash
pytest -m smoke
```

---

## Run Resiliency Tests

```bash
pytest -m resiliency
```

---

# Allure Reporting

## Generate Results

```bash
pytest --alluredir=reports/allure-results
```

---

## Open Interactive Report

```bash
allure serve reports/allure-results
```

---

# Jenkins Integration

The framework includes a Jenkins declarative pipeline supporting:

* automated test execution
* marker-based execution
* environment setup
* report archival

Pipeline file:

```text
jenkins/Jenkinsfile
```

---

# Public API Validation Platform

Framework validations are currently executed against:

## [httpbin](https://httpbin.org?utm_source=chatgpt.com)

Used for:

* retry validation
* timeout simulation
* header verification
* distributed-system-like failure testing

---

# Future Enhancements

* Dockerized execution
* Kubernetes-based distributed runners
* Parallel execution support
* OAuth2 integration
* Secret management integration
* API contract testing expansion
* Grafana/Prometheus observability integration

---

# Engineering Focus

This framework is intentionally designed to demonstrate:

* scalable automation architecture
* distributed-system testing strategies
* resiliency engineering mindset
* Staff-level QE design principles
* CI/CD-oriented execution strategy

