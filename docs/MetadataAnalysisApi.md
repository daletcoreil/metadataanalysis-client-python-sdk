# metadataanalysis_client.MetadataAnalysisApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze**](MetadataAnalysisApi.md#analyze) | **POST** /metadata-analysis/analyze | 
[**knowledge_graph_search**](MetadataAnalysisApi.md#knowledge_graph_search) | **GET** /metadata-analysis/knowledge-graph-search | 
[**segment_text**](MetadataAnalysisApi.md#segment_text) | **POST** /metadata-analysis/segment-text | 
[**translate_captions**](MetadataAnalysisApi.md#translate_captions) | **POST** /metadata-analysis/translate-captions | 
[**translate_text**](MetadataAnalysisApi.md#translate_text) | **POST** /metadata-analysis/translate-text | 


# **analyze**
> AnalyzedTextResponse analyze(project_service_id, analyze_request)



Perform metadata analysis on the provided text.

### Example

* Api Key Authentication (tokenSignature):
```python
from __future__ import print_function
import time
import metadataanalysis_client
from metadataanalysis_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with metadataanalysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadataanalysis_client.MetadataAnalysisApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
analyze_request = metadataanalysis_client.AnalyzeRequest() # AnalyzeRequest | Text to be analyzed and list of requested analysis methods.

    try:
        api_response = api_instance.analyze(project_service_id, analyze_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataAnalysisApi->analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **analyze_request** | [**AnalyzeRequest**](AnalyzeRequest.md)| Text to be analyzed and list of requested analysis methods. | 

### Return type

[**AnalyzedTextResponse**](AnalyzedTextResponse.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_graph_search**
> KnowledgeGraphSearchResponse knowledge_graph_search(project_service_id, ids)



Get information for given knowledge graph ids. Knowledge graph ids are returned by the entities extractor of the analyzed method. This returns detailed information on an entity including image and description.

### Example

* Api Key Authentication (tokenSignature):
```python
from __future__ import print_function
import time
import metadataanalysis_client
from metadataanalysis_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with metadataanalysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadataanalysis_client.MetadataAnalysisApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
ids = ['ids_example'] # list[str] | Query knowledge graph ids

    try:
        api_response = api_instance.knowledge_graph_search(project_service_id, ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataAnalysisApi->knowledge_graph_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **ids** | [**list[str]**](str.md)| Query knowledge graph ids | 

### Return type

[**KnowledgeGraphSearchResponse**](KnowledgeGraphSearchResponse.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_text**
> SegmentTextResponse segment_text(project_service_id, segment_text_request)



Create segments from a given text.

### Example

* Api Key Authentication (tokenSignature):
```python
from __future__ import print_function
import time
import metadataanalysis_client
from metadataanalysis_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with metadataanalysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadataanalysis_client.MetadataAnalysisApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
segment_text_request = metadataanalysis_client.SegmentTextRequest() # SegmentTextRequest | Request which contains the needed information for the segment operation.

    try:
        api_response = api_instance.segment_text(project_service_id, segment_text_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataAnalysisApi->segment_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **segment_text_request** | [**SegmentTextRequest**](SegmentTextRequest.md)| Request which contains the needed information for the segment operation. | 

### Return type

[**SegmentTextResponse**](SegmentTextResponse.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_captions**
> TranslateCaptionsResponse translate_captions(project_service_id, translate_captions_request)



Translate captions from a given text.

### Example

* Api Key Authentication (tokenSignature):
```python
from __future__ import print_function
import time
import metadataanalysis_client
from metadataanalysis_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with metadataanalysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadataanalysis_client.MetadataAnalysisApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
translate_captions_request = metadataanalysis_client.TranslateCaptionsRequest() # TranslateCaptionsRequest | Request which contains the needed information for the traslate captions operation.

    try:
        api_response = api_instance.translate_captions(project_service_id, translate_captions_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataAnalysisApi->translate_captions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **translate_captions_request** | [**TranslateCaptionsRequest**](TranslateCaptionsRequest.md)| Request which contains the needed information for the traslate captions operation. | 

### Return type

[**TranslateCaptionsResponse**](TranslateCaptionsResponse.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_text**
> TranslateTextResponse translate_text(project_service_id, translate_text_request)



Translate a given text to a target language.

### Example

* Api Key Authentication (tokenSignature):
```python
from __future__ import print_function
import time
import metadataanalysis_client
from metadataanalysis_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = metadataanalysis_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with metadataanalysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadataanalysis_client.MetadataAnalysisApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
translate_text_request = metadataanalysis_client.TranslateTextRequest() # TranslateTextRequest | Request which contains the needed information for the translate operation.

    try:
        api_response = api_instance.translate_text(project_service_id, translate_text_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataAnalysisApi->translate_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **translate_text_request** | [**TranslateTextRequest**](TranslateTextRequest.md)| Request which contains the needed information for the translate operation. | 

### Return type

[**TranslateTextResponse**](TranslateTextResponse.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

