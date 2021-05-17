# BIOS Releated scripts

## List of scripts

1. power_graceful_restart.yml

This playbooks helps us to restart server using iDRAC ip and verify wheather server is up or not

### How to run

    ```ansible-playbook power_graceful_restart.yml -e "iDRAC_ip=10.207.240.94 iDRAC_user=ADMIN iDRAC_password=Commscope123! server_ip=10.53.198.168"```

#### Parameters Details

    ```
    iDRAC_ip = IP address of iDRAC Server
    iDRAC_user = Username of iDRAC Server
    iDRAC_password = Password of iDRAC Server
    server_ip = Server IP which we will testing when it restarts
    ```
