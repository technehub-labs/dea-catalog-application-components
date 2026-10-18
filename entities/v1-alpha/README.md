# v1-alpha :  Information System Component catalogue

This directory contains the v1-alpha catalogue records for the Information System Component (ISC) entity. The records are populated through the 5-CR ISC programme (CR-IS-CAT-02 + 02A + 02B + 02C + 02D).

## Directory structure

```
entities/v1-alpha/
├── README.md (this file)
├── index.yaml (catalog-level index)
└── components/
    ├── index.yaml (component-level index)
    ├── identity-and-access/ (the ISCC-07 Security domain; example domain)
    │   ├── index.yaml (domain-level index)
    │   └── components/
    │       ├── dea-isc-identity-broker/ (F2 example)
    │       │   ├── component.yaml
    │       │   └── README.md
    │       └── dea-isc-oidc-discovery/ (F4 example)
    │           ├── component.yaml
    │           └── README.md
    └── <other-domains>/
```

The directory is populated by 02C; 02B establishes the directory structure and the example records. The example records (F2 + F4) are illustrative only; the 02C population exercise replaces them with the P1 component inventory.

## Component record format

Each component record is a YAML file with a paired README.md. The component record MUST conform to the v2 schema in `schemas/entities/information-system-component.v2.json`. The README MUST follow the 19-section template in `templates/README-template.md`.

See `components/identity-and-access/components/dea-isc-identity-broker/component.yaml` for an example.
