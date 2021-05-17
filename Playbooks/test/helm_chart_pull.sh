#!/bin/bash
# Helm chart repository name (as configured with 'helm repo add' command)
chartrepo="oc5g-helm-prod-suwanee"
# Helm chart version
chartversion="0.1.0-siqbuild.6.0.0.40.5-intota"

helm pull ${chartrepo}/cs-gnb-dltg --version ${chartversion}
helm pull ${chartrepo}/cs-gnb-cu-cp --version ${chartversion}
helm pull ${chartrepo}/cs-gnb-cu-up --version ${chartversion}
helm pull ${chartrepo}/cs-gnb-l3uesim --version ${chartversion}
helm pull ${chartrepo}/cs-gnb-ultg --version ${chartversion}
helm pull ${chartrepo}/cs-gnb-du --version ${chartversion}
