import adal

AZURE_DATABRICKS_RESOURCE_ID = '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d'


def _get_adal_auth_context(authority, verify_ssl=None, timeout=None):
    authority_url = "https://login.microsoftonline.com/{0}".format(authority)
    return adal.AuthenticationContext(authority_url, verify_ssl=verify_ssl, timeout=timeout)


def adal_user_auth(authority="common", resource="", client_id="", 
                   username="", password="", verify_ssl=None, timeout=None):
    """
    Generates an Azure AD Access Token 
    """
    context = _get_adal_auth_context(authority, verify_ssl, timeout)
    token = context.acquire_token_with_username_password(
        resource, 
        username, 
        password, 
        client_id
    )
    return token


def adal_refresh_token(authority="common", resource="", client_id="", 
                       refresh_token="", verify_ssl=None, timeout=None):
    """
    Refreshes an Azure AD Access Token
    """
    context = _get_adal_auth_context(authority, timeout)
    token = context.acquire_token_with_refresh_token(
        refresh_token, 
        client_id, 
        resource
    )
    return token