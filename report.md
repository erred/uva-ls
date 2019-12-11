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
- could we use Seans results for cold start?
- warm:
- single concurrency 6x10=960, no failures
- 50 concurrency:  96x500=48000
    - alibaba: 1053, too many requests
    - gcp-fun: 3, too many requests
    - azure: 49, too many requests
    -gcp-run: 4, too many requests
    - zeit: 1, Cannot connect to host warm.lsproject.now.sh:443 ssl:default [Connection reset by peer] too many request?

#### from client view
  - azure(specially 10 req) and ibm execution time the most inestable. WHY?
  - zeit now and lambada really similar -> same DC?
  - ali performance seems good(more inestable for 10 req) but do not forget about the lange amount of errors
  - google works ok, no differences between 500 and 10. Func maybe the worst performance but not a big difference. 

#### from server time 2 view (image resizing part)
  - zeit and lambda are not that similar anymore. Zeit better, because they use the bigges machine from amazon?
  - amazon lambda two big blocks, they use two types of machines?
  - ibm and azure are still the most inestable  with worst performance?
  - here we can see how that google products behave a bit different -> gpc run the best?
  - 

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

  

### plots on the report and what they show:
- do we need to show the reliability of our data??
- 10 vs 500, does it change much? (platforms shoud mantain performance, it really happens?)
- representing relation btw cpu time and client time so overhead of each platform
- represent performance(cpu and client time) at different points in time
- warm vs cold start, how performance changes in each case


- x:time to  y:percentage