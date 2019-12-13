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
  - python runtime
    - not good for performance measurements
    - different frameworks

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

  

### INFO


| Type | Platform      | Product          | Location              | Endpoint TTL(s)   | Our bill                               |
| ---- | ------------- | ---------------- | ----------------      | -------------     | -------------------------------------- |
| FaaS | AWS           | Lambda           | London                | 60                |  (hosted zone) 0.45 eur (1)            |
| FaaS | GCP           | Functions        | St. Ghislain, Belgium | 300               | 0 eur (2)                              |
| CaaS | GCP           | Cloud Run        | St. Ghislain, Belgium | 21600             | 0 eur (3)                              |
| PaaS | GCP           | App Engine       | St. Ghislain, Belgium | 300               | 0 eur (4)                              |
| FaaS | Azure         | Functions        | Netherlands           | CNAMEs 30,1799,59 | 0 eur (5)                              |
| FaaS | IBM Cloud     | Functions        | London                | 300               | 0 eur. Free trial, cannot check costs  |
| FaaS | Alibaba Cloud | Function Compute | Frankfurt             | CNAME 60,59       | 0.11$                                  |
| FaaS | Zeit          | Now              | Brussels, Belgium**   | 60                | 0 eur free trial, cannot check costs   |

**By default, the closest region to the geographical location of the deployment is used**


| Platform      | Product          | vCPU      | Memory | Timeout | Concurrency | CPU speed | Notes |
| ------------- | ---------------- | --------- | ------ | ------- | ----------- | --------- | ----- |
| AWS           | Lambda           | ??        | 128 MB | 60s     |  1000       |           |       |
| GCP           | Functions        | ??        | 128 MB | 60s     |  ??         |  200 MHz  |       |
| GCP           | Cloud Run        | 1         | 128MiB | 300s    |   5         |           | autoscaling up to 1000 container instances|
| GCP           | App Engine       | ??        | ??     |  ??     |  ??         |           |       |
| Azure         | Functions        | ??        | ??     |  ??     |  ??         |  ??       |       |
| IBM Cloud     | Functions        | ??        | 128MiB | 60s     |  ??         |           |       |
| Alibaba Cloud | Function Compute | ??        | 1128MB | 60s     |  ??         |  ??       |       |                      
| Zeit          | Now              | ??        | ??     |         |             |           | need to use the console?     |


(1) We had free tier. Free tier usage:
   - Compute time per month: 4.08% (16,333.11/400,000 seconds). Need to divide it by 2 
   - Request per month: 11.01% (110,081.00/1,000,000 Requests). Need to divide it by 2
   - Amazon Cloud Watch (log ingestion): 0.71% (0.04/5 GB). Need to divide it by 2 
   - Amazon Cloud Watch (log storage):  0.09%(0.00/5 GB-Mo). Need to divide it by 2 

   Pricing (if we would had have to pay): 

    | Product          | Price                     | 
    | ---------------- | ---------                 | 
    | Requests         | $0.20 per 1M              | 
    | Memory (128 MB)  | $0.000000208 per 100ms    | 
    | Cloud Watch      | Free tier for everybody   | 


(2) All users have 2 milion requests + 400,000 GB-seconds, 200,000 GHz-seconds of compute time + 5GB of Internet egress traffic per month

(3) All users have first 180,000 vCPU-seconds + 360,000 GB-seconds + 2 million requests for free 
But, if we did not have the free tier we had to pay:
    - €0.14 for Cloud Run Network Internet Egress Europe to Europe 

(4) If we did not have free trial:
     - Frontend Instances  App Engine  1,384.2 hour  €55.29?

(5) Without fre  e trial:  1.07 eur of log analytics, 0.95 eur of functions, 0.01 eur of storage = 2.02 eur



### MEMORY-CPU-PRICE TABLE

#### AWS Lambda
keep searching


#### Google Cloud Functions 

| Memory  | CPU     | Price/100ms  |
|-------- | ------- | ------------ |
| 128MB   | 200MHz  | $0.000000231 |
| 256MB   | 400MHz  | $0.000000463 |
| 512MB   | 800MHz  | $0.000000925 |
| 1024MB  | 1.4 GHz | $0.000001650 |
| 2048MB  | 2.4 GHz | $0.000002900 |

#### Google Cloud Run 
keep searching

#### Google App Engine
keep searching

#### Microsoft Azure Functions 
keep searching


#### IBM Cloud Functions 
keep searching

#### Zeit Now  
keep searching