# uva-ls

LS project

## Services

| type | platform      | Product            | docs       | python | status   |
| ---- | ------------- | ------------------ | ---------- | ------ | -------- |
| FaaS | AWS           | Lambda             | [docs][1]  | 3.8    |          |
| FaaS | GCP           | Functions          | [docs][2]  | 3.7    | can work |
| FaaS | Azure         | Functions          | [docs][3]  | 3.7    |          |
| FaaS | IBM Cloud     | Functions          | [docs][4]  | 3.7    |          |
| FaaS | Alibaba Cloud | Function Compute   | [docs][5]  | 3.6    |          |
| FaaS | Zeit          | Now                | [docs][6]  | 3.6    | can work |
| CaaS | AWS           | Fargate            | [docs][7]  | 3.8    |          |
| CaaS | GCP           | Cloud Run          | [docs][8]  | 3.8    | can work |
| CaaS | Azure         | Container Instance | [docs][9]  | 3.8    |          |
| CaaS | Alibaba Cloud | Container Service  | [docs][10] | 3.8    |          |

## background

| platform      | Product            | framework          |
| ------------- | ------------------ | ------------------ |
| AWS           | Lambda             | custom             |
| GCP           | Functions          | flask              |
| Azure         | Functions          | custom             |
| IBM Cloud     | Functions          | openwhisk          |
| Alibaba Cloud | Function Compute   | WSGI               |
| Zeit          | Now                | Python HTTP / WSGI |
| AWS           | Fargate            | N/A                |
| GCP           | Cloud Run          | Kubernetes         |
| Azure         | Container Instance | N/A                |
| Alibaba Cloud | Container Service  | N/A                |

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
