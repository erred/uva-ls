# Report

## Abstract

## Introduction

current state of serverless:

- old: app engine
- current: FaaS
- next: run

## Related Work

## Research Question

How do serverless (FaaS) products compare across cloud platforms?

- Are machine types comparable across cloud platforms?
- Performance under load (scale)
- pricing model make sense?

## Methodology

### Variables

- product selection:
  - major cloud providers
  - publicly reachable HTTPS endpoint / autoscale to 0 / pay only for usage
- workload selection:
  - no external calls / raw CPU
  - burst
- product variation:
  - Datacenter location
  - machine size selection
  - language runtime version
  - Addons (logging, monitoring, etc...)
- Network
  - bandwith
  - latency / location
  - DNS lookup
  - single source, single dest
- server code:
  - frameworks
  - same across platforms / no microoptimizations
  - python code not good for perf

### Setup

- single source, single datacenter
- hourly test, 10x1, 10x50
- 4 days

## Results

### Overall performance

- failure rate
- cold starts
- parallel instances

### Overhead

- cold vs warm
- single vs multi

### CPU

- cold vs warm (maybe exclude this one?)
- single vs multi

### Pricing

- CPU time / cost
- adjust for frequency?

## Discussion

- alibaba doesn't scale
- ms doesn't want to scale
- ibm is slow
- aws is consistent, but slow

## Discussion

### Overhead

### Overhead

### Compute Performance

### Scaling

### Price to Performance

### Technologies

#### Current

#### What to look forward to

- all except lambda show a slow cpu, lambda, ibm cpu starved of time

### Research Question

#### Applicability

## Conclusion

- no thinking about servers
  - fit in machine type to save costs
  - machine type for perfomance
- scaling worries
  - depends on your cloud
- which cloud to choose?
  - lock-in
- what to look forward to
  - kubernetes unified api

## References

- https://engineering.opsgenie.com/how-does-proportional-cpu-allocation-work-with-aws-lambda-41cd44da3cac
- https://epsagon.com/blog/how-to-make-aws-lambda-faster-memory-performance/
- https://www.simform.com/aws-lambda-pricing/
- http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/pdf/FunctionCompute-develop-guide-intl-en-2018-12-07.pdf
- http://jamesthom.as/
- https://webcache.googleusercontent.com/search?q=cache:IvHnCCWD2IkJ:https://www.icsr.agh.edu.pl/~malawski/CloudFunctionsHeteroPar17CPE.pdf+&cd=6&hl=en&ct=clnk&gl=nl
- https://sci-hub.se/10.1002/cpe.4792
- https://mikhail.io/2018/10/azure-functions-v2-released-how-performant-is-it/
- https://markheath.net/post/avoiding-azure-functions-cold-starts
- https://github.com/ahmetb/cloud-run-faq#how-is-it-different-than-app-engine-flexible
- https://read.acloud.guru/the-good-and-the-bad-of-google-cloud-run-34455e673ef5

## Appendix
