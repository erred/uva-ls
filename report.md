# report brainstorming

## results

- errors on day 1: ~5 hours of inconsistent data
- single concurrency: 94x10, no failures
- 50 concurrecy: 94x500 = 47000

  - ali 3499: 429 too many requests
  - gcp-fun 28: 500 internal server error
  - zeit 5: 400 bad request
  - azure 3: 502 bad gateway

- compare: request time vs cpu
- location / routing
- overhead comparison

### results from Mar tests
- single concurrency 6x10=960, no failures
- 50 concurrency:  96x500=48000
    - alibaba: 1053, too many requests
    - gcp-fun: 3, too many requests
    - azure: 49, too many requests
    -gcp-run: 4, too many requests
    - zeit: 1, Cannot connect to host warm.lsproject.now.sh:443 ssl:default [Connection reset by peer] too many request?
    
->> Question, how do we know that we haven't been executing the test at the same time againts the same services?
Then we would have more concurrency than expected!

    **from client view**
  - azure(specially 10 req) and ibm execution time  the most inestable. WHY?
  - zeit now and lambada really similar -> same DC?
  - ali performance seems good(more inestable for 10 req) but do not forget about the lange amount of errors
  - google works ok, no differences between 500 and 10.

## layout

```
abstract
introduction
related work
research question
- business case
- CPU
- overhead / latencies
- pricing model
methodology
- variables
- test setup
results
- data
- pricing
discussion
- applicability
- billing
- other tech
conclusion
references
```

## research question

- performance difference between FaaS and CaaS
  - proposal
  - cpu performance
  - platform overhead
  - cold start latencies
- business case: low friction serverless deployments
  - featureset:
    - serverless: no management of runtimes
    - autoscale
    - globally reachable HTTPS endpoint
    - pay only for usage
- available technologies
  - PaaS
    - 1st generation
    - GCP App Engine
  - FaaS
    - 2nd generation
    - AWS Lambda
    - GCP Functions
    - Zeit Now
    - Azure Functions
    - IBM Functions
    - Alicloud Functions
  - CaaS on demand
    - GCP Cloud Run
    - AWS Fargate (needs NLB)

### testing variables

- Workload:
  - distribution: stable / burst
    - burst
  - memory usage
    - doesn't fail
  - cpu usage
  - latency sensitivity
    - no
  - wasted cycles / external calls
    - no
  - async / concurrent / parallel
    - async, single concurrecy
- Network:
  - DNS resolution
    - no restriction
  - bandwidth / payload size
    - 2048 -> 256
  - location / latency
    - europe
- Platform:
  - layers / overhead
  - machine size
    - target 128 memory
    - cpu freq
      - shared?
    - memory limit
  - runtime version
    - 3.6 - 3.8
  - addons feature parity
    - logging, monitoring
- code / server
  - optimized for platform ?
    - same-ish for all
  - concurrent / parallel ?
    - not very

### pitfalls

- develop / test / release cycle
  - local test env
    - Good: docker (Zeit), GCP, Azure, Alicloud
    - Meh: AWS
    - No: IBM
  - deploy time
  - logging
    - No: IBM, Alicloud
  - traffic splitting

### backing technology

- GCP App Engine: cloud build, nginx reverse proxy wsgi gateway for python
- AWS Lambda: firecracker?
- GCP Functions: cloud build
- Zeit Now: "lambdas", multicloud: AWS and GCP
- Azure Functions: Oryx build, docker containers
- IBM Functions: openwhisk, docker containers, cloudflare
- Alicloud Functions: custom?, docker containers
- GCP Cloud Run: Kubernetes / Knative, containers

### other

- Shared VPS
- Heroku
- Cloudflare workers: JS only V8 runtime
- AWS Fargate
- Hosted Kubernetes:
  - interface to infra
