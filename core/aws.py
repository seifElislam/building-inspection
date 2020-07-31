import logging
import boto3
from botocore.exceptions import ClientError
from inspection.settings.dev import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION


def create_presigned_url_expanded(client_method_name, method_parameters=None,
                                  expiration=3600, http_method=None):
    """Generate a presigned URL to invoke an S3.Client method

    Not all the client methods provided in the AWS Python SDK are supported.

    :param client_method_name: Name of the S3.Client method, e.g., 'list_buckets'
    :param method_parameters: Dictionary of parameters to send to the method
    :param expiration: Time in seconds for the presigned URL to remain valid
    :param http_method: HTTP method to use (GET, etc.)
    :return: Presigned URL as string. If error, returns None.
    """
    # Generate a presigned URL for the S3 client method
    s3_client = boto3.client('s3', region_name=REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
    try:
        response = s3_client.generate_presigned_url(ClientMethod=client_method_name,
                                                    Params=method_parameters,
                                                    ExpiresIn=expiration,
                                                    HttpMethod=http_method)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response