# Report

## Abstract

## Introduction

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
- server code:
  - frameworks
  - same across platforms / no microoptimizations

### Setup

- single source, single datacenter
- hourly test, 10x1, 10x50
- 4 days

### Limitations

- single source, single datacenter
- python not the best for perf mon

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
- all except lambda show a slow cpu, lambda, ibm cpu starved of time

### Applicability

### Pricing

### Other Tech

- fargate
- Kubernetes

## Conclusion

## References

## Appendix
