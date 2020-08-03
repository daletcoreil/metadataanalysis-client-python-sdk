# AnalyzedTextResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | 
**language_is_reliable** | **bool** |  | [optional] 
**entities** | [**list[Entity]**](Entity.md) |  | [optional] 
**topics** | [**list[Topic]**](Topic.md) | List of topics detected in the text. each detected topic refers to wikiLink and wikidataId or None if no wikipedia reference is found. | [optional] 
**categories** | [**list[ClassifierCategory]**](ClassifierCategory.md) | List of categories associated to the text. IPTC news codes refer to - http://cv.iptc.org/newscodes/subjectcode IPTC media topics refer to - http://cv.iptc.org/newscodes/mediatopic IAB taxonomy refer to - https://www.iab.com/guidelines/taxonomy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


