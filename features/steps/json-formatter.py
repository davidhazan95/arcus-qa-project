#Behave is imported for the BDD structure used in these automated tests, it's responsible for coordinating the tests and organizing the execution
from behave import *
from features.steps.mocks_json import *
from features.steps.mocks_dataset import *
from src.json_formatter.validators import *

# Scenario: 02-0001 Transform Valid Dataset in JSON
@given(u'I have a Dataset')
def step_impl(context):
    # This step is responsible for generating the Dataset for validation.
    context.cisco_valid_dataset= mock_generate_dataset( "cisco.com",
                                                        "https://www.cisco.com/c/en/us/support/routers/910-industrial-router/model.html",
                                                        "Cisco 900 Series Industrial Routers",
                                                        "Routers",
                                                        "Cisco 910 Industrial Router",
                                                        "/Support/Product Support/Routers/Cisco 900 Series Industrial Routers",
                                                        1404766800,
                                                        1473886800,
                                                        1645998200).__dict__


@when(u'I validate the Dataset with a base json')
def step_impl(context):
    #This step is responsible for bringing the JSON mock that will be used as validation of the Dataset
    context.cisco_910_json = cisco_910_json_mock

@then(u'I see that the two are compatible')
def step_impl(context):
    # Simple assert to validate that the Dataset is equal to the JSON. Making sure that the Dataset doesn't have any typing issue with the JSON
    assert context.cisco_910_json == context.cisco_valid_dataset


# Scenario: 02-0002 Return Invalid Path on Wrong Path structure
@given(u'I have a Dataset with {invalid_path}')
def step_impl(context,invalid_path):
    #This step will run as many times as there are example rows in the Examples of this Scenario
    #For each run, it'll change the "invalid_path" value to mirror another case of invalid path to guarantee that we cover as much as possible as fast as possible
    #All the other values don't matter for this test.
    context.cisco_invalid_path_dataset= mock_generate_dataset( "cisco.com",
                                                        "https://www.cisco.com/c/en/us/support/routers/910-industrial-router/model.html",
                                                        "Cisco 900 Series Industrial Routers",
                                                        "Routers",
                                                        "Cisco 910 Industrial Router",
                                                        invalid_path,
                                                        1404766800,
                                                        1473886800,
                                                        1645998200).__dict__

@when(u'I validate the Dataset with wrong path')
def step_impl(context):
    #This step is responsible for actually validating the Path, it'll return a fail or ok message. This was made to mock a real validation of Path
    context.message_invalid_path = validate_path_regex(context.cisco_invalid_path_dataset["path"])

@then(u'I see message of invalid path')
def step_impl(context):
    #This step asserts that when we send a invalid Path Syntax to the validator, it'll return the correct error message
    assert context.message_invalid_path == "Path Syntax in Dataset is not valid!"

# Scenario: 02-0003 Return Obligatory Field $Name_of_field Not Found if dataset gives insufficient minimal data
@given(u'I have a Dataset generated by the WebScraper with "{vendor}","{url}","{series}","{category}","{model}","{path}","{release}"')
def step_impl(context,vendor,url,series,category,model,path,release):
    #This step will run as many times as there are example rows in the Examples of this Scenario
    #For each run, it'll instantiate a Product Objet with a different value being "null", so we can test that the system is validating that every main value is being looked upon.
    #For test sake, it was not used real "null" values, in the real implementation, this mock needs to use real "null"s
    context.empty_field_dataset= mock_generate_dataset( vendor,
                                                        url,
                                                        series,
                                                        category,
                                                        model,
                                                        path,
                                                        release,
                                                        1473886800,
                                                        1645998200).__dict__

@when(u'I validate the Dataset with wrong field')
def step_impl(context):
    #This step asserts that when we send a empty field to the validator, it'll return the correct error message
    context.message_empty_field = validate_dataset_empty_field(context.empty_field_dataset)


@then(u'I see message with invalid {field}')
def step_impl(context,field):
    #This step is responsible for validating that the system show the correct message for each empty field.
    assert context.message_empty_field == "The following field is empty: "+field