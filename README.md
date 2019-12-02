# uva-ls

LS project

## Services

| type | platform      | Product           | docs       | python | status |
| ---- | ------------- | ----------------- | ---------- | ------ | ------ |
| FaaS | AWS           | Lambda            | [docs][1]  | 3.8    | works  |
| FaaS | GCP           | Functions         | [docs][2]  | 3.7    | works  |
| FaaS | Azure         | Functions         | [docs][3]  | 3.7    | works  |
| FaaS | IBM Cloud     | Functions         | [docs][4]  | 3.7    | works  |
| FaaS | Alibaba Cloud | Function Compute  | [docs][5]  | 3.6    | works  |
| FaaS | Zeit          | Now               | [docs][6]  | 3.6    | works  |
| CaaS | AWS           | Fargate           | [docs][7]  | 3.8    |        |
| CaaS | GCP           | Cloud Run         | [docs][8]  | 3.8    | works  |

- IBM also has docker, but STDIN/STDOUT?
- Alibaba also has docker functions, but not really documented?
- Azure docker functions?
- Google Appengine scale to 0?

### background

| platform      | Product            | framework                     | dev notes                                                        |
| ------------- | ------------------ | ----------------------------- | ---------------------------------------------------------------- |
| AWS           | Lambda             | custom                        | so many pieces to configure, long feedback cycle, scarce logging |
| GCP           | Functions          | flask                         | just works, good logging                                         |
| Azure         | Functions          | custom / MS Oryx build        | good docs, + local testing, really bad web console               |
| IBM Cloud     | Functions          | openwhisk / cloudflare        | meh docs on openwhisk                                            |
| Alibaba Cloud | Function Compute   | WSGI / Terraform              |                                                                  |
| Zeit          | Now                | Python HTTP / WSGI            | just works, good logging                                         |
| AWS           | Fargate            | containers on ECS             |                                                                  |
| GCP           | Cloud Run          | kubernetes / anthos / knative | just works, good logging                                         |
| Azure         | Container Instance | N/A                           |                                                                  |
| Alibaba Cloud | Container Service  | N/A                           |                                                                  |

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

fun init
fun deploy

in virtualenv
func init azurefunctions --python
func azure functionapp publish lsproject

```

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

- [GCP Functions vs Run][11]

[1]: https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
[2]: https://cloud.google.com/functions/docs/writing/http
[3]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python
[4]: https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-actions
[5]: https://www.alibabacloud.com/help/doc-detail/56316.htm
[6]: https://zeit.co/docs/runtimes#official-runtimes/python
[7]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
[8]: https://cloud.google.com/run/docs/deploying
[9]: https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app
[10]: https://www.alibabacloud.com/help/doc-detail/90670.htm
[11]: https://medium.com/google-cloud/cloud-run-vs-cloud-functions-whats-the-lowest-cost-728d59345a2e
[photos1]: https://github.com/seankhliao/uva-ls/releases/tag/v0.0.0-photos.raw
