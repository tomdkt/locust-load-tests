# Performance Testing with Locust

A starter project and guide for getting started with performance testing using Locust.

## 1. Installation

First, ensure you have all the required Python packages installed. From your project's root directory, run:

```shell
  uv sync
```

## 2. Running the Locust Web Interface
```shell
  locust -f src/locustfile.py
```

Server: [`http://127.0.0.1:8089`](http://127.0.0.1:3000)


## 3. How to Start a Test from the GUI
On the Locust web page, you will see a form to configure and start your test.

- Number of users: Enter the total number of concurrent users you want to simulate. (e.g., 100)
- Spawn rate: Enter how many users should be started per second. (e.g., 10 means 10 new users are added every second until the total of 100 is reached).
- Host: Enter the base URL of the API you want to test (e.g., http://localhost:3000). This is the target for your test simulation.

Click the "Start swarming" button to begin the test.


# Load Testing Guide

There's no universal standard for "high" traffic, as it varies by application. A small blog's "high" is an e-commerce giant's "low." Choose numbers based on your app's goals and real-world traffic.

## How to Determine Your Numbers

Before setting numbers, answer these:
- **Check Analytics 📊:** Use Google Analytics, New Relic, or Datadog. What's the peak concurrent users in a normal hour? During a big sale or event?
- **Define Business Goals:** Preparing for a product launch or Black Friday? Simulate *expected* traffic, not just current.

## General Scenarios & Starting Points

### Low Traffic (Smoke Test)
Verifies system functionality under light load. Ideal for development/staging.

- **Purpose:** Sanity checks, validate scripts, catch major performance issues.
- **Number of Users:** 10 - 100
- **Spawn Rate:** 1 - 10 users/sec
- **Example:** 50 users, 5 users/sec (ramps up over 10 seconds).
```shell
  locust -f src/locustfile.py --headless -u 50 -r 5 -t 1m --host http://localhost:3000
```
  

### Normal / Average Traffic (Load Test)
Simulates a typical day or busy hour to ensure stability.

- **Purpose:** Measure baseline performance, identify bottlenecks, meet SLAs.
- **Number of Users:** 100 - 1,000+ (based on real traffic)
- **Spawn Rate:** 10 - 50 users/sec
- **Example:** 1,000 users, 20 users/sec (50-second ramp-up).
```shell
  locust -f src/locustfile.py --headless -u 1000 -r 20 -t 10m --host http://localhost:3000
```
### High Traffic (Stress Test) 🚀
Simulates peak events (e.g., viral post, major sale) to find breaking points.

- **Purpose:** Test max capacity, failure modes, and recovery.
- **Number of Users:** 1,000 - 10,000+
- **Spawn Rate:** 50 - 200+ users/sec
- **Example:** 5,000 users, 100 users/sec (50-second ramp-up, flash crowd effect).
```shell
  locust -f src/locustfile.py --headless -u 5000 -r 100 -t 10m --host http://localhost:3000
```
**Key Formula:** `(Number of Users / Spawn Rate) = Ramp-up Time`. Adjust to control load application speed.