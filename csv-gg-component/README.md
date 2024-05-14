# AWS IoT Greengrass Custom Component for csv

A custom AWS Greengrass component to periodically fetch data from a csv file and publish it to an Amazon S3 bucket.

## Architecture

 ![Architecture](architect.png)


## Prerequisites

Before starting the implementation, ensure the following prerequisites are met:

1. **AWS Account**: You should have access to an AWS account to utilize AWS services such as AWS Greengrass and Amazon S3.

2. **AWS Greengrass Core**: Set up an AWS Greengrass Core on your edge device following the official documentation.

3. **Python Environment**: Ensure Python is installed on your system. The Python version should be compatible with the AWS Greengrass Core and SDKs.

4. [Greengrass Installation](Greengrass.md)

## CSV Custom Component

## Implementation Steps

1. **CSV directory Setup**:
   - Create a directory locally where the simulated data can be stored in csv format.
   - [Setup for csv](csv.md)

2. **Python Thermostat Simulator**:
   - Create a Python script to simulate thermostat data.
   - The script generated csv file and stores in a given directory, inserts one record into the directory, sleeps for 1 second, inserts a new record with random data, and loops indefinitely.

3. **AWS Greengrass Component Development**:
   - Develop a custom AWS Greengrass component utilizing Python and AWS SDKs.
   - Implement robust database connectivity logic, ensuring secure and efficient data retrieval.
   - Configure the component to execute periodic data retrieval operations, maintaining synchronization with the directory.
   - Employ appropriate data transformation techniques to facilitate seamless compatibility with Amazon S3.

4. **Amazon S3 Configuration**:
   - Create an Amazon S3 bucket tailored to accommodate the extracted dataset.
   - Establish appropriate access controls and permissions to ensure data integrity and confidentiality.

5. **Deployment and Monitoring**:
   - Deploy the finalized Greengrass component to edge devices leveraging AWS Greengrass Core.
   - Implement comprehensive monitoring and logging mechanisms to track component execution and ensure operational reliability.


## Copyright

© Uday Singamala [2024]


## References

- [Greengrass Installation](Greengrass.md)
- [Setup for csv](csv.md)
- [AWS Greengrass Documentation](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)
- [Python Documentation](https://docs.python.org/)
- [Linux Commands](Linux.md)

