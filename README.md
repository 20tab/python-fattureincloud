# python-fattureincloud


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Python package](https://github.com/20tab/python-fattureincloud/actions/workflows/python-package.yml/badge.svg)](https://github.com/20tab/python-fattureincloud/actions/workflows/python-package.yml)

> A python wrapper for the [FattureInCloud REST API](https://api.fattureincloud.it/v1/documentation/dist/).

<!-- ## 📝 Conventions -->


## 📦 Installation

Change directory and create a new project as in this example:

```console
$ pip install python-fattureincloud
```

## 🔑 API Credentials

The `FattureInCloudAPI` needs `api_uid` and `api_key` parameters to make requests.

```python
from fattureincloud.client import FattureInCloudAPI


client = FattureInCloudAPI(
    api_uid="your_api_uid", 
    api_key="your_api_key"
)
```

## 🚀️ Usage

At the moment, only method to read information are implemented.
Every model has `list` method with different parameter to filter results.

For each model there is a set of methods to get a specific element.

### ⚫ Anagrafica

```python
# Get all customers 
customers = client.clienti().lista()

# Get all suppliers
suppliers = client.fornitori().lista()
```

### ⚫ Prodotti

```python
# Get all products 
customers = client.prodotti().lista()
```

### ⚫ Documenti

The following example show how you can get all invoices. But you can use all the following document types: `fatture`, `proforma`, `ordini`, `preventivi`, `ndc`, `ricevute`, `ddt`.

```python
# Get all documents 
invoices = client.fatture().lista()

invoice_details = client.fatture.dettagli(
    _id="invoice_id", 
    token="invoice_token"
)

info = clienti.fatture.info(anno_competenza=2021)

invoice_infomail = client.fatture.infomail(
    _id="invoice_id", 
    token="invoice_token"
)
```