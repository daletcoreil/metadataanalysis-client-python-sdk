# Entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**mid** | **str** | Google knowledge graph id when detected. | [optional] 
**wikipedia_url** | **str** |  | [optional] 
**salience** | **float** | The salience score associated with the entity in the [0, 1.0] range. The salience score for an entity provides information about the importance or centrality of that entity to the entire document text. Scores closer to 0 are less salient, while scores closer to 1.0 are highly salient. | [optional] 
**mentions** | [**list[Mention]**](Mention.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


