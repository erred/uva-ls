# uva-ls

LS project

## Services

| type | platform      | Product           | docs       | python | status |
| ---- | ------------- | ----------------- | ---------- | ------ | ------ |
| FaaS | AWS           | Lambda            | [docs][1]  | 3.8    |        |
| FaaS | GCP           | Functions         | [docs][2]  | 3.7    | work   |
| FaaS | Azure         | Functions         | [docs][3]  | 3.7    |        |
| FaaS | IBM Cloud     | Functions         | [docs][4]  | 3.7    |        |
| FaaS | Alibaba Cloud | Function Compute  | [docs][5]  | 3.6    |        |
| FaaS | Zeit          | Now               | [docs][6]  | 3.6    | work   |
| CaaS | AWS           | Fargate           | [docs][7]  | 3.8    |        |
| CaaS | GCP           | Cloud Run         | [docs][8]  | 3.8    | work   |
| CaaS | Alibaba Cloud | Container Service | [docs][10] | 3.8    |        |

IBM also has docker, but STDIN/STDOUT ?

## background

| platform      | Product            | framework                     | dev notes                                                        |
| ------------- | ------------------ | ----------------------------- | ---------------------------------------------------------------- |
| AWS           | Lambda             | custom                        | so many pieces to configure, long feedback cycle, scarce logging |
| GCP           | Functions          | flask                         | just works, good logging                                         |
| Azure         | Functions          | custom                        |                                                                  |
| IBM Cloud     | Functions          | openwhisk                     |                                                                  |
| Alibaba Cloud | Function Compute   | WSGI / Terraform              |                                                                  |
| Zeit          | Now                | Python HTTP / WSGI            | just works, good logging                                         |
| AWS           | Fargate            | N/A                           |                                                                  |
| GCP           | Cloud Run          | kubernetes / anthos / knative | just works, good logging                                         |
| Azure         | Container Instance | N/A                           |                                                                  |
| Alibaba Cloud | Container Service  | N/A                           |                                                                  |

## testing variables

- image size
- image contents
- DNS resolution
- platform location
- machine size
- Python version
- platform feature parity ?

## docs

| lib    | docs                                                       |
| ------ | ---------------------------------------------------------- |
| pillow | [docs](https://pillow.readthedocs.io/en/latest/)           |
| http   | [docs](https://docs.python.org/3/library/http.server.html) |

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
