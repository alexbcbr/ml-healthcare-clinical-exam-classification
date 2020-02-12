import boto3

client=boto3.client('sagemaker')
response = client.list_trials(
    ExperimentName='job-autopilot-experiment-aws-auto-ml-job', # this is an experiment in my account
    MaxResults=2,
    #NextToken='string'
)

trial_summaries=response['TrialSummaries']
#next_token=response['NextToken']

for trial in trial_summaries:
    trial_name = trial['TrialName']
    print("*************** trial_name ***************")
    print(trial_name)

    response2=client.list_trial_components(
        TrialName=trial_name, # this is a trial from the above experiment
        MaxResults=10,
        #NextToken='string'
    )
    trial_component_summaries=response2['TrialComponentSummaries']

    for trial_component in trial_component_summaries:
        trial_component_name = trial_component['TrialComponentName']
        print("*************** trial_component_name ***************")
        print(trial_component_name)

        response3 = client.disassociate_trial_component(
            TrialComponentName=trial_component_name,
            TrialName=trial_name
        )

        #response4 = client.delete_trial_component(
        #    TrialComponentName=trial_component_name
        #)
        #print("Trial component deleted: " + trial_component_name)

    response5 = client.delete_trial(
        TrialName=trial_name
    )
    print("Trial deleted: " + trial_component_name)
