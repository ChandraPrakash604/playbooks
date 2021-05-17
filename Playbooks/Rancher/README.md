
## List of Dependecies required if we  want to shift our ansible playbook server
1. Need to copy rancher cli from ansu server (/root/rancher-v2.4.10/rancher) if not download it from link # TODO "{{  }}"


## Code Explanation
1. Code block 1 ref 03-Rancher_Login.yaml
```
    PATH: /usr/local/bin:{{ ansible_env.PATH }}
```

- this is required because in some server we  don't have "/usr/local/bin" in path.

2. Create a API key from rancher ui and copy token into host file
Sample
```
    [rancher:vars]
        token= <Copied Token>
```
