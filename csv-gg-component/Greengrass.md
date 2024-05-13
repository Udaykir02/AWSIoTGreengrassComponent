# Greengrass Installation Guide

1. **Connect to AWS Lightsail Instance via Command Line**

    Open your command prompt or terminal and SSH into the AWS Lightsail instance using the following commands:

    ```bash
    Download pem file from AWS Console
    chmod 400 xxx.pem # Change permission of the pem file to read-only for root user.
    ssh -i LightsailDefaultKey-us-east-1.pem user@Ip_address
    ```

2. **Environment Setup: Installing Java JDK 17**

    Install and upgrade necessary packages:

    ```bash
    sudo apt update && sudo apt upgrade
    sudo apt install default-jdk
    java --version
    sudo apt install unzip
    ```

3. **Install AWS IoT Greengrass Core Software via Console**

    Set up your environment variables with your AWS credentials:

    ```bash
    export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXX
    export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ```

4. **Install AWS IoT Greengrass Core Software via CLI**

    Download and install the Greengrass Core software:

    ```bash
    cd ~
    curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
    unzip greengrass-nucleus-latest.zip -d GreengrassInstaller && rm greengrass-nucleus-latest.zip

    sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
    -jar ./GreengrassInstaller/lib/Greengrass.jar \
    --aws-region us-east-1 \
    --thing-name DDIGreengrassCore \
    --thing-group-name DDIGreengrassCoreGroup \
    --thing-policy-name GreengrassV2IoTThingPolicy \
    --tes-role-name GreengrassV2TokenExchangeRole \
    --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
    --component-default-user ggc_user:ggc_group \
    --provision true \
    --setup-system-service true \
    --deploy-dev-tools true
    ```

5. **Open VS Code and Terminal**

    Launch VS Code and open a terminal. Navigate to your preferred directory, ideally 'Documents'. Then, create project and Greengrass folders:

    ```bash
    mkdir project
    cd project
    mkdir greengrass
    cd greengrass
    ```

    Install Greengrass Development Kit (GDK) CLI and verify the installation:

    ```bash
    python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
    gdk --version
    ```

6. **Validate Credentials**

    Check your AWS credentials:

    ```bash
    echo $AWS_ACCESS_KEY_ID
    echo $AWS_SECRET_ACCESS_KEY
    ```

    If not recognized, set them:

    ```bash
    export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXX"
    export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```

    For Windows:

    ```bash
    setx AWS_ACCESS_KEY_ID "XXXXXXXXXXXXXXXXX"
    setx AWS_SECRET_ACCESS_KEY "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```

    **Note:** Replace the access key ID and secret access key with your own credentials.
