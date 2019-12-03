# uva-ls

LS project

## Services

| type | platform      | Product          | docs      | python | status                | notes                                  |
| ---- | ------------- | ---------------- | --------- | ------ | --------------------- | -------------------------------------- |
| FaaS | AWS           | Lambda           | [docs][1] | 3.8    | not working           | nightmare to configure                 |
| FaaS | GCP           | Functions        | [docs][2] | 3.7    | working | okay                                   |
| FaaS | Azure         | Functions        | [docs][3] | 3.7    | working         | dodgy web console, good local testing  |
| FaaS | IBM Cloud     | Functions        | [docs][4] | 3.7    | working       | no logs                                |
| FaaS | Alibaba Cloud | Function Compute | [docs][5] | 3.6    | working               | how many different CLIs do I need      |
| FaaS | Zeit          | Now              | [docs][6] | 3.6    | working               | Just Works                             |
| CaaS | GCP           | Cloud Run        | [docs][7] | 3.8    | working               | thread time is broken for some reason? |
| CaaS | AWS           | Fargate          | [docs][8] | 3.8    |                       | how do you do this?                    |

- IBM also has docker, but STDIN/STDOUT?
- Alibaba also has docker functions, but not really documented?
- Azure docker functions?
- Google Appengine scale to 0?

### additional docs

| lib        | docs                                                       |
| ---------- | ---------------------------------------------------------- |
| pillow     | [docs](https://pillow.readthedocs.io/en/latest/)           |
| http       | [docs](https://docs.python.org/3/library/http.server.html) |
| flask      | [docs](https://flask.palletsprojects.com/en/1.1.x/api/)    |
| time (3.6) | [docs](https://docs.python.org/3.6/library/time.html)      |
| aiohttp    | [docs](https://aiohttp.readthedocs.io/en/stable/)          |
| asyncio    | [docs](https://docs.python.org/3/library/asyncio.html)     |

## testing

- 583 raw photos (larger than 4000x4000): [releases: v0.0.0-photos.raw][photos1]

```
ibmcloud fn action create --kind python:3.7 --web raw --memory 128 cold ibmfunctions.zip
ibmcloud fn get warm --url

in virtualenv
func init azurefunctions --python
func azure functionapp publish lsproject

fun init
fun deploy
fun install -v --runtime python3 --package-type pip package-here
```

https://webcache.googleusercontent.com/search?q=cache:FmmiJU_o6qkJ:https://www.alibabacloud.com/help/doc-detail/74571.htm+&cd=2&hl=en&ct=clnk&gl=nl

## report ideas

### target featureset

- globally / publicly available HTTPS terminated endpoint
- serverless: no managing of runtimes
- scalable: autoscale
- pay for usage

### testing variables

- Workload:
  - distribution: stable / burst
  - memory usage
  - cpu usage
  - latency sensitivity
  - wasted cycles / external calls
  - async / concurrent / parallel
- Network:
  - DNS resolution
  - bandwidth / payload size
  - location / latency
- Platform:
  - layers / overhead
  - machine size
  - runtime version
  - addons feature parity
- code / server
  - optimized for platform ?
  - concurrent / parallel ?

### additional testing ideas

- probe runtime CPU frequency, does 1vcpu = 1vcpu

## additional references:

- [GCP Functions vs Run][ref1]

[1]: https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
[2]: https://cloud.google.com/functions/docs/writing/http
[3]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python
[4]: https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-actions
[5]: https://partners-intl.aliyun.com/help/doc-detail/56316.htm#adding-modules
[6]: https://zeit.co/docs/runtimes#official-runtimes/python
[7]: https://cloud.google.com/run/docs/deploying
[8]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
[ref1]: https://medium.com/google-cloud/cloud-run-vs-cloud-functions-whats-the-lowest-cost-728d59345a2e
[photos1]: https://github.com/seankhliao/uva-ls/releases/tag/v0.0.0-photos.raw
