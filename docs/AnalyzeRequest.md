# AnalyzeRequest

Text to be analyzed and requested analysis methods. if not specified all analyses are executed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Up to 200kb of UTF-8 encoded raw text to be analyzed. The language is detected automatically and it should be one of the following: English (en), French (fr), German (de), Italian (it), Japanese (ja), Korean (ko), Portuguese (pt), Russian (ru), Spanish (es) | 
**extractors** | **list[str]** | Extractors detect spans in the text and return their normalized description. | [optional] 
**extractors_score_threshold** | **float** | Only return extractors results with score above the threshold between 0 and 1. if not specified return all results. | [optional] 
**classifiers** | **list[str]** | Classifiers categorize the whole text according to industry standard taxonomies. | [optional] 
**classifier_score_threshold** | **float** | Only return categories with score above the threshold between 0 and 1. if not specified return all detected categories. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


